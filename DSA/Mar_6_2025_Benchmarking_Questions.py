""" Counter and Thermostat Classes """

class Counter:
    def __init__(self, start: int = 0):
        self.count = start

    def get_count(self) -> int:
        return self.count

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

class LimitCounter(Counter):
    def __init__(self, start: int = 0, max_threshold: int = 100):
        super().__init__(start)
        self.max_threshold = max_threshold

    def increment(self):
        if self.count + 1 > self.max_threshold:
            raise ValueError(f"Counter cannot exceed {self.max_threshold}")
        self.count += 1

class Thermostat:
    def __init__(self, temperature: float = 72.0):
        self._temperature = temperature

    def get_temperature(self) -> float:
        return self._temperature

    def set_temperature(self, new_temp: float):
        if not (50 <= new_temp <= 90):
            raise ValueError("Temperature must be between 50°F and 90°F")
        self._temperature = new_temp

    def __str__(self):
        return f"Thermostat set to {self._temperature}°F"

class SmartThermostat(Thermostat):
    def __init__(self, temperature: float = 72.0, eco_mode: bool = False):
        super().__init__(temperature)
        self.eco_mode = eco_mode

    def set_temperature(self, new_temp: float):
        if self.eco_mode and not (60 <= new_temp <= 78):
            raise ValueError("Eco mode: Temperature must be between 60°F and 78°F")
        elif not (50 <= new_temp <= 90):
            raise ValueError("Temperature must be between 50°F and 90°F")
        self._temperature = new_temp

    def toggle_eco_mode(self):
        self.eco_mode = not self.eco_mode

    def __str__(self):
        return f"SmartThermostat set to {self._temperature}°F (Eco mode: {'On' if self.eco_mode else 'Off'})"

