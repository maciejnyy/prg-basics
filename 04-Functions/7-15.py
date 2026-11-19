def f(detector):
    current = 0
    for action in detector:
        if action == '+': current += 1
        elif action == '-': current -= 1
        if current >= 3: return True
    return False
if __name__ == "__main__":
    print(f("+-+++-+---"))
    print(f("+-+-+-+-"))
