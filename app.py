import streamlit as st
import pandas as pd

# Create a function to calculate the difference
def calculate_difference(total_cash, payments, gratuity):
    return total_cash - payments - gratuity

# Create a function to display the form and calculate the difference
def pretty_plates_cash_log():
    st.title('Pretti Plates Bar Cash Log')
    st.markdown("Welcome to the Pretty Plates Bar Cash Log! Please fill out the following details:")

    # Define form inputs
    with st.form(key='pretty_plates_cash_log_form'):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input('Name')
            date = st.date_input('Date')
            job = st.selectbox('Job', ['Bartender', 'Waitstaff', 'Manager'])
        with col2:
            shift = st.selectbox('Shift', ['Morning', 'Afternoon', 'Evening'])
            total_cash = st.number_input('Total Cash', step=0.01)
            payments = st.number_input('Payments', step=0.01)
            gratuity = st.number_input('Gratuity', step=0.01)
        submit_button = st.form_submit_button('Submit')

    # Process form submission
    if submit_button:
        difference = calculate_difference(total_cash, payments, gratuity)
        st.write(f'**Difference:** ${difference:.2f}')

        # Save data to a DataFrame
        data = {'Name': [name], 'Date': [date], 'Job': [job], 'Shift': [shift],
                'Total Cash': [total_cash], 'Payments': [payments], 'Gratuity': [gratuity],
                'Difference': [difference]}
        df = pd.DataFrame(data)
        
        st.markdown("### Cash Log Details")
        st.write(df)

        # Display summary statistics
        st.markdown("### Summary Statistics")
        summary_data = df.describe()
        st.write(summary_data)

        # Display a line chart of total cash over time
        st.markdown("### Total Cash Trend")
        st.line_chart(df.set_index('Date')['Total Cash'])

pretty_plates_cash_log()
