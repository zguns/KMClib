"""" Module for testing KMCInteractions """


# Copyright (c)  2012  Mikael Leetmaa
#
# This file is part of the KMCLib project distributed under the terms of the
# GNU General Public License version 3, see <http://www.gnu.org/licenses/>.
#


import unittest


from KMCLib.KMCLocalConfiguration import KMCLocalConfiguration
from KMCLib.Exceptions.Error import Error
from KMCLib.Backend import Backend

# Import the module to test.
from KMCLib.KMCInteractions import KMCInteractions

# Implementing the tests.
class KMCInteractionsTest(unittest.TestCase):
    """ Class for testing the KMCInteractions class """

    def testConstruction(self):
        """ Test that the KMCInteractions class can be constructed. """
        # A first interaction.
        coords = [[1.0,2.0,3.4],[1.1,1.2,1.3]]
        types = ["A","B"]
        local_config_0 = KMCLocalConfiguration(coordinates=coords,
                                               types=types,
                                               center=0)
        types = ["B","A"]
        local_config_1 = KMCLocalConfiguration(coordinates=coords,
                                               types=types,
                                               center=0)
        rate_0_1 = 3.5
        interaction_0 = (local_config_0, local_config_1, rate_0_1)

        # A second interaction.
        coords = [[1.0,2.0,3.4],[1.1,1.2,1.3]]
        types = ["A","C"]
        local_config_0 = KMCLocalConfiguration(coordinates=coords,
                                               types=types,
                                               center=0)
        types = ["C","A"]
        local_config_1 = KMCLocalConfiguration(coordinates=coords,
                                               types=types,
                                               center=0)
        rate_0_1 = 1.5
        interaction_1 = (local_config_0, local_config_1, rate_0_1)

        interactions = [interaction_0, interaction_1]

        # Construct the interactions object.
        kmc_interactions = KMCInteractions(interactions=interactions)

        # Check the raw interactions stored on the object.
        stored_interactions = kmc_interactions._KMCInteractions__raw_interactions

        # Checks that the address is the same.
        self.assertTrue(stored_interactions == interactions)

    def testConstructionFailNoList(self):
        """ Test that the construction fails if the interactions list is not a list. """
        self.assertRaises(Error, lambda: KMCInteractions(interactions=KMCLocalConfiguration))

    def testConstructionFailNoTuple(self):
        """ Test that the construction fails if the elements in the interactions list are not lists or tuples of the correct length. """
        # A first interaction.
        coords = [[1.0,2.0,3.4],[1.1,1.2,1.3]]
        types = ["A","B"]
        local_config_0 = KMCLocalConfiguration(coordinates=coords,
                                               types=types,
                                               center=0)
        types = ["B","A"]
        local_config_1 = KMCLocalConfiguration(coordinates=coords,
                                               types=types,
                                               center=0)
        rate_0_1 = 3.5
        interaction_0 = (local_config_0, local_config_1, rate_0_1)

        # A second interaction.
        coords = [[1.0,2.0,3.4],[1.1,1.2,1.3]]
        types = ["A","C"]
        local_config_0 = KMCLocalConfiguration(coordinates=coords,
                                               types=types,
                                               center=0)
        types = ["C","A"]
        local_config_1 = KMCLocalConfiguration(coordinates=coords,
                                               types=types,
                                               center=0)
        rate_0_1 = 1.5
        interaction_1 = (local_config_0, local_config_1, rate_0_1, rate_0_1)

        interactions = [interaction_0, interaction_1]

        # Fails because interaction_1 is of wrong length.
        self.assertRaises( Error, lambda: KMCInteractions(interactions=interactions) )

        interaction_0 = local_config_0
        interaction_1 = local_config_1
        interactions = [interaction_0, interaction_1]

        # Fails because the interactions are not lists or tuples.
        self.assertRaises( Error, lambda: KMCInteractions(interactions=interactions) )

    def testConstructionFailWrongType(self):
        """ Test that the construction fails if the configurations are of wrong type. """
        interaction_0 = (Error("dummy"),1.0, 123.0)
        interactions = [interaction_0, interaction_0]

        # Check that it fails.
        self.assertRaises( Error, lambda: KMCInteractions(interactions=interactions) )

    def testConstructionFailWrongRateType(self):
        """ Test that the construction fails if the rate is of wrong type. """
        # A first interaction.
        coords = [[1.0,2.0,3.4],[1.1,1.2,1.3]]
        types = ["A","B"]
        local_config_0 = KMCLocalConfiguration(coordinates=coords,
                                               types=types,
                                               center=0)
        types = ["B","A"]
        local_config_1 = KMCLocalConfiguration(coordinates=coords,
                                               types=types,
                                               center=0)
        rate_0_1 = 3.5
        interaction_0 = (local_config_0, local_config_1, rate_0_1)

        # A second interaction.
        coords = [[1.0,2.0,3.4],[1.1,1.2,1.3]]
        types = ["A","C"]
        local_config_0 = KMCLocalConfiguration(coordinates=coords,
                                               types=types,
                                               center=0)
        types = ["C","A"]
        local_config_1 = KMCLocalConfiguration(coordinates=coords,
                                               types=types,
                                               center=0)
        # Integer rate to fail.
        rate_0_1 = 1
        interaction_1 = (local_config_0, local_config_1, rate_0_1)

        interactions = [interaction_0, interaction_1]

        # Construct the interactions object - fails because of the integer rate.
        self.assertRaises( Error, lambda: KMCInteractions(interactions=interactions) )

    def testConstructionFailNotSameCoords(self):
        """ Test that the construction fails unless the coordinates are equal. """
        # A first interaction.
        coords = [[1.0,2.0,3.4],[1.1,1.2,1.3]]
        types = ["A","B"]
        local_config_0 = KMCLocalConfiguration(coordinates=coords,
                                               types=types,
                                               center=0)
        types = ["B","A"]
        local_config_1 = KMCLocalConfiguration(coordinates=coords,
                                               types=types,
                                               center=0)
        rate_0_1 = 3.5
        interaction_0 = (local_config_0, local_config_1, rate_0_1)

        # A second interaction - not the same coords, to fail.
        coords = [[1.0,2.0,3.4],[1.1,1.2,1.2]]
        types = ["A","C"]
        local_config_0 = KMCLocalConfiguration(coordinates=coords,
                                               types=types,
                                               center=0)
        coords = [[1.0,2.0,3.4],[1.1,1.2,1.3]]
        types = ["C","A"]
        local_config_1 = KMCLocalConfiguration(coordinates=coords,
                                               types=types,
                                               center=0)
        rate_0_1 = 1.3
        interaction_1 = (local_config_0, local_config_1, rate_0_1)

        interactions = [interaction_0, interaction_1]

        # Fails because of different coordinates.
        self.assertRaises( Error, lambda: KMCInteractions(interactions=interactions) )

    def testConstructionFailSameTypes(self):
        """ Test that the construction fails if the types are identical. """
        # A first interaction.
        coords = [[1.0,2.0,3.4],[1.1,1.2,1.3]]
        types = ["A","B"]
        local_config_0 = KMCLocalConfiguration(coordinates=coords,
                                               types=types,
                                               center=0)
        types = ["B","A"]
        local_config_1 = KMCLocalConfiguration(coordinates=coords,
                                               types=types,
                                               center=0)
        rate_0_1 = 3.5
        interaction_0 = (local_config_0, local_config_1, rate_0_1)

        # A second interaction.
        coords = [[1.0,2.0,3.4],[1.1,1.2,1.3]]
        types = ["A","C"]
        local_config_0 = KMCLocalConfiguration(coordinates=coords,
                                               types=types,
                                               center=0)
        types = ["A","C"]
        local_config_1 = KMCLocalConfiguration(coordinates=coords,
                                               types=types,
                                               center=0)
        rate_0_1 = 1.5
        interaction_1 = (local_config_0, local_config_1, rate_0_1)

        interactions = [interaction_0, interaction_1]

        # Fails because of same types.
        self.assertRaises( Error, lambda: KMCInteractions(interactions=interactions) )

    def testBackend(self):
        """
        Test that the generated backend object is what we expect.
        """
        # A first interaction.
        coords = [[1.0,2.0,3.4],[1.1,1.2,1.3]]
        types = ["A","B"]
        local_config_0 = KMCLocalConfiguration(coordinates=coords,
                                               types=types,
                                               center=0)
        types = ["B","A"]
        local_config_1 = KMCLocalConfiguration(coordinates=coords,
                                               types=types,
                                               center=0)
        rate_0_1 = 3.5
        interaction_0 = (local_config_0, local_config_1, rate_0_1)

        # A second interaction.
        coords = [[1.0,2.0,3.4],[1.1,1.2,1.3]]
        types = ["A","C"]
        local_config_0 = KMCLocalConfiguration(coordinates=coords,
                                               types=types,
                                               center=0)
        types = ["C","A"]
        local_config_1 = KMCLocalConfiguration(coordinates=coords,
                                               types=types,
                                               center=0)
        rate_0_1 = 1.5
        interaction_1 = (local_config_0, local_config_1, rate_0_1)

        interactions = [interaction_0, interaction_1]

        # Construct the interactions object.
        kmc_interactions = KMCInteractions(interactions=interactions)

        # Setup a dict with the possible types.
        possible_types = {
            "A" : 13,
            "D" : 2,
            "B" : 3,
            "J" : 4,
            "C" : 5,
            }

        # Get the backend.
        cpp_interactions = kmc_interactions._backend(possible_types)

        # Check the type.
        self.assertTrue( isinstance(cpp_interactions, Backend.Interactions) )

        # Get the processes out.
        cpp_processes = cpp_interactions.processes()

        # Check the length of the processes.
        self.assertEqual(cpp_processes.size(), 2)

        # Get the elements out of the second process.
        match_type  = cpp_processes[1].matchList()[0].matchType()
        update_type = cpp_processes[1].matchList()[0].updateType()

        # Match type should be "A" -> 15 and update type "C" -> 5
        self.assertEqual( match_type, 13)
        self.assertEqual( update_type, 5)

        # Get the elements out of the second process.
        match_type  = cpp_processes[1].matchList()[1].matchType()
        update_type = cpp_processes[1].matchList()[1].updateType()

        # Match type should be "C" -> 5 and update type "A" -> 13
        self.assertEqual( match_type,   5)
        self.assertEqual( update_type, 13)


if __name__ == '__main__':
    unittest.main()
