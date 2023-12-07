from pydantic import BaseModel

class IssueKeyword(BaseModel):
    issue_date: str
    issue_name: str 
    positive_keyword: list
    negative_keyword: list