# Collection of utility methods to solve the puzzles

# Reads the lines of a file into an enumerable,
# removing new line character at the end of each line
# and optionally applying additional mapping.
def readlines(file, mapper=None):
    with open(file) as f:
        lines = map(lambda x: x.rstrip('\n'), f.readlines())
        if mapper is not None:
            lines = map(mapper, lines)
        return lines