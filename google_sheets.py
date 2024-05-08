import os
from verifier import verify_number
from format_number import format_number
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SPREADSHEET_ID = '1SCWW2SugKsNoyzoAKYwDUxGdiOmEyRuD_y4gv8qmtqI'

def main():
    credentials = None
    if os.path.exists('token.json'):
        credentials = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            credentials = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(credentials.to_json())


    try:
        service = build('sheets', 'v4', credentials = credentials)
        sheets = service.spreadsheets()

        for row in range(2,100): # Number of rows
            result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f'Lapas1!A{row}').execute()
            values = result.get('values')
            if not values:
                continue

            num1 = values[0][0]
            mobile_count = 0
            landline_count = 0
            if num1 != 'Not found':  
                for i in num1.split(','):
                    if mobile_count > 0 and landline_count > 0:
                        break
                    number = format_number(i)
                    dictionary = verify_number(number)
                    if dictionary['line_type'] == 'mobile' and mobile_count == 0:
                        sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f'Lapas1!C{row}',
                                valueInputOption='USER_ENTERED', body = {'values':[[f'\'+{number}']]}).execute()
                        mobile_count += 1
                    if dictionary['line_type'] == 'landline' and landline_count == 0:
                        sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f'Lapas1!B{row}',
                                    valueInputOption='USER_ENTERED', body = {'values':[[f'\'+{number}']]}).execute()
                        landline_count += 1
                

            
    except HttpError as error:
        print(error)


if  __name__ == '__main__':
    main()
