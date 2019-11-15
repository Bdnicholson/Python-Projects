import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('client_secret.json')) # json credentials you downloaded earlier
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope) # get email and key from creds

file = gspread.authorize(credentials) # authenticate with Google
sheet = file.open("Revenue by Vertical 2014 thru Sept '19").sheet1 # open sheet



# need to open both workspace's
# read column A on "master" of workspace1 and column A on workspace2
# if column A on "master" and workspace 2 match write the revenue number found in workspace 2 and write it to workspace 1.
# if a name is found in workspace2 but not workspace1, print the name and amount.
