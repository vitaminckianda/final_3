import random
import time

def execute(data):
    if len(data) // 2 == 0:
        return data

    data_a, data_b = divide(data)

    data_a = execute(data_a)
    data_b = execute(data_b)

    return merge(data_a, data_b)

def divide(data):
    split_point = len(data) // 2
    data_a = data[:split_point]
    data_b = data[split_point:]
    return data_a, data_b

def merge(data_a, data_b):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(data_a) and right_idx < len(data_b):
        if data_a[left_idx] < data_b[right_idx]:
            result.append(data_a[left_idx])
            left_idx += 1
        else:
            result.append(data_b[right_idx])
            right_idx += 1

    result.extend(data_a[left_idx:])
    result.extend(data_b[right_idx:])
    return result

def generate_list(list_length):
    # Generate a list of random integers
    return [random.randint(1, 999999) for _ in range(list_length)]

def sort_list(list_length):
    data = generate_list(list_length)
    start_time = time.time()
    sorted_data = execute(data)
    end_time = time.time()
    execution_time = end_time - start_time

    # Uncomment below line to print sorted data
    # print(sorted_data)

    print(f"Execution time: {execution_time:.6f} seconds")
    return len(sorted_data), execution_time

if __name__ == '__main__':
    # Example usage
    sort_list(10)  # You can replace 10 with any number to generate a list of that length
