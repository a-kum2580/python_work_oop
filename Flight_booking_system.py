from datetime import datetime
import os
import re
from abc import ABC, abstractmethod

# Abstract base class demonstrating abstraction
class Booking(ABC):
    @abstractmethod
    def calculate_price(self):
        pass
    
    @abstractmethod
    def display_details(self):
        pass

class Flight:
    def __init__(self, flight_number, origin, destination, price):
        self.__flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.price = price
        self.available_seats = 50

    def get_flight_number(self):
        return self.__flight_number

    def book_seat(self):
        if self.available_seats > 0:
            self.available_seats -= 1
            return True
        return False

    def display_flight_info(self):
        return f"Flight {self.__flight_number}: {self.origin} → {self.destination} | Price: ${self.price} | Seats available: {self.available_seats}"

class FlightBooking(Booking):
    def __init__(self, flight, passenger_name, passenger_email, passport_number):
        self.flight = flight
        self.passenger_name = passenger_name
        self.passenger_email = passenger_email
        self.passport_number = passport_number
        self.booking_date = datetime.now()
        self.booking_id = f"{flight.get_flight_number()}-{passenger_name[:3]}-{self.booking_date.strftime('%Y%m%d')}"

    def calculate_price(self):
        return self.flight.price

    def display_details(self):
        return f"""
╔══════════════════════════════════════════════════════════
║ BOOKING CONFIRMATION
║ Booking ID: {self.booking_id}
║ Passenger: {self.passenger_name}
║ Email: {self.passenger_email}
║ Passport Number: {self.passport_number}
║ Flight: {self.flight.get_flight_number()}
║ Route: {self.flight.origin} to {self.flight.destination}
║ Price: ${self.calculate_price()}
║ Date: {self.booking_date.strftime('%Y-%m-%d %H:%M')}
╚══════════════════════════════════════════════════════════
        """

class BookingSystem:
    def __init__(self):
        self.flights = []
        self.bookings = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_flights(self, origin, destination):
        return [flight for flight in self.flights 
                if flight.origin.lower() == origin.lower() 
                and flight.destination.lower() == destination.lower()]

    def create_booking(self, flight, passenger_name, passenger_email, passport_number):
        if flight.book_seat():
            booking = FlightBooking(flight, passenger_name, passenger_email, passport_number)
            self.bookings.append(booking)
            return booking
        return None

    def display_all_flights(self):
        print("\nAvailable Flights:")
        print("═" * 65)
        for i, flight in enumerate(self.flights, 1):
            print(f"{i}. {flight.display_flight_info()}")
        print("═" * 65)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_valid_email():
    while True:
        email = input("Enter your email: ").strip()
        if '@' in email and '.' in email:
            return email
        print("Invalid email format. Please try again.")

def get_valid_passport():
    while True:
        passport = input("Enter your passport number: ").strip().upper()
        # Basic passport validation: 1-2 letters followed by 5-7 numbers
        if re.match(r'^[A-Z]{1,2}\d{5,7}$', passport):
            return passport
        print("Invalid passport format. Please enter a valid passport number (e.g., A1234567 or AB123456)")

def main():
    # Initialize booking system
    booking_system = BookingSystem()

    # Add sample flights
    sample_flights = [
        Flight("FL001", "New York", "London", 500),
        Flight("FL002", "London", "Paris", 200),
        Flight("FL003", "Paris", "Rome", 150),
        Flight("FL004", "Rome", "Madrid", 180),
        Flight("FL005", "Madrid", "Berlin", 220)
    ]
    
    for flight in sample_flights:
        booking_system.add_flight(flight)

    while True:
        clear_screen()
        print("\n=== Welcome to Flight Booking System ===")
        print("1. View all available flights")
        print("2. Search flights")
        print("3. Book a flight")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            booking_system.display_all_flights()
            input("\nPress Enter to continue...")

        elif choice == '2':
            clear_screen()
            origin = input("\nEnter departure city: ")
            destination = input("Enter destination city: ")
            
            available_flights = booking_system.search_flights(origin, destination)
            
            if available_flights:
                print("\nFlights found:")
                for i, flight in enumerate(available_flights, 1):
                    print(f"{i}. {flight.display_flight_info()}")
            else:
                print("\nNo flights found for this route!")
            input("\nPress Enter to continue...")

        elif choice == '3':
            clear_screen()
            booking_system.display_all_flights()
            
            try:
                flight_choice = int(input("\nEnter flight number (1-5): ")) - 1
                if 0 <= flight_choice < len(booking_system.flights):
                    selected_flight = booking_system.flights[flight_choice]
                    
                    print("\nEnter passenger details:")
                    name = input("Enter your full name: ")
                    email = get_valid_email()
                    passport = get_valid_passport()
                    
                    booking = booking_system.create_booking(selected_flight, name, email, passport)
                    
                    if booking:
                        clear_screen()
                        print(booking.display_details())
                    else:
                        print("\nSorry, no seats available on this flight!")
                else:
                    print("\nInvalid flight number!")
            except ValueError:
                print("\nInvalid input! Please enter a number.")
            input("\nPress Enter to continue...")

        elif choice == '4':
            print("\nThank you for using our Flight Booking System. Goodbye!")
            print("\tBy @Oscar,@Edube,@Mukama,@Zahara,@Ann")
            break

        else:
            print("\nInvalid choice! Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()