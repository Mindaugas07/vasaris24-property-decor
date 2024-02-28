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

# from hashlib import sha256


# class Passwords:
#     PASSWORD_LENGTH = 7

#     def __init__(self, password: str) -> None:
#         if len(password) > self.PASSWORD_LENGTH:
#             self._password = sha256(password.encode("utf-8")).hexdigest()
#         else:
#             raise ValueError("Password should be at least 8 characters long!")

#     @property
#     def password(self) -> str:
#         return self._password

#     @password.setter
#     def set_password(self, new_password: str) -> None:
#         if len(new_password) > self.PASSWORD_LENGTH:
#             self._password = sha256(new_password.encode("utf-8")).hexdigest()
#         else:
#             raise ValueError("Password should be at least 8 characters long!")

#     @password.deleter
#     def delete_password(self) -> None:
#         del self._password


# mano_password = Passwords("1namas")
# print(mano_password.password)
# mano_password.set_password = "456slaptazodis"
# print(mano_password.password)



import hashlib, random
from dataclasses import dataclass


@dataclass
class NewPassword:
    old_password: str
    new_password: str


class WrongPasswordError(Exception):
    pass


class Password:
    MIN_PASSWORD_LENGTH = 6
    WEAK_PASSWORDS = [
        "123456",
        "12345678",
        "123456789",
        "12345",
        "1234567",
        "password",
        "abcdef",
        "abc123",
        "qwerty",
        "111111",
        "1234",
        "iloveyou",
    ]

    def __init__(self, password: str) -> None:
        self._password = self._validate_password(password)

    def _validate_password(self, password) -> str:
        if (
            len(password) >= self.MIN_PASSWORD_LENGTH
            and password not in self.WEAK_PASSWORDS
        ):
            print("Password meets the requirements.")
            hashed_password = self._hash_password(password=password)
            return hashed_password
        else:
            return "Weak password"

    @staticmethod
    def _hash_password(password) -> str:
        password_bytes = password.encode("utf-8")
        hash_object = hashlib.sha256(password_bytes)
        return hash_object.hexdigest()

    def get_scrambled_hash(self) -> str:
        hash_list = []
        while len(hash_list) < random.randint(8, 12):
            x = self._password[random.randrange(64)]
            if x not in hash_list:
                hash_list.append(x)
        scrambled_hash = "".join(hash_list)
        return scrambled_hash

    @property
    def password(self) -> str:
        return self.get_scrambled_hash()

    @password.setter
    def password(self, new_password: "NewPassword") -> None:
        compare_hash = self._hash_password(password=new_password.old_password)
        if compare_hash == self._password:
            self._password = self._validate_password(new_password.new_password)
            print("New password has been set")
        else:
            raise WrongPasswordError("Wrong password")


passw = Password("passwordas")

print(passw.password)

new_password = NewPassword(old_password="passwordas", new_password="blablablabal")

try:
    passw.password = new_password
except WrongPasswordError as err:
    print(err)

print(passw.password)



# class Person:
#     def __init__(self, name: str) -> None:
#         self._name = name

#     @property
#     def name(self) -> None:
#         return self._name

#     @name.setter
#     def set_name(self, new_name: str) -> None:
#         self._name = new_name

#     @name.deleter
#     def del_name(self):
#         del self._name


# class PersonOne(Person):
#     def __init__(self, name: str) -> None:
#         super().__init__(name)

#     @property
#     def name(self):
#         return super().name


# # person_one = Person(name="Vytautas")
# # print(person_one.name)
# # person_one.set_name = "Algirdas"
# # print(person_one.name)
# # person_one.del_name()
# # print(person_one.name)

# person_two = PersonOne(name="Vilius")
# print(person_two.name)
# person_two.name = "Mykolas"


# Create a class UserProfile that manages user information and access privileges. 
# Use properties with getters, setters, and deleters to control access to sensitive data and modify privileges.

# Requirements:
#  - Define properties for:
#  - username (getter and setter)
#  - email (getter and setter)
#  - is_admin (getter, setter, and deleter) – This property should validate that the user is authorized to
#    modify the is_admin attribute and provide appropriate error messages for unauthorized attempts.

class UserProfile:
    
    def __init__(self, username: str, email: str, ) -> None:
        pass