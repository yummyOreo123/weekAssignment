
from pydantic import BaseModel, field_validator
from typing import List
import ast

class FoodList(BaseModel): 
    foods: List[str]

    @field_validator("foods")
    def must_be_three_foods(cls, v):
        if len(v) != 3:      # length must be exactly 3
            raise ValueError("Must be list that contains exactly 3 foods")
        return v
    
class FoodBool(BaseModel):
    type: str

    @field_validator("type")
    def must_be_vegetarian_or_not(cls, v):
        if v.lower() not in ["vegetarian", "non-vegetarian"]:   # answer must be either 'vegetarian' or 'non-vegetarian'
            raise ValueError("Type error: must be 'vegetarian' or 'non-vegetarian'")
        return v.lower()


def validate_food_response(raw: str) -> FoodList:  #validation function to ensure response is a list of 3 foods
    #print("Validating food list response:", raw)
    try:
        foods_list = ast.literal_eval(raw)
    except Exception:
        raise ValueError("AI must respond with a clean list format like ['a','b','c']")
    
    return FoodList(foods=foods_list)

def validate_food_bool(raw: str) -> FoodBool:       #validation function to ensure response is either 'vegetarian' or 'non-vegetarian'
    return FoodBool(type=raw.strip().lower())