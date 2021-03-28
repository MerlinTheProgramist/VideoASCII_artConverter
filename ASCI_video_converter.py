import time

from PIL import Image, ImageDraw, ImageFont, ImageSequence
import sys
import os
import cv2
import numpy as np


ASCII_CHARS = ["@","#","S","%","?","*","+",";",":",",","."]

def conversion (image,new_width=200):
    width, height=image.size
    ratio = height/width
    new_height = int(new_width*ratio)
    resized_image=image.resize((new_width,new_height))

    gray = resized_image.convert("L")

    pixels = gray.getdata()
    new_image_data = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])

    return (new_image_data,new_height,new_width)

def textToImage(text,height,width):
    img = Image.new('RGB', (width*11,height*13), color = 'white')
    draw = ImageDraw.Draw(img)
    draw.text((0, 0),text,(0,0,0),font = font,spacing = -4)
    return (img)


def main(frame,new_width=200):

    image = Image.fromarray(frame)
    last_time = time.time()
    new_image_data,height,width = conversion(image)
    print('ToAsci: {}'.format(time.time() - last_time))

    last_time = time.time()
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0,pixel_count, new_width))
    print('Entering: {}'.format(time.time()-last_time))

    last_time = time.time()

    imageWithText = textToImage(ascii_image,height,width)
    print('To Image with text: {}'.format(time.time()-last_time))

    return (imageWithText)


font = ImageFont.truetype("andalemo.ttf", 18)
viewPort=False

fn = './input/'+sys.argv[1]
if(os.path.exists(fn)):
    if(len(sys.argv) == 3 and sys.argv[2]=='-v'):
        viewPort=True

    videoB = cv2.VideoCapture(fn)
    fps = videoB.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')

    success, frame = videoB.read()

    img = main(frame)
    height, width = img.size
    ASCIIFrame = np.array(img)

    count = 1
    videoA = cv2.VideoWriter('./output/'+sys.argv[1],fourcc,fps,(img.size))
    videoA.write(ASCIIFrame)
    print('frame ',count)
    if(viewPort):
        cv2.imshow('ASCII Live', np.array(ASCIIFrame))
    while success:
        ASCIIFrame = np.array(main(frame))
        videoA.write(ASCIIFrame)
        if(viewPort):
            cv2.imshow('ASCII Live', np.array(ASCIIFrame))
        count += 1
        print('frame ',count)
        success, frame = videoB.read()

        if cv2.waitKey(1) == ord('q'):
            break

    videoA.release()
    cv2.destroyAllWindows()
else:
    print('file directory does not exist')

#py ASCI_video_converter.py b.avi -v
