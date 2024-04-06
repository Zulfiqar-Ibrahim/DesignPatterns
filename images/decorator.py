# Component interface
class Coffee:
    def cost(self):
        pass

    def description(self):
        pass

# Concrete component
class SimpleCoffee(Coffee):
    def cost(self):
        return 5

    def description(self):
        return "Simple coffee"

# Decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()

# Concrete decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2

    def description(self):
        return self._coffee.description() + ", with milk"

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

    def description(self):
        return self._coffee.description() + ", with sugar"

# Client code
def main():
    coffee = SimpleCoffee()
    print(coffee.description())  # Output: Simple coffee
    print(f"Cost: ${coffee.cost()}")  # Output: Cost: $5

    coffee_with_milk = MilkDecorator(coffee)
    print(coffee_with_milk.description())  # Output: Simple coffee, with milk
    print(f"Cost: ${coffee_with_milk.cost()}")  # Output: Cost: $7

    coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
    print(coffee_with_milk_and_sugar.description())  # Output: Simple coffee, with milk, with sugar
    print(f"Cost: ${coffee_with_milk_and_sugar.cost()}")  # Output: Cost: $8

if __name__ == "__main__":
    main()