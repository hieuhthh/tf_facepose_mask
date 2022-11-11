import os
import shutil
from glob import glob
import cv2

try:
    os.mkdir('dataset')
    os.mkdir('dataset/mask')
    os.mkdir('dataset/nonmask')
except:
    pass

im_size = 192

print('len mask', len(os.listdir('dataset/mask')))
print('len nonmask', len(os.listdir('dataset/nonmask')))

#

from_r = '/home/lap14880/hieunmt/facepose_classify_mask/unzip/Face Mask Dataset'
to_r = 'dataset'

for stage in os.listdir(from_r):
  stage_p = from_r + '/' + stage

  mp = stage_p + '/WithMask'
  to_m = to_r + '/mask'

  for fn in os.listdir(mp):
    fpath = mp + '/' + fn
    topath = to_m + '/12k_' + fn
    shutil.copy(fpath, topath)

  mp = stage_p + '/WithoutMask'
  to_m = to_r + '/nonmask'

  for fn in os.listdir(mp):
    fpath = mp + '/' + fn
    topath = to_m + '/12k_' + fn
    shutil.copy(fpath, topath)

#

for img_path in glob('/home/lap14880/hieunmt/facepose_classify_mask/unzip/data_train/*/*'):
  img = cv2.imread(img_path) 
  img = cv2.resize(img, (im_size, im_size))
  fn = img_path.split('/')[-1]
  ftype = fn.split('_')[0]

  if ftype == 'norm':
    to_m = to_r + '/nonmask'
  else:
    to_m = to_r + '/mask'
    
  savep = to_m + '/huy_' + fn
  cv2.imwrite(savep, img)

#

stage_p = '/home/lap14880/hieunmt/facepose_classify_mask/unzip/dataset'

mp = stage_p + '/with_mask'
to_m = to_r + '/mask'

for fn in os.listdir(mp):
    fpath = mp + '/' + fn
    topath = to_m + '/det_' + fn
    shutil.copy(fpath, topath)

mp = stage_p + '/without_mask'
to_m = to_r + '/nonmask'

for fn in os.listdir(mp):
    fpath = mp + '/' + fn
    topath = to_m + '/det_' + fn
    shutil.copy(fpath, topath)

print('len mask', len(os.listdir('dataset/mask')))
print('len nonmask', len(os.listdir('dataset/nonmask')))

