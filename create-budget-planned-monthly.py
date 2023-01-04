import boto3
import csv
from datetime import datetime
import time
from date_utils import date_to_epoch_start_of_month

# Use script to create a budget plan by month. 

client = boto3.client('budgets')
    
def create_budget_from_csv():
    with open('Budget-Template-Monthly.csv', 'r') as csvfile:
        datareader = csv.DictReader(csvfile)
        for row in datareader:
            response = client.create_budget(
                AccountId='XXX',
                Budget={
                    'BudgetName': row['BudgetName'],
                    # 'BudgetLimit': {
                    #     'Amount': row['BudgetAmount'],
                    #     'Unit': row['Currency']
                    # },
                    'PlannedBudgetLimits': {
                    '1672531200': {# jan, #1672531200
                        'Amount': row['Month1'],
                        'Unit': 'USD'
                    },
                    '1675209600': {# Feb
                        'Amount': row['Month2'],
                        'Unit': 'USD'
                    },
                    '1677628800': {# mar
                        'Amount': row['Month3'],
                        'Unit': 'USD'
                    },
                    '1680307200': {# apr
                        'Amount': row['Month4'],
                        'Unit': 'USD'
                    },
                    '1682899200': {# may 1682899200
                        'Amount': row['Month5'],
                        'Unit': 'USD'
                    },
                    '1685577600': {# jun 1685577600
                        'Amount': row['Month6'],
                        'Unit': 'USD'
                    },
                    '1688169600': {# jul 1688169600
                        'Amount': row['Month7'],
                        'Unit': 'USD'
                    },
                    '1690848000': {# aug 1690848000
                        'Amount': row['Month8'],
                        'Unit': 'USD'
                    },
                    '1693526400': {# sept
                        'Amount': row['Month9'],
                        'Unit': 'USD'
                    },
                    '1696118400': {# oct
                        'Amount': row['Month10'],
                        'Unit': 'USD'
                    },
                    '1698796800': {# nov
                        'Amount': row['Month11'],
                        'Unit': 'USD'
                    },
                    '1701388800': {# dec
                        'Amount': row['Month12'],
                        'Unit': 'USD'
                    },
                    },
                    # 'CostFilters': { # Add if you want to create a filtered budget by service, region, etc
                    #     'Service': [row['Filteredby']],
                    # },
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
