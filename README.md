# Phone Number Verifier Google Sheets Script

This Python script verifies phone numbers in a Google Sheet using an external API (APILayer). It checks if the phone number is a mobile or landline and updates the relevant columns in the Google Sheet with the formatted number.

## Prerequisites

Before running the script, make sure you have the following:

1. **Python**: Ensure that Python 3 is installed on your system.
2. **Google API Setup**:
   - Set up a project on Google Cloud and enable the Google Sheets API.
   - Download the `credentials.json` file and save it in the project directory.
3. **APILayer API Key**: Get an API key from [APILayer](https://apilayer.com/).
4. **Configuration**: Adjust the constants accordingly in the main.py file.
5. **Python Packages**: Install the necessary dependencies by running:
   ```bash
   pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
