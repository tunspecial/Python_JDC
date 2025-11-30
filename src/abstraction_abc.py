from abc import ABC, abstractmethod


class Student(ABC):

    @abstractmethod
    def read_book(self) -> str:
        pass

    @abstractmethod
    def play_football(self) -> str:
        pass


class Activity(Student):
    def __init__(self, name: str):
        self.name = name

    def read_book(self) -> str:
        print(f"Student is read {self.name}")

    def play_football(self) -> str:
        print(f"Student is playing {self.name}")


if __name__ == "__main__":
    a1 = Activity("Python")
    a1.read_book()

    a2 = Activity("Football")
    a2.play_football()
