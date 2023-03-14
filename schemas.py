from typing import Union, Optional

from pydantic import BaseModel, Json

class UserBase(BaseModel):
    id: int
    email: Optional[str]
    username: str

    class Config:
        orm_mode = True

class EnvironmentBase(BaseModel):
    id: str
    document: dict

    class Config:
        orm_mode = True

class UserEnvironmentBase(BaseModel):
    user_id: int
    environment_id: str
    document: Optional[dict]

    class Config:
        orm_mode = True

class Environment(EnvironmentBase):
    users: list[UserBase]
    environment_users: list[UserEnvironmentBase]

class User(UserBase):
    environments: list[EnvironmentBase]