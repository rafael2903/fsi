# Arquivo para rodar o modelo diretamente no terminal e tirar o overhead de rodar o jupyter notebook
import os

os.system('jupyter nbconvert model_training.ipynb --to script')
os.system('python .\model_training.py')
