def calculate_calories(age, weight, height, sex, activity):
    if sex == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    if sex == 'female':
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    if activity == 'sedentary':
        calories = bmr * 1.2
    if activity == 'lightly active':
        calories = bmr * 1.375
    if activity == 'moderately active':
        calories = bmr * 1.55
    if activity == 'very active':
        calories = bmr * 1.7
    if activity == 'extra active':
        calories = bmr * 1.9
    return calories
