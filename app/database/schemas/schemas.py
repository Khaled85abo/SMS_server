from pydantic import BaseModel, Field, ConfigDict,  EmailStr
from typing import Optional, List
from datetime import datetime

class ItemSchema(BaseModel):
    name: str = Field(..., description="The name of the item")
    description: str = Field(..., description="The description of the item")
    quantity: int = Field(..., description="The quantity of the item")
    image: Optional[str] = Field(None, description="The image of the item")
    box_id: int = Field(..., description="The box id of the item")
    box: Optional[str] = Field(None, description="The box of the item")
    workspace: Optional[str] = Field(None, description="The workspace of the item")
    
    model_config = ConfigDict(from_attributes=True, json_schema_extra={
        "example": {
            "name": "my favoruite jeans",
            "description": "deep pockets",
            "quantity": "1",
            "user_id": "1",
        }
    })

class ItemOutSchema(ItemSchema):
    status: str | None = Field(..., description="The status of the item")
    id: int

class BoxSchema(BaseModel):
    name: str = Field(..., description="The name of the box")
    description: str = Field(..., description="The description of the box")
    work_space_id: int = Field(..., description="The work space id of the box") #TODO: change to work space id

    model_config = ConfigDict(from_attributes=True, json_schema_extra={
        "example": {
            "name": "my favoruite jeans",
            "description": "deep pockets",
            "work_space_id": 1
        }
    })

class BoxOutSchema(BoxSchema):
    items: Optional[list[ItemOutSchema]] = Field(default=[], description="The items of the box")
    created_date: datetime = Field(..., description="The created date of the work space")
    updated_date: datetime | None = Field(None, description="The updated date of the work space")
    id: int

class WorkSpaceSchema(BaseModel):
    name: str = Field(..., description="The name of the work space")
    description: str = Field(..., description="The description of the work space")

    model_config = ConfigDict(from_attributes=True, json_schema_extra={
        "example": {
            "name": "my favoruite jeans",
            "description": "deep pockets",  
        }
    })  

class WorkSpaceOutSchema(WorkSpaceSchema):
    boxes: list[BoxOutSchema] = Field(..., description="The boxes of the work space")
    created_date: datetime = Field(..., description="The created date of the work space")
    updated_date: datetime | None = Field(..., description="The updated date of the work space")
    role: Optional[str] = Field(..., description="The role of the user in the work space")
    id: int



class UserOutSchema(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr = Field(..., min_length=1, max_length=50, description="Email has to be Unique and is required.")
    username: str = Field(..., min_length=1, max_length=100)
    email_verified: bool
    # token_type: str  = Field(default=None)
    is_active: bool
    # access_token: str = Field(default=None)
    id: int

class UserSchema(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr = Field(..., min_length=1, max_length=50, description="Email has to be Unique and is required.")
    password: str = Field(...)
    username: str = Field(..., min_length=1, max_length=100)
	# json_schema_extra gör så att vår swagger-dokumentation visar ett exempel
    model_config = ConfigDict(from_attributes=True, json_schema_extra={
        "example": {
            "first_name": "Robert",
            "last_name": "Johnson",
            "email": "robert@email.com",
            "password": "password123",
        }
    })


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str
    model_config = ConfigDict(from_attributes=True, json_schema_extra={
        "example": {
            "email": "robert@email.com",
            "password": "password123",
        }
    })

class ResetPasswordRequestScheam(BaseModel):
    email: EmailStr

class ResetPasswordSchema(BaseModel):
    password: str

class ImageSchema(BaseModel):
    id: int
    url: str

class ItemWithImagesSchema(BaseModel):
    id: int
    name: str
    description: str
    images: List[ImageSchema]

class BoxWithItemsAndImagesSchema(BaseModel):
    id: int
    name: str
    items: List[ItemWithImagesSchema]

    class Config:
        orm_mode = True
