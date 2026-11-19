dec = int(input("Enter decimal number: "))
orig = dec
bin_str = ""
if dec == 0: bin_str = "0"
while dec > 0:
    bin_str = str(dec % 2) + bin_str
    dec //= 2
print(f"{orig}(10) = {bin_str}(2)")
