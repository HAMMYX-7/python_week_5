# Parent class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.__origin = origin  # Encapsulation: hidden from direct access

    def introduce(self):
        return f"I am {self.name}, and my power is {self.power}!"

    def get_origin(self):
        return self.__origin

    def set_origin(self, origin):
        if origin:
            self.__origin = origin

# Child class
class FlyingHero(Superhero):
    def __init__(self, name, power, origin, max_altitude):
        super().__init__(name, power, origin)
        self.max_altitude = max_altitude

    def fly(self):
        return f"{self.name} is flying up to {self.max_altitude} feet!"

# Usage
hero1 = FlyingHero("SkyBolt", "Wind Control", "Sky Nation", 5000)

print(hero1.introduce())        # Inherited method
print(hero1.fly())              # Child-specific method
print(hero1.get_origin())       # Encapsulated origin via getter
