class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        text = f"{self.surname}{self.name[0]}{self.seniority}"
        return text.upper() if self.age >= 18 else text.lower()

if __name__ == "__main__":
    print(C("Anna", "May", 17, 7))
    print(C("George", "Brown", 21, 4))
