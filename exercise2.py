
class TemperatureSensor:
    def read(self):
        return "24°C"

class PressureSensor:
    def read(self):
        return "101.3 kPa"

# Polymorphism in action
sensors = [TemperatureSensor(), PressureSensor()]

for s in sensors:
    print(s.read()) # Same method name, different behaviors
