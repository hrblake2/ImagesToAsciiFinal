import os
import re
class file_picker():

    def __init__(self, fileName, fileType):
        self.fileName = fileName
        self.fileType = fileType

    def chooseFile(self):
        endsWithjpg = re.compile(r'jpg$')

    def getName(self):
        return self.fileName

    def getType(self):
        return self.fileType

    def printInfo(self):
        print('File name: '+ self.fileName, '\nFile type: '+ self.fileType)

endsWithjpg = re.compile(r'jpg$')

for i in os.listdir('C:\\Users\\Harrison\\PythonStuff'):
    if endsWithjpg.search(i) != None:
        print(i)
