# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 16:07:23 2025

@author: Sajan
"""

# Import Statements

from lakefs_spec import LakeFSFileSystem
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


# Data Preparation #

# Connect to file store and grab data set from lakefs

fs = LakeFSFileSystem(host= "http://127.0.0.1:8000/",
                      username= "http://127.0.0.1:8000/",
                      password= "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY")

data = pd.read_csv("lakefs://athletes/v1/data/complete.csv")
print(data.head())

# Clean data #

# Remove not relevant columns
data = data.dropna(subset=['region','age','weight','height','howlong','gender','eat', \
                           'train','background','experience','schedule','howlong', \
                           'deadlift','candj','snatch','backsq','experience',\
                           'background','schedule','howlong'])
data = data.drop(columns=['affiliate','team','name','athlete_id','fran','helen','grace',\
                          'filthy50','fgonebad','run400','run5k','pullups','train'])

# Remove Outliers

data = data[data['weight'] < 1500]
data = data[data['gender'] != '--']
data = data[data['age'] >= 18]
data = data[(data['height'] < 96) & (data['height'] > 48)]

data = data[(data['deadlift'] > 0) & (data['deadlift'] <= 1105)|((data['gender'] == 'Female') \
             & (data['deadlift'] <= 636))]
data = data[(data['candj'] > 0) & (data['candj'] <= 395)]
data = data[(data['snatch'] > 0) & (data['snatch'] <= 496)]
data = data[(data['backsq'] > 0) & (data['backsq'] <= 1069)]

# Clean Survey Data

decline_dict = {'Decline to answer|': np.nan}
data = data.replace(decline_dict)
data = data.dropna(subset=['background','experience','schedule','howlong','eat'])

# Split data
train, test = train_test_split(data, test_size = 0.2, random_state = 42)

# To csv
train.to_csv(r"C:\Users\Sajan\OneDrive\Documents\UChicago\MLOps\Assignment 1\Data\v2_train.csv", index=False)
test.to_csv(r"C:\Users\Sajan\OneDrive\Documents\UChicago\MLOps\Assignment 1\Data\v2_test.csv", index = False)
data.to_csv(r"C:\Users\Sajan\OneDrive\Documents\UChicago\MLOps\Assignment 1\Data\v2_complete.csv", index = False)


