import sys
import os
from PIL import Image

#grab first and second argument
path = sys.argv[1]
directory = sys.argv[2]

#check is new/ exists, if not create
if not os.path.exists(directory):
    os.makedirs(directory)

#loop through Pokedex
for filename in os.listdir(path):
    #convert images to png
    clean_name = os.path.splitext(filename)[0]
    img = Image.open('{}{}'.format(path, filename))
    #save to the new folder
    img.save(f'{directory}/{clean_name}.png', 'png')
    print('all done!')
