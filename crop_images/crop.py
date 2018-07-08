import cv2
import dlib
import numpy as np
import os
from multiprocessing import Pool, Value
ID = Value('i', 0)

def get_images(path):
    path = path
    images = []
    image_names = os.listdir(path)
    for img in image_names:
        images.append(os.path.join(path,img))
        
    return images
def crop_image(image):
    global ID
    ID.value +=1
    # if ID.value % 100 == 0:
    print(ID.value)


    image_name = image
    path = '/home/beriani/data/test/'
    
    image = cv2.imread(image)

    detector = dlib.get_frontal_face_detector()
    number_of_faces = len(detector(image))
    if number_of_faces < 3:

        left_half = image[0:int(image.shape[0]), 0: int(image.shape[1]/2)]
        right_half = image[0:int(image.shape[0]),  int(image.shape[1]/2) :  int(image.shape[1])]

        left_iamge_path = os.path.join(path, image_name.split('/')[-1].replace('.jpg','left.jpg' ))
        right_iamge_path = os.path.join(path, image_name.split('/')[-1].replace('.jpg', 'right.jpg'))
        
        cv2.imwrite(left_iamge_path, left_half)
        cv2.imwrite(right_iamge_path, right_half)
        
    if number_of_faces == 3:
        one_third = int(image.shape[1]/3)
        
        left = image[0:int(image.shape[0]), 0: one_third]
        right = image[0:int(image.shape[0]),  one_third * 2:  int(image.shape[1])]
        middle = image[0:int(image.shape[0]), one_third: one_third*2]
        
        left_iamge_path = os.path.join(path, image_name.split('/')[-1].replace('.jpg','left.jpg' ))
        right_iamge_path = os.path.join(path, image_name.split('/')[-1].replace('.jpg', 'right.jpg'))
        middle_iamge_path = os.path.join(path, image_name.split('/')[-1].replace('.jpg', 'middle.jpg'))
        
        cv2.imwrite(left_iamge_path, left)
        cv2.imwrite(right_iamge_path, right)
        cv2.imwrite(middle_iamge_path, middle)
        
    if number_of_faces == 4:
        quarter = int(image.shape[1]/4)

        left = image[0:int(image.shape[0]), 0 : quarter]
        right = image[0:int(image.shape[0]),  quarter * 3 :  int(image.shape[1])]
        second = image[0:int(image.shape[0]), quarter : quarter * 2]
        third = image[0:int(image.shape[0]), quarter * 2 : quarter * 3]

        left_iamge_path = os.path.join(path, image_name.split('/')[-1].replace('.jpg','left.jpg' ))
        right_iamge_path = os.path.join(path, image_name.split('/')[-1].replace('.jpg', 'right.jpg'))
        third_iamge_path = os.path.join(path, image_name.split('/')[-1].replace('.jpg', 'third.jpg'))
        second_iamge_path = os.path.join(path, image_name.split('/')[-1].replace('.jpg', 'second.jpg'))


        cv2.imwrite(left_iamge_path, left)
        cv2.imwrite(right_iamge_path, right)
        cv2.imwrite(third_iamge_path, third)
        cv2.imwrite(second_iamge_path, second)

        
if __name__ == '__main__':
    
    path = '/home/beriani/data/avatartest/'
    images = get_images(path)
    pool = Pool(processes = 4)
    pool.map(crop_image, images)
    
    