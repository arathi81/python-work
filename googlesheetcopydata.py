from oauth2client.service_account import ServiceAccountCredentials
import gspread

# Define the scope and credentials for accessing Google Sheets API
scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

# Authenticate with Google Sheets API
client = gspread.authorize(credentials)

# Open the source Google Sheet for reading and select the first sheet
source_sheet = client.open('sourcesheet').sheet1

# Select the first sheet
sheet = source_sheet.spreadsheet

# Get all values from the sheet
#records_data = source_sheet.get_all_records()
sheetData = source_sheet.get_all_values()

#print(records_data1)

# Print the content of the spreadsheet
for row in sheetData:
    print(row)

# Open the destination Google Sheet for writing
destination_sheet = client.open('DestinationSheetName').sheet1

# Get all values from the source sheet
#all_values = source_sheet.get_all_values()

# Iterate over each row in the source sheet
for row in sheetData:
    # Define the format for the destination sheet (modify as needed)
    formatted_row = [
        row[0],  # Example: Copying column A from source to column B in destination
        row[1],  # Example: Copying column B from source to column D in destination
        row[2],  # Example: Copying column C from source to column A in destination
        # Add more columns as needed
    ]
    
    # Append the formatted row to the destination sheet
    destination_sheet.append_row(formatted_row)

print("Data copied successfully to the destination sheet.")
