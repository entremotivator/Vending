import streamlit as st
import pandas as pd

# Create a DataFrame to store vending inventory for multiple locations
locations = ['Location 1', 'Location 2', 'Location 3']
location_inventory = {location: pd.DataFrame(columns=['Item Name', 'Quantity', 'Price', 'Cost', 'Profit']) for location in locations}

# Demo inventory items
demo_items = [
    ('Location 1', 'Kit Kat', 20, 1.5, 0.75, 0.75),
    ('Location 1', 'Doritos', 15, 2.0, 1.0, 1.0),
    ('Location 1', 'Snickers', 10, 1.75, 0.85, 0.90),
    ('Location 1', 'Coca-Cola', 30, 1.0, 0.50, 0.50),
    ('Location 1', 'M&M\'s', 25, 1.25, 0.60, 0.65),
    ('Location 1', 'Pringles', 18, 1.75, 0.90, 0.85),
    ('Location 1', 'Skittles', 22, 1.25, 0.60, 0.65),
    ('Location 1', 'Twix', 12, 1.75, 0.85, 0.90),
    ('Location 1', 'Pepsi', 28, 1.0, 0.50, 0.50),
    ('Location 2', 'Ruffles', 20, 2.25, 1.10, 1.15),
    ('Location 2', 'Hershey\'s Bar', 16, 1.85, 0.90, 0.95),
    ('Location 2', 'Fritos', 10, 1.75, 0.85, 0.90),
    ('Location 2', 'Mountain Dew', 30, 1.25, 0.60, 0.65),
    ('Location 2', 'Milky Way', 25, 1.75, 0.85, 0.90),
    ('Location 2', 'Lay\'s', 18, 2.0, 1.0, 1.0),
    ('Location 2', 'Reese\'s', 22, 1.50, 0.75, 0.75),
    ('Location 2', 'Dr. Pepper', 15, 1.25, 0.60, 0.65),
    ('Location 2', 'Twizzlers', 12, 1.0, 0.50, 0.50),
    ('Location 3', 'Cheetos', 20, 1.75, 0.85, 0.90),
    ('Location 3', 'Mars Bar', 16, 1.85, 0.90, 0.95),
    ('Location 3', 'Sprite', 10, 1.0, 0.50, 0.50),
    ('Location 3', 'Nestle Crunch', 30, 1.25, 0.60, 0.65),
    ('Location 3', 'Gummy Bears', 25, 1.50, 0.75, 0.75),
    ('Location 3', 'Sun Chips', 18, 2.0, 1.0, 1.0),
    ('Location 3', 'Butterfinger', 22, 1.75, 0.85, 0.90),
    ('Location 3', 'Fanta', 15, 1.25, 0.60, 0.65),
    ('Location 3', 'Starburst', 12, 1.0, 0.50, 0.50),
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
