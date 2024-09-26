# W. Fifita Menu Planner - Iteration 1

def menu_planner():
    # Enhanced menu with prices and descriptions
    menu = {
        "food": {
            "Burger": {"price": 5, "description": "Juicy beef burger with cheese"},
            "Pizza": {"price": 8, "description": "Wood-fired margherita pizza"},
            "Salad": {"price": 6, "description": "Fresh garden salad with vinaigrette"}
        },
        "drink": {
            "Water": {"price": 1, "description": "Refreshing spring water"},
            "Soda": {"price": 2, "description": "Chilled fizzy soda"},
            "Juice": {"price": 3, "description": "Freshly squeezed orange juice"}
        },
        "dessert": {
            "Ice Cream": {"price": 4, "description": "Creamy vanilla ice cream"},
            "Cake": {"price": 5, "description": "Rich chocolate cake"},
            "Pie": {"price": 3, "description": "Homemade apple pie"}
        }
    }
    
    # Function to display the menu
    def display_menu():
        print("Menu:")
        for category, items in menu.items():
            print(f"\n{category.capitalize()}:")
            for item, details in items.items():
                print(f"  {item}: ${details['price']} - {details['description']}")

    # Function to get user input with validation
    def get_user_input(prompt, valid_options):
        while True:
            choice = input(prompt).title()
            if choice in valid_options:
                return choice
            else:
                print("Invalid choice, please try again.")

    # Function to get and validate budget input
    def get_valid_budget():
        while True:
            try:
                budget = float(input("Enter your budget: $"))
                if budget > 0:
                    return budget
                else:
                    print("Budget must be greater than zero. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    # Function to get user selection and validate budget
    def get_selection_and_validate_budget():
        budget = get_valid_budget()
        while True:
            display_menu()
            food_choice = get_user_input("\nSelect a food item: ", menu["food"].keys())
            drink_choice = get_user_input("Select a drink item: ", menu["drink"].keys())
            dessert_choice = get_user_input("Select a dessert item: ", menu["dessert"].keys())
            
            total_cost = menu["food"][food_choice]["price"] + menu["drink"][drink_choice]["price"] + menu["dessert"][dessert_choice]["price"]
            if total_cost <= budget:
                return budget, food_choice, drink_choice, dessert_choice, total_cost
            else:
                print("\nYour selections exceed your budget. Please try again.\n")

    # Main program flow
    while True:
        budget, food_choice, drink_choice, dessert_choice, total_cost = get_selection_and_validate_budget()
        
        # Print receipt
        print("\nReceipt:")
        print(f"  Food: {food_choice} - ${menu['food'][food_choice]['price']} ({menu['food'][food_choice]['description']})")
        print(f"  Drink: {drink_choice} - ${menu['drink'][drink_choice]['price']} ({menu['drink'][drink_choice]['description']})")
        print(f"  Dessert: {dessert_choice} - ${menu['dessert'][dessert_choice]['price']} ({menu['dessert'][dessert_choice]['description']})")
        print(f"\nTotal Cost: ${total_cost}")
        remaining_budget = budget - total_cost
        print(f"Remaining Budget: ${remaining_budget}")

        # Ask if the user wants to restart or exit
        restart = get_user_input("\nWould you like to plan another menu? (yes/no): ", ["Yes", "No"])
        if restart == "No":
            print("Thank you for using the menu planner. Goodbye!")
            break

# Run the menu planner
menu_planner()