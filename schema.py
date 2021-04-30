from pydantic import BaseModel,EmailStr
from typing import List

class Email(BaseModel):
    user:str
    email:List[EmailStr]
    subject:str
    topic:str


