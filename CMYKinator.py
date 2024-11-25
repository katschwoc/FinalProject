from PIL import Image, ImageEnhance, ImageFilter
import os

def main():
    """
        Main function that calls the program.
        """
    # input filename and path
    input_file = "input_image.jpg"
    watermark_path = "watermark_image.png"
    output_folder = "CMYK_Images"

    # create output folder
    # check if output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # adds watermark before converting entire image to cmyk
    watermarked_image = watermark(input_file, watermark_path, transparency=128, position=(100, 100))

    # converts image to CMYK
    cmyk_image = rgb_to_cmyk(watermarked_image)

    # adjust CMYK channels (choose value from 0-255)

    cmyk_image = adjust_cyan(cmyk_image, adjustment_value=0)   # Adjust cyan
    cmyk_image = adjust_magenta(cmyk_image, adjustment_value=0)  # Adjust magenta
    cmyk_image = adjust_yellow(cmyk_image, adjustment_value=0)  # Adjust yellow
    cmyk_image = adjust_black(cmyk_image, adjustment_value=0)    # Adjust black

    # applies adjustments
    adjusted_image = adjust_contrast(cmyk_image, factor=0) # contrast
    
    # saves the adjusted image as "filename_CMYK_Adjusted.jpg"
    output_file = os.path.join(output_folder, "filename_CMYK_Adjusted.jpg")
    adjusted_image.save(output_file)
    print(f"Image saved as {output_file}")

def watermark(image, watermark_path, transparency=128, position=(0, 0)):
    """
    Adds a watermark to the image with transparency and position options.
    Alpha channel for transparency adjustments.
    Pasts the watermark onto the original image.
    """
    # Open the background image and the watermark (foreground) image using with statement
    with (Image.open(image) as img, 
        Image.open(watermark_path) as watermark):
        
        # Resize watermark if needed (optional, resizing to 25% of the original image size)
        width = img.width // 4
        height = img.height // 4
        watermark_resized = watermark.resize((width, height))
        
        # Get the position (defaults to bottom-left)
        padding = 50
        x = padding
        y = img.height - watermark.height - padding
        
        # If watermark is not in RGBA mode, convert it to RGBA to support transparency
        if watermark_resized.mode != 'RGBA':
            watermark_resized = watermark_resized.convert("RGBA")
        
        # Modify the transparency (alpha channel) of the watermark
        watermark_data = watermark_resized.getdata()
        new_watermark_data = []
        for item in watermark_data:
            r, g, b, a = item
            a = int(a * (transparency / 255)) #adjust transparency (0-255)
            new_watermark_data.append((r, g, b, a))
        watermark_resized.putdata(new_watermark_data)

        img.paste(watermark_resized, (x, y), mask=watermark_resized.getchannel('A'))
        img.show()

        return img

def rgba_to_cmyk(image):
    """
        Converts the image from the watermark function to CMYK.
        """
    # Ensure the image is in RGB mode first
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Convert RGB to CMYK
    cmyk_image = image.convert('CMYK')

    return cmyk_image

def adjust_cyan(cmyk_image, adjustment_value):
    """
        Adjust the Cyan channel in the CMYK image.
        Adjustment_value is a value between 0 and 255.
        """
    c, m, y, k = cmyk_image.split()
    c = c.point(lambda i: i + adjustment_value)  # Adjust cyan
    c = c.point(lambda i: max(min(i, 255), 0))  # Range is between 0 and 255

    return Image.merge("CMYK", (c, m, y, k))


def adjust_magenta(cmyk_image, adjustment_value):
    """
        Adjust the Magenta channel in the CMYK image.
        Adjustment_value is a value between 0 and 255.
        """
    c, m, y, k = cmyk_image.split()
    m = m.point(lambda i: i + adjustment_value)  # Adjust magenta
    m = m.point(lambda i: max(min(i, 255), 0))  # Range is between 0 and 255

    return Image.merge("CMYK", (c, m, y, k))

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