import heapq


class SeatManager:

    def __init__(self, n):
        self.available_seats = list(range(1, n+1))
    def reserve(self):
        return heapq.heappop(self.available_seats)

    def unreserve(self, seatNumber):
        heapq.heappush(self.available_seats, seatNumber)

