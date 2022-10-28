import boto3
import json
from datetime import datetime
import csv

client = boto3.client('budgets')

# OPEN CSV LOCAL DRIVE

def create_budget_from_csv():
    with open('Budget-Template.csv', 'r') as csvfile:
        datareader = csv.DictReader(csvfile)
        for row in datareader:
            response = client.create_budget(
                AccountId='XXXXXX',
                Budget={
                    'BudgetName': row['BudgetName'],
                    'BudgetLimit': {
                        'Amount': row['BudgetAmount'],
                        'Unit': row['Currency']
                    },
                    # 'PlannedBudgetLimits': {
                    # 'string': {
                    # 'Amount': 'string',
                    # 'Unit': 'string'
                    # }
                    # },
                    'CostFilters': {
                        'Service': [row['Filteredby']],
                    },
                    # 'CostTypes': {
                    #     'IncludeTax': True|False,
                    #     'IncludeSubscription': True|False,
                    #     'UseBlended': True|False,
                    #     'IncludeRefund': True|False,
                    #     'IncludeCredit': True|False,
                    #     'IncludeUpfront': True|False,
                    #     'IncludeRecurring': True|False,
                    #     'IncludeOtherSubscription': True|False,
                    #     'IncludeSupport': True|False,
                    #     'IncludeDiscount': True|False,
                    #     'UseAmortized': True|False
                    # },
                    'TimeUnit': row['TimeUnit'],
                    'TimePeriod': {
                        'Start': row['BudgetStart'],
                        'End': row['BudgetEnd']
                        # },
                        # 'CalculatedSpend': {
                        #     'ActualSpend': {
                        #         'Amount': 'string',
                        #         'Unit': 'string'
                        #     },
                        #     'ForecastedSpend': {
                        #         'Amount': 'string',
                        #         'Unit': 'string'
                        #     }
                    },
                    'BudgetType': row['BudgetType'],
                    'LastUpdatedTime': row['CreatedDt'],
                    # 'AutoAdjustData': {
                    #     # 'AutoAdjustType': 'HISTORICAL'|'FORECAST',
                    #     # 'HistoricalOptions': {
                    #     # 'BudgetAdjustmentPeriod': 123,
                    #     # 'LookBackAvailablePeriods': 123
                    #     # },
                    #     # 'LastAutoAdjustTime': datetime(2015, 1, 1)
                    # }
                },
                NotificationsWithSubscribers=[
                    {
                        'Notification': {
                            'NotificationType': 'ACTUAL',
                            'ComparisonOperator': 'GREATER_THAN',
                            'Threshold': 80,
                            'ThresholdType': 'PERCENTAGE'
                            # 'NotificationState': 'ALARM'
                        },
                        'Subscribers': [
                            {
                                'SubscriptionType': row['NotificationType'],
                                'Address': row['Email']
                            },
                        ]
                    },
                ]
            )


create_budget_from_csv()
print('check your budget in console')
