ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"

# In Python 3.10 (and in all versions), tuples are immutable,
# meaning their elements cannot be modified once the tuple is created.
# If you try to modify a tuple directly, you'll get an error.
ft_tuple = ("Hello", "France!")

# A set in Python is an unordered collection of unique elements.
# Unlike lists or tuples, sets do not allow duplicates,
# and the elements are not stored in any particular order.
# Since a set is unordered, you cannot modify specific elements by their index
# (because there's no concept of index in sets).
# However, you can add(val), remove(val), discard(val), or update([vals]) elements in the set.
ft_set.discard("tutu!")
ft_set.add("Nice!")

# In Python, a dictionary (dict) is a collection of key-value pairs.
# Each key in a dictionary is unique, and it maps to a value.
# Dictionaries are mutable, meaning you can change, add,
# or remove (del or .pop()) key-value pairs after the dictionary is created.
ft_dict["Hello"] = "42Nice!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)