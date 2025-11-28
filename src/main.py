from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

car_park = CarPark("moondalup", 100, log_file="moondalup.txt", config_file="moondalup_config.json")
car_park.write_config()
entry_sensor = EntrySensor(1, True, car_park)
exit_sensor = ExitSensor(2, True, car_park)
display = Display(1, "Welcome to Moondalup", True)
for i in range(10):
    entry_sensor.detect_vehicle()
for i in range(2):
    exit_sensor.detect_vehicle()