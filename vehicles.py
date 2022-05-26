class Vehicle:
    def __init__(self, average_speed_in_km_per_hour: int, number_of_passengers: int):
        self.average_speed_in_km_per_hour = average_speed_in_km_per_hour
        self.number_of_passengers = number_of_passengers

    def __str__(self):
        return "Average speed = {} km/h".format(self.average_speed_in_km_per_hour) + \
               "\nNumber of passengers: {}".format(self.number_of_passengers)


class Car(Vehicle):
    def __init__(self, average_speed_in_km_per_hour: int, number_of_passengers: int, car_type: str, car_model: str):
        super().__init__(average_speed_in_km_per_hour, number_of_passengers)
        self.car_type = car_type
        self.car_model = car_model

    def __str__(self):
        return super().__str__() + "\nType: {}".format(self.car_type) + "\nModel: {}".format(self.car_model)


class Bus(Vehicle):
    def __init__(self, average_speed_in_km_per_hour: int, number_of_passengers: int, is_adapted_for_disabled: bool):
        super().__init__(average_speed_in_km_per_hour, number_of_passengers)
        self.is_adapted_for_disabled = is_adapted_for_disabled

    def __str__(self):
        res = super().__str__()
        if self.is_adapted_for_disabled:
            s = ""
        else:
            s = "NOT "
        return res + "\nBus is {}adapted for disabled".format(s)


class Plane(Vehicle):
    def __init__(self, average_speed_in_km_per_hour: int, number_of_passengers: int, maximum_flight_altitude_in_metres: int):
        super().__init__(average_speed_in_km_per_hour, number_of_passengers)
        self.maximum_flight_altitude_in_metres = maximum_flight_altitude_in_metres

    def __str__(self):
        return super().__str__() + "\nMaximum flight attitude = {} metres".format(self.maximum_flight_altitude_in_metres)


class Trolleybus(Vehicle):
    def __init__(self, average_speed_in_km_per_hour: int, number_of_passengers: int, number_of_wheels: int):
        super().__init__(average_speed_in_km_per_hour, number_of_passengers)
        self.number_of_wheels = number_of_wheels

    def __str__(self):
        return super().__str__() + "\nTrolleybus have {} wheels".format(self.number_of_wheels)


class Tram(Vehicle):
    def __init__(self, average_speed_in_km_per_hour: int, number_of_passengers: int, manufacture_year: int):
        super().__init__(average_speed_in_km_per_hour, number_of_passengers)
        self.manufacture_year = manufacture_year

    def __str__(self):
        return super().__str__() + "\nTram was manufactured in {} year".format(self.manufacture_year)
