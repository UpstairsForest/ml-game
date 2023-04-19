# RGB values
import json

background_colour = (0, 0, 0)
text_colour = (175, 175, 175)

green = (150, 255, 70)
red = (255, 100, 50)
gray = (30, 30, 30)

# sizes
dis_x = 900
dis_y = 800
step = 50
border_width = 8

# game speed
fps = 8

# board
board_data = json.load(open("fixtures/board_data.json", "r"))


# checks:
def checks():
    if (dis_x % step, dis_y % step) != (0, 0):
        print(f"{__name__}ugly grid:step ratio")
    _ = None
    for i in range(len(board_data)):
        if _ is None:
            _ = len(board_data[i])
        elif _ != len(board_data[i]):
            print(f"{__name__}: inconsistent board dimensions for rows {i - 1}:{_} and {i}:{len(board_data[i])}")


checks()
