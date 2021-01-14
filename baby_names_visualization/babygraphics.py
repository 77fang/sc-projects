"""
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
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
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
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    return (width-(GRAPH_MARGIN_SIZE*2))//year_index


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # Draw horizontal line.
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    x = get_x_coordinate(CANVAS_WIDTH, len(YEARS))
    # Draw straight line.
    for j in range(len(YEARS)):
        canvas.create_line(GRAPH_MARGIN_SIZE+j*x, 0, GRAPH_MARGIN_SIZE+j*x, CANVAS_HEIGHT)
        canvas.create_text(GRAPH_MARGIN_SIZE+j*x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                           text=str(YEARS[j]), anchor=tkinter.NW)


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
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # Write your code below this line
    #################################
    x = get_x_coordinate(CANVAS_WIDTH, len(YEARS))
    k = 0                                       # count numbers of searched name
    for name in lookup_names:                   # for each name in the lookup names
        k += 1
        if name in name_data:                   # find name in name_data
            year_rank = name_data[name]
            for i in range(len(YEARS)):         # time that name has to print == len(YEARS)
                a = str(YEARS[i])               # string of each year
                if a in year_rank:
                    # find x1 and y1
                    y1 = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - (GRAPH_MARGIN_SIZE * 2)) / 1000 * int(year_rank[a])
                    x1 = GRAPH_MARGIN_SIZE + i * x
                    # add text
                    canvas.create_text(GRAPH_MARGIN_SIZE + i * x + TEXT_DX,
                                       GRAPH_MARGIN_SIZE+(CANVAS_HEIGHT - (GRAPH_MARGIN_SIZE*2))/1000*int(year_rank[a]),
                                       text=name + str(year_rank[a]),
                                       anchor=tkinter.SW, fill=COLORS[(k % len(COLORS))-1])
                # if there are no data in the dictionary
                else:
                    y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    x1 = GRAPH_MARGIN_SIZE + i * x
                    canvas.create_text(GRAPH_MARGIN_SIZE + i * x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                       text=name + '*', anchor=tkinter.SW, fill=COLORS[(k % len(COLORS))-1])
                # there are only 11 lines in the graphic in each chart
                if i+1 < len(YEARS):
                    # find the second x, y to draw a line
                    b = str(YEARS[i + 1])
                    if b in year_rank:
                        y2 = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - (GRAPH_MARGIN_SIZE * 2)) / 1000 * int(year_rank[b])
                        x2 = GRAPH_MARGIN_SIZE + (i+1) * x
                    else:
                        y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                        x2 = GRAPH_MARGIN_SIZE + (i+1) * x
                    canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=COLORS[(k % len(COLORS))-1])


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
