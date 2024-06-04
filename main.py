import streamlit as st
import pandas as pd
import time

# Function to read the CSV file
def read_csv():
    # Read the CSV file into a DataFrame
    df = pd.read_csv('data.csv')
    return df

# Streamlit app
def main():
    st.title("Real-time CSV Data Visualization")

    # Read the CSV file initially
    df = read_csv()

    # Create a line chart
    chart = st.line_chart(df.set_index('time')['price'])

    # Add a placeholder for updating the chart
    placeholder = st.empty()

    # Loop to update the chart every second
    while True:
        # Read the updated CSV file
        new_df = read_csv()

        # Update the line chart
        with placeholder.container():
            chart.add_rows(new_df.set_index('time')['price'])

        # Wait for 1 second before updating again
        time.sleep(1)

# Run the app
if __name__ == "__main__":
    main()