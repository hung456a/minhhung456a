import math
import random

class HUMAN(object):
    def __init__(self, name=None, age=None, gender=None):
        if age is not None:
            self._age = age
        else:
            self._age = random.randint(0, 160)
            random.ran
        if gender is not None:
            self._gender = gender
        else:
            self._gender = random.choice(['female', 'male'])


    def age(self):
        return self._age

    def gender(self):
        return self._gender

    def eat(self):
        pass
    def sleep(self):
        pass
    def run(self):
        pass
class STUDENT(HUMAN):

    def __init__(self, age=None, gender=None, id=None, credits=None, grade=None):
        super().__init__(name, age, gender)
        #Using instance's attribute, not Class Attribute here
        self._complex_list = []
        if id is not None:
            self._id = id
        else:
            self._id = random.randint(0, 9999)
        if credits is not None:
            self._credits = credits
        else:
            self._credits = random.randrange(0, 250)
        if grade is not None:
            self._grade = grade
        else:
            self._grade = random.randint(0, 4)
        if self.grande > 3.8 and self.score < 4 :
          return "A+"
        elif self.grande < 3.5 and self.score > 3.3 :
          return "A"
        elif self.grande > 3 and self.score < 3.2 :
          return "B+"
        elif self.grande > 2.6 and self.score < 2.9 :
          return "B"
        elif self.grande > 1.8 and self.score < 2.5 :
          return "C"
        elif self.grande < 1.8 :
          return "D"
    def graduate(result, self):
        if result != "D" and self.credit == 250 :
          return True
        else:
          return False