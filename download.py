import gdown

from utils import *

settings = get_settings()
globals().update(settings)

des = path_join(route, 'download')
mkdir(des)

# url = "https://drive.google.com/file/d/1WrWI9G-y7_ymPjAps_iC9xg3zF_Xs6ct/view?usp=sharing"
# output = f"{des}/huy_mask_classify_data.zip"
# gdown.download(url=url, output=output, quiet=False, fuzzy=True)

# url = "https://drive.google.com/file/d/1-B7BnxP0Ht8QuPyal_2h_3Xj3bbvylS3/view?usp=share_link"
# output = f"{des}/face-mask-12k-images-dataset.zip"
# gdown.download(url=url, output=output, quiet=False, fuzzy=True)

# url = "https://drive.google.com/file/d/1--X60MbOVAbDZZz1D-JIjl0HJOBm9hZR/view?usp=share_link"
# output = f"{des}/face_mask_detection.zip"
# gdown.download(url=url, output=output, quiet=False, fuzzy=True)

# url = "https://drive.google.com/file/d/1tX2mIRN5mTDgckdMkyGyTz093es9Q5Ty/view?usp=share_link"
# output = f"{des}/best_model_facepose_EfficientNetV1B3_192_68.h5"
# gdown.download(url=url, output=output, quiet=False, fuzzy=True)