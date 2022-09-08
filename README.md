# VideoASCII_artConverter

## General info
Simple python script for converting video file to ASCII art video file!

## Works like that:
this took around 3 sec for every frame <br/>
![sampleInput](https://user-images.githubusercontent.com/69404231/112722866-159e2f80-8f0c-11eb-990f-9e0e252daee0.mp4)   
![sampleUotput](https://user-images.githubusercontent.com/69404231/112723125-56e30f00-8f0d-11eb-9039-0453582832b9.mp4)   

## How to use 
You run a the py script with following arguments: <br/>
  ```bash
  python3 ASCI_video_converter.py video.avi -v
  ```

Save your video file in to `input` folder and script outputs in in output folder with the same name <br/>
If you wish to watch your frames converting live, add `-v` flag
  
 I will try to improove it over time and add new functionality, Im open on submission <br/>
  
## Note
You must to have installed libs: 
* Pillow (pip install Pillow)
* OpenCV (pip install opencv-python)
* numpy  (pip install numpy)

