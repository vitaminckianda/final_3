# run_sorting.py
import main
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Initialize lists to store data
    list_lengths = list(range(1000, 100000, 1000))
    execution_times = []

    # Call sort_list function from the sort_algorithm module and record execution times
    for length in list_lengths:
        _, execution_time = main.sort_list(length)
        execution_times.append(execution_time)

    # Plot the data
    plt.plot(list_lengths, execution_times, marker='o', linestyle='-')
    plt.title('Execution Time vs. List Length')
    plt.xlabel('List Length')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True)
    plt.show()
