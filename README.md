# Create Budgets in AWS Budgets using Excel #

## Common Challenges ##

### Finance, IT, operations typically dont want users going into the portal to do work ###

* **But you still to need to create a budget in AWS to track your spend, get notified, and detect anomalies**

## How to use Excel to enter, then create Budgets in AWS ##

### Assumptions: Already have python, and AWS SDK Boto3 installed on laptop ###
* Download github repo or clone to desktop
* Install libraries in requirements.txt
* Csv should be in same directory, if not, move to same directory where the code is stored
* Open excel, enter your data (test data is fine). In this example, I used filters by service. You could set this up by Tag, to encompass a product or category of products.
* Open the create-budget.py code, and update account with your information
* Update email address
* Save
* Run python code [Budgets API links](Budgets — Boto3 Docs 1.25.2 documentation)
* Check results in AWS Console

### Link to Demo in youtube ###
* Demo [AWS Budgets with CSV](https://www.youtube.com/watch?v=ApUmqOvZyYc)

## Coming soon ##
* Create buget from csv file that gets uploaded to S3, which operationally a way to handle budget creation, and updates on an ongoing basis without going in the portal, and or learning skills (just use excel).
*   Budget pipeline deployment integration.
*   A S3 trigger will run lambda function (serverless compute in the cloud), then create AWS budget.
*   Move upload file from bucket to a processed bucket in S3.

## Remember this is a POC, only to be used for testing ##
* I excluded logging
* I excluded error handling
* I excluded Excel data validation
