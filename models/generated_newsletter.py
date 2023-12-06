from pydantic import BaseModel

class GeneratedNewsletter(BaseModel):
    issue_date: str
    issue_name: str 
    title: str
    html: str