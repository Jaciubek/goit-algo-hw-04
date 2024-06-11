import timeit
import random

# Sorting algorithms
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def measure_time(sort_fn, data):
    return timeit.timeit(lambda: sort_fn(data.copy()), number=1)

#Generate random data sets
def random_data_sets_gen():
    data_sets = {
        'small': [random.randint(0, 1000) for _ in range(100)],
        'medium': [random.randint(0, 1000) for _ in range(1000)],
        'large': [random.randint(0, 1000) for _ in range(10000)]
    }
    return data_sets

data_sets = random_data_sets_gen()

# Measure execution times
results = {
    'merge_sort': {},
    'insertion_sort': {},
    'timsort': {}
}

for size, data in data_sets.items():
    results['merge_sort'][size] = measure_time(merge_sort, data)
    results['insertion_sort'][size] = measure_time(insertion_sort, data)
    results['timsort'][size] = measure_time(sorted, data)

# Analyze the results
def analyze_results(results):
    for algorithm, times in results.items():
        print(f"\nResults for {algorithm}:")
        for size, time in times.items():
            print(f"{size.capitalize()} dataset: {time:.6f} seconds")

    for size in data_sets.keys():
        fastest_algorithm = min(results, key=lambda alg: results[alg][size])
        fastest_time = results[fastest_algorithm][size]
        print(f"\nFastest algorithm for {size.capitalize()} dataset: {fastest_algorithm} with time {fastest_time:.6f} seconds")

analyze_results(results)