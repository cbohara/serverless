https://read.iopipe.com/the-right-way-to-do-serverless-in-python-e99535574454

sls create -n my-serverless-project -t aws-python3
generates default serverless.yml file 

generates handler.py

The handler.py file contains your function code. The function definition in serverless.yml will point to this handler.py file and the function exported here.

Serverless's configuration file 

functions:
hello: (function name)

https://github.com/egrajeda/serverless-python-template/blob/master/serverless.yml

handler: handler.hello (path/to/filename.functionname)

serverless.yml is used to create a CloudFormation json template

https://aws.amazon.com/cloudformation/

sls deploy
Compress hello.py into a zip archive

Copy my-serverless-project.zip and compiled-cloudformation-template.json to deploy specific timestamped S3 path

Executing the CloudFormation template, which includes configuring an AWS Lambda function and pointing it to the S3 zip archive

Need to deploy whenever making any code changes
