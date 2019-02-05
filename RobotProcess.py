class RobotProcess:
    def __init__(self, roomSize, coords, patches, instructions):

        self.roomSize = roomSize
        self.coords = coords
        self.patches = patches
        self.instructions = instructions
        self.patchesCleaned = []

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

    def cleanPatch(self):
        if (self.coords in self.patches) and (self.coords not in self.patchesCleaned):
            patch = [self.coords[0], self.coords[1]]
            self.patchesCleaned.append(patch)

    def navigate(self):

        directions = {"N": self.north,
                      "E": self.east,
                      "S": self.south,
                      "W": self.west}

        for instruction in self.instructions:
            self.cleanPatch()
            directions[instruction]()

        self.cleanPatch()

    def getPosition(self):
        return self.coords

    def getPatchesCleaned(self):
        return self.patchesCleaned

    def getNoOfPatchesCleaned(self):
        return len(self.patchesCleaned)
