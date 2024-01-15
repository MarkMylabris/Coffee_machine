from coffee_machine import CoffeeMachine
from menu import Menu
from admin import Admin

def main():
    coffee_machine = CoffeeMachine()
    menu = Menu(coffee_machine)
    admin = Admin(coffee_machine)

    while True:
        menu.display_menu()
        choice = input("\nEnter your choice (x to Exit): ")

        if choice == '0':
            password = input("Enter Admin password: ")
            if password == '314':
                admin.admin_menu()
            else:
                print("Incorrect password. Try again.")
        elif choice.lower() == 'x':
            print("Exiting the program. Goodbye!")
            break
        else:
            menu.process_user_choice(choice)

if __name__ == "__main__":
    main()
