import time

from PIL import Image, ImageDraw, ImageFont, ImageSequence
import sys
import os
import PIL.Image
from os import system
import cv2
import numpy as np


ASCII_CHARS=["@","#","S","%","?","*","+",";",":",",","."]





def resize_image(image,new_width=200):
    width, height=image.size
    ratio=height/width
    new_height=int(new_width*ratio)
    resized_image=image.resize((new_width,new_height))


    return(resized_image,new_height,new_width)

def grayify(image):
    grayscale_image=image.convert("L")
    return(grayscale_image)

def pixels_to_ascii(image):
    pixels=image.getdata()
    characters="".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)

def textToImage(text,height,width):
    img = Image.new('RGB', (width*11,height*13), color = 'white')
    draw = ImageDraw.Draw(img)
    draw.text((0, 0),text,(0,0,0),font=font,spacing=-4)
    return (img)


def main(frame,new_width=200):

    image = Image.fromarray(frame)
    last_time=time.time()
    resized,height,width=resize_image(image)
    new_image_data=pixels_to_ascii(grayify(resized))
    print('ToAsci: {}'.format(time.time()-last_time))

    last_time=time.time()
    pixel_count=len(new_image_data)
    ascii_image="\n".join(new_image_data[i:(i+new_width)] for i in range(0,pixel_count, new_width))
    print('Entering: {}'.format(time.time()-last_time))

    last_time=time.time()

    imageWithText=textToImage(ascii_image,height,width)
    print('To Image with text: {}'.format(time.time()-last_time))

    cv2.imshow('textIMG', np.array(imageWithText))
    return imageWithText


#start
#if len(sys.argv) ==5:
    #font = ImageFont.truetype("andalemo.ttf", int(sys.argv[2]))

font = ImageFont.truetype("andalemo.ttf", 18)


fn ='./input/'+sys.argv[1]
if(os.path.exists(fn)):
    #SaveName=sys.arvg[]#-------------------------------------------------------------------------

    videoB=cv2.VideoCapture(fn)
    fps=videoB.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')

    success, frame = videoB.read()

    img=main(frame)
    height, width = img.size
    ASCIIFrame=np.array(img)

    videoA=cv2.VideoWriter('./output/'+sys.argv[1],fourcc,fps,(img.size))
    videoA.write(ASCIIFrame)
    count=1
    while success:
        #cv2.imshow('terdown',frame)
        videoA.write(np.array(main(frame)))
        print('frame ',count)
        count+=1
        success, frame = videoB.read()

        if cv2.waitKey(1) == ord('q'):
            break

    videoA.release()
    cv2.destroyAllWindows()
else:
    print('file directory does not exist')

#py ASCI_video_converter.py ./images/v.mp4
