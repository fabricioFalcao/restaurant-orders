import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    with pytest.raises(TypeError):
        Dish("name", "5 conto")

    with pytest.raises(ValueError):
        Dish("name", -5)

    carbonara = Dish("carbonara", 25)
    carbonara2 = Dish("carbonara", 25)
    lasagna = Dish("lasagna", 30)

    assert carbonara.name == "carbonara"

    assert repr(carbonara) == "Dish('carbonara', R$25.00)"

    assert carbonara == carbonara2

    assert hash(carbonara) == hash(carbonara2)
    assert hash(carbonara) != hash(lasagna)

    carbonara.add_ingredient_dependency(Ingredient("massa de ravioli"), 150)
    carbonara.add_ingredient_dependency(Ingredient("queijo parmesão"), 50)
    carbonara.add_ingredient_dependency(Ingredient("ovo"), 2)
    carbonara.add_ingredient_dependency(Ingredient("bacon"), 75)

    assert carbonara.get_ingredients() == {Ingredient('massa de ravioli'), Ingredient('bacon'), Ingredient('queijo parmesão'), Ingredient('ovo')}

    assert carbonara.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
        Restriction.LACTOSE,
        Restriction.GLUTEN,
    }
