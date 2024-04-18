from src.models.ingredient import Ingredient, Restriction

# Req 1
def test_ingredient():
    salmon = Ingredient('salmão')
    salmon2 = Ingredient('salmão')
    bacon = Ingredient('bacon')

    # The class can be correctly instantiated
    assert salmon.name == 'salmão'


    # Test the custom __repr__ method
    assert repr(salmon) == "Ingredient('salmão')"

    # Test the custom __eq__ method
    assert salmon == salmon2

    # Test the custom __hash__ method
    assert hash(salmon) == hash(salmon2)
    assert hash(salmon) != hash(bacon)

    # The restrictions are correctly set (order-independent comparison)
    assert salmon.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED,
    }

