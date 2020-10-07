

## COMMANDE
##
## python provok.py numSegment churnOld(0,1) churnNew(0,1)



import pandas as pd
import numpy as np
import os
import sys

BASE_PATH = os.path.dirname(__file__)

from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db=client["ooredoo-db"]



try:
    if sys.argv[1]:
        cluster = sys.argv[1]
        fileName = "clustered_"+cluster
        df = pd.read_csv("app/mapek/dataset/_{0}.csv".format(fileName),index_col="index")

        if sys.argv[2] and sys.argv[3]:
            churnOld = int(sys.argv[2])
            churnNew = int(sys.argv[3])

            if (churnOld==1 or churnOld==0) and (churnNew==0 or churnNew==1):
                df[df.churn==churnOld] = churnNew
                df.to_csv("app/mapek/dataset/{0}.csv".format(fileName), encoding='utf-8')
                result = db.customers.update_many({"$and":[
                                                            {"segment":int(cluster)},
                                                            {"churn":bool(churnOld)}
                                                        ]},
                                                        {"$set":{"churn":bool(churnNew)}}
                                                        )
                print ("raw:", result.raw_result)
                print ("acknowledged:", result.acknowledged)
                print ("matched_count:", result.matched_count)
                print("updated")

except Exception as e:
    print("____________\nException")
    print(e)
