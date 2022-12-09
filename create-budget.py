import boto3
import csv
from datetime import datetime

client = boto3.client('budgets')

def create_budget_from_csv():
    with open('Budget-Template.csv', 'r') as csvfile:
        datareader = csv.DictReader(csvfile)
        for row in datareader:
            response = client.create_budget(
                AccountId='XXXX',
                Budget={
                    'BudgetName': row['BudgetName'],
                    'BudgetLimit': {
                        'Amount': row['BudgetAmount'],
                        'Unit': row['Currency']
                    },
                    'CostFilters': {
                        'Service': [row['Filteredby']],
                    },
                    'TimeUnit': row['TimeUnit'],
                    'TimePeriod': {
                        'Start': row['BudgetStart'],
                        'End': row['BudgetEnd']
                    },
                    'BudgetType': row['BudgetType'],
                    'LastUpdatedTime': row['CreatedDt'],
                },
                NotificationsWithSubscribers=[
                    {
                        'Notification': {
                            'NotificationType': 'ACTUAL',
                            'ComparisonOperator': 'GREATER_THAN',
                            'Threshold': 80,
                            'ThresholdType': 'PERCENTAGE'
                        },
                        'Subscribers': [
                            {
                                'SubscriptionType': row['NotificationType'],
                                'Address': row['NotificationEmail']
                            },
                        ]
                    },
                ]
            )

create_budget_from_csv()
print('check your budget in console')
