class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(2,8)
print(p1.x)
print(p1.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats(): #same thing as if self.open_seats() == 0
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["gimrod", "rodrick","gimmy","dimmy"]
print (f"people wanting to take the flight: {people}")

for person in people:
    added = flight.add_passenger(person)
    if added:
        print(f"the following added to flight: {person}")
    else:
        print(f"max capacity, {person} not added")
print(f"plane passengers final: {flight.passengers}")