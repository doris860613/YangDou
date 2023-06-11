"""
File: babygraphics.py
Name: Doris
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_coordinate = ((width-GRAPH_MARGIN_SIZE * 2) / len(YEARS)) * year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # Horizontal line on the top
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    # Horizontal line at the bottom
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    # Vertical lines
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)  # To get the x coordinate of year index of YEARS list
        canvas.create_line(GRAPH_MARGIN_SIZE + x, 0, GRAPH_MARGIN_SIZE + x, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(GRAPH_MARGIN_SIZE + x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i],
                           anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    lookup_names_count = 0  # Count the number of names to be viewed by all users
    for lookup_name in lookup_names:
        previous_x_coordinate = 0
        previous_y_coordinate = 0
        year_index = 0  # Represent the year index of YEARS list
        color = COLORS[lookup_names_count % len(COLORS)]  # Use the remainder as the index of COLOR's list
        for year in YEARS:
            current_x_coordinate = get_x_coordinate(CANVAS_WIDTH, year_index) + GRAPH_MARGIN_SIZE
            if str(year) in name_data[lookup_name]:
                current_y_coordinate = GRAPH_MARGIN_SIZE + ((CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / (MAX_RANK-1))\
                                       * int(name_data[lookup_name][str(year)])
                canvas.create_text(current_x_coordinate + TEXT_DX, current_y_coordinate,
                                   text=f'{lookup_name} {name_data[lookup_name][str(year)]}', anchor=tkinter.SW,
                                   fill=color)
            else:
                current_y_coordinate = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                canvas.create_text(current_x_coordinate + TEXT_DX, current_y_coordinate,
                                   text=f'{lookup_name} *', anchor=tkinter.SW, fill=color)
            if year_index > 0:  # Draw the line start from the second year(two points that can be connected into a line)
                canvas.create_line(previous_x_coordinate, previous_y_coordinate, current_x_coordinate,
                                   current_y_coordinate, width=LINE_WIDTH, fill=color)
            year_index += 1
            # Each loop reassign the previous x,y coordinate to the current x,y coordinate
            previous_x_coordinate = current_x_coordinate
            previous_y_coordinate = current_y_coordinate
        lookup_names_count += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
