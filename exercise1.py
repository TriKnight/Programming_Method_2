# Object-oriented approach
class TemperatureSensor:
    def __init__(self):
        self._value = 0
        self._error = False
    
    def read(self):
        try:
            self._value = self._get_raw_value()
            self._error = False
        except Exception as e:
            self._error = True
            self._value = -999
    
    def is_valid(self):
        return not self._error
    
    def get_value(self):
        return self._value if self.is_valid() else None

# Usage is cleaner and more intuitive
sensor = TemperatureSensor()
sensor.read()
if sensor.is_valid():
    print(sensor.get_value())