"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr, AnyUrl
from typing import Optional

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# VOICE lead schema (used by the contact form)
class Lead(BaseModel):
    """
    Leads collected from the VOICE marketing site
    Collection name: "lead"
    """
    name: str = Field(..., min_length=2, description="Contact person full name")
    company: Optional[str] = Field(None, description="Company name")
    email: EmailStr = Field(..., description="Work email")
    social_link: Optional[str] = Field(None, description="Link to social media or product")
    message: Optional[str] = Field(None, max_length=2000, description="Message from the prospect")
    plan: Optional[str] = Field(None, description="Selected plan at submission time")
