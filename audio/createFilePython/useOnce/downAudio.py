import gdown

url = 'https://drive.google.com/drive/folders/1zti9o0Vvgp_oBrei1W_pyZmNqaZ2TZTD'
gdown.download_folder(url,output='../audioFile')