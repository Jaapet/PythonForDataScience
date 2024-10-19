import sys

try:
	if len(sys.argv) <= 1:
		print(f"")
	elif len(sys.argv) > 2:
		raise AssertionError("more than one argument is provided")
	else:
		try:
			n = int(sys.argv[1])
			if n % 2 == 0:
				print(f"I'm Even.")
			else:
				print(f"I'm Odd.")
		except:
			raise AssertionError("argument is not an integer")
except AssertionError as e:
	print(f"{AssertionError.__name__}: {e}")
