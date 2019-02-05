# Class containing all input parameters and methods required
class RobotProcess:
    def __init__(self, roomSize, coords, patches, instructions):

        self.roomSize = roomSize
        self.coords = coords
        self.patches = patches
        self.instructions = instructions
        self.patchesCleaned = []

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

    # Main process
    def navigate(self):

        # Dictionary for switch case according to instruction
        directions = {"N": self.north,
                      "E": self.east,
                      "S": self.south,
                      "W": self.west}

        # Traverse through instructions, cleaning any dirty patches
        for instruction in self.instructions:
            self.cleanPatch()
            directions[instruction]()

        # Check if final position needs to be cleaned
        self.cleanPatch()

    # Getter methods
    def getPosition(self):
        return self.coords

    def getPatchesCleaned(self):
        return self.patchesCleaned

    def getNoOfPatchesCleaned(self):
        return len(self.patchesCleaned)
