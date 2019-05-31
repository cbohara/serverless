https://read.iopipe.com/the-right-way-to-do-serverless-in-python-e99535574454

sls create -n my-serverless-project -t aws-python3
generates default serverless.yml file 

generates handler.py

The handler.py file contains your function code. The function definition in serverless.yml will point to this handler.py file and the function exported here.

Serverless's configuration file 

functions:
hello: (function name)

https://github.com/egrajeda/serverless-python-template/blob/master/serverless.yml

handler: handler.hello (relative/path/to/filename.functionname)

serverless.yml is used to create a CloudFormation json template

https://aws.amazon.com/cloudformation/

sls deploy
Compress hello.py into a zip archive

Copy my-serverless-project.zip and compiled-cloudformation-template.json to deploy specific timestamped S3 path

Executing the CloudFormation template, which includes configuring an AWS Lambda function and pointing it to the S3 zip archive

Need to deploy whenever making any code changes

sls invoke -f hello

invokes hello function located in handler.py

leverage serverless-python-requirements pluggin to deal with python requirements
you do not need to install modules on local machine
specify dependencies in requirements.txt 

add custom section to serverless.yml
custom:
  pythonRequirements:
    dockerizePip: true

tells serverless-python-requirements pluging to compile the Python packages in a Docker container BEFORE bundling them into the zip archive
ensure they are compiled for 64-bit Linux (not using MacOS)

https://hub.docker.com/editions/community/docker-ce-desktop-mac
need to install Docker on local machine 
https://medium.com/@charlie.b.ohara/building-a-flask-rest-api-with-docker-94ca4219f460

Lambda functions are event-driven
when you invoke a function > triggering an event within AWS Lambda
first arg = event that triggered the function
represeted within AWS Lambda as a JSON object, but what is passed to Python is a dict object rep 

sls invoke -f hello 
event = empty dict {}

if it was an API request, it would contain the entire HTTP request represented as a dict

context object 

useful metadata about the lambda function and current invocation
ex: every invocation has an aws_request_id

https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

if your app can work with a JSON serializable input and produce a JSON serializable output > plug right into AWS Lambda

scheduling 
https://serverless.com/framework/docs/providers/aws/events/schedule/
https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html
question- why would you want to enable scheduling of a lambda function if it is supposed to be event driven?
functions:
  httprequest:
    handler: httprequest.handler
    events:
      - schedule: rate(10 minutes)

web API - HTTP request can be represented as an event
ex: send submission from your typeform directly to any URL
Amazon's API Gateway service will trigger events 
API Gatewill will provide hostname that can
receive HTTP requests > transform HTTP requests into an event object > invoke lambda > collect response + pass it on to the requester as an HTTP response

functions:
  webapi:
    handler: webapi.handler
    events:
      - http:
        path: / (http request path)
        method: get (HTTP method this handler will handle)

after deploy Serverless framework provides endpoint 
Serverless created our new AWS Lambda function and then configured API Gateway to point to this lambda function
endpoints
  GET - https://ybza0t9l93.execute-api.us-east-1.amazonaws.com/dev/

check it out
curl https://ybza0t9l93.execute-api.us-east-1.amazonaws.com/dev/

next task
create simple typeform
get input from user sent to API using webhooks options
use serverless to setup api gateway and deploy lambda function
get survery data from typeform and execute lambda function to transform input into a JSON file in s3

https://www.typeform.com/help/webhooks/
webhook = notification sent over the web
notification is triggered after new typeform submission
response data is sent to webhook URL
notification sent via HTTP POST request and the request body (containing response data) is in JSON format

s3 permissions
https://gist.github.com/tomfa/7bb519a34262353087a83712539eb6b0

https://netdevops.me/2017/building-aws-lambda-with-python-s3-and-serverless/

https://serverless.com/framework/docs/providers/aws/events/s3/
