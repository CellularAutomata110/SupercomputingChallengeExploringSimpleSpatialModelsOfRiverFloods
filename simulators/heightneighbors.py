import collections
import itertools

def neighbours_of(list2, j, i):
    """Positions of neighbours (includes out of bounds but excludes cell itself)."""
    initiali = i

    neighbor_values = []
    neighbours = list(itertools.product(range(i-1, i+2), range(j-1, j+2)))
    neighbours.remove((i, j))

    if (initiali%2)==0:
        neighbours.remove((i-1,j+1))
        neighbours.remove((i+1,j+1))
    else:
        neighbours.remove((i-1,j-1))
        neighbours.remove((i+1,j-1))


    for indexValue in neighbours:
        if ((indexValue[0]>=0) and (indexValue[1]>=0) and (indexValue[0]<len(list2[0])) and (indexValue[1]<len(list2))):
            neighbor_values.append(list2[(indexValue[1])][(indexValue[0])])

    return neighbor_values

