import unittest, sys, os

sys.path.append(os.getcwd())
import src.main.split as split


class SplitTestClass(unittest.TestCase):   

    def cleanUp(self):
        files = os.listdir("resources/test/output/test")

        if(len(files) > 0):
            for file in files:
                os.remove("resources/test/output/test/"+file)

    def setUp(self):
        self.cleanUp()

    def test_mustHaveFourDefaultOutputFiles(self):
        split.main(isTest=True)

        files = os.listdir("resources/test/output/test")

        self.assertEqual(len(files), 4)
        
        self.cleanUp()

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SplitTestClass)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()