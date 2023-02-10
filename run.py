import os

os.system('jupyter nbconvert model.ipynb --to script')
os.system('python .\model.py')
