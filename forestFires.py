from ucimlrepo import fetch_ucirepo
import pandas as pd
import numpy as np

################# Forest fires dataset ####################
#
# # fetch dataset
# forest_fires = fetch_ucirepo(id=162)
#
# # data (as pandas dataframes)
# X = forest_fires.data.features
# y = forest_fires.data.targets
#
# # metadata
# #print(forest_fires.metadata)
#
# # variable information
# #print(forest_fires.variables)
#
# #Since X and y are already of type DataFrame we can use them directly to create a separate DataFrame of X and y combined (if thats what you want)
# df=pd.DataFrame(X)
# #print (df.head()) #checking to see what the dataframe looks like
#
# df['Target']=y
# print(df.head())


############################### Communities and Crime dataset ########################
""""

# fetch dataset
communities_and_crime = fetch_ucirepo(id=183)

# data (as pandas dataframes)
X = communities_and_crime.data.features
y = communities_and_crime.data.targets


# metadata 
print(communities_and_crime.metadata)

# variable information 
print(communities_and_crime.variables) 

df=pd.DataFrame(X)
df['Target']=y
print (df.head())
"""

############# WINE dataset #############

# fetch dataset
# wine_quality = fetch_ucirepo(id=186)
#
# # data (as pandas dataframes)
# X = wine_quality.data.features
# y = wine_quality.data.targets


# # metadata
# print(wine_quality.metadata)
#
# # variable information
# print(wine_quality.variables)


# df=pd.DataFrame(X)
# df['Target']=y
# print (df.head())

########################### BREAST CANCER WISCONSIN DATASET ######################

# from ucimlrepo import fetch_ucirepo
#
# # fetch dataset
# breast_cancer_wisconsin_original = fetch_ucirepo(id=15)
#
# # data (as pandas dataframes)
# X = breast_cancer_wisconsin_original.data.features
# y = breast_cancer_wisconsin_original.data.targets
#
# # metadata
# print(breast_cancer_wisconsin_original.metadata)
#
# # variable information
# print(breast_cancer_wisconsin_original.variables)
#
# df=pd.DataFrame(X)
# df['Target']=y
# print (df.head())

####################### CREDIT APPROVAL DATASET ########################
from ucimlrepo import fetch_ucirepo

# fetch dataset
credit_approval = fetch_ucirepo(id=27)

# data (as pandas dataframes)
X = credit_approval.data.features
y = credit_approval.data.targets

# metadata
print(credit_approval.metadata)

# variable information
print(credit_approval.variables)

df=pd.DataFrame(X)
df['Target']=y
print (df.head())
