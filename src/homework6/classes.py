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
        self.parked = False

    def __str__(self):
        return self.model


class Driver(object):
    """Describes person who owns vehicle and key for it.

    He can buy, sell, park and pick up vehicle from parking lot.
    """
    def __init__(self, name, *vehicles):
        self.name = name
        if vehicles:
            self.vehicles = {vehicle.key: vehicle for vehicle in vehicles}
        else:
            self.vehicles = {}

    def buy_vehicle(self, vehicle):
        self.vehicles[vehicle.key] = vehicle
        print("{} bought {}".format(self.name, vehicle))

    def sell_vehicle(self, key):
        """Sell vehicle.

        Driver won't be able to sell his vehicle
        until it is in the parking lot.
        """
        vehicle = self.vehicles.get(key, None)
        if not vehicle:
            print(self.name, "has no vehicle with this key.")
        elif vehicle.parked:
            print(self.name, "can't sell vehicle, it is in the parking lot.")
        else:
            del self.vehicles[key]
            print("{} sold {}".format(self.name, vehicle))

    def park_vehicle(self, parking, key):
        """Park vehicle int the parking lot.

        Driver can't park vehicle if parking has not enough space.
        """
        vehicle = self.vehicles.get(key, None)
        if not vehicle:
            print(self.name, "has no vehicle with this key.")
        elif vehicle.parked:
            print(self.name, "already has parked vehicle.")
        else:
            parking.park(vehicle)
            if vehicle.parked:
                print("{} parked {}.".format(self.name, vehicle))
            else:
                print("Parking has not enough space.")

    def pick_up_vehicle(self, parking, key):
        """Pick up vehicle from the parking lot."""
        vehicle = self.vehicles.get(key, None)
        if not vehicle:
            print(self.name, "has no vehicle with this key.")
        elif not vehicle.parked:
            print(self.name, "didn't park his vehicle.")
        else:
            parking.pick_up(vehicle)
            if vehicle.parked:
                print("In parking there is no vehicle with this key.")
            else:
                print("{} picked up {}".format(self.name, vehicle))

    def print_info(self):
        """Display info about driver."""
        print("Driver:", self.name)
        print("Vehicles:")
        [print(vehicle) for vehicle in self.vehicles.values()]


class Parking(object):
    """Describes place where driver can park his vehicle."""
    def __init__(self, capacity):
        self.keys = set()
        self.free_space = capacity

    def park(self, vehicle):
        if vehicle.size > self.free_space:
            return

        vehicle.parked = True
        self.keys.add(vehicle.key)
        self.free_space -= vehicle.size

    def pick_up(self, vehicle):
        if vehicle.key in self.keys:
            vehicle.parked = False
            self.free_space += vehicle.size
            self.keys.remove(vehicle.key)

    def print_info(self):
        """Display info about parking."""
        print("Free space in parking:", self.free_space)
        print("Count of vehicles in parking:", len(self.keys))


if __name__ == "__main__":
    parking = Parking(100)

    bugatti = Vehicle("Bugatti La Voiture Noire", 10)
    maxim = Driver("Maxim", bugatti)
    maxim.print_info()
    maxim.park_vehicle(parking, bugatti.key)

    aist = Vehicle("Aist Bicycle", 1)
    artem = Driver("Artemiy", aist)
    artem.park_vehicle(parking, aist.key)
    parking.print_info()
    artem.sell_vehicle(aist.key)

    bel = Vehicle("BelAZ", 100)
    nazar = Driver("Nazar")
    nazar.park_vehicle(parking, bel.key)
    nazar.buy_vehicle(bel)
    nazar.park_vehicle(parking, bel.key)

    maxim.pick_up_vehicle(parking, bugatti.key)
    artem.pick_up_vehicle(parking, aist.key)

    nazar.park_vehicle(parking, bel.key)
    artem.pick_up_vehicle(parking, aist.key)
