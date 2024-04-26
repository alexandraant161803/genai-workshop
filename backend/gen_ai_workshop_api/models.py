from typing import List, Optional

from pydantic import BaseModel


class Ingredient(BaseModel):
    name: Optional[str] = None
    unit: Optional[str] = None
    quantity: Optional[str] = None


class Recipe(BaseModel):
    name: Optional[str] = None
    ingredients: Optional[List[Ingredient]] = None
    steps: Optional[List[str]] = None
    total_time_minutes: Optional[str] = None
    person_count: Optional[str] = None
