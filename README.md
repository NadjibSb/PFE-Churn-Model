# Segment-specific Modeling

An approach to build better predictive models. \
**Use Case :** Telecom

<div style="text-align:center"><img src="./segment-specefic%20modeling.png" /></div>

## 1- Clustering

Cluster clients according to their behavior (Calls, Data, SMS, Recharge) 
\
\
***Development steps :***
- Data exploration
- Data cleaning
- Modeling : using k-means & aggmolorative clustering
- Model evaluation
- Visualization
- Deploy the model via REST API using flask

## 2- Churn prediction

Build a predictive model for each cluster of client instead of one model for all the clients
**Use Case :** Churn prediction 
\
\
***Development steps :***
- Data exploration
- Segment-specific Modeling: using Auto-ML with TPOT
- Models evaluation
- Deploy the models via REST API using flask

## 3- MAPE-K Control Loop

Self-adaptive system based on MAPE-K architecture to monitor the resulted models
\
\
***Components :***
- Monitor
- Analyze
- Plan
- Execute
- Knowledge
