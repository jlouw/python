''' This module calculates the gap between burglar bars
    given the number of bars in the dimension
    and the distance between the window frames '''

CENTER_DISTANCE_BETWEEN_WINDOW_FRAMES = 884 # in millimeter
BURGLAR_BAR_SQTUBING_WIDTH = 18 # in millimeter

class OutOfRangeError(ValueError):
    '''An error class to catch OutOfRangeError errors'''
    pass

class WrongInputTypeError(ValueError):
    '''An error class to catch WrongInputTypeError errors'''
    pass

def print_separator():
    '''the function prints a seperator line of stars'''
    print('***************************************************************\n')

def printheader():
    '''the function prints the header of the script output'''
    print_separator()
    print('Calculate pane size when distance frame beams are '
          + str(CENTER_DISTANCE_BETWEEN_WINDOW_FRAMES) + 'mm apart\n')
    print_separator()

def calc_burglarbar_size(panesize, bar_width):
    '''the function calculates the burglar bar sizes'''
    barlist = []
    if isinstance(panesize, str) or isinstance(bar_width, str):
        raise WrongInputTypeError
    if panesize < 0 or bar_width < 0:
        raise OutOfRangeError
    for num_bars in range(1, 20):
        totalbarwidth = num_bars*bar_width
        remaining_space = panesize - totalbarwidth
        pane_width = remaining_space/(num_bars+1)
        if pane_width < 0:
            break
        barlist.append([num_bars, round(pane_width, 1)])
    return barlist

def print_barlist(barlist):
    '''the function prints the gap between the burlglar bars'''
    for bars in barlist:
        print('Bars: ' + str(bars[0]) + ' - Pane width: ' + str(bars[1]))

def run_main():
    '''the main function'''
    printheader()
    barlist = calc_burglarbar_size(CENTER_DISTANCE_BETWEEN_WINDOW_FRAMES,
                                   BURGLAR_BAR_SQTUBING_WIDTH)
    print_barlist(barlist)
    print('\n')
    print_separator()

run_main()
