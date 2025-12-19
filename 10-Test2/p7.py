import re
def f(array):
    pattern = '^[a-z0-9_]{4,}$'
    wynik = 0
    for name in array:
        if bool(re.match(pattern,name)):
            wynik += 1
    return wynik

print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f", "xdd","xddd","maciek.bentko"]))
