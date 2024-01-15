from admin import Drink

class CoffeeMachine:
    def __init__(self):
        self.cash_inside = 0
        self.milk = 100
        self.coffee_beans = 100
        self.sugar = 100
        self.load_drinks()

    def load_drinks(self):
        self.drinks = []
        try:
            with open('drinks.txt', 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    name, price, milk, coffee_beans = parts
                    drink = Drink(name, float(price), float(milk), float(coffee_beans))
                    self.drinks.append(drink)
        except FileNotFoundError:
            print("Error: drinks.txt file not found.")

    def dispense(self, drink, sugar):
        if sugar > 5:
            sugar = 5
        elif sugar < 0:
            sugar = 0

        if self.milk >= drink.milk and self.coffee_beans >= drink.coffee_beans:
            self.milk -= drink.milk
            self.coffee_beans -= drink.coffee_beans
            self.sugar -= sugar
            return True
        else:
            print("Out of stock! Please choose another drink.")
            return False

    def process_payment(self, method, price):
        if method == 'cash':
            amount_paid = float(input("Enter the amount in cash: "))
            if amount_paid < price:
                print("Not enough money. Returning {0:.2f}".format(amount_paid))
            elif amount_paid == price:
                print("Drink received. Thank you!")
                self.cash_inside += price
            else:
                change = amount_paid - price
                print("Drink received. Your change: {0:.2f}".format(change))
                self.cash_inside += price
        elif method == 'card':
            print("Drink received. Thank you!")

    def restock(self):
        self.milk = 100
        self.coffee_beans = 100
        self.sugar = 100
        self.cash_inside = 0

    def check_restock_warning(self):
        if self.milk < 50 or self.coffee_beans < 50 or self.sugar < 50:
            print("Warning: Low stock! Please replenish.")
