from test.models import Topping, Pizza


def main() -> None:
    for topping in Topping.objects.all():
        pizza: Pizza = topping.pizzaz

        print(pizza)
