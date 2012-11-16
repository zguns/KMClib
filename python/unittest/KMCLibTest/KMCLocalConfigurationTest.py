"""" Module for testing KMCLocalConfiguration """


# Copyright (c)  2012  Mikael Leetmaa
#
# This file is part of the KMCLib project distributed under the terms of the
# GNU General Public License version 3, see <http://www.gnu.org/licenses/>.
#


import unittest
import numpy


from KMCLib.Exceptions.Error import Error


# Import the module to test.
from KMCLib.KMCLocalConfiguration import KMCLocalConfiguration

# Implementing the tests.
class KMCLocalConfigurationTest(unittest.TestCase):
    """ Class for testing the KMCLocalConfiguration class """

    def testConstruction(self):
        """ Test that the KMCLocalConfiguration class can be constructed. """
        # Construct with coordinate list.
        coords = [[1.0,2.0,3.4],[1.1,1.2,1.3]]
        types = ["A","B"]
        local_config = KMCLocalConfiguration(cartesian_coordinates=coords, types=types, center=1)

        # Test.
        self.assertTrue(isinstance(local_config, KMCLocalConfiguration))

        # Construct with numpy coordinates.
        coords = numpy.array([[1.0,2.0,3.4],[1.1,1.2,1.3]])
        local_config = KMCLocalConfiguration(cartesian_coordinates=coords, types=types, center=0)

        # Test.
        self.assertTrue(isinstance(local_config, KMCLocalConfiguration))

    def testMemberData(self):
        """ Check that the correct member data is stored on the class. """
        # Setup the configuration.
        coords = [[1.0,2.0,3.0],[1.0,1.0,3.0],[3.0,8.0,9.0]]
        types = ["C","B","A"]
        local_config = KMCLocalConfiguration(cartesian_coordinates=coords, types=types, center=1)

        # Define the reference data.
        ref_coords    = numpy.array([[0.0,0.0,0.0],[0.0,1.0,0.0],[2.0,7.0,6.0]])
        ref_types     = ["B","C","A"]
        ref_distances = [numpy.linalg.norm(ref_coords[0]),
                         numpy.linalg.norm(ref_coords[1]),
                         numpy.linalg.norm(ref_coords[2])]

        # Check the coordinates.
        self.assertAlmostEqual(numpy.linalg.norm(local_config._KMCLocalConfiguration__cartesain_coordinates - ref_coords), 0.0, 10)

        # Check the types.
        self.assertEqual(local_config._KMCLocalConfiguration__types, ref_types)

        # Check the distances.
        self.assertAlmostEqual(numpy.linalg.norm(local_config._KMCLocalConfiguration__distances - ref_distances), 0.0, 10)

    def testConstructionFails(self):
        """ Make sure the construction fails in the correct way with wrong arguments. """
        # Data do use.
        coords = [[1.0,2.0,3.4],[1.1,1.2,1.3]]
        types = ["A","B"]
        center = -1
        # No arguments.
        self.assertRaises(Error, lambda: KMCLocalConfiguration())
        # Center out of bounds.
        self.assertRaises(Error, lambda: KMCLocalConfiguration(coords, types, center))
        # Missing types information.
        self.assertRaises(Error, lambda: KMCLocalConfiguration(cartesian_coordinates=coords, center=center))
        # Missing coordinate information.
        self.assertRaises(Error, lambda: KMCLocalConfiguration(types=types, center=center))
        # Wrong type of types.
        self.assertRaises(Error, lambda: KMCLocalConfiguration(coords, coords, center))
        # Wrong type of coordinates.
        self.assertRaises(Error, lambda: KMCLocalConfiguration(types, types, center))
        # Wrong type of center.
        self.assertRaises(Error, lambda: KMCLocalConfiguration(coords, types, center="A"))



if __name__ == '__main__':
    unittest.main()



