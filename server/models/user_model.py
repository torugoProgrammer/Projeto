from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    cpf: str

class UserDTO(BaseModel):
    name: str
    cpf: str