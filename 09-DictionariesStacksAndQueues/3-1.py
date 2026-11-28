import queue

cards = queue.LifoQueue()
for num in [2, 3, 7, 4, 1, 9, 8]:
    cards.put(num)

last = cards.get()
second_last = cards.get()
print(f"Sum of last two: {last + second_last}")

remaining_sum = 0
while not cards.empty():
    remaining_sum += cards.get()

print(f"Remaining sum: {remaining_sum}")
