#https://pythonim.ru/osnovy/klass-self-v-python

class Person:
    # name made in constructor
    def __init__(self, Q):
        self.name = Q;

    def get_person_name(self):
        return self.name

p1 = Person('David')
p2 = Person('Lisa')

print("Name", p1.get_person_name())
print("Name", p2.get_person_name())

