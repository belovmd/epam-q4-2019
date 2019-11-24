"""Create simulator from real life. This can be booking room in hotel,
visit to casino, visit to bar. Create 3-4 objects, that can describe situation
Objects should contain attributes and methods to simulate some use cases.
Completed program should print object states, it actions (methods)
and objects interaction."""


class Vehicle(object):
    """Describes vehicle with model, key and size.

    Key is unique for each vehicle.
    Size shows how much space vehicle will occupy in parking lot.
    """
    def __init__(self, model, size):
        self.model = model
        self.size = size
        self.key = id(self)

    def __str__(self):
        return self.model


class Driver(object):
    """Describes person who owns vehicle and key for it.

    He can buy, sell, park and pick up from parking lot vehicle.
    """
    def __init__(self, name, vehicle=None):
        self.name = name
        self.vehicle = vehicle
        if vehicle:
            self.key = vehicle.key
        else:
            self.key = None

    def buy_vehicle(self, vehicle):
        """Buy vehicle.

        Driver won't be able to buy a new vehicle until he sells his.
        """
        if self.key:
            print(self.name, "already has vehicle.".format(self.name))
        else:
            self.vehicle = vehicle
            self.key = vehicle.key
            print("{} bought {}".format(self.name, vehicle))

    def sell_vehicle(self):
        """Sell vehicle.

        Driver won't be able to sell his vehicle
        until it is in the parking lot.
        """
        if self.vehicle:
            self.vehicle = None
            self.key = None
            print("{} sold {}".format(self.name, self.vehicle))
        elif self.key:
            print(self.name, "can't sell vehicle, it is in the parking lot.")
        else:
            print(self.name, "has no vehicle.")

    def park_vehicle(self, parking):
        """Park vehicle int the parking lot.

        Driver can't park vehicle if parking has not enough space.
        """
        if not self.key:
            print(self.name, "has no vehicle.")
        elif not self.vehicle:
            print(self.name, "already has parked vehicle.")
        else:
            success = parking.park(self.vehicle)
            if success:
                print("{} parked {}.".format(self.name, self.vehicle))
                self.vehicle = None
            else:
                print("Parking has not enough space.")

    def pick_up_vehicle(self, parking):
        """Pick up vehicle from the parking lot."""
        if self.vehicle:
            print(self.name, "didn't park his vehicle.")
        elif not self.key:
            print(self.name, "has no vehicle.")
        else:
            self.vehicle = parking.pick_up(self.key)
            if not self.vehicle:
                print("In parking there is no vehicle belongs to", self.name)
            else:
                print("{} picked up {}".format(self.name, self.vehicle))

    def print_info(self):
        """Display info about driver."""
        print("Driver:", self.name)
        print("Key:", self.key)
        print("Vehicle:", self.vehicle)


class Parking(object):
    """Describes place where driver can park his vehicle."""
    def __init__(self, capacity):
        self.vehicles = {}
        self.free_space = capacity

    def park(self, vehicle):
        """Park vehicle.

        Return False if there is not enough space
        else return True.
        """
        if vehicle.size > self.free_space:
            return False

        self.vehicles[vehicle.key] = vehicle
        self.free_space -= vehicle.size
        return True

    def pick_up(self, key):
        """Pick up vehicle.

        Return None if it doesn't contain vehicle with that key
        else return instance of Vehicle.
        """
        vehicle = self.vehicles.get(key, None)
        if vehicle:
            del self.vehicles[key]
            self.free_space += vehicle.size
        return vehicle

    def print_info(self):
        """Display info about parking."""
        print("Free space in parking:", self.free_space)
        print("Vehicles in parking:")
        for vehicle in self.vehicles.values():
            print(vehicle)


if __name__ == "__main__":
    parking = Parking(100)

    maxim = Driver("Maxim", Vehicle("Bugatti La Voiture Noire", 10))
    maxim.print_info()

    maxim.park_vehicle(parking)
    maxim.print_info()

    artem = Driver("Artemiy", Vehicle("Aist Bicycle", 1))
    artem.park_vehicle(parking)
    parking.print_info()
    artem.sell_vehicle()

    veh = Vehicle("BelAZ", 100)

    maxim.buy_vehicle(veh)

    nazar = Driver("Nazar")
    nazar.park_vehicle(parking)
    nazar.buy_vehicle(veh)
    nazar.park_vehicle(parking)

    maxim.pick_up_vehicle(parking)
    artem.pick_up_vehicle(parking)

    nazar.park_vehicle(parking)
    artem.pick_up_vehicle(parking)
