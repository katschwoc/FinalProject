from PIL import Image, ImageEnhance, ImageFilter
import os

def main():
    """
    Main function that runs the program.
    """
    input_file = "XianleWar_RGB.png"
    watermark_path = "watermark.png"
    output_folder = "CMYK_Images"

    os.makedirs(output_folder, exist_ok=True)

    with Image.open(input_file) as image:
        # Resize image
        resized_image = resize_img(image, height=720)

        # Add watermark before converting to CMYK
        watermarked_image = watermark(resized_image, watermark_path,transparency=50, position=(0, 0)) #adjust transparency and position

        # Convert image to CMYK
        cmyk_image = rgba_to_cmyk(watermarked_image)

        # Adjust CMYK channels (choose values from 0-255)
        cmyk_image = adjust_cyan(cmyk_image, adjustment_value=0)   # Adjust cyan
        cmyk_image = adjust_magenta(cmyk_image, adjustment_value=0)  # Adjust magenta
        cmyk_image = adjust_yellow(cmyk_image, adjustment_value=0)  # Adjust yellow
        cmyk_image = adjust_black(cmyk_image, adjustment_value=0)    # Adjust black
        
        # Save the adjusted image as TIFF in CMYK mode
        output_file = os.path.join(output_folder, f"{os.path.splitext(input_file)[0]}_CMYK_Adjusted.tiff")
        cmyk_image.save(output_file, mode="CMYK")
        cmyk_image.show()
        print(f"Image saved as {output_file}")

def watermark(image, watermark_path, transparency=128, position=(0, 0)):
    """
    Adds a watermark to the image with transparency and position options.
    Alpha channel for transparency adjustments.
    Pastes the watermark onto the original image.
    """
    with Image.open(watermark_path) as watermark:
        
        aspect_ratio = watermark.width / watermark.height
        resize_height = int(image.height * 0.15)  # Resize watermark to 25% of image height
        resize_width = int(resize_height * aspect_ratio)
        watermark_resized = watermark.resize((resize_width, resize_height))

        # Watermark position (defaults to bottom-left)
        padding = 50
        x = position[0] if position[0] else padding
        y = position[1] if position[1] else image.height - watermark_resized.height - padding

        if watermark_resized.mode != 'RGBA':
            watermark_resized = watermark_resized.convert("RGBA")

        watermark_data = watermark_resized.getdata()
        new_watermark_data = []
        for item in watermark_data:
            r, g, b, a = item
            a = int(a * (transparency / 150))  # Adjust transparency (0-255)
            new_watermark_data.append((r, g, b, a))
        watermark_resized.putdata(new_watermark_data)

        image.paste(watermark_resized, (x, y), mask=watermark_resized.getchannel('A'))

        return image

def rgba_to_cmyk(image):
    """
    Converts the image from RGBA to CMYK.
    """
    if image.mode != 'RGB':
        image = image.convert('RGB')

    cmyk_image = image.convert('CMYK')

    return cmyk_image

def adjust_cyan(cmyk_image, adjustment_value):
    """
    Adjust the Cyan channel in the CMYK image.
    Adjustment_value is a value between 0 and 255.
    """
    c, m, y, k = cmyk_image.split()
    c = c.point(lambda i: i + adjustment_value)
    c = c.point(lambda i: max(min(i, 255), 0)) 

    return Image.merge("CMYK", (c, m, y, k))

def adjust_magenta(cmyk_image, adjustment_value):
    """
    Adjust the Magenta channel in the CMYK image.
    Adjustment_value is a value between 0 and 255.
    """
    c, m, y, k = cmyk_image.split()
    m = m.point(lambda i: i + adjustment_value) 
    m = m.point(lambda i: max(min(i, 255), 0))  

    return Image.merge("CMYK", (c, m, y, k))

def adjust_yellow(cmyk_image, adjustment_value):
    """
    Adjust the Yellow channel in the CMYK image.
    Adjustment_value is a value between 0 and 255.
    """
    c, m, y, k = cmyk_image.split()
    y = y.point(lambda i: i + adjustment_value)  
    y = y.point(lambda i: max(min(i, 255), 0))  

    return Image.merge("CMYK", (c, m, y, k))

def adjust_black(cmyk_image, adjustment_value):
    """
    Adjust the Black channel in the CMYK image.
    Adjustment_value is a value between 0 and 255.
    """
    c, m, y, k = cmyk_image.split()
    k = k.point(lambda i: i + adjustment_value)  
    k = k.point(lambda i: max(min(i, 255), 0)) 

    return Image.merge("CMYK", (c, m, y, k))

def resize_img(img, height):
    """
    Resize the image while maintaining aspect ratio.
    """
    aspect_ratio = img.width / img.height
    resize_width = int(height * aspect_ratio)
    resized_img = img.resize((resize_width, height))

    return resized_img

if __name__ == "__main__":
    main()