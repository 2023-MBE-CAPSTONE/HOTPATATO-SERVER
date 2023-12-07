from pydantic import BaseModel

class User(BaseModel):
    id: str
    email_address: str
    name: str
    signup_date: str