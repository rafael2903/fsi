from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

class Drive:
    def __init__(self):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        self.drive = GoogleDrive(gauth)

    def upload_files_from_folder(self, folder_path, folder_id):
        file_list = os.listdir(folder_path)
        h5_files = [os.path.join(folder_path, file_name) for file_name in file_list if file_name.endswith('.h5')]
        for file_name in h5_files:
            file1 = self.drive.CreateFile({'parents': [{'id': folder_id}], 'title': file_name})
            file1.SetContentFile(file_name)
            file1.Upload()

    def download_folder_files(self, folder_id, dest_path):
        file_list = self.drive.ListFile({'q': "'{}' in parents and trashed=false".format(folder_id)}).GetList()
        for f in file_list:
            if f['mimeType'] == 'application/vnd.google-apps.folder':
                self.download_folder_files(f['id'], dest_path + '/' + f['title'])
            else:
                f_ = self.drive.CreateFile({'id': f['id']})
                if not os.path.exists(dest_path):
                    os.makedirs(dest_path)
                f_.GetContentFile(dest_path + '/' + f['title'])

    def download_dataset(self):
        self.download_folder_files('1Z_jWi3iNP8rzq7OsvcpsZ8amb0d9vUs9', 'dataset')

    def download_latest_models(self):
        self.download_folder_files('1xNq5nAD8PshJSQM5kp4Z-j9z81W1MGmD', 'saved_models')

    def upload_models(self):
        self.upload_files_from_folder('saved_models', '1xNq5nAD8PshJSQM5kp4Z-j9z81W1MGmD')

    def upload_file(self, file_path, folder_id='1xNq5nAD8PshJSQM5kp4Z-j9z81W1MGmD'):
        filename = os.path.basename(file_path)
        file1 = self.drive.CreateFile({'parents': [{'id': folder_id}], 'title': filename})
        file1.SetContentFile(file_path)
        file1.Upload()

    def download_file(self, filename, folder_id='1xNq5nAD8PshJSQM5kp4Z-j9z81W1MGmD'):
        file_list = self.drive.ListFile({'q': "'{}' in parents and trashed=false".format(folder_id)}).GetList()
        for f in file_list:
            if f['title'] == filename:
                f_ = self.drive.CreateFile({'id': f['id']})
                f_.GetContentFile(filename)

def unzip_dataset():
    import zipfile
    with zipfile.ZipFile("dataset/dataset.zip","r") as zip_ref:
        zip_ref.extractall("dataset")
