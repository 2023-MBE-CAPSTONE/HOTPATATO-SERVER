import json
import os
# db에 넣는 로직
import boto3
from dotenv import load_dotenv
from boto3.dynamodb.conditions import Key
from flask import jsonify, make_response
from utils.date import get_today_date

from utils.uuid import make_user_id

def signup_service(name,email):

    try:
        load_dotenv(verbose=True)
   
        dynamodb = boto3.resource(
            "dynamodb", 
            region_name=os.getenv("AWS_REGION_NAME"),
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
        )
        user_table = dynamodb.Table('user')

        ## test - query
        # user_table = dynamodb.Table('user')
        # response = user_table.query(KeyConditionExpression=Key("id").eq("test"))
        
        user_id = make_user_id()
        signup_date = get_today_date()
        response = user_table.put_item(
            Item={
                "id": user_id,
                "email_address": email,
                "name": name,
                "signup_date": signup_date,
            },
        )
        print(f"success {json.dumps(response, indent=2)}",flush=True) 
        return jsonify({'msg': '구독 완료!'})
    except Exception as e:
        print(f"error {e} in connecting db",flush=True)
        return make_response({'message':str(e)},404)
