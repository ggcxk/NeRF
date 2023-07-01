import cv2
import os
from PIL import Image


def downSample(images_path,output_dir,factor = 8):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    images_list = os.listdir(images_path)
    img = Image.open(images_path + images_list[0])
    (W,H) = (img.width,img.height) #[W,H]
    print("image_size : ",(W ,H))
    for image_name in images_list:
        img = cv2.imread(images_path+image_name)
        img_resize = cv2.resize(img, (int(W/factor), int(H/factor)))
        cv2.imwrite(output_dir + image_name, img_resize)
        print(image_name , " done")
    print("all images done")


if __name__ == "__main__":
    images_path = '/kaggle/working/mynerf/data/COLMAP_test/images/' # 原图路径
    output_dir = '/kaggle/working/mynerf/data/COLMAP_test/images_8/' # resize后路径
    downSample(images_path,output_dir)