import random

def rand_elem(array):
    return random.choice(array)

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50, 60]
    print("Random elements:")
    for _ in range(3):
        print(rand_elem(arr))
