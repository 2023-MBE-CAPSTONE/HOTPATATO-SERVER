from datetime import datetime
import sys
import os

from dotenv import load_dotenv
from dynamodb.issue_keywords import IssueKeywords

from models.issue_keyword import IssueKeyword
from utils.date import get_today_date


sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

if __name__ == "__main__":
    # get issue keyword
    ik = IssueKeywords()

    response = ik.query_by_issue_date(20231205)
    print(response)
    
    # generate news letter
    # TODO

    