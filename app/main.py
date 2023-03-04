class Car:
    def __init__(self,
                 comfort_class: int = 7,
                 clean_mark: int = 1,
                 brand: str = "Unknown"
                 ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float = 1,
                 clean_power: float or int = 10,
                 average_rating: float = 5,
                 count_of_ratings: int = 1
                 ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        cars_to_wash = [car for car in cars
                        if car.clean_mark < self.clean_power]
        for car in cars_to_wash:
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        price = (car.comfort_class * (self.clean_power - car.clean_mark)
                 * (self.average_rating / self.distance_from_city_center))
        return round(price, 1)

    def wash_single_car(self, single_car: Car) -> None:
        if single_car.clean_mark < self.clean_power:
            single_car.clean_mark = self.clean_power

    def rate_service(self, score: int) -> None:
        self.average_rating = ((self.average_rating * self.count_of_ratings
                                + score) / (self.count_of_ratings + 1))
        self.count_of_ratings += 1
        self.average_rating = round(self.average_rating, 1)
