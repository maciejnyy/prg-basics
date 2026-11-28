class Statistics:
    def __init__(self):
        self.numbers = []

    def add_number(self, number=None):
        if number is None:
            number = float(input("Enter a number: "))
        self.numbers.append(number)

    def display_numbers(self):
        print(" ".join(str(n) for n in self.numbers))

    def get_max(self):
        return max(self.numbers) if self.numbers else None

    def get_min(self):
        return min(self.numbers) if self.numbers else None

    def get_mean(self):
        return sum(self.numbers) / len(self.numbers) if self.numbers else None

    def get_median(self):
        if not self.numbers:
            return None
        sorted_nums = sorted(self.numbers)
        n = len(sorted_nums)
        mid = n // 2
        if n % 2 == 1:
            return sorted_nums[mid]
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2

    def print_statistics(self):
        print(f"Minimum: {self.get_min()}")
        print(f"Maximum: {self.get_max()}")
        print(f"Arithmetic mean: {self.get_mean():.2f}")
        print(f"Median: {self.get_median()}")

if __name__ == "__main__":
    stats = Statistics()
    for num in [12, 37, 6, 9, 17]:
        stats.add_number(num)
    stats.display_numbers()
    stats.print_statistics()
