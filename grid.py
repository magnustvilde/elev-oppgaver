from random import randint as r

def make_grid():
    input_rows = int(input('Number of rows: '))
    input_cols = int(input('Number of columns: '))
    grid = []
    for row in range(input_rows):
        next_row = []
        for col in range(input_cols):
            next_row.append(r(0,1))
        grid.append(next_row)
    return grid

def print_grid(grid):
    for i in range(len(grid)):
        row = ''
        for number in grid[i]:
            row+=f'{number}\t'
        print(row)

def limits(x,y):
    x_left, x_right, y_top, y_bot = False, False, False, False
    if x==0:
        x_left = True
    if y==0:
        y_top = True
    if x==20:
        x_right = True
    if y==20:
        y_bot = True
    return x_left, x_right, y_top, y_bot

def run_on_limits(l,r,t,b):
    if (l and r and t and b):
        run_all()

def run_all():
    pass

def run_not_top():
    pass

def run_not_left():
    pass

def run_not_bot():
    pass

def run_not_right():
    pass

def run_not_left_top():
    pass

# run_on_limits(limits(x,y))


def run(x,y):
    grid = make_grid()
    print_grid(grid)
    x_l, x_r, y_t, y_b = limits(x,y)
    run_all()
    if x_l:
        pass

run(1,3)

