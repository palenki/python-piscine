from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = dark_spell_allowed_ingredients()

    ingredients_lower: str = ingredients.lower()

    is_valid: bool = any(
        ingredient in ingredients_lower
        for ingredient in allowed
            )

    status: str = "VALID" if is_valid else "INVALID"

    return f"{ingredients} - {status}"
