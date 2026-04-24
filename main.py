numbers = [6, 5, 7, 1, 3, 8, 2]

def get_sum(numbers):
    total = 0
    i = 0

    while i < len(numbers):
        total += numbers[i]
        i += 1
    return total

def find_max(numbers):
    max_num = numbers[0]
    i = 0

    while i < len(numbers):
        if numbers[i] > max_num:
            max_num = numbers[i]
        i += 1
    return max_num

def find_min(numbers):
    min_num = numbers[0]
    i = 0

    while i < len(numbers):
        if numbers[i] < min_num:
            min_num = numbers[i]
        i += 1
    return min_num

def count_even(numbers):
    count = 0
    i = 0

    while i < len(numbers):
        if numbers[i] % 2 == 0:
            count += 1
        i += 1
    return count

if __name__ == "__main__":
    
    print("Sum:", get_sum(numbers))
    print("Max:", find_max(numbers))
    print("Min:", find_min(numbers))
    print("Even count:", count_even(numbers))
