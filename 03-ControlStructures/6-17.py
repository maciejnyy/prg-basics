time24 = input("Enter time (24-hour format): ")
h, m = map(int, time24.split(':'))
ampm = "am" if h < 12 or h == 24 else "pm"
h12 = h % 12
if h12 == 0: h12 = 12
print(f"Time in 12-hour format: {h12}:{m:02d}{ampm}")
