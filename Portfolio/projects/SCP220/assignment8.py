import colorama
from colorama import Fore, Style

colorama.init()


class Car:
    def __init__(self, make, model, VIN, mileage, price, features):
        self.make = make
        self.model = model
        self.VIN = VIN
        self.mileage = mileage
        self.price = price
        self.features = features


# empty list to store Car objects
cars = []


def main():
    global cars

    # save and load methods
    def load_data():
        try:
            with open("data.txt", "r") as data:
                for line in data:
                    values = line.strip().split(",")
                    if len(values) >= 6:
                        make, model, VIN, mileage, price, *features = values
                        mileage = int(mileage)
                        price = float(price)
                        car = Car(make, model, VIN, mileage, price, features)
                        cars.append(car)
                if not cars:
                    print(Fore.YELLOW + "File is empty. Please add some data.")
        except FileNotFoundError:
            print(Fore.RED + "File does not exist.")
        except ValueError:
            print(Fore.YELLOW + "File is empty. Please add some data.")
        return cars

    def save_data():
        with open("data.txt", "w") as data:
            for car in cars:
                data.write(
                    f"{car.make},{car.model},{car.VIN},{car.mileage},{car.price},{','.join(car.features)}\n"
                )
        print(Fore.GREEN + "Data saved successfully!" + Style.BRIGHT)

    # CLI menu
    while True:
        print(Fore.BLUE + Style.BRIGHT + "\n====Used Car Inventory====")
        print(Style.RESET_ALL + Fore.YELLOW + "\n1. Add Car")
        print(Fore.YELLOW + "2. Edit Car")
        print("3. Remove Car")
        print("4. Display all Cars")
        print(Fore.GREEN + "5. Save Cars")
        print(Fore.GREEN + "6. Load Cars")
        print(Fore.RED + "7. Exit")

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print(Fore.RED + "Invalid Input. Please enter a number.")

        if choice == 1:
            make = input("Enter car make: ")
            model = input("Enter car model: ")
            VIN = input("Enter car VIN: ")
            mileage = int(input("Enter car mileage: "))
            price = float(input("Enter car price: "))
            features = input("Enter car features (separated by commas): ").split(",")
            car = Car(make, model, VIN, mileage, price, features)
            cars.append(car)
            print(Fore.GREEN + "Car added successfully!")

        elif choice == 2:
            VIN = input("Enter car VIN to edit: ")
            found = False
            for car in cars:
                if car.VIN == VIN:
                    make = input(
                        "Enter new car make (or press enter to keep the same): "
                    )
                    if make:
                        car.make = make
                    model = input(
                        "Enter new car model (or press enter to keep the same): "
                    )
                    if model:
                        car.model = model
                    mileage = int(
                        input(
                            "Enter new car mileage (or press enter to keep the same): "
                        )
                    )
                    if mileage:
                        car.mileage = float(mileage)
                    price = input(
                        "Enter new car price (or press enter to keep the same): "
                    )
                    if price:
                        car.price = price
                    features = input(
                        "Enter new car features (separated by commas, or press enter to keep the same): "
                    )
                    if features:
                        car.features = features.split(",")
                    print(Fore.GREEN + "Car updated successfully!")
                    found = True
                    break
            if not found:
                print(Fore.RED + "Car not found")

        elif choice == 3:
            VIN = input("Enter car VIN to remove: ")
            found = False
            for car in cars:
                if car.VIN == VIN:
                    cars.remove(car)
                    print(Fore.GREEN + "Car removed successfully!")
                    found = True
                    break
            if not found:
                print(Fore.RED + "Car not found")

        elif choice == 4:
            print(Fore.BLUE + "\nAll cars in inventory:")
            for car in cars:
                print(
                    f"{car.make} {car.model}, VIN: {car.VIN}, Mileage: {car.mileage}, Price: ${car.price}, Features: {', '.join(car.features)}"
                )

        elif choice == 5:
            save_data()

        elif choice == 6:
            try:
                cars = load_data()
                print("All cars in inventory:")
                for car in cars:
                    print(
                        f"{car.make} {car.model}, VIN: {car.VIN}, Mileage: {car.mileage}, Price: ${car.price}, Features: {', '.join(car.features)}"
                    )
            except FileNotFoundError:
                print("File does not exist")
            except ValueError:
                print("File is empty")

        elif choice == 7:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
