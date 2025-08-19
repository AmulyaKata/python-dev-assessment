def calculate_average(numbers):
    try:
        total = sum(numbers)
        return total / len(numbers)
    except ZeroDivisionError:
        print("Warning: Attempted to calculate average of an empty list.")
        return None


def get_list_element(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        print("Error: Index is out of bounds.")
    except TypeError:
        print("Error: Provided argument is not a list.")
    return None


# Testing average calculation
data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = []  # This will cause an error

print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}")

# Testing get_list_element
print("\n--- get_list_element Tests ---")
print(get_list_element([1, 2, 3], 1))        # Valid: should return 2
print(get_list_element([1, 2, 3], 5))        # Out of bounds
print(get_list_element("not a list", 2))    # Invalid type