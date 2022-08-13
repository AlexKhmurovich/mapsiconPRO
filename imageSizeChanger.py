import os
from pathlib import Path

from PIL import Image

countries = ['COUNTRIES_GO_HERE'] #ex: 'by'

sizes = [16,24,32,48,64,80,96,128,256,512,1024]


for country in countries:
     path = Path(f'FOLDER_WITH_COUNTRIES_GOES_HERE/{country}'
     path.mkdir()
     image = Image.open('IMAGE_PATH_GOES_HERE')

     for imgSize in sizes:
         new_image = image.resize((imgSize,imgSize))
         new_image.save(f'{path}/{imgSize}.png', optimize=True, quality=30)
