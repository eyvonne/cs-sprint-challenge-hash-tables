#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # construct the lookup table
    trip = {tick.source: tick.destination for tick in tickets}

    current_city = "NONE"
    layovers = []
    while len(layovers) == 0 or current_city != 'NONE':
        layovers.append(trip[current_city])
        current_city = trip[current_city]

    return layovers
