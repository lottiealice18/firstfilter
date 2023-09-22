import pandas as pd
import streamlit as st
import datetime

# Function to process the uploaded file
def process_file(file):
    # Load the Excel file into a DataFrame
    df = pd.read_excel(file)

    # Remove rows where Country is South Africa
    # = df[df['Country'] != 'South Africa']

    # Define the columns to drop
    columns_to_drop = ['Country', 'Runner Country', 'BF Fav', 'Place', 'ISP',
                       'Hi', 'Low', 'Finish Position', 'Distance From Winner', 'Place Result', 'Lay Odd', 'Winner', 'Improving Horse', 'WFF',  'FAV Rank']

    # Drop the specified columns
    df.drop(columns_to_drop, axis=1, inplace=True)

    # Rename columns
    column_mapping = {

                      'Date Last Run': 'Days Since Last Run',
                      'OR': 'Official Rating',
                      'RPR': 'Racing Post Rating'}
    df.rename(columns=column_mapping, inplace=True)

    # Get the current date for the datestamp
    current_date = datetime.datetime.now().strftime('%Y%m%d')

    # Generate the filename with the datestamp
    filename = f'Todays_Card_{current_date}.csv'

    # Save the modified DataFrame as a new CSV file in the Downloads folder
    output_path = fr'C:\Users\liamh\Downloads\{filename}'
    df.to_csv(output_path, index=False)

    # Display a success message to the user
    st.success(f"Processed file saved as: {filename}")

# Streamlit app
def main():
    st.title("Excel File Processor")

    # File uploader
    uploaded_file = st.file_uploader("Upload Excel File", type=['xlsx'])

    if uploaded_file:
        if st.button("Process File"):
            process_file(uploaded_file)

if __name__ == "__main__":
    main()
