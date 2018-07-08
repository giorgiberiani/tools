
import time, urllib.parse, os
import pandas as pd
from multiprocessing import Pool, Value
from urllib.request import urlretrieve
ID = Value('i', 0)

def get_image(image_link):
    try:
        global ID
        ID.value+=1
        if ID.value % 100 == 0:
            print('------------------------------{}-----------------------------'.format(ID.value))
        image_link = image_link[0]
        link = image_link.split('/')[-1].split('.')
        id = link[0]
        type = link[1]

        image_local_path ='/home/beriani/data/lizard_blood_data/{}'.format(id) + '.' + type
        print(image_local_path)
        urlretrieve(image_link, image_local_path)

    except Exception as ex:
        print(ex)

if __name__ == '__main__':
        
    image_links = pd.read_table('/home/beriani/data/onoffimages.txt', delimiter='\n')
    image_links =  image_links.values.tolist()
    pool = Pool()
    pool.map(get_image,  image_links)