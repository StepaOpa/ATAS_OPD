def calculate_calories(age, weight, height, sex, activity):
    calories = 0
    bmr = 0
    
    if sex == 'Мужской':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    if sex == 'Женский':
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    if activity == 'Не занимаюсь':
        calories = bmr * 1.2
    if activity == '1 раз в неделю':
        calories = bmr * 1.375
    if activity == '3 раза в неделю':
        calories = bmr * 1.55
    if activity == '5 раз в неделю':
        calories = bmr * 1.7
    if activity == 'Каждый день':
        calories = bmr * 1.9

    return round(calories)