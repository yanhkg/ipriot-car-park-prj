import unittest
from sensor import EntrySensor, ExitSensor
from car_park import CarPark

class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.EntrySensor = EntrySensor(1, True, self.car_park)
        self.ExitSensor = ExitSensor(2, True, self.car_park)

    def test_exit_sensor_scan_plate(self):
        plate = "TEST-001"
        self.car_park.add_car(plate)
        scanned_plate = self.ExitSensor._scan_plate()
        self.assertIn(scanned_plate, self.car_park.plates)

    def test_update_car_park(self):
        plate = "FAKE-123"
        self.EntrySensor.update_car_park(plate)
        self.assertIn(plate, self.car_park.plates)
        self.assertEqual(self.car_park.available_bays, self.car_park.capacity - 1)