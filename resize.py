from PIL import Image
from os import listdir, makedirs
from os.path import isfile, join, exists

#resize based on width
def main():
  path = r'[LOCATION OF THE IMAGES]'
  new_path = r'[LOCATION OF THE IMAGES TO BE SAVED]'
  for image in listdir(path):
    print image
    try:
      im = Image.open(path+image)
      width, height = im.size
      if width > 100:
        basewidth = 100
        wpercent = (basewidth/float(width))
        hsize = int((float(height)*float(wpercent)))
        im = im.resize((basewidth,hsize), Image.ANTIALIAS)
        if not exists(new_path):
          makedirs(new_path)
      image = image.replace(' ','_')
      image = image.replace('-','_')
      im.save(new_path+'/'+image)
      print '------done'
    except:
      print 'failed'
        
                
#Resize an image
def resize():
  path = r'[LOCATION OF THE IMAGES]'
  images = ['edlogo2014.png']
  new_path = r'[LOCATION OF THE IMAGES TO BE SAVED]'
  for image in images:
    print image
      try:
        im = Image.open(path+image)
        width, height = im.size
        if width > 100:
            basewidth = 329
            wpercent = (basewidth/float(width))
            hsize = int((float(height)*float(wpercent)))
            im = im.resize((basewidth,hsize), Image.ANTIALIAS)
            if not exists(new_path):
                makedirs(new_path)
        image = image.replace(' ','_')
        image = image.replace('-','_')
        im.save(new_path+'/'+image)
        print '------done'
      except:
        print 'failed'
          
        
        
    
                

