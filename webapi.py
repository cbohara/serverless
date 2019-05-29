import json

def handler(event, context):
	# return status code you want API Gateway to respond with
	# return body of response as a serialized JSON message
	return {"statusCode": 200, "body": json.dumps({"message": "I'm an HTTP response"})}
