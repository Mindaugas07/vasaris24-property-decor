# class Position:
#     def __init__(self, x: float, y: float) -> None:
#         self._x = x
#         self._y = y

#     def get_x(self) -> float:
#         return self._x

#     def get_y(self) -> float:
#         return self._y

#     def set_x(self, value: float) -> None:
#         self._x = value

#     def set_y(self, value: float) -> None:
#         self._x = value


# coord = Position(x=10.4, y=12.0)
# print(coord.get_x())

# coord.set_x(9.2)
# print(coord.get_x())

# from random import randint


# class Position:
#     def __init__(self, x: float, y: float) -> None:
#         self._position_x = x
#         self._position_y = y

#     @property
#     def position_x(self):
#         print("Getting position x")
#         return self._position_x

#     @position_x.setter
#     def position_x(self, value: float):
#         print("Setting position x")
#         random_numb = randint(0, 100)
#         self._position_x = value * random_numb

#     @position_x.deleter
#     def position_x(self):
#         print("Deleting position x ")
#         del self._position_x


# cord = Position(x=12.1, y=11.1)
# print(cord.position_x)
# cord.position_x = 13.33

# print(cord.position_x)
# del cord.position_x
# cord.position_x = 17.33
# print(cord.position_x)


# Create a class that encapsulates logic for converting temperatures between Celsius and Fahrenheit, Kelvin .
# Use properties with getters and setters to ensure valid temperature values and provide a user-friendly interface.


# class ConvertTemperature:
#     LOWEST_CELSIUS_TEMP = -273.15
#     KELVIN_VALUE = 273.15
#     FAHRENHEIT_VALUE = 32

#     def __init__(self, temp_in_celsius=0.0) -> None:
#         self._temp_in_celsius = temp_in_celsius

#     @property
#     def temp_in_celsius(self) -> float:
#         print("Temperature in Celsius: ")
#         return self._temp_in_celsius

#     @property
#     def celsius_to_fahrenheit(self) -> float:
#         return round(((1.8 * self._temp_in_celsius) + self.FAHRENHEIT_VALUE), 2)

#     @property
#     def celsius_to_kelvin(self) -> float:
#         return round((self._temp_in_celsius + self.KELVIN_VALUE), 2)

#     @temp_in_celsius.setter
#     def temp_in_celsius(self, value):
#         if value > self.LOWEST_CELSIUS_TEMP:
#             print("Setting temperature in Celsius...")
#             self._temp_in_celsius = value
#         else:
#             self._temp_in_celsius = self.LOWEST_CELSIUS_TEMP
#             print(
#                 "Value you've entered is below lowest temperature.\nTemperature has been set to it's lowest."
#             )


# converter = ConvertTemperature()

# print(converter.celsius_to_fahrenheit, converter.celsius_to_kelvin)

# converter.temp_in_celsius = 15.0

# print(converter.celsius_to_fahrenheit, converter.celsius_to_kelvin)


# Create a class that securely stores and manages passwords. 
# Use properties with getters and setters to ensure password security and prevent unauthorized access.

# Requirements:
#  - Define a property named password that sets the password. The setter should:
#  - Enforce a minimum password length (e.g., 8 characters).
#  - Check for common password patterns or dictionary words (optional for an extra challenge).
#  - Hash the password using a secure hashing algorithm (e.g., SHA-256) before storing it.
#  - Create a getter for password that always returns randomly places 8 to 12 elements from hash function  (symbols must not be duplicated) to prevent direct access to the actual password.
#  - Create a setter, that would take current password and new one, if current password is correct , would set new one, otherwise raise error.

