import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import sqlite3

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Z:/Environments/car_issues/creds/rental-car-issues-5eaa526ceb89.json', scope)
client = gspread.authorize(creds)

spreadsheet = client.open("rental_car_issues")  # case-sensitive
sheet = spreadsheet.sheet1
data = sheet.get_all_records()

df = pd.DataFrame(data)
print("Data frame created.")
output_path = 'Z:/Environments/car_issues/data/rental_car_issues_output.csv'
