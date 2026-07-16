from pydantic import BaseModel



class Postgree(BaseModel):
    DB_SERV:str
    DB_PORT:int | None
    DB_DATA:str
    DB_USER:str
    DB_PASS:str
