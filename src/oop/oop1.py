# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class:

#vehicle defines the basic requirements of all kinds of vehicles
class Vehicle:
    pass

# ground vehicles are vehicles, inherits attributes
class GroundVehicle(Vehicle):
    pass
#cars and motorcycles are types of ground vehicles, and therefore vehicles
class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

#flight vehicles are vehicles, inherits attributes
class FlightVehicle(Vehicle):
    pass
#starships and airplanes are types of flight vehicles, and therefore vehicles
class Starship(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass
