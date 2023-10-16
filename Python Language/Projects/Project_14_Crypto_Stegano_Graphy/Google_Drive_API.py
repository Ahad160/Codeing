from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Set up the service account credentials
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = r"E:\Codeing\Python Language\Projects\Project_14_Crypto_Stegano_Graphy\Credentials.json"

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
drive_service = build('drive', 'v3', credentials=credentials)

# Define the folder ID where you want to upload the file
folder_id = '1SFIcQWqHiQrN94XVbkePvGGpjPE6tOAG'

# Upload a file to Google Drive within the specified folder
file_metadata = {
    'name': 'example.txt',  # Name for the uploaded file
    'parents': [folder_id],  # ID of the target folder
}
media = MediaFileUpload('E:\Codeing\Python Language\Projects\Project_14_Crypto_Stegano_Graphy\Project-14_Encrypting.key', mimetype='text/plain')
file = drive_service.files().create(body=file_metadata, media_body=media).execute()

print(f'File ID: {file.get("id")}')
