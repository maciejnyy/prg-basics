def day_name(day_number):
    days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    return days.get(day_number, '')

if __name__ == "__main__":
    print('The name of day 5 in the week is', day_name(5))
    print('The name of day 3 in the week is', day_name(3))
    print('The name of day 7 in the week is', day_name(7))
