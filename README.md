# Create Budgets in AWS Budgets using Excel #

## Common Challenges ##

### Finance, IT, operations typically dont want users going into the portal to do work ###

* **But you still to create a budget in AWS to track spend, get notified, and detect anomolies**

## How to use Excel to enter, then create Budgets in AWS ##

### Assumptions: Already have python, and AWS SDK Boto3 installed on laptop ###
* Download github repo or clone to desktop
* Open excel, enter your data (test data is fine)
* Open the create-budget.py code, and update account with your information
* Update email address
* Run python code
* Check results in AWS Console

## Coming soon ##
* Create buget from csv file that gets uploaded to S3, which is a operational efficient way to handle these updates on an ongoing basis.
*   Finance/Product updates spreadsheet.
*   Sends to IT or operations.
*   IT or operations uploads to bucket in S3.
*   A S3 trigger will run lambda function (serverless compute in the cloud), then create AWS budget.
*   Move upload file from bucket to a processed bucket in S3.


