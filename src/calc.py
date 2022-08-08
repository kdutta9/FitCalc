def bmi(height, weight):
	height_m = height / 39.37
	weight_kg = weight / 2.205
	return round((weight_kg / (height_m ** 2)), 2)

def bmi_status(val):
	if val < 18.5:
		return "Your BMI category is underweight."
	elif val < 25:
		return "Your BMI category is healthy weight."
	elif val < 30:
		return "Your BMI category is overweight."
	else:
		return "Your BMI category is obese."
