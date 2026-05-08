class CannotVoteException(Exception):
    def __init__(self, age, message="below 18 cannot vote "):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.age} is invalid age {self.message}"


def age_check(age):
    if age < 18:
        raise CannotVoteException(age, message="18 katesi aaaijo")
    return f"your age is {age} you can vote .....proceed"


try:
    print(age_check(1))
except CannotVoteException as e:
    print(e)
