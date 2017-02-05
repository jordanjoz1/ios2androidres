class ResourceType(object):

    def __init__(self, dirName, scaleFactor):
        self.dirName = dirName
        self.scaleFactor = scaleFactor
        self.files = []

    def addFile(self, fname):
        self.files.append(fname)
