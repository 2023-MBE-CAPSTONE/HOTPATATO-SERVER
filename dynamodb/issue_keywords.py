import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key
from dotenv import load_dotenv, find_dotenv

import os
import sys

from models.issue_keyword import IssueKeyword
from utils.date import get_today_date

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
dotenv_file = find_dotenv()
load_dotenv(verbose=True)


class IssueKeywords():
    """Encapsulates an Amazon DynamoDB table of data(issue keywords)."""
    def __init__(self):
        dynamodb = boto3.resource(
            "dynamodb", 
            region_name=os.environ["AWS_REGION_NAME"],
            aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"]
        )
        self.table = dynamodb.Table('issue_keyword')
    
    def add_issue_keyword(self,issue_keyword: IssueKeyword) -> dict:
        """
        Adds an issue keyword data to the table.

        :param issue_keyword: An instance of IssueKeyword (a Pydantic model) containing data to be added to the table.
        :return: Response from the database after adding the item.
        """
        try:
            response = self.table.put_item(
                Item={
                    "issue_date": issue_keyword.issue_date,
                    "issue_name": issue_keyword.issue_name,
                    "positive_keyword": issue_keyword.positive_keyword,
                    "negative_keyword": issue_keyword.negative_keyword,
                }
            )
        except ClientError as err:
            print(
                f"Couldn't add issue_keyword Here's why: {err.response['Error']['Code']}: {err.response['Error']['Message']}",
            )
            raise
        else:
            return response
    
    def query_by_issue_date(self,issue_date: str) ->  list:
        """
        Queries for issue and issue keyword that were occurred in the specified date.

        :param issue_date: The issue date to query.
        :return: The list of issue keyword data that were occurred in the specific date.
        """
        try:
            response = self.table.query(
                KeyConditionExpression=Key("issue_date").eq(issue_date)
            )['Items']
        except Exception as err:
            print(
                "Couldn't query for issue keyword data occurred in %s. Here's why: %s: %s",
                issue_date,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"]
            )
            raise
        else:
            return response
        
if __name__ == "__main__":
    # insert keyword
    ik = IssueKeywords()
    data = {
        "issue_date": get_today_date(),
        "issue_name": "의대 정원 확대",
        "positive_keyword": ["찬성", "특권", "이기적"],
        "negative_keyword": ["반대", "파업", "피부과"],
    }
    data = IssueKeyword(**data)
    response = ik.add_issue_keyword(data)
    print(response)