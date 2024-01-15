class Menu:
    def __init__(self, coffee_machine):
        self.coffee_machine = coffee_machine

    def display_menu(self):
        print("\nMenu:")
        for i, drink in enumerate(self.coffee_machine.drinks, start=1):
            print(f"{i}. {drink.name} - ${drink.price:.2f}")

    def process_user_choice(self, choice):
        try:
            choice = int(choice)
            if 1 <= choice <= len(self.coffee_machine.drinks):
                sugar = int(input("Enter sugar amount (0-5): "))
                drink = self.coffee_machine.drinks[choice - 1]
                if self.coffee_machine.dispense(drink, sugar):
                    payment_method = input("Choose payment method (1. Cash / 2. Card): ")
                    if payment_method == '1':
                        self.coffee_machine.process_payment('cash', drink.price)
                    elif payment_method == '2':
                        self.coffee_machine.process_payment('card', drink.price)
            else:
                print("Invalid choice. Please choose again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
