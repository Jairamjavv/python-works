"""
source: https://www.youtube.com/watch?v=7GupibhOTdY
"""

from uuid import uuid4, UUID

underscore_in_numbers: int = 1_000_000  # visually helps reading
print(f"1_000_000 in python is taken as {underscore_in_numbers}")


_ = 10  # unimportant values can be assigned with `_`

for _ in range(2):  # can be used in for loops instead of using `i`
    print(_ + 1)

for _ in range(1, 6):
    for __ in range(1, 4):
        for ___ in range(1, 2):
            print(f"_:{_}, __:{__}, ___:{___}")


sample_tuple = (1, 2, 3)
a, _, _ = sample_tuple
print(f"a:{a}")

# unpack first and last element
sample_list = [10, 20, 30, 40]
a, *_, b = sample_list  # `*_` takes all the middle values
print(f"a:{a}, b:{b}, _:{_}")


class User:
    def __init__(self) -> None:
        self._id = uuid4()  # protected value, scope is current class and subclass
        self.__user_name: str = "Jairam"  # private variable

    def __get_id(self) -> UUID:  # private function, scope is current class
        return self._id

    def _get_id(
        self,
    ) -> UUID:  # protected function, scope is current class and subclass
        return self.__get_id()

    def get_id(self) -> UUID:  # normal function
        return self._get_id()


user: User = User()
print(f"Id returned from user is:{user.get_id()}")
