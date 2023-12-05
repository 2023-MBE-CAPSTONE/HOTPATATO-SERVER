import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key
from dotenv import load_dotenv, find_dotenv

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


from utils.date import get_today_date
from models.generated_article import GeneratedArticle


dotenv_file = find_dotenv()
load_dotenv(verbose=True)


class GeneratedArticles():
    """Encapsulates an Amazon DynamoDB table of data(generated articles)."""
    def __init__(self):
        dynamodb = boto3.resource(
            "dynamodb", 
            region_name=os.environ["AWS_REGION_NAME"],
            aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"]
        )
        self.table = dynamodb.Table('generated_article')
    
    def add_generated_article(self,generated_article: GeneratedArticle) -> dict:
        """
        Adds an generated article data to the table.

        :param generated_article: An instance of GeneratedArticle (a Pydantic model) containing data to be added to the table.
        :return: Response from the database after adding the item.
        """
        try:
            response = self.table.put_item(
                Item={
                    "issue_date": generated_article.issue_date,
                    "issue_name": generated_article.issue_name,
                    "positive_article": generated_article.positive_article,
                    "negative_article": generated_article.negative_article,
                }
            )
        except ClientError as err:
            print(
                f"Couldn't add generated_article Here's why: {err.response['Error']['Code']}: {err.response['Error']['Message']}",
            )
            raise
        else:
            return response
    
    def query_by_issue_date(self,issue_date: str) ->  list:
        """
        Queries for generated article that were generated in the specified date.

        :param issue_date: The issue date to query.
        :return: The list of generated article that were generated in the specific date.
        """
        try:
            response = self.table.query(
                KeyConditionExpression=Key("issue_date").eq(issue_date)
            )['Items']
        except Exception as err:
            print(
                "Couldn't query for generated article data occurred in %s. Here's why: %s: %s",
                issue_date,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"]
            )
            raise
        else:
            return response
        
    