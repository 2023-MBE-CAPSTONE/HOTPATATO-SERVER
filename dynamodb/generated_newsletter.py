import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key
from dotenv import load_dotenv, find_dotenv

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


from models.generated_newsletter import GeneratedNewsletter


dotenv_file = find_dotenv()
load_dotenv(verbose=True)


class GeneratedNewsletters():
    """Encapsulates an Amazon DynamoDB table of data(generated newsletter)."""
    def __init__(self):
        dynamodb = boto3.resource(
            "dynamodb", 
            region_name=os.environ["AWS_REGION_NAME"],
            aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"]
        )
        self.table = dynamodb.Table('generated_newsletter')
    
    def add_generated_newsletter(self,generated_newsletter: GeneratedNewsletter) -> dict:
        """
        Adds an generated newsletter data to the table.

        :param generated_newsletter: An instance of GeneratedNewsletter (a Pydantic model) containing data to be added to the table.
        :return: Response from the database after adding the item.
        """
        try:
            response = self.table.put_item(
                Item={
                    "issue_date": generated_newsletter.issue_date,
                    "issue_name": generated_newsletter.issue_name,
                    "title": generated_newsletter.title,
                    "html": generated_newsletter.html,
                }
            )
        except ClientError as err:
            print(
                f"Couldn't add generated_newsletter Here's why: {err.response['Error']['Code']}: {err.response['Error']['Message']}",
            )
            raise
        else:
            return response
    
    def query_by_issue_date(self,issue_date: str) ->  list:
        """
        Queries for generated newsletter that were generated in the specified date.

        :param issue_date: The issue date to query.
        :return: The list of generated newsletter that were generated in the specific date.
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
    
    def get_generated_newsletter_list(self,issue_date: str):
        total_generated_newsletter = self.query_by_issue_date(issue_date)
        title_html_list = list(map(lambda news_leter_item: (news_leter_item["title"],news_leter_item["html"]),total_generated_newsletter))
        return title_html_list

if __name__ == "__main__":
    gm = GeneratedNewsletters()
    with open('./templates/sample_newsletter.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    data = {
        "issue_date": "20231205",
        "issue_name": "노란 봉투법",
        "title": "노란봉투법 논쟁: 노동자 보호 vs 기업 부담, 양날의 검",
        "html": html_content

    }
    data = GeneratedNewsletter(**data)
    gm.add_generated_newsletter(data)