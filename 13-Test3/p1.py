def f(word):
    tab = list(word)
    words = []
    wynik = ""
    for i in range(len(tab)):
        string = ""
        for j in range(len(tab)):
            if i != 0:
                tab[i-1] = tab[i-1].lower()
            tab[i] = tab[i].upper()
            string += tab[j]
        if i != len(tab)-1 :
            string += '-'
        words.append(string)
        
    for i in words:
       wynik += i 
    return wynik
    
print(f("meksyk"))
print(f("a"))
print(f(""))