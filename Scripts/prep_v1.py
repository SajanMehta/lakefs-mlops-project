# -*- coding: utf-8 -*-
"""
This file is to convert the raw data into version 1 by adding a total lift column
"""

# Import statements

from lakefs_spec import LakeFSFileSystem
import pandas as pd
from sklearn.model_selection import train_test_split


# Connect to LakeFS and grab the data #

fs = LakeFSFileSystem(host= "http://127.0.0.1:8000/",
                      username= "http://127.0.0.1:8000/",
                      password= "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY")

data = pd.read_csv('lakefs://athletes/main/data/raw/athletes.csv')


# Data preparation #

# Create total lift
data['total_lift'] = data['snatch'] + data['deadlift'] + data['backsq'] + data['candj']
data = data.dropna(subset=['total_lift'])

# Train Test Split reproducible with random state and constant test size
train, test = train_test_split(data, test_size = 0.2, random_state = 42)

# To csv
train.to_csv(r"C:\Users\Sajan\OneDrive\Documents\UChicago\MLOps\Assignment 1\Data\v1_train.csv", index=False)
test.to_csv(r"C:\Users\Sajan\OneDrive\Documents\UChicago\MLOps\Assignment 1\Data\v1_test.csv", index = False)
data.to_csv(r"C:\Users\Sajan\OneDrive\Documents\UChicago\MLOps\Assignment 1\Data\v1_complete.csv", index = False)

