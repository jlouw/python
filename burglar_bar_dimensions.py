CENTER_DISTANCE_BETWEEN_WINDOW_FRAMES = 884 # in millimeter
BURGLAR_BAR_SQTUBING_WIDTH = 18 # in millimeter

class OutOfRangeError(ValueError):
    pass

class WrongInputTypeError(ValueError):
    pass

def printheader():
    print('\n**********************************************************************************************\n')
    print('Calculate pane size when distance frame beams are ' + str(CENTER_DISTANCE_BETWEEN_WINDOW_FRAMES) + 'mm apart\n')
    print('**********************************************************************************************\n')


def calc_burglarbar_size(panesize, bar_width):
    barlist = []
    if isinstance(panesize, str) or isinstance(bar_width, str):
       raise WrongInputTypeError
    if panesize < 0 or bar_width < 0:
       raise OutOfRangeError
    for num_bars in range(1, 20):
        totalbarwidth=num_bars*bar_width
        remaining_space = panesize - totalbarwidth
        pane_width = remaining_space/(num_bars+1)
        if pane_width < 0:
            break
        barlist.append([num_bars, round(pane_width,1)])
    return barlist


def print_barlist(barlist):
    for bars in barlist:
        print('Bars: ' + str(bars[0]) + ' - Pane width: ' + str(bars[1]))


def print_footer():
    print('\n***********************************************************************************************\n')


def run_main():
    printheader()
    barlist = calc_burglarbar_size(CENTER_DISTANCE_BETWEEN_WINDOW_FRAMES, BURGLAR_BAR_SQTUBING_WIDTH)
    print_barlist(barlist)
    print_footer()


run_main()