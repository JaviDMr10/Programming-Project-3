
from seat import Seat

class Airplane:
    def __init__(self):
        self.seats = []
        self.setup_seats()

    def setup_seats(self):
        for i in range(20):
            if i < 4:
                seat_type = "First Class"
            elif i < 6:
                seat_type = "Emergency"
            else:
                seat_type = "Regular Seat"
            self.seats.append(Seat(i + 1, seat_type))

    def display_prices(self):
        print("The prices of each class is:")
        print("Regular seats (seats 7-20): $40 each")
        print("Emergency seats (seats 5-6): $30 each")
        print("First Class Seat (seats 1-4): $40 regular seat price + $100 = $140 each")

    def display_seats(self):
        print("Seat map:")
        for seat in self.seats:
            print(f"Seat {seat.seat_number} - {seat.seat_type} - {seat.status}")
        print()

    def purchase_seats(self):
        seats_taken = 0
        for seat in self.seats:
            if seat.status == "Taken":
                seats_taken += 1

        if seats_taken == len(self.seats):
            print("All seats are taken. No seats are available for purchase.")
            return

        while True:
            seat_numbers = input("Enter the seat numbers you would like to purchase (comma separated): \n").split(",")
            for i in range(len(seat_numbers)):
                seat_numbers[i] = seat_numbers[i].strip()
            total_cost = 0
            valid_selection = True

            for selection in seat_numbers:
                selection = int(selection)
                seat = self.seats[selection - 1]
                if seat.status == "Taken":
                    print(f"Seat {selection} is already taken. Please choose a different seat.")
                    valid_selection = False
                    break

            if not valid_selection:
                continue

            for selection in seat_numbers:
                selection = int(selection)
                seat = self.seats[selection - 1]

                if seat.seat_type == "First Class":
                    total_cost += 140
                    print(f"Seat {selection} is First Class. $140 has been added to your total.")
                elif seat.seat_type == "Emergency":
                    total_cost += 30
                    response = input(
                        f"Seat {selection} is an Emergency seat. Do you accept the terms in case of an emergency? (yes/no) \n")
                    response = response.lower()
                    if response != "yes":
                        print(f"You must accept the terms in order to purchase this seat.")
                        continue
                    print("$30 has been added to your total.")
                else:
                    total_cost += 40
                    print(f"Seat {selection} is a regular seat. $40 has been added to your total.")

                seat.select()


            print(f"The total cost for your selected seats is: ${total_cost}")
            print("Thank you for using Come Fly with me!")
            break












