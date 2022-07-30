
from pydantic import BaseModel

class Address(BaseModel):
    First_name : str
    Last_name : str
    Latitude : float
    Longitude : float


class Split_address(BaseModel):
    First_name: str
    Last_name: str
    class Config():
        orm_mode=True