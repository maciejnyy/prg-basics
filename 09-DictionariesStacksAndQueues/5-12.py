import queue

def reverse_string(text):
    stack = queue.LifoQueue()
    for char in text:
        stack.put(char)
    reversed_text = ""
    while not stack.empty():
        reversed_text += stack.get()
    return reversed_text

if __name__ == "__main__":
    user_text = input("Enter text to reverse: ")
    print("Reversed text:", reverse_string(user_text))
