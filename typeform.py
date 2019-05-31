import os
import json
import boto3

def handler(event, context):
	body = json.loads(event["body"])
	answers = body["form_response"]["answers"]

	output = ''
	for answer in answers:
		boolean = answer["boolean"]
		if boolean:
			output += 'yes\n'
		else:
			output += 'no\n'
	# CloudWatch logs /aws/lambda/typeform-dev-typeform/{timestamped directory per execution}
	print(output)

	s3 = boto3.resource("s3")
	bucket = s3.Bucket("typeformresponses")
	bucket.put_object(Key="responses.txt", Body=output)

	response = {
		"statusCode": 200,
		"body": json.dumps(event)
	}
	return response
