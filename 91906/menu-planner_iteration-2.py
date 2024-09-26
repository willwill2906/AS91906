# W. Fifita Menu Planner - Iteration 2

import tkinter as tk
from tkinter import messagebox

# Docstring for MenuPlanner class
"""
Iteration 2 is a Tkinter-based GUI app that allows users to plan a meal 
by selecting food, drink, and dessert items from a predefined menu. User 
can input a budget, choose menu items, and view a receipt based on their choices. 
Program makes sure that selections fit within specified budget.
"""

# Prices and descriptions
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

class MenuPlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Planner")
        self.root.geometry("600x200")  # Set consistent window size

        # Variables to hold budget + user choices
        self.budget = 0.0
        self.food_choice = None
        self.drink_choice = None
        self.dessert_choice = None

        # Frames for different stages of application
        self.welcome_frame = tk.Frame(root, bg="peachpuff", width=400, height=400)
        self.menu_frame = tk.Frame(root, bg="peachpuff", width=400, height=400)
        self.selection_frame = tk.Frame(root, bg="peachpuff", width=400, height=400)
        self.receipt_frame = tk.Frame(root, bg="peachpuff", width=400, height=400)

        self.welcome_frame.grid_propagate(False)
        self.menu_frame.grid_propagate(False)
        self.selection_frame.grid_propagate(False)
        self.receipt_frame.grid_propagate(False)

        self.create_welcome_page()

    def create_welcome_page(self):
        """Creates the welcome page with an option to proceed or exit the app."""
        self.clear_frames()  # Clear all frames before displaying the new one
        self.welcome_frame.pack(fill=tk.BOTH, expand=True)
        
        # Welcome message
        welcome_label = tk.Label(self.welcome_frame, text="Welcome to Menu Planner!", font=("Arial", 18), bg="peachpuff", fg="black")
        welcome_label.pack(pady=40)

        # Buttons for proceeding or exiting
        proceed_button = tk.Button(self.welcome_frame, text="Proceed", command=self.create_menu_page, bg="white", fg="black")
        proceed_button.pack(pady=10)
        exit_button = tk.Button(self.welcome_frame, text="Exit", command=self.root.quit, bg="white", fg="black")
        exit_button.pack(pady=10)

    def create_menu_page(self):
        """Creates the menu page where the user can input their budget and select items."""
        self.clear_frames()  # Clear the frame for the menu
        self.menu_frame.pack(fill=tk.BOTH, expand=True)
        
        # Label and entry for budget input
        budget_label = tk.Label(self.menu_frame, text="Enter your budget: $", font=("Arial", 14), bg="peachpuff", fg="black")
        self.menu_frame.grid_columnconfigure(0, weight=1)  # Center the budget label and input
        self.menu_frame.grid_columnconfigure(1, weight=1)
        self.menu_frame.grid_columnconfigure(2, weight=1)

        budget_label.grid(row=0, column=0, pady=10, padx=5)
        self.budget_entry = tk.Entry(self.menu_frame, font=("Arial", 14))  # Input field for budget
        self.budget_entry.grid(row=0, column=1, pady=10, padx=5)
        
        # Button to set budget
        set_budget_button = tk.Button(self.menu_frame, text="Set Budget", command=self.set_budget, bg="white", fg="black")
        set_budget_button.grid(row=0, column=2, pady=10, padx=5)

        self.update_choices_display()

        # Buttons to select food, drink, dessert
        food_button = tk.Button(self.menu_frame, text="Choose Food", command=self.create_food_page, bg="white", fg="black")
        food_button.grid(row=2, column=0, pady=10, padx=5)
        drink_button = tk.Button(self.menu_frame, text="Choose Drink", command=self.create_drink_page, bg="white", fg="black")
        drink_button.grid(row=2, column=1, pady=10, padx=5)
        dessert_button = tk.Button(self.menu_frame, text="Choose Dessert", command=self.create_dessert_page, bg="white", fg="black")
        dessert_button.grid(row=2, column=2, pady=10, padx=5)

    def set_budget(self):
        """Sets the user's budget, validates input, and provides feedback."""
        try:
            # Attempt to convert budget input to a float
            budget = float(self.budget_entry.get())
            if budget > 0:
                self.budget = budget  # Update the budget
                messagebox.showinfo("Budget Set", f"Your budget is set to ${self.budget}")
                self.update_choices_display()
            else:
                # Display error if budget is zero or negative
                messagebox.showerror("Invalid Budget", "Budget must be greater than zero. Please try again.")
        except ValueError:
            # Display error if input is not a valid number
            messagebox.showerror("Invalid Input", "Please enter a numeric value.")

    def create_food_page(self):
        """Navigates to the food selection page."""
        self.create_selection_page("food")

    def create_drink_page(self):
        """Navigates to the drink selection page."""
        self.create_selection_page("drink")

    def create_dessert_page(self):
        """Navigates to the dessert selection page."""
        self.create_selection_page("dessert")

    def create_selection_page(self, category):
        """Creates a selection page based on the category (food, drink, dessert)."""
        self.clear_frames()  # Clear frames before showing new options
        self.selection_frame.pack(fill=tk.BOTH, expand=True)

        # Display the category the user is selecting from
        label = tk.Label(self.selection_frame, text=f"Choose your {category}:", font=("Arial", 18), bg="peachpuff", fg="black")
        label.pack(pady=10)

        # Display menu options for the selected category
        for item, details in menu[category].items():
            button = tk.Button(self.selection_frame, text=f"{item} - ${details['price']}\n{details['description']}",
                               command=lambda i=item, c=category: self.set_choice(c, i), bg="white", fg="black")
            button.pack(pady=5, padx=10, fill=tk.X)

        # Button to return to the main menu page
        back_button = tk.Button(self.selection_frame, text="Back", command=self.create_menu_page, bg="white", fg="black")
        back_button.pack(pady=10)

    def set_choice(self, category, item):
        """Sets the user's choice for food, drink, or dessert."""
        if category == "food":
            self.food_choice = item
        elif category == "drink":
            self.drink_choice = item
        elif category == "dessert":
            self.dessert_choice = item

        self.create_menu_page()  # Go back to the menu page after selection

    def update_choices_display(self):
        """Updates the display of chosen food, drink, and dessert on the menu page."""
        for widget in self.menu_frame.grid_slaves():
            if int(widget.grid_info()["row"]) > 2:
                widget.grid_forget()

        # Display the selected food, drink, and dessert with prices
        if self.food_choice:
            food_label = tk.Label(self.menu_frame, text=f"Food: {self.food_choice} - ${menu['food'][self.food_choice]['price']}",
                                  font=("Arial", 12), bg="peachpuff", fg="black")
            food_label.grid(row=3, column=0, columnspan=3, pady=5)

        if self.drink_choice:
            drink_label = tk.Label(self.menu_frame, text=f"Drink: {self.drink_choice} - ${menu['drink'][self.drink_choice]['price']}",
                                   font=("Arial", 12), bg="peachpuff", fg="black")
            drink_label.grid(row=4, column=0, columnspan=3, pady=5)

        if self.dessert_choice:
            dessert_label = tk.Label(self.menu_frame, text=f"Dessert: {self.dessert_choice} - ${menu['dessert'][self.dessert_choice]['price']}",
                                     font=("Arial", 12), bg="peachpuff", fg="black")
            dessert_label.grid(row=5, column=0, columnspan=3, pady=5)

        # Check if all choices are made and ensure they fit within the budget
        if self.food_choice and self.drink_choice and self.dessert_choice:
            total_cost = menu["food"][self.food_choice]["price"] + menu["drink"][self.drink_choice]["price"] + menu["dessert"][self.dessert_choice]["price"]
            if total_cost <= self.budget:
                self.create_receipt_page(total_cost)
            else:
                # Display error if total cost exceeds budget
                messagebox.showerror("Budget Exceeded", "Your selections exceed your budget. Please choose other items.")
                self.food_choice = self.drink_choice = self.dessert_choice = None
                self.update_choices_display()

    def create_receipt_page(self, total_cost):
        """Creates the receipt page displaying the total cost and remaining budget."""
        self.clear_frames()  # Clear previous frames before displaying receipt
        self.receipt_frame.pack(fill=tk.BOTH, expand=True)

        receipt_label = tk.Label(self.receipt_frame, text="Receipt:", font=("Arial", 18), bg="peachpuff", fg="black")
        receipt_label.pack(pady=10)

        # Receipt details with item descriptions
        receipt_details = f"  Food: {self.food_choice} - ${menu['food'][self.food_choice]['price']} ({menu['food'][self.food_choice]['description']})\n"
        receipt_details += f"  Drink: {self.drink_choice} - ${menu['drink'][self.drink_choice]['price']} ({menu['drink'][self.drink_choice]['description']})\n"
        receipt_details += f"  Dessert: {self.dessert_choice} - ${menu['dessert'][self.dessert_choice]['price']} ({menu['dessert'][self.dessert_choice]['description']})\n"
        receipt_details += f"\nTotal Cost: ${total_cost}"
        receipt_details += f"\nRemaining Budget: ${self.budget - total_cost}"

        receipt_text = tk.Text(self.receipt_frame, font=("Arial", 14), width=45, height=10, bg="peachpuff", fg="black")
        receipt_text.insert(tk.END, receipt_details)  # Insert receipt details into text box
        receipt_text.config(state=tk.DISABLED)  # Disable editing of receipt
        receipt_text.pack(pady=10)

        # Buttons to restart planner or exit
        restart_button = tk.Button(self.receipt_frame, text="Plan Another Menu", command=self.reset_planner, bg="white", fg="black")
        restart_button.pack(pady=5)

        exit_button = tk.Button(self.receipt_frame, text="Exit", command=self.root.quit, bg="white", fg="black")
        exit_button.pack(pady=5)

    def reset_planner(self): # Resets planner, clearing budget and all selections
        self.budget = 0.0  # Reset budget
        self.food_choice = None
        self.drink_choice = None
        self.dessert_choice = None
        self.create_welcome_page()  # Return to welcome page

    def clear_frames(self):
        """Clears all frames by removing their child widgets."""
        for frame in [self.welcome_frame, self.menu_frame, self.selection_frame, self.receipt_frame]:
            for widget in frame.winfo_children():
                widget.destroy()  # Destroy all widgets in current frame
            frame.pack_forget()  # Hide frame from view
  
# Run the menu planner
root = tk.Tk()

app = MenuPlanner(root)  # Initialise app
root.mainloop()  # Start the Tkinter event loop