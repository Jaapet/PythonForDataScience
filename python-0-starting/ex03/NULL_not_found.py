import math
def NULL_not_found(object: any) -> int:
	if object is None:
		print(f"Nothing: {object} {type(object)}")
	elif object == 0 and type(object) is int:
		print(f"Zero: {object} {type(object)}")
	elif isinstance(object, float) and math.isnan(object):
		print(f"Cheese: {object} {type(object)}")
	elif object == '':
		print(f"Empty: {object} {type(object)}")
	elif type(object) is str and object == "":
		print(f"String: {object}")
	elif not object and type(object) is bool:
		print(f"Fake: {object} {type(object)}")
	else:
		print("Type not Found")
		return 1
	return 0