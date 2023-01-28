class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        else:
            self.passengers.append(name)
            return True
    def open_seats(self):
        return self.capacity - len(self.passengers) 

flight = Flight(3)

people = ["Ali", "Samira", "Parviz", "Amoo"]

for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")
