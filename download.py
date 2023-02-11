from utils import Drive

drive = Drive()

drive.download_latest_models()
drive.download_file('metrics.csv')
