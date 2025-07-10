from pydantic import BaseModel, Field, EmailStr, EmailStr
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Person(BaseModel):
    name: str = Field(description="The name of the person", default="Kasinath Nalla")
    age: Optional[int] = Field(description="The age of the person", default=None)
    email: EmailStr = Field(description="The email of the person")
    cgpa: float = Field(gt=0, lt=10, default=5, description="A decimal value representing the cgpa of the student")


person = Person(name="John Doe", age=30, email="john.doe@example.com", cgpa=2)
print(person)