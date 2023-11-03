import os
# db에 넣는 로직
import boto3
from dotenv import load_dotenv
from boto3.dynamodb.conditions import Key
from flask import make_response

def signup_service():

    try:
        load_dotenv(verbose=True)
   
        dynamodb = boto3.resource(
            "dynamodb", 
            region_name=os.getenv("AWS_REGION_NAME"),
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
        )
        user_table = dynamodb.Table('user')
        response = user_table.query(KeyConditionExpression=Key("id").eq("test"))
        print(f"success {response['Items'][0]}",flush=True) 
        return make_response(response['Items'][0])
    except Exception as e:
        print(f"error {e} in connecting db",flush=True)
        return make_response({'message':str(e)},404)
    



# uuid 로직

# 오늘 날짜 구하는 로직