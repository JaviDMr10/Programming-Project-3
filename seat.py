class Seat:
    def __init__(self, seat_number, seat_type):
        self.seat_number = seat_number
        self.seat_type = seat_type
        self.status = "Available"

    def select(self):
        self.status = "Taken"
