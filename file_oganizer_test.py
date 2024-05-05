import unittest
import os
import file_oganizer
import shutil

class TestStringMethods(unittest.TestCase):

    def test_create_file(self):
        #Setup
        path = './'
        createFileNames = ['20241201']
        openedFiles = []
        # for f in createFolderNames :
        #     os.makedirs(path + f, exist_ok=True)          
        for s in createFileNames : 
            openedFiles.append(open(path + s + '.txt', 'w'))
        
        for of in openedFiles:
            of.close()
            
        file_oganizer.organize()

        for fileName in createFileNames:
            self.assertTrue(fileName[:4] in os.listdir())
                       
        #Teardown
        # for x in createFolderNames:
        #     shutil.rmtree(path + x)
        
        


if __name__ == '__main__':
    unittest.main()