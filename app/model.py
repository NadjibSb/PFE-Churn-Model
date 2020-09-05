## imports
import pandas as pd
import numpy as np
import pickle
import os

from sklearn.metrics import accuracy_score

from app.util import BASE_PATH


def splitData(df):
	segmented_data = []
	for seg in df['segment'].unique():
		segmented_data.append(df[df['segment']==seg])
	return segmented_data

def loadModels():
	if os.path.isfile('{0}/model/_tpot_model1.pickle'.format(BASE_PATH)):
		model1 = pickle.load(open('{0}/model/_tpot_model1.pickle'.format(BASE_PATH),"rb"))
	else:
		model1 = pickle.load(open('{0}/model/tpot_model1.pickle'.format(BASE_PATH),"rb"))

	if os.path.isfile('{0}/model/_tpot_model2.pickle'.format(BASE_PATH)):
		model2 = pickle.load(open('{0}/model/_tpot_model2.pickle'.format(BASE_PATH),"rb"))
	else:
		model2 = pickle.load(open('{0}/model/tpot_model2.pickle'.format(BASE_PATH),"rb"))

	if os.path.isfile('{0}/model/_tpot_model3.pickle'.format(BASE_PATH)):
		model3 = pickle.load(open('{0}/model/_tpot_model3.pickle'.format(BASE_PATH),"rb"))
	else:
		model3 = pickle.load(open('{0}/model/tpot_model3.pickle'.format(BASE_PATH),"rb"))
	return (model1, model2, model3)

def model(segmented_data):
	models = loadModels()

	for df in segmented_data:
		seg_num = df['segment'].unique()[0]
		_df = df.drop(['mobile_number','segment','churn'], axis=1)
		pred = models[seg_num].predict(_df)
		df['pred_churn'] = pred
		
	return segmented_data


def predict(data):
	columns = "mobile_number,arpu_6,arpu_7,arpu_8,onnet_mou_6,onnet_mou_7,onnet_mou_8,offnet_mou_6,offnet_mou_7,offnet_mou_8,roam_ic_mou_6,roam_ic_mou_7,roam_ic_mou_8,roam_og_mou_6,roam_og_mou_7,roam_og_mou_8,total_og_mou_6,total_og_mou_7,total_og_mou_8,total_ic_mou_6,total_ic_mou_7,total_ic_mou_8,total_rech_num_6,total_rech_num_7,total_rech_num_8,total_rech_amt_6,total_rech_amt_7,total_rech_amt_8,total_rech_data_6,total_rech_data_7,total_rech_data_8,av_rech_amt_data_6,av_rech_amt_data_7,av_rech_amt_data_8,aon,sms_ic_6,sms_ic_7,sms_ic_8,sms_og_6,sms_og_7,sms_og_8,churn,days_since_last_rech_6,days_since_last_rech_7,days_since_last_rech_8,days_since_last_rech_data_6,days_since_last_rech_data_7,days_since_last_rech_data_8,count_2g3g,vol_2g3g,monthly_2g3g,segment".split(",")
	df_in = pd.DataFrame(data,columns=columns)

	df = splitData(df_in)
	segmented_data = model(df)
	result = pd.concat((x for x in segmented_data), axis=0)

	json_data = result[["mobile_number","pred_churn"]].to_json(orient='records')
	return json_data



def evaluate(data):
	
	df_in = pd.DataFrame(data,columns=["churn","pred_churn","segment"])
	segmented_data = splitData(df_in)

	scores = dict()
	for df in segmented_data:
		seg_num = int(df['segment'].unique()[0])
		test_acc = accuracy_score(df["churn"], df["pred_churn"])

		key = "Model_{0}".format(seg_num)
		if key not in scores:
			scores[key]= {}
		scores[key]["id"] = seg_num
		scores[key]["accurency"] = round(test_acc,4)

	return scores
	