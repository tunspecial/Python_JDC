class Student:
    def __init__(self , passing_score:int):
        self.__score = passing_score

    @property
    def exam_mark(self):
        print("Checking Passing Score")
        return self.__score

    @exam_mark.setter
    def exam_mark(self , mark):
        if mark >= 40 :
            print(f"Passing Score is {mark}")
            self.__score = mark
        else:
            print(f"Exam Fail!!!")
            self.__score = mark

score = Student(50)
print(f"Current Mark : {score.exam_mark}")

score.exam_mark = 30
print(f"Update Mark : {score.exam_mark}")

class Person:
    def __init__(self , age):
        self.__person_age = age


    def get_age(self):
        return self.__person_age

    def set_age(self , current_age):
        if current_age >= 0:
            print(f"Proper Information Age : {current_age}")
            self.__person_age = current_age
            return current_age
        else:
            print("Age Must Positive Number!!")
            return  current_age

person_age = Person(10)
print(person_age.get_age())

print(person_age.set_age(-1))

print(person_age.get_age())