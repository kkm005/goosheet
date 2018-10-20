pip install --upgrade oauth2client PyOpenSSL gspread
from oauth2client.service_account import ServiceAccountCredentials
import gspread
# for read-only access, use this line
scope = [“https://www.googleapis.com/auth/spreadsheets.readonly”] 
# for read-and-write access, use this line
scope = [“https://www.googleapis.com/auth/spreadsheets”]
credentials = ServiceAccountCredentials.from_json_keyfile_name(‘credentials.json’, scope)
gc = gspread.authorize(credentials)
