import streamlit as st
import pandas as pd

# Create a DataFrame to store vending inventory for multiple locations
locations = ['Location 1', 'Location 2', 'Location 3']
location_inventory = {location: pd.DataFrame(columns=['Item Name', 'Quantity', 'Price', 'Cost', 'Profit']) for location in locations}

# Function to add items to the inventory
def add_item(location, name, quantity, price, cost, profit):
    global location_inventory
    location_inventory[location] = location_inventory[location].append({
        'Item Name': name,
        'Quantity': quantity,
        'Price': price,
        'Cost': cost,
        'Profit': profit
    }, ignore_index=True)

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
    if location_inventory[selected_location] is not None and not location_inventory[selected_location].empty:
        selected_item = st.sidebar.selectbox('Select Item', location_inventory[selected_location]['Item Name'].tolist())
        new_quantity = st.sidebar.number_input('New Quantity', min_value=0)
        if st.sidebar.button('Edit Quantity'):
            item_index = location_inventory[selected_location][location_inventory[selected_location]['Item Name'] == selected_item].index[0]
            edit_item(selected_location, item_index, new_quantity)
            st.success('Quantity updated successfully!')
    else:
        st.sidebar.warning('No items in inventory.')

    st.sidebar.write('---')
    st.sidebar.header('Delete Item')
    if location_inventory[selected_location] is not None and not location_inventory[selected_location].empty:
        item_to_delete = st.sidebar.selectbox('Select Item to Delete', location_inventory[selected_location]['Item Name'].tolist())
        if st.sidebar.button('Delete Item'):
            item_index = location_inventory[selected_location][location_inventory[selected_location]['Item Name'] == item_to_delete].index[0]
            delete_item(selected_location, item_index)
            st.success('Item deleted successfully!')
    else:
        st.sidebar.warning('No items in inventory.')

    # Main section to display inventory, revenue, cost, and profit
    st.header(f'{selected_location} Inventory')
    if location_inventory[selected_location] is not None and not location_inventory[selected_location].empty:
        show_inventory(selected_location)

        revenue = calculate_revenue(selected_location)
        st.write(f'Revenue: ${revenue:.2f}')

        cost = calculate_cost(selected_location)
        st.write(f'Cost: ${cost:.2f}')

        profit = calculate_profit(selected_location)
        st.write(f'Profit: ${profit:.2f}')
    else:
        st.warning('No items in inventory.')

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

# Adding 25 product examples to the inventory
for i in range(25):
    add_item('Location 1', f'Product {i + 1}', 100, 10.0, 7.0, 3.0)

# Main navigation
pages = {
    'Vending Inventory': location_management
}

# Display the selected page based on the sidebar selection
selected_page = st.sidebar.radio('Navigation', list(pages.keys()))
pages[selected_page]()
