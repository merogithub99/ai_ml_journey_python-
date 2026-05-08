class InvalidAgeError(Exception):
    def __init__(self, age, message="age must be between 0 and 120"):
        # this message for default if no message is provided when creating the object
        self.age = age
        self.message = message
        super.__init__(self.message)
#Refers to the parent class (Exception).
# This sends the message to Python's built-in exception system.

    def __str__(self):
        return f"{self.age} is invalid {self.message}"


def set_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age, "galat age halis")
    return f"age set to {age}"


try:
    print(set_age(150))
except InvalidAgeError as e:
    print(e)
