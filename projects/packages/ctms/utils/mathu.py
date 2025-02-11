def gte(value: int | float, min: int | float) -> int | float:
	""" 
	Ensures that a numeric value is greater than or equal to a minimum value

	Parameters
	----------
	value
		The numeric value to bound
	min
		The minimum allowable numeric value

	Returns
	-------
	If the value is >= min, value is returned, otherwise min is returned
	"""
	return value if value >= min else min