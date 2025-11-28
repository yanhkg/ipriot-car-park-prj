import unittest
from sensor import EntrySensor, ExitSensor
from car_park import CarPark

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.EntrySensor = EntrySensor(1, True, self.car_park)
        self.ExitSensor = ExitSensor(2, True, self.car_park)

    def test_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.EntrySensor, EntrySensor)
        self.assertEqual(self.EntrySensor.id, 1)
        self.assertEqual(self.EntrySensor.is_active, True)
        self.assertEqual(self.EntrySensor.car_park, self.car_park)
        self.assertIsInstance(self.ExitSensor, ExitSensor)
        self.assertEqual(self.ExitSensor.id, 2)
        self.assertEqual(self.ExitSensor.is_active, True)
        self.assertEqual(self.ExitSensor.car_park, self.car_park)

    def test_update_car_park(self):
        plate = "FAKE-123"
        self.EntrySensor.update_car_park(plate)
        self.assertIn(plate, self.car_park.plates)
        self.assertEqual(self.car_park.available_bays, self.car_park.capacity - 1)