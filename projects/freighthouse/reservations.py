import datetime
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
   
    

class Reservation:
    def __init__(self, username, customer_name, guests, start_time, end_time):
        self.username = username
        self.customer_name = customer_name
        self.guests = guests
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"Reservation for {self.customer_name} (Username: {self.username}) for {self.guests} guests from {self.start_time} to {self.end_time}"


class ReservationSystem:
    def __init__(self):
        self.users = []
        self.reservations = []
        self.available_tables_2 = 6
        self.available_tables_4 = 8
        self.available_tables_6 = 2
        self.current_user = None

    def create_user(self, username, password):
        if any(user.username == username for user in self.users):
            print("Username already exists.")
        else:
            self.users.append(User(username, password))
            print("User created successfully.")

    def login_user(self, username, password):
        if any(user.username == username and user.password == password for user in self.users):
            self.current_user = username
            print("Login successful.")
        else:
            print("Login failed.")

    def make_reservation(self, username, customer_name, guests, start_time):
        if self.current_user is None:
            choice = input("You are not logged in. Would you like to log in or create an account? (1. Log in / 2. Create Account): ")
            if choice == "1":
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                self.login_user(username, password)

                username = input("Enter your username: ")
                customer_name = input("Enter customer name: ")
                guests = int(input("Enter the number of guests: "))
                start_time = input("Enter the start time (YYYY-MM-DD HH:MM): ")



            elif choice == "2":
                username = input("Enter a username: ")
                password = input("Enter a password: ")
                self.create_user(username, password)
                self.login_user(username, password)

                username = input("Enter your username: ")
                customer_name = input("Enter customer name: ")
                guests = int(input("Enter the number of guests: "))
                start_time = input("Enter the start time (YYYY-MM-DD HH:MM): ")


            else:
                print("Invalid choice.")
                return

        start_datetime = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M")
        end_datetime = start_datetime + datetime.timedelta(hours=1)

        # Check if there are any available tables of the specified size
        if guests <= 2 and self.available_tables_2 > 0:
            self.available_tables_2 -= 1
        elif 2 < guests < 5 and self.available_tables_4 > 0:
            self.available_tables_4 -= 1
        elif 4 < guests < 7 and self.available_tables_6 > 0:
            self.available_tables_6 -= 1
        else:
            print("Sorry, no available tables of that size.")
            return

        reservation = Reservation(
            self.current_user, customer_name, guests, start_datetime, end_datetime
        )
        self.reservations.append(reservation)
        print("Reservation made successfully!")

    def release_tables(self):
        current_time = datetime.datetime.now()
        for reservation in self.reservations[:]:
            if current_time >= reservation.end_time:
                self.reservations.remove(reservation)
                if reservation.guests <= 2:
                    self.available_tables_2 += 1
                elif 2 < reservation.guests < 5:
                    self.available_tables_4 += 1
                elif 4 < reservation.guests < 7:
                    self.available_tables_6 += 1

    def show_reservations(self):
        if not self.reservations:
            print("No reservations found.")
        else:
            username = input("Enter the username: ")
            user_reservations = [reservation for reservation in self.reservations if reservation.username == username]
        
            if not user_reservations:
                print("No reservations found for the entered username.")
            else:
                print(f"Reservations for {username}:")
                for i, reservation in enumerate(user_reservations, start=1):
                    print(f"Reservation {i}:")
                    print(f"Customer Name: {reservation.customer_name}")
                    print(f"Table Size: {reservation.guests}")
                    print(f"Start Time: {reservation.start_time}")
                    print()
    def show_accounts(self):
        if not self.users:
            print("No user accounts found.")
        else:
            print("User Accounts:")
            for i, user in enumerate(self.users, start=1):
                print(f"Account {i}:")
                print(f"Username: {user.username}")
                print()


reservation_system = ReservationSystem()

@app.route('/')
def index():
    return render_template('projects/freighthouse/reservations.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    customer_name = request.form['customer_name']
    guests = int(request.form['guests'])
    start_time = request.form['start_time']

    reservation_system.make_reservation(username, customer_name, guests, start_time)

    return redirect('/')

if __name__ == '__main__':
    app.run()



while True:
    print("\n==== Reservation System ====")
    print("1. Make a reservation")
    print("2. Show reservations")
    print("3. Accounts")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":

        reservation_system.make_reservation(username, customer_name, guests, start_time)

    elif choice == "2":
        reservation_system.show_reservations()

    elif choice == "3":
        reservation_system.show_accounts()

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")

