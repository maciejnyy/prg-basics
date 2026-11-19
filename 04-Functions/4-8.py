def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f"{hours:02d}:{minutes:02d}"
    elif time_format == '12':
        ampm = 'am' if hours < 12 or hours == 24 else 'pm'
        h12 = hours % 12
        if h12 == 0: h12 = 12
        return f"{h12}:{minutes:02d}{ampm}"

if __name__ == "__main__":
    print(time_string(15, 38, '24'))
    print(time_string(8, 3, '24'))
    print(time_string(11, 15, '12'))
    print(time_string(19, 2, '12'))
