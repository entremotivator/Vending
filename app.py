import streamlit as st
import pandas as pd

# Create a DataFrame to store vending inventory for multiple locations
locations = ['Location 1', 'Location 2', 'Location 3']
location_inventory = {location: pd.DataFrame(columns=['Item Name', 'Quantity', 'Price']) for location in locations}

# Function to add items to the inventory
def add_item(location, name, quantity, price):
    global location_inventory
    location_inventory[location] = location_inventory[location].append({
        'Item Name': name,
        'Quantity': quantity,
        'Price': price
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

# Sidebar for managing locations and adding/editing items
def location_management():
    st.sidebar.header('Manage Locations')
    selected_location = st.sidebar.selectbox('Select Location', locations)

    st.sidebar.header('Add/Edit Item')
    item_name = st.sidebar.text_input('Item Name')
    item_quantity = st.sidebar.number_input('Quantity', min_value=0)
    item_price = st.sidebar.number_input('Price', min_value=0.0)

    if st.sidebar.button('Add Item'):
        add_item(selected_location, item_name, item_quantity, item_price)
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

    # Main section to display inventory and revenue
    st.header(f'{selected_location} Inventory')
    show_inventory(selected_location)

    revenue = calculate_revenue(selected_location)
    st.write(f'Revenue: ${revenue:.2f}')

# Adding a to-do checklist page
def to_do_list():
    st.sidebar.header('To-Do List')

    # Create an empty list to store tasks
    tasks = []

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

    # Sidebar for adding tasks
    task_input = st.sidebar.text_input('Add Task')
    if st.sidebar.button('Add Task'):
        add_task(task_input)
        st.success('Task added successfully!')

    # Displaying the to-do list page
    show_tasks()

    # Functionality to delete tasks
    task_to_delete = st.sidebar.selectbox('Select Task to Delete', tasks, key='delete_task')
    if st.sidebar.button('Delete Task'):
        task_index = tasks.index(task_to_delete)
        delete_task(task_index)
        st.success('Task deleted successfully!')

# Main navigation
pages = {
    'Vending Inventory': location_management,
    'To-Do List': to_do_list
}

# Display the selected page based on the sidebar selection
selected_page = st.sidebar.radio('Navigation', list(pages.keys()))
pages[selected_page]()
