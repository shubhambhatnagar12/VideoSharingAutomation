from pydantic import BaseModel

class insertValues(BaseModel):
    name:str
    date:str
    phoneNum:str
    email:str


