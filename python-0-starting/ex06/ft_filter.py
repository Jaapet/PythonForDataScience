def ft_filter(function, iterable):

	"""
    ft_filter(function or None, iterable) --> iterator

    This is a custom implementation of the built-in filter function.
    It returns an iterator that yields only the items in 'iterable'
    for which the function returns True. If 'function' is None, it returns
    the items that are considered 'True' in a Boolean context.
    """

	if function is None:
		return (element for element in iterable if element)
	else:
		return (element for element in iterable if function(element))


# tests with built-in filter() comparison

# def main():

# 	# Built-in filter
# 	print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])))  # Output: [2, 4, 6]
# 	# Custom ft_filter
# 	print(list(ft_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])))  # Output: [2, 4, 6]

# 	# Built-in filter with None as the function
# 	print(list(filter(None, [0, 1, "", "Hello", None, False, True])))  # Output: [1, 'Hello', True]
# 	# Custom ft_filter with None as the function
# 	print(list(ft_filter(None, [0, 1, "", "Hello", None, False, True])))  # Output: [1, 'Hello', True]

# 	# Built-in filter
# 	print(list(filter(lambda x: x > 10, [1, 2, 3, 4, 5])))  # Output: []
# 	# Custom ft_filter
# 	print(list(ft_filter(lambda x: x > 10, [1, 2, 3, 4, 5])))  # Output: []

# if __name__ == "__main__":
# 	main()