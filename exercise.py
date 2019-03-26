class Location:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Trip:
    def __init__(self):
        self.destinations = []

    def add_destination(self, location):
        self.destinations.append(location)

    def __str__(self):
        result = ""
        result += "Began Trip"
        for index, destination in enumerate(self.destinations):
            if index + 1 <= (len(self.destinations) - 1):
                result += f"\nTravelled from {destination} to {self.destinations[index+1]}."
        result += "\nEnded trip."
        return result

location_names = ['Toronto', 'Ottawa', 'Montreal', 'Quebec City', 'Halifax', "St. John's"]
myTrip = Trip()

for name in location_names:
    myLocation = Location(name)
    myTrip.add_destination(myLocation)

print(myTrip)
