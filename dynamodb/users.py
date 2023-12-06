import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key
from dotenv import load_dotenv, find_dotenv

from models.user import User

dotenv_file = find_dotenv()
load_dotenv(verbose=True)


class Users():
    """Encapsulates an Amazon DynamoDB table of data(users)."""
    def __init__(self):
        dynamodb = boto3.resource(
            "dynamodb", 
            region_name=os.environ["AWS_REGION_NAME"],
            aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"]
        )
        self.table = dynamodb.Table('user')
    
    def add_user(self,user: User) -> dict:
        """
        Adds an user data to the table.

        :param user: An instance of User (a Pydantic model) containing data to be added to the table.
        :return: Response from the database after adding the item.
        """
        try:
            response = self.table.put_item(
                Item={
                    "id": user.id,
                    "email_address": user.email_address,
                    "name": user.name,
                    "signup_date":  user.signup_date,
                }
            )
        except ClientError as err:
            print(
                f"Couldn't add user Here's why: {err.response['Error']['Code']}: {err.response['Error']['Message']}",
            )
            raise
        else:
            return response
    
    def query_all_users(self) ->  list:
        """
        Queries for every user.

        :return: The list of user data in the table.
        """
        try:
            response = self.table.scan()['Items']
        except Exception as err:
            print(
                "Couldn't query for users. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"]
            )
            raise
        else:
            return response
    
    def get_user_email_list(self):
        """
        Gets every user's email address

        :return: The list of user's email address data in the table.
        """
        total_user_data = self.query_all_users()
        email_list = list(map(lambda user_item:user_item["email_address"],total_user_data))
        return email_list
        
    
    