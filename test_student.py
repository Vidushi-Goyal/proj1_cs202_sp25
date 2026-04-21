import unittest
from proj1 import *
#proj1.py should contain your data class and function definitions
#these do not contribute positivly to your grade. 
#but your grade will be lowered if they are missing

class TestRegionFunctions(unittest.TestCase):

    def test_emissions_per_capita1(self):
        rc_del = RegionCondition(Region(GlobeRect(28.24,28.53,76.50,77.20),"Delhi","other"),2025,34670000,25000000.0)
        expected = 25000000.0 / 34670000
        self.assertAlmostEqual(emissions_per_capita(rc_del), expected, places=4)
    def test_emissions_per_capita2(self):
        rc_edge = RegionCondition(Region(GlobeRect(28.24,28.53,76.50,77.20),"Delhi","other"),2025,0,25000000.0)
        expected = 0.0
        self.assertAlmostEqual(emissions_per_capita(rc_edge), expected)

    def test_area1(self):
        gr_mex = GlobeRect(19.3,19.5,-99.2,-99.0)
        expected = 467.5320
        self.assertAlmostEqual(area(gr_mex), expected, places=4)
    def test_area2(self):
        gr_2 = GlobeRect(1.0,1.0,-1.0,-5.0)
        expected = 0
        self.assertAlmostEqual(area(gr_2), expected, places=4)

    def test_emissions_per_square_km_edge(self):
        rc = RegionCondition(
        Region(GlobeRect(0.0,0.0,0.0,0.0),"Morro Bay","other"), 2025,10550,110000.0
    )
        expected = 0.0
        self.assertAlmostEqual(emissions_per_square_km(rc), expected)
    def test_emission_per_square_km_edge1(self):
        rc = RegionCondition(
            Region(GlobeRect(19.3,19.5,-99.2,-99.0),"Morro Bay","other"), 2025,10550,100
    )
        expected = 100.0 / 467.5320
        self.assertAlmostEqual(emissions_per_square_km(rc), expected, places=4)


    def test_densesnt(self):

if __name__ == '__main__':
    unittest.main()
