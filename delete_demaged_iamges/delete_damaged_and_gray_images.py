import os
import cv2
import imghdr
from PIL import Image,ImageChops
from multiprocessing import Pool, Value

ID = Value('i', 0)

def get_images(path):
    iamges = os.listdir(path)
    image_paths = []

    for image in iamges:
        image_path = os.path.join(path,image)
        image_paths.append(image_path)
    return image_paths


def is_grey_scale(img_path):
    try:
        im = Image.open(img_path).convert('RGB')
        w,h = im.size
        for i in range(w):
            for j in range(h):
                r, g, b = im.getpixel((i, j))
                if r != g != b:
                    return False
        return True
    except Exception:
        return True

def clean_iamges(img):
    global ID
    ID.value +=1
    if ID.value % 100 == 0:
        print(ID.value)

    im = cv2.imread(img,1)

    image_type = imghdr.what(img)
    if im is None:
        os.remove(img)
        return
        
    img_is_gray_scale = is_grey_scale(img)
        
    if  img_is_gray_scale:
        os.remove(img)
        return
    if image_type == 'png':
        
        os.rename(img, img.replace('.jpg', '.png'))
        return
        
if __name__ == '__main__':
    path  = '/home/beriani/data/lizard_blood_data'
    
    images = get_images(path)
    pool = Pool()
    pool.map(clean_iamges,images)
    print('finish')

  