# W. Fifita Menu Planner - Iteration 3

import tkinter as tk
from tkinter import messagebox
import json

# Docstring for the MenuPlanner class
"""
MenuPlanner is a Tkinter-based GUI application that allows users to plan a meal 
by selecting food, drink, and dessert items from a predefined menu. The user 
can input a budget, choose menu items, and view a receipt based on their choices. 
The program ensures that selections fit within the specified budget. The updated version 
includes enhanced error handling, the ability to save/load previous plans, and improved UI feedback.
"""

# Menu with prices and descriptions
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
        """
        Initialises the MenuPlanner application and sets up frames for each stage of the UI.
        """
        self.root = root
        self.root.title("Menu Planner")
        self.root.geometry("700x300")  # Adjust window size for more space
        
        # Variables to hold budget and user choices
        self.budget = 0.0
        self.food_choice = None
        self.drink_choice = None
        self.dessert_choice = None

        # Set frames for different stages of the application
        self.welcome_frame = tk.Frame(root, bg="peachpuff", width=500, height=400)
        self.menu_frame = tk.Frame(root, bg="peachpuff", width=500, height=400)
        self.selection_frame = tk.Frame(root, bg="peachpuff", width=500, height=400)
        self.receipt_frame = tk.Frame(root, bg="peachpuff", width=500, height=400)

        # Ensure frames maintain size
        self.welcome_frame.grid_propagate(False)
        self.menu_frame.grid_propagate(False)
        self.selection_frame.grid_propagate(False)
        self.receipt_frame.grid_propagate(False)

        # Call the welcome page to start the app
        self.create_welcome_page()

    def create_welcome_page(self):
        """Creates the welcome page with an option to proceed or exit the app."""
        self.clear_frames()  # Clear all frames before displaying the new one
        self.welcome_frame.pack(fill=tk.BOTH, expand=True)
        
        # Welcome message
        welcome_label = tk.Label(self.welcome_frame, text="Welcome to the Menu Planner!", 
                                 font=("Arial", 18, "bold"), bg="peachpuff", fg="black")
        welcome_label.pack(pady=40)

        # Buttons for proceeding or exiting
        proceed_button = tk.Button(self.welcome_frame, text="Proceed", command=self.create_menu_page, 
                                   bg="white", fg="black", font=("Arial", 12))
        proceed_button.pack(pady=10)
        
        # Load previous menu plan button
        load_button = tk.Button(self.welcome_frame, text="Load Previous Menu", 
                                command=self.load_previous_menu, bg="white", fg="black", font=("Arial", 12))
        load_button.pack(pady=10)
        
        # Exit button
        exit_button = tk.Button(self.welcome_frame, text="Exit", command=self.root.quit, 
                                bg="white", fg="black", font=("Arial", 12))
        exit_button.pack(pady=10)

    def create_menu_page(self):
        """Creates the menu page where the user can input their budget and select items."""
        self.clear_frames()  # Clear the frame for the menu
        self.menu_frame.pack(fill=tk.BOTH, expand=True)

        # Label and entry for budget input
        budget_label = tk.Label(self.menu_frame, text="Enter your budget: $", font=("Arial", 14, "bold"), 
                                bg="peachpuff", fg="black")
        self.menu_frame.grid_columnconfigure(0, weight=1)  # Center the budget label and input
        self.menu_frame.grid_columnconfigure(1, weight=1)
        self.menu_frame.grid_columnconfigure(2, weight=1)

        budget_label.grid(row=0, column=0, pady=10, padx=5)
        self.budget_entry = tk.Entry(self.menu_frame, font=("Arial", 14))  # Entry field for the budget
        self.budget_entry.grid(row=0, column=1, pady=10, padx=5)
    
        # Button to set the budget
        set_budget_button = tk.Button(self.menu_frame, text="Set Budget", command=self.set_budget, 
                                      bg="white", fg="black", font=("Arial", 12))
        set_budget_button.grid(row=0, column=2, pady=10, padx=5)

        # Update the display to show user choices dynamically
        self.update_choices_display()

        # Buttons to select food, drink, and dessert
        food_button = tk.Button(self.menu_frame, text="Choose Food", command=self.create_food_page, 
                                bg="white", fg="black", font=("Arial", 12))
        food_button.grid(row=2, column=0, pady=10, padx=5)
        
        drink_button = tk.Button(self.menu_frame, text="Choose Drink", command=self.create_drink_page, 
                                 bg="white", fg="black", font=("Arial", 12))
        drink_button.grid(row=2, column=1, pady=10, padx=5)
        
        dessert_button = tk.Button(self.menu_frame, text="Choose Dessert", command=self.create_dessert_page, 
                                   bg="white", fg="black", font=("Arial", 12))
        dessert_button.grid(row=2, column=2, pady=10, padx=5)

    def set_budget(self):
        """Sets the budget based on user input and validates it."""
        try:
            # Try to convert the budget entry to a float
            self.budget = float(self.budget_entry.get())
            
            # Validate that the budget is a positive number
            if self.budget <= 0:
                raise ValueError("Budget must be greater than zero.")

            # Inform the user that the budget has been set successfully
            messagebox.showinfo("Budget Set", f"Your budget has been set to ${self.budget:.2f}")
            self.update_choices_display()  # Update display with the new budget
            
        except ValueError as e:
            # Show error message if budget is invalid
            messagebox.showerror("Invalid Budget", "Please enter a valid positive number for the budget.")
            self.budget_entry.delete(0, tk.END)  # Clear the entry field

    def update_choices_display(self):
        """Updates the display to show the current budget and user choices."""
        # Display current budget, food, drink, and dessert choices dynamically
        for widget in self.menu_frame.grid_slaves(row=1):
            widget.destroy()  # Clear previous labels

        display_text = f"Budget: ${self.budget:.2f}\n"
        display_text += f"Food: {self.food_choice if self.food_choice else 'None'}\n"
        display_text += f"Drink: {self.drink_choice if self.drink_choice else 'None'}\n"
        display_text += f"Dessert: {self.dessert_choice if self.dessert_choice else 'None'}"
        
        choices_label = tk.Label(self.menu_frame, text=display_text, font=("Arial", 14), 
                                 bg="peachpuff", fg="black", justify="left")
        choices_label.grid(row=1, column=0, columnspan=3, pady=10)

    def create_food_page(self):
        """Creates the page for selecting food items."""
        self.clear_frames()
        self.selection_frame.pack(fill=tk.BOTH, expand=True)
        self.create_selection_page("food", self.set_food_choice)

    def create_drink_page(self):
        """Creates the page for selecting drink items."""
        self.clear_frames()  # Clear the frame to prevent showing the previous page
        self.selection_frame.pack(fill=tk.BOTH, expand=True)
        self.create_selection_page("drink", self.set_drink_choice)

    def create_dessert_page(self):
        """Creates the page for selecting dessert items."""
        self.clear_frames()  # Clear the frame to prevent showing the previous page
        self.selection_frame.pack(fill=tk.BOTH, expand=True)
        self.create_selection_page("dessert", self.set_dessert_choice)

    def create_selection_page(self, category, select_function):
        """
        Creates a selection page where users can choose from food, drink, or dessert options.
        Parameters:
        category (str): The category of items to display (e.g., "food", "drink", "dessert").
        select_function (function): The function to call when an item is selected.
        """
        # Clear the selection_frame completely
        for widget in self.selection_frame.winfo_children():
            widget.destroy()

        # Pack the cleared selection_frame
        self.selection_frame.pack(fill=tk.BOTH, expand=True)

        # Heading label for the selection page
        heading_label = tk.Label(self.selection_frame, text=f"Select a {category.title()}",
                                font=("Arial", 18, "bold"), bg="peachpuff", fg="black")
        heading_label.pack(pady=10)

        # Display all options for the selected category
        for item, details in menu[category].items():
            item_button = tk.Button(self.selection_frame, text=f"{item} (${details['price']})\n{details['description']}",
                                    font=("Arial", 12), bg="white", fg="black", 
                                    command=lambda i=item: select_function(i))
            item_button.pack(pady=5)

        # Button to go back to the menu page
        back_button = tk.Button(self.selection_frame, text="Back to Menu", command=self.create_menu_page, 
                                bg="white", fg="black", font=("Arial", 12))
        back_button.pack(pady=10)

    def set_food_choice(self, choice):
        """Sets the user's food choice."""
        self.food_choice = choice
        self.check_if_all_selected()

    def set_drink_choice(self, choice):
        """Sets the user's drink choice."""
        self.drink_choice = choice
        self.check_if_all_selected()

    def set_dessert_choice(self, choice):
        """Sets the user's dessert choice."""
        self.dessert_choice = choice
        self.check_if_all_selected()

    def check_if_all_selected(self):
        """Checks if the user has selected food, drink, and dessert, and if so, moves to the receipt page."""
        if self.food_choice and self.drink_choice and self.dessert_choice:
            self.create_receipt_page()
        else:
            self.create_menu_page()

    def create_receipt_page(self):
        """Creates the receipt page and calculates the total cost of the selected items."""
        self.clear_frames()
        self.receipt_frame.pack(fill=tk.BOTH, expand=True)

        total_cost = 0.0

        # Calculate the total cost based on user choices
        if self.food_choice:
            total_cost += menu["food"][self.food_choice]["price"]
        if self.drink_choice:
            total_cost += menu["drink"][self.drink_choice]["price"]
        if self.dessert_choice:
            total_cost += menu["dessert"][self.dessert_choice]["price"]

        # Check if the total cost exceeds the budget
        if total_cost > self.budget:
            messagebox.showerror("Over Budget", "Your selections exceed the budget. Please adjust your choices.")
            self.create_menu_page()  # Go back to the menu page to adjust choices
            return

        # Create a summary of the selections and cost
        receipt_text = f"Food: {self.food_choice} (${menu['food'][self.food_choice]['price']})\n"
        receipt_text += f"Drink: {self.drink_choice} (${menu['drink'][self.drink_choice]['price']})\n"
        receipt_text += f"Dessert: {self.dessert_choice} (${menu['dessert'][self.dessert_choice]['price']})\n"
        receipt_text += f"\nTotal: ${total_cost:.2f}"

        # Title for Receipt Page
        receipt_title = tk.Label(self.receipt_frame, text="Receipt", font=("Arial", 18, "bold"), bg="peachpuff", fg="black")
        receipt_title.pack(pady=10)

        # Display the receipt
        receipt_label = tk.Label(self.receipt_frame, text=receipt_text, font=("Arial", 14), 
                                 bg="peachpuff", fg="black", justify="left")
        receipt_label.pack(pady=10)

        # Button to save receipt to JSON
        save_button = tk.Button(self.receipt_frame, text="Save Receipt", command=self.save_receipt, 
                                bg="white", fg="black", font=("Arial", 12))
        save_button.pack(pady=10)

        # Button to return to the welcome page
        back_button = tk.Button(self.receipt_frame, text="Back to Welcome", command=self.create_welcome_page, 
                                bg="white", fg="black", font=("Arial", 12))
        back_button.pack(pady=10)

    def save_receipt(self):
        """Saves the current receipt as a JSON file."""
        # Collect data to save
        receipt_data = {
            "food": self.food_choice,
            "drink": self.drink_choice,
            "dessert": self.dessert_choice,
            "budget": self.budget
        }
        
        # Save the receipt data to a JSON file
        with open("receipt.json", "w") as file:
            json.dump(receipt_data, file, indent=4)
        
        messagebox.showinfo("Receipt Saved", "Your receipt has been saved as receipt.json.")

    def load_previous_menu(self):
        """Loads a previous menu plan from a JSON file."""
        try:
            # Attempt to load data from the JSON file
            with open("receipt.json", "r") as file:
                receipt_data = json.load(file)

            # Set the loaded data to the corresponding fields
            self.budget = receipt_data["budget"]
            self.food_choice = receipt_data["food"]
            self.drink_choice = receipt_data["drink"]
            self.dessert_choice = receipt_data["dessert"]
            
            messagebox.showinfo("Menu Loaded", "Previous menu plan loaded successfully.")
            self.create_menu_page()  # Go to the menu page with loaded data
            
        except FileNotFoundError:
            # Handle the case where the file does not exist
            messagebox.showerror("File Not Found", "No saved menu found. Please save a receipt first.")
        except json.JSONDecodeError:
            # Handle the case of invalid JSON
            messagebox.showerror("Error", "The saved menu file is corrupted or invalid.")

    def clear_frames(self):
        """Clears all frames to display a new page."""
        for frame in [self.welcome_frame, self.menu_frame, self.selection_frame, self.receipt_frame]:
            frame.pack_forget()

# Main loop for the application
if __name__ == "__main__":
    root = tk.Tk()
    app = MenuPlanner(root)
    root.mainloop()