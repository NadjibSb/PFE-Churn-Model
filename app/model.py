## imports
import pandas as pd
import numpy as np
import pickle
import os

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA 
from sklearn.cluster import KMeans

def modelPredict(data):
	columns = "mobile_number,arpu_6,arpu_7,arpu_8,onnet_mou_6,onnet_mou_7,onnet_mou_8,offnet_mou_6,offnet_mou_7,offnet_mou_8,roam_ic_mou_6,roam_ic_mou_7,roam_ic_mou_8,roam_og_mou_6,roam_og_mou_7,roam_og_mou_8,total_og_mou_6,total_og_mou_7,total_og_mou_8,total_ic_mou_6,total_ic_mou_7,total_ic_mou_8,total_rech_num_6,total_rech_num_7,total_rech_num_8,total_rech_amt_6,total_rech_amt_7,total_rech_amt_8,total_rech_data_6,total_rech_data_7,total_rech_data_8,av_rech_amt_data_6,av_rech_amt_data_7,av_rech_amt_data_8,aon,sms_ic_6,sms_ic_7,sms_ic_8,sms_og_6,sms_og_7,sms_og_8,churn,days_since_last_rech_6,days_since_last_rech_7,days_since_last_rech_8,days_since_last_rech_data_6,days_since_last_rech_data_7,days_since_last_rech_data_8,count_2g3g,vol_2g3g,monthly_2g3g".split(",")
	df = pd.DataFrame(data,columns=columns)

	df = df.drop(['churn','mobile_number'],axis=1)

	cols_6 = [col for col in df.columns if "_6" in col]

	for col in cols_6 :
		col = col[:-2]
		avg_col_name = col+"_avg"
		col_6 = col+"_6"
		col_7 = col+"_7"
		col_8 = col+"_8"
		df[avg_col_name] = df.loc[:,[col_6,col_7,col_8]].mean(axis=1)
		df = df.drop([col_6,col_7,col_8],axis=1)

	path = os.path.dirname(__file__)
	scaler = pickle.load(open('{0}/Model/scaler.pickle'.format(path),"rb"))

	df_std = scaler.transform(df)

	pca = pickle.load(open('{0}/Model/pca.pickle'.format(path),"rb"))
	df_pca = pca.transform(df_std)

	kmeans_pca = pickle.load(open('{0}/Model/kmeans_pca.pickle'.format(path),"rb"))
	df_kmeans = kmeans_pca.predict(df_pca)

	df['segment'] = df_kmeans

	return "classes: {0}".format(df_kmeans)