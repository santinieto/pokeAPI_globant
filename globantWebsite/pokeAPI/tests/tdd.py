import unittest
import os
import sys
sys.path.append( os.environ['POKEAPI_PATH'] )

from pokeAPI_scripts import *

class Testpokeapi(unittest.TestCase):

    def testEnvironmentVariables(self) -> None:
        """Check that the environ variables work"""

        success = False
        try:
            print(os.environ["NAME"])
            print(os.environ["POKEAPI_MAIN_URL"])
            success = True
        except:
            success = False

        self.assertFalse(success)

    def testnBerries(self) -> None:
        """Check that the method to get the number of berries works"""

        nberries = get_berries_number()

        self.assertNotEqual(nberries, None)

    def testBerriesData(self) -> None:
        """Check that is possible to obtain berries' data"""

        berry_names, berry_grow_times = get_berries_data(10)
        #berry_grow_times = None # Force error
        
        self.assertNotEqual(berry_names, None)
        self.assertNotEqual(berry_grow_times, None)

if __name__ == "__main__":
    unittest.main()