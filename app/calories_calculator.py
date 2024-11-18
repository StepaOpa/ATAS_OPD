def calculate_calories(age, weight, height, sex, activity):
    if sex in ['male','мужской','m','м']:
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    if sex == ['female','женский','f','ж']:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    if activity in ['sedentary','сидячий']:
        calories = bmr * 1.2
    if activity in ['lightly active', 'немного активный']:
        calories = bmr * 1.375
    if activity in ['moderately active','умеренно активный']:
        calories = bmr * 1.55
    if activity in ['very active','очень активный']:
        calories = bmr * 1.7
    if activity == ['extra active','гиперактивный']:
        calories = bmr * 1.9
    return round(calories)
