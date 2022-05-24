class Vehicle:
    def __init__(self, average_speed_in_km_per_hour: int, number_of_passengers: int):
        self.average_speed_in_km_per_hour = average_speed_in_km_per_hour
        self.number_of_passengers = number_of_passengers

    def print_info(self):
        print("Average speed = {} km/h".format(self.average_speed_in_km_per_hour))
        print("Number of passengers: {}".format(self.number_of_passengers))


class Car(Vehicle):
    def __init__(self, average_speed_in_km_per_hour: int, number_of_passengers: int, car_type: str, car_model: str):
        super().__init__(average_speed_in_km_per_hour, number_of_passengers)
        self.car_type = car_type
        self.car_model = car_model

    def print_info(self):
        super().print_info()
        print("Type: {}".format(self.car_type))
        print("Model: {}".format(self.car_model))


class Bus(Vehicle):
    def __init__(self, average_speed_in_km_per_hour: int, number_of_passengers: int, is_adapted_for_disabled: bool):
        super().__init__(average_speed_in_km_per_hour, number_of_passengers)
        self.is_adapted_for_disabled = is_adapted_for_disabled

    def print_info(self):
        super().print_info()
        if self.is_adapted_for_disabled:
            s = ""
        else:
            s = "NOT "
        print("Bus is {}adapted for disabled".format(s))


class Plane(Vehicle):
    def __init__(self, average_speed_in_km_per_hour: int, number_of_passengers: int, maximum_flight_altitude_in_metres: int):
        super().__init__(average_speed_in_km_per_hour, number_of_passengers)
        self.maximum_flight_altitude_in_metres = maximum_flight_altitude_in_metres

    def print_info(self):
        super().print_info()
        print("Maximum flight attitude = {} metres".format(self.maximum_flight_altitude_in_metres))


class Trolleybus(Vehicle):
    def __init__(self, average_speed_in_km_per_hour: int, number_of_passengers: int, number_of_wheels: int):
        super().__init__(average_speed_in_km_per_hour, number_of_passengers)
        self.number_of_wheels = number_of_wheels

    def print_info(self):
        super().print_info()
        print("Trolleybus have {} wheels".format(self.number_of_wheels))


class Tram(Vehicle):
    def __init__(self, average_speed_in_km_per_hour: int, number_of_passengers: int, manufacture_year: int):
        super().__init__(average_speed_in_km_per_hour, number_of_passengers)
        self.manufacture_year = manufacture_year

    def print_info(self):
        super().print_info()
        print("Tram was manufactured in {} year".format(self.manufacture_year))
