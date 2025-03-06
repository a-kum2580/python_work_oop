# a. Character and Vehicle Classes

class Character:
    """Base class for a character in the game, with encapsulated attributes."""
    
    def __init__(self, name, health=100, position=(0, 0)):
        # Initialize character attributes
        self._name = name               # Name of the character
        self._health = health           # Health points
        self._position = position       # Position on the map
        self._current_vehicle = None    # Current vehicle the character is in, if any

    # Getters (accessors) for encapsulated attributes
    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @property
    def position(self):
        return self._position

    def move(self, new_position):
        # Move the character to a new position
        self._position = new_position
        print(f"{self._name} moved to position {new_position}")

    def attack(self, target):
        # Character attacks a target, reducing its health
        print(f"{self._name} attacks {target.name}")
        target._health -= 10

    def interact(self, object_name):
        # Character interacts with an object in the environment
        print(f"{self._name} interacts with {object_name}")

# Vehicle class
class Vehicle:
    """Base class for a vehicle in the game."""
    
    def __init__(self, type_name, speed, fuel_level=100):
        # Initialize vehicle attributes
        self._type = type_name               # Type of vehicle (e.g., car, truck)
        self._speed = speed                  # Speed of vehicle
        self._fuel_level = fuel_level        # Initial fuel level
        self._is_running = False             # Whether the vehicle is running
        self._current_driver = None          # Current driver of the vehicle

    # Getters (accessors) for encapsulated attributes
    @property
    def type(self):
        return self._type

    @property
    def fuel_level(self):
        return self._fuel_level

    def drive(self, distance):
        # Drive the vehicle a certain distance, reducing fuel level
        if self._is_running and self._fuel_level > 0:
            self._fuel_level -= distance * 0.1
            print(f"{self._type} driven for {distance} units. Fuel remaining: {self._fuel_level}")
        else:
            print("Vehicle cannot drive - either not running or out of fuel")

    def refuel(self, amount):
        # Refuel the vehicle, up to a maximum of 100
        self._fuel_level = min(100, self._fuel_level + amount)
        print(f"{self._type} refueled. Current fuel level: {self._fuel_level}")

    def stop(self):
        # Stop the vehicle
        self._is_running = False
        print(f"{self._type} stopped")


# b. Interaction Between Objects
class Character(Character):  # Extending the previous Character class
    """Extends Character to allow for vehicle interactions."""
    
    def get_in(self, vehicle):
        # Character gets into a vehicle if it has no driver
        if vehicle._current_driver is None:
            print(f"{self._name} gets into the {vehicle.type}")
            self._current_vehicle = vehicle
            vehicle._current_driver = self
            vehicle._is_running = True
        else:
            print("Vehicle already has a driver")

    def get_out(self):
        # Character gets out of the vehicle they are currently in
        if self._current_vehicle:
            print(f"{self._name} gets out of the {self._current_vehicle.type}")
            self._current_vehicle._current_driver = None
            self._current_vehicle._is_running = False
            self._current_vehicle = None
        else:
            print(f"{self._name} is not in any vehicle")


# c. Specialized Character Abilities
class HeroCharacter(Character):
    """Specialized HeroCharacter with additional abilities."""

    def __init__(self, name, health=150, position=(0, 0)):
        # Initialize hero character with higher health
        super().__init__(name, health, position)
        self._special_ability_ready = True  # Ability status

    def double_jump(self):
        # Special ability: double jump
        if self._special_ability_ready:
            print(f"{self.name} performs a double jump!")
            self._special_ability_ready = False
        else:
            print("Double jump not ready!")

    def fast_run(self):
        # Special ability: run at super speed
        print(f"{self.name} runs at super speed!")


# d. Handling Different Types of Objects (Polymorphism)
class Police(HeroCharacter):
    """Police officer character with specific interaction."""

    def interact(self, object_name):
        # Overriding interaction to investigate objects
        print(f"{self._name} investigates {object_name}")

class Firefighter(HeroCharacter):
    """Firefighter character with specific interaction."""

    def interact(self, object_name):
        # Overriding interaction to check for hazards
        print(f"Firefighter {self._name} checks {object_name} for hazards")


# e. Simple Game Scenario
def run_game_scenario():
    # Create objects for the game scenario
    hero = HeroCharacter("Harley")
    police = Police("Officer Goodwin")
    car = Vehicle("Sports Car", 120)
    
    print("\n=== Starting Mission: Bank Robbery Response ===")
    
    # Demonstrate character movement and special abilities (Phase 1)
    print("\nPhase 1: Initial Response")
    hero.move((10, 10))
    hero.double_jump()  # Unique ability of HeroCharacter
    
    # Vehicle interaction: getting into, driving, and getting out (Phase 2)
    print("\nPhase 2: Vehicle Chase")
    hero.get_in(car)
    car.drive(50)
    
    # Character and vehicle interaction with the environment (Phase 3)
    print("\nPhase 3: Investigation")
    hero.get_out()
    hero.interact("Bank Door")  # HeroCharacter interacting with the environment
    police.interact("Crime Scene")  # Police object with specialized interaction
    
    # Demonstrate further special abilities of HeroCharacter (Phase 4)
    print("\nPhase 4: Pursuit")
    hero.fast_run()
    
    # Manage vehicle refueling and further driving (Phase 5)
    print("\nPhase 5: Mission Completion")
    car.refuel(30)
    hero.get_in(car)
    car.drive(20)
    hero.get_out()
    
    print("\n=== Mission Complete ===")

# Run the game scenario
if __name__ == "__main__":
    run_game_scenario()
