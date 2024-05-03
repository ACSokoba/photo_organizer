import unittest
import os
import file_oganizer
import shutil

class TestStringMethods(unittest.TestCase):

    def test_create_file(self):
        path = './'
        createFileNames = ['20241201']
        # createFolderNames = ['2024']
        openedFiles = []
        # for f in createFolderNames :
        #     os.makedirs(path + f, exist_ok=True)          
        for s in createFileNames : 
            openedFiles.append(open(path + s + '.txt', 'w'))
        
        for of in openedFiles:
            of.close()
            
        file_oganizer.organize()
                       
        # self.assertEqual('foo'.upper(), 'FOO')
        
        #Teardown
        for x in createFolderNames:
            shutil.rmtree(path + x)
        
        


if __name__ == '__main__':
    unittest.main()