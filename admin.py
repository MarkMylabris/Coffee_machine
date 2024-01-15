class Drink:
    def __init__(self, name, price, milk, coffee_beans):
        self.name = name
        self.price = price
        self.milk = milk
        self.coffee_beans = coffee_beans

class Admin:
    def __init__(self, coffee_machine):
        self.coffee_machine = coffee_machine

    def admin_menu(self):
        while True:
            print("\nAdmin Menu:")
            self.display_current_values()
            print("1. Replenish")
            print("2. Add a new drink")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.replenish()
            elif choice == '2':
                self.add_new_drink()
            elif choice == '3':
                print("Exiting Admin Menu.")
                break
            else:
                print("Invalid choice. Please choose again.")

    def display_current_values(self):
        print("\nCurrent Values:")
        print(f"Cash Inside: ${self.coffee_machine.cash_inside:.2f}")
        print(f"Milk: {self.coffee_machine.milk}%")
        print(f"Coffee Beans: {self.coffee_machine.coffee_beans}%")
        print(f"Sugar: {self.coffee_machine.sugar}%")

    def add_new_drink(self):
        name = input("Enter drink name: ")
        price = float(input("Enter drink price: "))
        milk = float(input("Enter required milk (less than 1): "))
        coffee_beans = float(input("Enter required coffee beans (less than 1): "))

        # Validate the input values
        if 0 <= milk < 1 and 0 <= coffee_beans < 1:
            new_drink = Drink(name, price, milk, coffee_beans)
            self.coffee_machine.drinks.append(new_drink)

            with open('drinks.txt', 'a') as file:
                file.write(f"{name},{price},{milk},{coffee_beans}\n")

            print(f"{name} added to the menu.")
        else:
            print("Invalid input. Milk and coffee beans must be between 0 and 1.")

    def replenish(self):
        self.coffee_machine.restock()
        print("Machine replenished.")