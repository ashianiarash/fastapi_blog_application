from pydantic import BaseModel , EmailStr , Field , BeforeValidator , model_validator
from typing import Annotated , Optional
def password_is_strong(password : str):
    striped = password.replace(" " ,"")
    if password != striped:
        raise ValueError('your password should not have space')
    if len(password) < 8 :
        raise ValueError('your password must be at least 8 charecter')
    if password.isdigit():
        raise ValueError('your password must include letters or special charecters')
    if password.isalpha():
        raise ValueError('your password must include numbers or special charecters')

    return password




class UserBase(BaseModel):
    email : EmailStr 
    username : str  = Field(... ,min_length=3 , max_length=20 , description='username of the user')
    name : str = Field(...,max_length=50, description = 'name of the user')

class UserCreate(UserBase):
    password : Annotated[BeforeValidator , password_is_strong]
    confirm_password : str 
    @model_validator(mode='after')
    def check_passwords(self):
        if (self.password != self.confirm_password):
            raise ValueError('passwords are the same')
        return self

class UserResponse(BaseModel):
    id : int 
    username : str  = Field(... ,min_length=3 , max_length=20 , description='username of the user')
    name : str = Field(...,max_length=50, description = 'name of the user')
    message : Optional[str] | None

