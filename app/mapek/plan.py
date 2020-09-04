## imports
import time

import pandas as pd
import numpy as np
import os
from tpot import TPOTClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pickle

from app.mapek.observer import Observer
from app.mapek.execute import Execute
from app.mapek.knowledge import Knowledge

BASE_PATH = os.path.dirname(__file__)

class Plan(Observer):
    __instance = None

    @staticmethod 
    def getInstance():
        if Plan.__instance == None:
            Plan()
        return Plan.__instance
        
    def __init__(self):
        if Plan.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Plan.__instance = self

    def _train(self,key,ID,df):

        # drop irrelevent columns
        _dfM = df.drop(['mobile_number','segment'], axis=1)

        ### Split data to train/test data
        _dfM1 = _dfM[_dfM.churn==0]
        _dfM2 = _dfM[_dfM.churn==1]
        print("- Churners :",_dfM1.shape)
        print("- Non Churners :",_dfM2.shape)

        # split dataset to 70% Train data & 30% test data
        X_train1, X_test1 = train_test_split(_dfM1, test_size=0.3, train_size=0.7, random_state=1)
        X_train2, X_test2 = train_test_split(_dfM2, test_size=0.3, train_size=0.7, random_state=1)
        train = pd.concat([X_train1,X_train2],axis=0).sample(frac=1)
        test= pd.concat([X_test1,X_test2],axis=0).sample(frac=1)


        X_train = train.drop(['churn'], axis=1)
        y_train = train['churn']
        X_test = test.drop(['churn'], axis=1)
        y_test = test['churn']

        print("X_train Shape : ", X_train.shape)
        print("X_test Shape : ", X_test.shape)

        # Train model
        model = TPOTClassifier(
                                config_dict='TPOT light',
                                memory='auto',
                                template='Selector-Transformer-Classifier',
                                scoring='accuracy',
                                max_time_mins=1,
                                #generations=1,
                                verbosity=2
                                )
        model.fit(X_train, y_train)

        # Evaluate model
        knowledge = Knowledge.getInstance()
        y_pred = model.predict(X_test)
        test_acc = model.score(X_test, y_test)
        knowledge.save("Plan",key,{"new_accuracy":test_acc})
        self.updateStatus(key)
        ####
        print("Test Accuracy score {0}".format(test_acc))
        print(classification_report(y_test, y_pred))
        print(confusion_matrix(y_test, y_pred))

        # Export model
        pickle.dump(model.fitted_pipeline_,open('{0}/models/model{1}.pickle'.format(BASE_PATH,ID),"wb"))




    def notify(self):
        print("\n--------\nPlanning ...")

        knowledge = Knowledge.getInstance()
        data = knowledge.get("Analyse")
        for key in data:
            modelInfo = data[key]
            if modelInfo["to_adapt"]:
                print(key+" adapting ...")
                df = pd.read_csv("{0}/dataset/clustered_{1}.csv".format(BASE_PATH,modelInfo["id"]),index_col="index")
                print("load dataset {0} : ".format(modelInfo["id"])+str(df.shape))  

                #self._train(key,modelInfo["id"],df)
                knowledge.save("Plan",key,{"test_accuracy":99})
                time.sleep(10)
                self.updateStatus(key)

                execute = Execute.getInstance()
                execute.notify()

    def updateStatus(self,key):
        knowledge = Knowledge.getInstance()
        status = knowledge.get("Status")[key]
        end = time.time()
        duration = end - status["start_adapt_time"]
        knowledge.save("Status",key,{"status":1, "last_adapt_time": end, "last_adapt_duration": duration},False)

            

        