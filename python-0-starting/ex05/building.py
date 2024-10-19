import sys
import string

def count(str):
	print(f"The text contains {len(str)} characters:")
	print(f"{sum(1 for char in str if char.isupper())} lower letters")
	print(f"{sum(1 for char in str if char.islower())} upper letters")
	print(f"{sum(1 for char in str if char in string.punctuation)} punctuation marks")
	print(f"{sum(1 for char in str if char.isspace())} spaces")
	print(f"{sum(1 for char in str if char.isdigit())} digits")

def main():
	try:
		if len(sys.argv) < 2:
			try:
				str = input("What is the text to count?\n")
				str += '\n'
			except EOFError:
				pass
		elif len(sys.argv) > 2:
			raise AssertionError("more than one argument is provided")
		else:
			str = sys.argv[1]
		count(str)
	except AssertionError as e:
		print(f"{AssertionError.__name__}: {e}")

if __name__ == "__main__":
	main()