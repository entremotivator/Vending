import streamlit as st
import pandas as pd

# Create a DataFrame to store vending inventory for multiple locations
locations = ['Location 1', 'Location 2', 'Location 3', 'Location 4', 'Location 5', 'Location 6', 'Location 7', 'Location 8', 'Location 9', 'Location 10']
location_inventory = {location: pd.DataFrame(columns=['Item Name', 'Quantity', 'Price', 'Cost', 'Profit']) for location in locations}

# Demo inventory items
demo_items = [
    ('Location 1', 'Kit Kat', 20, 1.5, 0.75, 0.75),
    ('Location 1', 'Doritos', 15, 2.0, 1.0, 1.0),
    ('Location 1', 'Lays Chips', 18, 1.75, 0.85, 0.90),
    ('Location 1', 'Snickers', 22, 1.95, 0.95, 1.0),
    ('Location 1', 'M&Ms', 25, 1.25, 0.65, 0.60),
    ('Location 1', 'Twix', 23, 1.75, 0.85, 0.90),
    ('Location 1', 'Reese\'s', 20, 1.85, 0.90, 0.95),
    ('Location 1', 'Milky Way', 18, 1.95, 0.95, 1.0),
    ('Location 1', 'Cheetos', 19, 1.75, 0.85, 0.90),
    ('Location 1', 'Popcorn', 17, 1.25, 0.65, 0.60),
    ('Location 1', 'Pretzels', 21, 1.35, 0.70, 0.65),
    ('Location 1', 'Rice Krispies Treats', 16, 1.75, 0.85, 0.90),
    ('Location 1', 'Gummy Bears', 20, 1.45, 0.75, 0.70),
    ('Location 1', 'Skittles', 22, 1.55, 0.80, 0.75),
    ('Location 1', 'Starburst', 19, 1.65, 0.80, 0.85),
    ('Location 1', 'Almonds', 18, 1.95, 0.95, 1.0),
    ('Location 1', 'Cashews', 15, 2.25, 1.10, 1.15),
    ('Location 1', 'Peanuts', 23, 1.75, 0.85, 0.90),
    ('Location 1', 'Granola Bars', 17, 1.25, 0.65, 0.60),
    ('Location 1', 'Cookies', 20, 1.45, 0.75, 0.70),
    ('Location 1', 'Brownies', 18, 1.95, 0.95, 1.0),
    ('Location 1', 'Crackers', 22, 1.55, 0.80, 0.75),
    ('Location 1', 'Peanut Butter Cups', 19, 1.65, 0.80, 0.85),
    ('Location 1', 'Chocolate Bars', 16, 1.75, 0.85, 0.90),
    ('Location 1', 'Gum', 20, 1.25, 0.65, 0.60),
    ('Location 1', 'Mints', 23, 1.75, 0.85, 0.90),
    ('Location 1', 'Trail Mix', 19, 1.55, 0.80, 0.75),
    ('Location 1', 'Beef Jerky', 17, 1.65, 0.80, 0.85),
    ('Location 1', 'Fruit Snacks', 22, 1.95, 0.95, 1.0),
    ('Location 1', 'Popsicles', 20, 1.75, 0.85, 0.90),
    ('Location 1', 'Ice Cream Bars', 18, 1.25, 0.65, 0.60),
    ('Location 1', 'Frozen Yogurt', 21, 1.45, 0.75, 0.70),
    ('Location 1', 'Energy Bars', 16, 1.95, 0.95, 1.0),
    ('Location 1', 'Protein Bars', 20, 1.55, 0.80, 0.75),
    ('Location 1', 'Tortilla Chips', 22, 1.65, 0.80, 0.85),
    ('Location 1', 'Salsa', 19, 1.75, 0.85, 0.90),
    ('Location 1', 'Queso Dip', 15, 1.25, 0.65, 0.60),
    ('Location 1', 'Guacamole', 23, 1.95, 0.95, 1.0),
    ('Location 1', 'Hummus', 20, 1.75, 0.85, 0.90),
    ('Location 1', 'Chips Ahoy!', 18, 1.45, 0.75, 0.70),
    ('Location 1', 'Oreos', 22, 1.95, 0.95, 1.0),
    ('Location 1', 'Rice Cakes', 19, 1.65, 0.80, 0.85),
    ('Location 1', 'Cheese Crackers', 16, 1.75, 0.85, 0.90),
    ('Location 1', 'Fruit Roll-Ups', 20, 1.25, 0.65, 0.60),
    ('Location 1', 'Pita Chips', 23, 1.75, 0.85, 0.90),
    ('Location 1', 'Bagel Chips', 19, 1.55, 0.80, 0.75),
    ('Location 1', 'Triscuits', 17, 1.65, 0.80, 0.85),
    ('Location 1', 'Wheat Thins', 22, 1.95, 0.95, 1.0),
    ('Location 1', 'Animal Crackers', 20, 1.75, 0.85, 0.90),
    ('Location 1', 'Goldfish Crackers', 18, 1.45, 0.75, 0.70),
    ('Location 1', 'Pretzel Crisps', 22, 1.95, 0.95, 1.0),
    ('Location 1', 'Cheez-Its', 19, 1.65, 0.80, 0.85),
    ('Location 1', 'Ritz Crackers', 16, 1.75, 0.85, 0.90),
    ('Location 1', 'Fritos', 20, 1.25, 0.65, 0.60),
    ('Location 1', 'Cheeto Puffs', 23, 1.75, 0.85, 0.90),
    ('Location 1', 'Takis', 19, 1.55, 0.80, 0.75),
    ('Location 1', 'Pretzel Sticks', 17, 1.65, 0.80, 0.85),
    ('Location 1', 'Fruit Leather', 22, 1.95, 0.95, 1.0),
    ('Location 1', 'Chex Mix', 20, 1.75, 0.85, 0.90),
    ('Location 1', 'Rice Krispies', 18, 1.45, 0.75, 0.70),
    ('Location 1', 'Fruit Cups', 22, 1.95, 0.95, 1.0),
    ('Location 1', 'Applesauce Cups', 19, 1.65, 0.80, 0.85),
    ('Location 1', 'Pudding Cups', 16, 1.75, 0.85, 0.90),
    ('Location 1', 'Yogurt Cups', 20, 1.25, 0.65, 0.60),
    ('Location 1', 'Smoothie Cups', 23, 1.75, 0.85, 0.90),
    ('Location 1', 'Ice Cream Sandwiches', 19, 1.55, 0.80, 0.75),
    ('Location 1', 'Ice Cream Cones', 17, 1.65, 0.80, 0.85),
    ('Location 1', 'Sorbet Cups', 22, 1.95, 0.95, 1.0),
    ('Location 1', 'Frozen Yogurt Cups', 20, 1.75, 0.85, 0.90),
    ('Location 1', 'Milkshakes', 18, 1.45, 0.75, 0.70),
    ('Location 1', 'Slushies', 22, 1.95, 0.95, 1.0),
    ('Location 1', 'Smoothies', 19, 1.65, 0.80, 0.85),
    ('Location 1', 'Juice Boxes', 16, 1.75, 0.85, 0.90),
    ('Location 1', 'Sodas', 20, 1.25, 0.65, 0.60),
    ('Location 1', 'Energy Drinks', 23, 1.75, 0.85, 0.90),
    ('Location 1', 'Bottled Water', 19, 1.55, 0.80, 0.75),
    ('Location 1', 'Sports Drinks', 17, 1.65, 0.80, 0.85),
    ('Location 1', 'Iced Tea', 22, 1.95, 0.95, 1.0),
    ('Location 1', 'Coffee', 20, 1.75, 0.85, 0.90),
    ('Location 1', 'Hot Chocolate', 18, 1.45, 0.75, 0.70),
    ('Location 1', 'Smoothie Bottles', 22, 1.95, 0.95, 1.0),
    ('Location 1', 'Protein Shakes', 19, 1.65, 0.80, 0.85),
    ('Location 1', 'Tea Bottles', 16, 1.75, 0.85, 0.90),
    ('Location 1', 'Juice Bottles', 20, 1.25, 0.65, 0.60),
    ('Location 1', 'Milk Bottles', 23, 1.75, 0.85, 0.90),
    ('Location 1', 'Water Bottles', 19, 1.55, 0.80, 0.75),
    ('Location 1', 'Wine Bottles', 17, 1.65, 0.80, 0.85),
    ('Location 1', 'Beer Bottles', 22, 1.95, 0.95, 1.0),
    ('Location 1', 'Cocktail Bottles', 20, 1.75, 0.85, 0.90),
    ('Location 1', 'Liquor Bottles', 18, 1.45, 0.75, 0.70),
    ('Location 1', 'Mixed Drinks', 22, 1.95, 0.95, 1.0),
    ('Location 1', 'Alcoholic Shots', 19, 1.65, 0.80, 0.85),
    ('Location 1', 'Wine Glasses', 16, 1.75, 0.85, 0.90),
    ('Location 1', 'Beer Cans', 20, 1.25, 0.65, 0.60),
    ('Location 1', 'Cocktail Glasses', 23, 1.75, 0.85, 0.90),
    ('Location 1', 'Liquor Glasses', 19, 1.55, 0.80, 0.75),
    ('Location 1', 'Margaritas', 17, 1.65, 0.80, 0.85),
    ('Location 1', 'Mojitos', 22, 1.95, 0.95, 1.0),
    ('Location 1', 'Martinis', 20, 1.75, 0.85, 0.90),
    ('Location 1', 'Cosmopolitans', 18, 1.45, 0.75, 0.70),
    ('Location 1', 'Sangrias', 22, 1.95, 0.95, 1.0),
    ('Location 1', 'Pina Coladas', 19, 1.65, 0.80, 0.85),
    ('Location 1', 'Mai Tais', 16, 1.75, 0.85, 0.90),
    ('Location 1', 'Whiskey', 20, 1.25, 0.65, 0.60),
    ('Location 1', 'Vodka', 23, 1.75, 0.85, 0.90),
    ('Location 1', 'Rum', 19, 1.55, 0.80, 0.75),
    ('Location 1', 'Tequila', 17, 1.65, 0.80, 0.85),
    ('Location 1', 'Gin', 22, 1.95, 0.95, 1.0),
    ('Location 1', 'Beer Mugs', 20, 1.75, 0.85, 0.90),
    ('Location 1', 'Wine Glasses', 18, 1.45, 0.75, 0.70),
    ('Location 1', 'Cocktail Glasses', 22, 1.95, 0.95, 1.0),
    ('Location 1', 'Shot Glasses', 19, 1.65, 0.80, 0.85),
    ('Location 1', 'Pint Glasses', 16, 1.75, 0.85, 0.90),
    ('Location 1', 'Highball Glasses', 20, 1.25, 0.65, 0.60),
    ('Location 1', 'Tumblers', 23, 1.75, 0.85, 0.90),
    ('Location 1', 'Wine Bottles', 19, 1.55, 0.80, 0.75),
    ('Location 1', 'Beer Bottles', 17, 1.65, 0.80, 0.85),
    ('Location 1', 'Cocktail Bottles', 22, 1.95, 0.95, 1.0),
    ('Location 1', 'Liquor Bottles', 20, 1.75, 0.85, 0.90),
    ('Location 1', 'Mixers', 18, 1.45, 0.75, 0.70),
    ('Location 1', 'Garnishes', 22, 1.95, 0.95, 1.0),
    ('Location 1', 'Ice', 19, 1.65, 0.80, 0.85),
    ('Location 1', 'Cups', 16, 1.75, 0.85, 0.90),
    ('Location 1', 'Straws', 20, 1.25, 0.65, 0.60),
    ('Location 1', 'Napkins', 23, 1.75, 0.85, 0.90),
    ('Location 1', 'Stirrers', 19, 1.55, 0.80, 0.75),
    ('Location 1', 'Coasters', 17, 1.65, 0.80, 0.85),
    ('Location 1', 'Trash Bags', 22, 1.95, 0.95, 1.0),
    ('Location 1', 'Utensils', 20, 1.75, 0.85, 0.90),
    ('Location 1', 'Plates', 18, 1.45, 0.75, 0.70),
    ('Location 1', 'Bowls', 22, 1.95, 0.95, 1.0),
    ('Location 1', 'Cups', 19, 1.65, 0.80, 0.85),
    ('Location 1', 'Straws', 16, 1.75, 0.85, 0.90),
    ('Location 1', 'Napkins', 20, 1.25, 0.65, 0.60),
    ('Location 1', 'Stirrers', 23, 1.75, 0.85, 0.90),
    ('Location 1', 'Coasters', 19, 1.55, 0.80, 0.75),
    ('Location 1', 'Trash Bags', 17, 1.65, 0.80, 0.85),
    ('Location 1', 'Utensils', 22, 1.95, 0.95, 1.0),
    ('Location 1', 'Plates', 20, 1.75, 0.85, 0.90),
    ('Location 1', 'Bowls', 18, 1.45, 0.75, 0.70),
    ('Location 1', 'Cups', 22, 1.95, 0.95, 1.0),
    ('Location 1', 'Straws', 19, 1.65, 0.80, 0.85),
    ('Location 1', 'Napkins', 16, 1.75, 0.85, 0.90),
    ('Location 1', 'Stirrers', 20, 1.25, 0.65, 0.60),
    ('Location 1', 'Coasters', 23, 1.75, 0.85, 0.90),
    ('Location 1', 'Trash Bags', 19, 1.55, 0.80, 0.75),
    ('Location 1', 'Utensils', 17, 1.65, 0.80, 0.85),
    ('Location 1', 'Plates', 22, 1.95, 0.95, 1.0),
    ('Location 1', 'Bowls', 20, 1.75, 0.85, 0.90),
    # Add more items for Location 1...

    ('Location 2', 'Ruffles', 20, 2.25, 1.10, 1.15),
    ('Location 2', 'Hershey\'s Bar', 16, 1.85, 0.90, 0.95),
    ('Location 2', 'Fritos', 10, 1.75, 0.85, 0.90),
    ('Location 2', 'Mountain Dew', 30, 1.25, 0.60, 0.65),
    ('Location 2', 'Milky Way', 25, 1.75, 0.85, 0.90),
    ('Location 2', 'Lay\'s', 18, 2.0, 1.0, 1.0),
    ('Location 2', 'Reese\'s', 22, 1.50, 0.75, 0.75),
    ('Location 2', 'Dr. Pepper', 15, 1.25, 0.60, 0.65),
    ('Location 2', 'Twizzlers', 12, 1.0, 0.50, 0.50),
    # Add more items for Location 2...

    ('Location 3', 'Cheetos', 20, 1.75, 0.85, 0.90),
    ('Location 3', 'Mars Bar', 16, 1.85, 0.90, 0.95),
    ('Location 3', 'Sprite', 10, 1.0, 0.50, 0.50),
    ('Location 3', 'Nestle Crunch', 30, 1.25, 0.60, 0.65),
    ('Location 3', 'Gummy Bears', 25, 1.50, 0.75, 0.75),
    ('Location 3', 'Sun Chips', 18, 2.0, 1.0, 1.0),
    ('Location 3', 'Butterfinger', 22, 1.75, 0.85, 0.90),
    ('Location 3', 'Fanta', 15, 1.25, 0.60, 0.65),
    ('Location 3', 'Starburst', 12, 1.0, 0.50, 0.50),
    # Add more items for Location 3...

    ('Location 4', 'Snapple', 20, 1.75, 0.85, 0.90),
    ('Location 4', 'Oreo', 16, 1.85, 0.90, 0.95),
    ('Location 4', '7UP', 10, 1.0, 0.50, 0.50),
    ('Location 4', 'Hershey\'s Kisses', 30, 1.25, 0.60, 0.65),
    ('Location 4', 'Twix', 25, 1.50, 0.75, 0.75),
    ('Location 4', 'Lay\'s', 18, 2.0, 1.0, 1.0),
    ('Location 4', 'Skittles', 22, 1.75, 0.85, 0.90),
    ('Location 4', 'Mountain Dew', 15, 1.25, 0.60, 0.65),
    ('Location 4', 'Milky Way', 12, 1.0, 0.50, 0.50),
    # Add more items for Location 4...

    ('Location 5', 'Doritos', 20, 2.25, 1.10, 1.15),
    ('Location 5', 'Hershey\'s Bar', 16, 1.85, 0.90, 0.95),
    ('Location 5', 'Fritos', 10, 1.75, 0.85, 0.90),
    ('Location 5', 'Coca-Cola', 30, 1.25, 0.60, 0.65),
    ('Location 5', 'M&M\'s', 25, 1.75, 0.85, 0.90),
    ('Location 5', 'Pringles', 18, 1.75, 0.90, 0.85),
    ('Location 5', 'Skittles', 22, 1.25, 0.60, 0.65),
    ('Location 5', 'Twix', 12, 1.75, 0.85, 0.90),
    ('Location 5', 'Pepsi', 28, 1.0, 0.50, 0.50),
    # Add more items for Location 5...

    ('Location 6', 'Ruffles', 20, 2.25, 1.10, 1.15),
    ('Location 6', 'Hershey\'s Bar', 16, 1.85, 0.90, 0.95),
    ('Location 6', 'Fritos', 10, 1.75, 0.85, 0.90),
    ('Location 6', 'Mountain Dew', 30, 1.25, 0.60, 0.65),
    ('Location 6', 'Milky Way', 25, 1.75, 0.85, 0.90),
    ('Location 6', 'Lay\'s', 18, 2.0, 1.0, 1.0),
    ('Location 6', 'Reese\'s', 22, 1.50, 0.75, 0.75),
    ('Location 6', 'Dr. Pepper', 15, 1.25, 0.60, 0.65),
    ('Location 6', 'Twizzlers', 12, 1.0, 0.50, 0.50),
    # Add more items for Location 6...

    ('Location 7', 'Cheetos', 20, 1.75, 0.85, 0.90),
    ('Location 7', 'Mars Bar', 16, 1.85, 0.90, 0.95),
    ('Location 7', 'Sprite', 10, 1.0, 0.50, 0.50),
    ('Location 7', 'Nestle Crunch', 30, 1.25, 0.60, 0.65),
    ('Location 7', 'Gummy Bears', 25, 1.50, 0.75, 0.75),
    ('Location 7', 'Sun Chips', 18, 2.0, 1.0, 1.0),
    ('Location 7', 'Butterfinger', 22, 1.75, 0.85, 0.90),
    ('Location 7', 'Fanta', 15, 1.25, 0.60, 0.65),
    ('Location 7', 'Starburst', 12, 1.0, 0.50, 0.50),
    # Add more items for Location 7...

    ('Location 8', 'Snapple', 20, 1.75, 0.85, 0.90),
    ('Location 8', 'Oreo', 16, 1.85, 0.90, 0.95),
    ('Location 8', '7UP', 10, 1.0, 0.50, 0.50),
    ('Location 8', 'Hershey\'s Kisses', 30, 1.25, 0.60, 0.65),
    ('Location 8', 'Twix', 25, 1.50, 0.75, 0.75),
    ('Location 8', 'Lay\'s', 18, 2.0, 1.0, 1.0),
    ('Location 8', 'Skittles', 22, 1.75, 0.85, 0.90),
    ('Location 8', 'Mountain Dew', 15, 1.25, 0.60, 0.65),
    ('Location 8', 'Milky Way', 12, 1.0, 0.50, 0.50),
    # Add more items for Location 8...

    ('Location 9', 'Doritos', 20, 2.25, 1.10, 1.15),
    ('Location 9', 'Hershey\'s Bar', 16, 1.85, 0.90, 0.95),
    ('Location 9', 'Fritos', 10, 1.75, 0.85, 0.90),
    ('Location 9', 'Coca-Cola', 30, 1.25, 0.60, 0.65),
    ('Location 9', 'M&M\'s', 25, 1.75, 0.85, 0.90),
    ('Location 9', 'Pringles', 18, 1.75, 0.90, 0.85),
    ('Location 9', 'Skittles', 22, 1.25, 0.60, 0.65),
    ('Location 9', 'Twix', 12, 1.75, 0.85, 0.90),
    ('Location 9', 'Pepsi', 28, 1.0, 0.50, 0.50),
    # Add more items for Location 9...

    ('Location 10', 'Ruffles', 20, 2.25, 1.10, 1.15),
    ('Location 10', 'Hershey\'s Bar', 16, 1.85, 0.90, 0.95),
    ('Location 10', 'Fritos', 10, 1.75, 0.85, 0.90),
    ('Location 10', 'Mountain Dew', 30, 1.25, 0.60, 0.65),
    ('Location 10', 'Milky Way', 25, 1.75, 0.85, 0.90),
    ('Location 10', 'Lay\'s', 18, 2.0, 1.0, 1.0),
    ('Location 10', 'Reese\'s', 22, 1.50, 0.75, 0.75),
    ('Location 10', 'Dr. Pepper', 15, 1.25, 0.60, 0.65),
    ('Location 10', 'Twizzlers', 12, 1.0, 0.50, 0.50),
    # Add more items for Location 10...
]

for item in demo_items:
    item_dict = {
        'Item Name': item[1],
        'Quantity': item[2],
        'Price': item[3],
        'Cost': item[4],
        'Profit': item[5]
    }
    location_inventory[item[0]] = pd.concat([location_inventory[item[0]], pd.DataFrame([item_dict])], ignore_index=True)

# Function to add items to the inventory
def add_item(location, name, quantity, price, cost, profit):
    global location_inventory
    item_dict = {
        'Item Name': name,
        'Quantity': quantity,
        'Price': price,
        'Cost': cost,
        'Profit': profit
    }
    location_inventory[location] = pd.concat([location_inventory[location], pd.DataFrame([item_dict])], ignore_index=True)

# Function to edit item quantity in the inventory
def edit_item(location, item_index, new_quantity):
    global location_inventory
    location_inventory[location].loc[item_index, 'Quantity'] = new_quantity

# Function to delete an item from the inventory
def delete_item(location, item_index):
    global location_inventory
    location_inventory[location] = location_inventory[location].drop(item_index).reset_index(drop=True)

# Function to display the inventory for a specific location
def show_inventory(location):
    st.write(location_inventory[location])

# Function to calculate revenue for a specific location
def calculate_revenue(location):
    revenue = (location_inventory[location]['Quantity'] * location_inventory[location]['Price']).sum()
    return revenue

# Function to calculate total cost for a specific location
def calculate_cost(location):
    cost = (location_inventory[location]['Quantity'] * location_inventory[location]['Cost']).sum()
    return cost

# Function to calculate total profit for a specific location
def calculate_profit(location):
    profit = (location_inventory[location]['Quantity'] * location_inventory[location]['Profit']).sum()
    return profit

# Sidebar for managing locations and adding/editing items
def location_management():
    st.sidebar.header('Manage Locations')
    selected_location = st.sidebar.selectbox('Select Location', locations)

    st.sidebar.header('Add/Edit Item')
    item_name = st.sidebar.text_input('Item Name')
    item_quantity = st.sidebar.number_input('Quantity', min_value=0)
    item_price = st.sidebar.number_input('Price', min_value=0.0)
    item_cost = st.sidebar.number_input('Cost', min_value=0.0)
    item_profit = st.sidebar.number_input('Profit', min_value=0.0)

    if st.sidebar.button('Add Item'):
        add_item(selected_location, item_name, item_quantity, item_price, item_cost, item_profit)
        st.success('Item added successfully!')

    st.sidebar.write('---')
    st.sidebar.header('Edit Item Quantity')
    selected_item = st.sidebar.selectbox('Select Item', location_inventory[selected_location]['Item Name'].tolist())
    new_quantity = st.sidebar.number_input('New Quantity', min_value=0)
    if st.sidebar.button('Edit Quantity'):
        item_index = location_inventory[selected_location][location_inventory[selected_location]['Item Name'] == selected_item].index[0]
        edit_item(selected_location, item_index, new_quantity)
        st.success('Quantity updated successfully!')

    st.sidebar.write('---')
    st.sidebar.header('Delete Item')
    item_to_delete = st.sidebar.selectbox('Select Item to Delete', location_inventory[selected_location]['Item Name'].tolist())
    if st.sidebar.button('Delete Item'):
        item_index = location_inventory[selected_location][location_inventory[selected_location]['Item Name'] == item_to_delete].index[0]
        delete_item(selected_location, item_index)
        st.success('Item deleted successfully!')

    # Main section to display inventory, revenue, cost, and profit
    st.header(f'{selected_location} Inventory')
    show_inventory(selected_location)

    revenue = calculate_revenue(selected_location)
    st.write(f'Revenue: ${revenue:.2f}')

    cost = calculate_cost(selected_location)
    st.write(f'Cost: ${cost:.2f}')

    profit = calculate_profit(selected_location)
    st.write(f'Profit: ${profit:.2f}')

# Function to add tasks to the to-do list
def add_task(task):
    global tasks
    tasks.append(task)

# Function to delete a task from the to-do list
def delete_task(task_index):
    global tasks
    del tasks[task_index]

# Function to display the to-do list
def show_tasks():
    st.write('## To-Do List')
    for i, task in enumerate(tasks):
        st.write(f'{i+1}. {task}')

# Adding tasks to the to-do list
tasks = ['Task 1: Finish project report', 'Task 2: Call client for follow-up', 'Task 3: Attend team meeting']

# Main navigation
pages = {
    'Vending Inventory': location_management
}

# Display the selected page based on the sidebar selection
selected_page = st.sidebar.radio('Navigation', list(pages.keys()))
pages[selected_page]()


