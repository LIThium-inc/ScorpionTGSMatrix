def remove_zero(array):
    while 0.0 in array:
        array.remove(0.0)


# noinspection t
def create_energy_matrix(matrix, array, pixels_per_event=1, min_filter=0.0):
    """Create a matrix of energy distribution.

        @param: matrix A matrix to save parameters
        @param: array A string with energy data
        @param: pixels_per_event The count of activated pixels per one event (default 1)
        @param: min_filter Allows to save data only with energy above filter parameter (default 0.0)

        """

    zeroless_x, array_x = array[:8], array[:8]
    zeroless_y, array_y = array[8:], array[8:]
    remove_zero(zeroless_x)
    remove_zero(zeroless_y)
    if pixels_per_event > 1:
        if ((len(zeroless_x) == pixels_per_event or len(zeroless_y) == pixels_per_event)
                and zeroless_x[0] >= min_filter and zeroless_y[0] >= min_filter):
            if len(zeroless_x) == pixels_per_event and len(zeroless_y) == 1:
                for j in range(len(zeroless_x)):
                    x = array_x.index(zeroless_x[j])
                    y = array_y.index(zeroless_y[0])
                    matrix[x, y] = matrix[x, y] + zeroless_x[j]
            if len(zeroless_y) == pixels_per_event and len(zeroless_x) == 1:
                for j in range(len(zeroless_y)):
                    x = array_x.index(zeroless_x[0])
                    y = array_y.index(zeroless_y[j])
                    matrix[x, y] = matrix[x, y] + zeroless_y[j]
    elif pixels_per_event == 1:
        if len(zeroless_x) == len(zeroless_y) == 1 and zeroless_x[0] >= min_filter and zeroless_y[0] >= min_filter:
            x = array_x.index(zeroless_x[0])
            y = array_y.index(zeroless_y[0])
            matrix[x, y] = matrix[x, y] + zeroless_x[0]


# noinspection t
def create_events_count_matrix(matrix, array, pixels_per_event=1, min_filter=0.0):
    """Create a matrix of count distribution.

        @param: matrix A matrix to save parameters
        @param: array A string with energy data
        @param: pixels_per_event The count of activated pixels per one event (default 1)
        @param: min_filter Allows to save data only with energy above filter parameter (default 0.0)

        """
    zeroless_x, array_x = array[:8], array[:8]
    zeroless_y, array_y = array[8:], array[8:]
    remove_zero(zeroless_x)
    remove_zero(zeroless_y)
    if pixels_per_event > 1:
        if ((len(zeroless_x) == pixels_per_event or len(zeroless_y) == pixels_per_event)
                and zeroless_x[0] >= min_filter and zeroless_y[0] >= min_filter):
            if len(zeroless_x) == pixels_per_event and len(zeroless_y) == 1:
                for j in range(len(zeroless_x)):
                    x = array_x.index(zeroless_x[j])
                    y = array_y.index(zeroless_y[0])
                    matrix[x, y] = matrix[x, y] + 1
            if len(zeroless_y) == pixels_per_event and len(zeroless_x) == 1:
                for j in range(len(zeroless_y)):
                    x = array_x.index(zeroless_x[0])
                    y = array_y.index(zeroless_y[j])
                    matrix[x, y] = matrix[x, y] + 1
    elif pixels_per_event == 1:
        if len(zeroless_x) == len(zeroless_y) == 1 and zeroless_x[0] >= min_filter and zeroless_y[0] >= min_filter:
            x = array_x.index(zeroless_x[0])
            y = array_y.index(zeroless_y[0])
            matrix[x, y] = matrix[x, y] + 1

