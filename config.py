import json

# RGB values
background_colour = (0, 0, 0)
text_colour = (175, 175, 175)

green = (41, 135, 31)
red = (122, 20, 6)
gray = (38, 34, 32)
white = (175, 175, 175)

# sizes
board_data = json.load(open("fixtures/board_data.json", "r"))
dis_x = 400
dis_y = dis_x
step = dis_x * 0.9 // len(board_data[0])
border_width = 8

# game speed
fps = 1


# checks:
def checks():
    _ = None
    for i in range(len(board_data)):
        if _ is None:
            _ = len(board_data[i])
        elif _ != len(board_data[i]):
            print(f"{__name__}: inconsistent board dimensions for rows {i - 1}:{_} and {i}:{len(board_data[i])}")


checks()
