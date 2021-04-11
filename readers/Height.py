from readers.statements import section_ends
import numpy as np

def read_height(filename):
    '''
    Read a SimGrid state from a flat text file.

    Syntax for the flat text file is as follows: rows are separated by newline
    characters; columns are separated by any kind of whitespace or commas (but
    not a mix of both); comment lines begin with either "#" or "%".

    Grid state files may optionally be ended by a line starting with the string
    "!END_INIT_STATE"
    '''
    with open(filename, 'rU') as height_file:
        return parse_height_stream(height_file)

def parse_height_stream(height_stream, debug = False):
    '''
    Read a SimGrid state from a stream of strings, as might be contained in a
    state file.
    See documentation for read_grid_state for a description of the grid state
    format.
    '''
    if debug:
        print("Reading grid state... ", end = "")
    heights = []
    for line in height_stream:
        if line.startswith(section_ends['height']):
            break
        if line.startswith('#') or line.startswith('%'):
            continue
        new_row = line.strip().split()
        if len(new_row) == 0:
            continue
        if len(new_row) == 1:
            new_row = new_row[0].split(',')
        heights.append(new_row)
    heights = np.array(heights).transpose()
    #print("when read, grid_height = ")
    #print(grid_height)
    if debug:
        print("done.")
    return heights