import module_7_5
if __name__ == "__main__":
    num = 7
    print(f"A number: {num}")
    print(f"Number {num} in the range <2,15>: {'yes' if module_7_5.is_in_range(num, 2, 15) else 'no'}")
