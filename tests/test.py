from metro import *
import unittest


class MetroTest(unittest.TestCase):
    def setUp(self):
        self.test = Metro(setup_environment=False)

    def test_01_find_path(self):
        self.test.set_language("ENG")

        dist, path = self.test.find_path(0, 1)
        assert dist is not None and path is not None, "PATH DID NOT FOUNDED"

        self.test.find_path_map(0)
        assert dist is not None and path is not None, "PATH MAP NOT FOUNDED"

    def test_02_get_path(self):
        self.test.set_language("RUS")

        dist, path = self.test.get_path(0, 1)
        assert dist is not None and path is not None, "PATH DID NOT GOTTEN"

        self.test.get_path_map(0)
        assert dist is not None and path is not None, "PATH MAP NOT GOTTEN"


metroTestSuite = unittest.TestSuite()
metroTestSuite.addTest(unittest.makeSuite(MetroTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(metroTestSuite)
