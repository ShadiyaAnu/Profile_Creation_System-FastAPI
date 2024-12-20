from pydantic import BaseModel, EmailStr, constr

class StudentProfileCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str | None = None
    password: constr(min_length=8)

class StudentProfileOut(BaseModel):
    id: int
    name: str
    email: str
    phone: str | None

    class Config:
        #orm_mode = True
        from_attributes = True
