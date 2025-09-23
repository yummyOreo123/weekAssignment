
from pydantic import BaseModel, field_validator
from typing import List
import json
import ast


class FoodList(BaseModel):
    foods: List[str]

    @field_validator("foods")
    def must_be_three_foods(cls, v):
        if len(v) != 3:
            raise ValueError("Must contain exactly 3 foods")
        return v
    
def validate_food_response(raw: str) -> FoodList:
    #foods_list = json.loads(raw.replace("'", '"'))
    foods_list = ast.literal_eval(raw)
    return FoodList(foods=foods_list)


class FoodBool(BaseModel):
    type: str

    @field_validator("type")
    def must_be_vegetarian_or_not(cls, v):
        if v.lower() not in ["vegetarian", "non-vegetarian"]:
            raise ValueError("Type error: must be 'vegetarian' or 'non-vegetarian'")
        return v.lower()

def validate_food_bool(raw: str) -> FoodBool:
    return FoodBool(type=raw.strip().lower())