## imports
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA 
from sklearn.cluster import KMeans

from app.util import BASE_PATH


def dataPreparation(df):
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

	return df

def standarise(df):
	scaler = pickle.load(open('{0}/Model/scaler.pickle'.format(BASE_PATH),"rb"))
	df_std = scaler.transform(df)
	return df_std

def pca(df):
	pca = pickle.load(open('{0}/Model/pca.pickle'.format(BASE_PATH),"rb"))
	df_pca = pca.transform(df)
	return df_pca

def kmeans(df):
	kmeans_pca = pickle.load(open('{0}/Model/kmeans_pca.pickle'.format(BASE_PATH),"rb"))
	df_kmeans = kmeans_pca.predict(df)
	return df_kmeans

def predict(data):
	columns = "mobile_number,arpu_6,arpu_7,arpu_8,onnet_mou_6,onnet_mou_7,onnet_mou_8,offnet_mou_6,offnet_mou_7,offnet_mou_8,roam_ic_mou_6,roam_ic_mou_7,roam_ic_mou_8,roam_og_mou_6,roam_og_mou_7,roam_og_mou_8,total_og_mou_6,total_og_mou_7,total_og_mou_8,total_ic_mou_6,total_ic_mou_7,total_ic_mou_8,total_rech_num_6,total_rech_num_7,total_rech_num_8,total_rech_amt_6,total_rech_amt_7,total_rech_amt_8,total_rech_data_6,total_rech_data_7,total_rech_data_8,av_rech_amt_data_6,av_rech_amt_data_7,av_rech_amt_data_8,aon,sms_ic_6,sms_ic_7,sms_ic_8,sms_og_6,sms_og_7,sms_og_8,churn,days_since_last_rech_6,days_since_last_rech_7,days_since_last_rech_8,days_since_last_rech_data_6,days_since_last_rech_data_7,days_since_last_rech_data_8,count_2g3g,vol_2g3g,monthly_2g3g".split(",")
	df_in = pd.DataFrame(data,columns=columns)

	df = dataPreparation(df_in)
	df = standarise(df)
	df = pca(df)
	pred = kmeans(df)
	df_in['segment'] = pred

	json_data = df_in[["mobile_number","segment"]].to_json(orient='records')
	return json_data


