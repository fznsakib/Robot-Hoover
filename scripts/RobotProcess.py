# Methods for each direction for switch case
# Include checking for wall before position update
def north(self):
    if self.coords[1] < self.roomSize[1] - 1:
        self.coords[1] += 1


def east(self):
    if self.coords[0] < self.roomSize[0] - 1:
        self.coords[0] += 1


def south(self):
    if self.coords[1] > 0:
        self.coords[1] -= 1


def west(self):
    if self.coords[0] > 0:
        self.coords[0] -= 1


# Clean patch if current position is dirty
def cleanPatch(self):
    if (self.coords in self.patches) and (self.coords not in self.patchesCleaned):
        # Break reference to class object
        patch = [self.coords[0], self.coords[1]]
        self.patchesCleaned.append(patch)


# Check to see if coordinate is in correct format
def coordChecker(coord, x, y):
    if not len(coord) == 2 and str(coord[0]).isnumeric() and str(coord[1]).isnumeric():
        return False
    # Take x, y as 0 if roomSize is being validated. No need to check if numbers within constraint so return True
    if x == 0 and y == 0:
        return True
    # Check if coordinates within room
    if coord[0] >= x or coord[1] >= y:
        return False

    # Otherwise coordinate check successful
    return True


# Class containing all input parameters and methods required
class RobotProcess:
    def __init__(self, roomSize, coords, patches, instructions):
        self.roomSize = roomSize
        self.coords = coords
        self.patches = patches
        self.instructions = instructions
        self.patchesCleaned = []

    # Main process
    def navigate(self):
        # Dictionary for switch case according to instruction
        directions = {"N": north,
                      "E": east,
                      "S": south,
                      "W": west}

        # Traverse through instructions, cleaning any dirty patches
        for instruction in self.instructions:
            cleanPatch(self)
            directions[instruction](self)

        # Check if final position needs to be cleaned
        cleanPatch(self)

    # Getter methods
    def getPosition(self):
        return self.coords

    def getPatchesCleaned(self):
        return self.patchesCleaned

    def getNoOfPatchesCleaned(self):
        return len(self.patchesCleaned)

    # Validate input
    def validate(self):
        # Initialise boundaries
        maxX = self.roomSize[0]
        maxY = self.roomSize[1]

        # Check room size
        if not coordChecker(self.roomSize, 0, 0):
            return [False, 'Room size must be numeric coordinates in the form [x, y]']

        # Check starting coords
        if not coordChecker(self.coords, maxX, maxY):
            return [False, 'Starting coordinates must be numeric coordinates in the form [x, y] and within '
                           'constraints of room size']

        # Check all patch coords
        for patch in self.patches:
            if not coordChecker(patch, maxX, maxY):
                return [False, 'All patches must be numeric coordinates in the form [x, y] and within '
                               'constraints of room size']

        # Check instructions
        allowed = "NESW"
        for instruction in self.instructions:
            if instruction not in allowed:
                return [False, 'Instructions must be a string only containing the letters N, E, S, W']

        return [True, 'Validation successful']
