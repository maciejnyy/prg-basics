array = ['Gensadasdasfffffffddaowasdasefa','Kjghhjonstantynopolitanczyk', 'Onufasdsadsadry', 'Celestyna', 'Aldjknadsndlkasjndsaljkdaojzy', 'Pankracy']
letters = len(array[0])
max = ""
for name in array:
    if len(name) > letters:
        letters = len(name)
        max = name
    elif len(name) == letters:
        max = name
    else: 
        continue
print(max)
