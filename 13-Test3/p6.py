class C:
    def f(self, first_name, last_name, age):

        if age < 18:
            digits = first_name[0].lower() + last_name[0].lower()
        else:
            digits = first_name[0].upper() + last_name[0].upper()

        wynik = digits + str(age)
        return wynik


c = C()
print(c.f("John", "May", 21))   # JM21
print(c.f("Anna", "Smith", 15)) # as15