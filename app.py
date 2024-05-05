import streamlit as st
import pandas as pd

# Create a function to calculate the difference, cash owed, total credit, tip, and gratuity
def calculate_values(total_cash, payments, gratuity):
    difference = total_cash - payments - gratuity
    cash_owed = payments - total_cash if payments > total_cash else 0
    total_credit = total_cash + cash_owed
    tip = gratuity - cash_owed if gratuity > cash_owed else 0
    return difference, cash_owed, total_credit, tip

# Create a function to display the form and calculate values
def pretty_plates_cash_log():
    st.title('Pretty Plates Bar Cash Log')
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
        difference, cash_owed, total_credit, tip = calculate_values(total_cash, payments, gratuity)

        # Display calculations
        st.markdown("### Calculated Values")
        st.write(f'**Difference:** ${difference:.2f}')
        st.write(f'**Cash Owed:** ${cash_owed:.2f}')
        st.write(f'**Total Credit:** ${total_credit:.2f}')
        st.write(f'**Tip:** ${tip:.2f}')

        # Save data to a DataFrame
        data = {'Name': [name], 'Date': [date], 'Job': [job], 'Shift': [shift],
                'Total Cash': [total_cash], 'Payments': [payments], 'Gratuity': [gratuity],
                'Difference': [difference], 'Cash Owed': [cash_owed],
                'Total Credit': [total_credit], 'Tip': [tip]}
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

        # Display data in a table format
        st.markdown("### Detailed Cash Log")
        st.write(df)

        # Show individual sections of the log
        st.markdown("### Individual Log Sections")
        selected_log = st.selectbox("Select Log Section", df['Name'].unique())
        st.write(df[df['Name'] == selected_log])

pretty_plates_cash_log()
