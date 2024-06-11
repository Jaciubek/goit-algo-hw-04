Results for merge_sort:
Small dataset: 0.000506 seconds
Medium dataset: 0.012063 seconds
Large dataset: 0.134011 seconds

Results for insertion_sort:
Small dataset: 0.000770 seconds
Medium dataset: 0.082159 seconds
Large dataset: 11.802331 seconds

Results for timsort:
Small dataset: 0.000019 seconds
Medium dataset: 0.000208 seconds
Large dataset: 0.005694 seconds

Fastest algorithm for Small dataset: timsort with time 0.000019 seconds

Fastest algorithm for Medium dataset: timsort with time 0.000208 seconds

Fastest algorithm for Large dataset: timsort with time 0.005694 seconds



Timsort, which combines merge and insertion sorting, is more efficient, especially on larger datasets, which is why it is used in Python's built-in sorting functions. Timsort is a superior sorting algorithm due to its hybrid nature, efficiently handling various types of data distributions.
