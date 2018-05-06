from test.models import Topping, Pizza


def main() -> None:
    for topping in Topping.objects.all():
        pizza: Pizza = topping.pizza

        print(pizza)
