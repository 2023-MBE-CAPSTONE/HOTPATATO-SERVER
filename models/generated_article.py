from pydantic import BaseModel

class GeneratedArticle(BaseModel):
    issue_date: str
    issue_name: str 
    positive_article: str
    negative_article: str