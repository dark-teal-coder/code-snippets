class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def __eq__(self, other):
        return  (self.firstname == other.firstname) \
        and   (self.lastname == other.lastname)

class Student(Person):
    def __init__(self, first, last, school, id):
        super().__init__(first, last)
        self.school = school
        self.id = id


man1 = Person('Homer', 'Simpson')
man2 = Person('Homer', 'Simpson')
woman = Person('Marge', 'Simpson')
student = Student('Marge', 'Simpson', 'Simmons', 2468)

print(man1 == man1)
print(man1 == man2)
print(man1 == woman)
print(woman == student)
print(student == woman)


print("Coding has the following benefits: ")
pros_iter = iter(["Computational Thinking Skills",
                  "Mathematics Skills",
                  "Logical Thinking Skills",
                  "Problem Solving Skills",
                  "..."])
while True:
    try:
        benefit = next(pros_iter)
    except StopIteration:
        break
    print(benefit)
