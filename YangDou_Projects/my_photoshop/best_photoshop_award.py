"""
File: best_photoshop_award.py
Name: Doris
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage


# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.3

# Controls the upper bound for black pixel
BLACK_PIXEL = 120


def main():
    """
    創作理念：每次坐電梯看到這張圖片的時候，都很好奇為什麼圖片上的人被困住了還這麼開心，
    於是習得P圖技能後，也把自己困在電梯裡面看看，結果還是不曉得原因。
    圖片來源：中華民國電梯協會
    """
    fg = SimpleImage('image_contest/Doris.jpg')
    bg = SimpleImage('image_contest/Doris_bg.jpg')
    bg.make_as_big_as(fg)
    combined_img = combine(fg, bg)
    combined_img.show()


def combine(fg, bg):
    """
    :param1 fg: SimpleImage, green screen figure image
    :param2 bg: SimpleImage, the background image
    :return fg: SimpleImage, the green screen pixels are replaced by pixels of background image
    """
    for x in range(fg.width):
        for y in range(fg.height):
            pixel_fg = fg.get_pixel(x, y)
            avg = (pixel_fg.red + pixel_fg.green + pixel_fg.blue) // 3
            total = pixel_fg.red + pixel_fg.green + pixel_fg.blue
            if pixel_fg.green > avg * THRESHOLD and total > BLACK_PIXEL:
                pixel_bg = bg.get_pixel(x, y)
                pixel_fg.red = pixel_bg.red
                pixel_fg.green = pixel_bg.green
                pixel_fg.blue = pixel_bg.blue
    return fg


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
