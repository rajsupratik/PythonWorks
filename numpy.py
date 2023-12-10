## Q.1--
import numpy as np

# a. Convert numbers = [1, 2.0, 3] to numpy array and convert all elements to string type.
numbers = [1, 2.0, 3]
numpy_array_a = np.array(numbers)
string_array_a = numpy_array_a.astype(str)
print("a. Numpy array with string elements:", string_array_a)

# b. Create a 2D array through list and set dtype as int32
two_d_array_b = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
print("\nb. 2D Array with dtype int32:\n", two_d_array_b)

# c. Find the rows and columns of the 2D array created in part b
rows, columns = two_d_array_b.shape
print("\nc. Rows:", rows, "Columns:", columns)

# d. Print 10 random numbers between 1 and 100.
random_numbers = np.random.randint(1, 101, 10)
print("\nd. 10 random numbers between 1 and 100:", random_numbers)

## Q.2--

# a. Write a NumPy program to get help on the add function
help(np.add)

# b. Write a NumPy program to test whether none of the elements of a given array is zero
array_b = np.array([1, 2, 3, 4])
result_b = np.all(array_b != 0)
print("\nb. None of the elements is zero:", result_b)

# c. Write a NumPy program to test whether any of the elements of a given array is non-zero
array_c = np.array([0, 0, 0, 4])
result_c = np.any(array_c != 0)
print("\nc. Any of the elements is non-zero:", result_c)

# d. Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution
random_numbers = np.random.randn(15)
print("\nd. Array of 15 random numbers from a standard normal distribution:\n", random_numbers)
