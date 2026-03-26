def validate_ingredients(ingredients: str) -> str:
    valid = {"fire", "water", "earth", "air"}
    for item in ingredients.split():
        if item not in valid:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
