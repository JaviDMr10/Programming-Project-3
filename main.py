from plane import Airplane

def main():
    plane = Airplane()

    while True:
        print("Welcome to Come Fly with me, choose one of the following options:")
        print()
        print("1. View Seat Map and availability.")
        print("2. View prices.")
        print("3. Exit.")
        print()
        choice = input("Enter your choice number: \n")
        print()

        if choice == "1":
            plane.display_seats()
            purchase = input("Would you like to select a seat? (yes/no): \n")
            purchase = purchase.lower()
            if purchase == "yes":
                plane.purchase_seats()
                print(". \n. \n. \n. \n")
            elif purchase == "no":
                print("Thank you for using Come Fly with me!")
                print(". \n. \n. \n. \n")
            else:
                print("Invalid selection, please enter yes or no.")
                continue

        elif choice == "2":
            plane.display_prices()
            print()
            purchase = input("Would you like to select a seat? (yes/no): \n")
            purchase = purchase.lower()
            if purchase == "yes":
                plane.purchase_seats()
                print(". \n. \n. \n. \n")
            else:
                print("Thank you for using Come Fly with me!")
                print(". \n. \n. \n. \n")

        elif choice == "3":
            print("Thank you for using Come Fly with me!")
            print(". \n. \n. \n. \n")

        else:
            print("Invalid choice. Please select: 1, 2, or 3.")

main()
