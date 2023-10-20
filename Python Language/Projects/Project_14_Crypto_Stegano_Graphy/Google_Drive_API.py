def Google_Drive_API(files):
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload

    # Set up the service account credentials
    SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_ACCOUNT_FILE = r"E:\Codeing\Python Language\Projects\Project_14_Crypto_Stegano_Graphy\Credentials_Key.json"

    Credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    drive_service = build('drive', 'v3', credentials=Credentials)

    # Extract the folder ID from the URL
    Folder_URL = 'https://drive.google.com/drive/folders/1SFIcQWqHiQrN94XVbkePvGGpjPE6tOAG'
    Folder_ID = Folder_URL.split('/')[-1]

    # Upload a File to Google Drive within the specified folder
    File_Metadata = {
        'name': 'Music_With_Hidden_Message.wav',  # Name for the uploaded File
        'parents': [Folder_ID],  # ID of the target folder
    }
    Upload=files
    Media = MediaFileUpload(Upload, mimetype='wav')
    File = drive_service.files().create(body=File_Metadata, media_body=Media).execute()

    print(f'File ID: {File.get("id")}')




