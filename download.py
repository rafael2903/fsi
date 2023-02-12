from utils import Drive

drive = Drive()

base_model_name = "DenseNet201" # Modelo base a ser utilizado. DenseNet201, ResNet50 ou EfficientNetB0

drive.download_latest_models(base_model_name)
drive.download_file(f'saved_models/{base_model_name}/metrics.csv', base_model_name)
