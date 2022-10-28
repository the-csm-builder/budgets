from http import client
import boto3
import json
import pandas as pd
from pandas.io.json import json_normalize
import csv

# get AWS budget data

client = boto3.client('budgets')
response = client.describe_budget(
    AccountId='XXXXX',  # Enter your Account ID
    BudgetName='XXXXX')  # Enter your Budget name
# print(response)

# create data frame, and save data to csv format
df = pd.json_normalize(response)

df.to_csv('Data.csv')
print("done")
