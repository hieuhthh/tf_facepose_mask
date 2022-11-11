import zipfile

from utils import *

settings = get_settings()
globals().update(settings)

from_dir = path_join(route, 'download')
des = path_join(route, 'unzip')
mkdir(des)

filename = 'huy_mask_classify_data'
zip_file = path_join(from_dir, filename + '.zip')
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(des)

filename = 'face-mask-12k-images-dataset'
zip_file = path_join(from_dir, filename + '.zip')
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(des)

filename = 'face_mask_detection'
zip_file = path_join(from_dir, filename + '.zip')
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(des)