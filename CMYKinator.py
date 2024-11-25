from PIL import Image, ImageEnhance, ImageFilter
import os

def main():
# main function that runs the program
# opens file
# create output folder 
# check if output folder exists
# applies adjustments
# saves the adjusted image as "filename_CMYK_Adjusted.jpg"



def rgb_to_cmyk():
# check image's color profile
# function converts rgb image to cmyk

 """
    Converts an RGB image to CMYK.
    """
    if image.mode != 'RGB':
        raise ValueError("Input image must be in RGB mode")
    
    # Convert RGB to CMYK
    cmyk_image = image.convert("CMYK")
    return cmyk_image

def watermark():
# function overlays one image on top of the converted cmyk image
# function includes a transparency option to adjust the overlaid image
# function resizes overlaid image
# function includes placement option 


def adjust_cyan():
# after rgb_to_cmyk converts image
# function breaks apart cmyk channels and adjusts the cyan channel


def adjust_magenta():
# after rgb_to_cmyk converts image
# function breaks apart cmyk channels and adjusts the magenta channel


def adjust_yellow():
# after rgb_to_cmyk converts image
# function breaks apart cmyk channels and adjusts the yellow channel


def adjust_black():
# after rgb_to_cmyk converts image
# function breaks apart cmyk channels and adjusts the black/k channel


def resize_img():
# after rgb_to_cmyk converts image
# function resizes image


def adjust_contrast():
# after rgb_to_cmyk converts image
# function adjusts contrast of image


def batch_render():
# optional function not needed if just one image is being manipulated
# if more than one image, use function. if not only one image, save file 
# after rgb_to_cmyk converts image and after image manipulations are completed
# function batch renders images with similar file names such as "artworkRGB.jpg and drawingRGB.jpg"
# function saves rendered images to new folder called "CMYK Images"




if __name__ == "__main__":
    main()