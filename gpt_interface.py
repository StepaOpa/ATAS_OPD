import requests
from config import YANDEX_CLOUD, YANDEX_GPT_API


def get_advice(goal, preferences, ban_products, allergy, number_of_calories):
    prompt = {
        "modelUri": f"gpt://{YANDEX_CLOUD}/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.5,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
                "text": "Ты опытный диетолог. Твоя цель - составлять персональные рационы питания учитывая все запросы пользователя."
            },
            {
                "role": "user",
                "text": f"Generate a varied meal plan for the week for {goal}."
                 f" Diet products should not include: {ban_products}. And maybe should include {preferences} (not neccessary)."
                 f"If this sentence has a semicolon followed by 'У меня нет аллергий' ignore that sentence: {allergy}. "
                 "If the proposal lists specific types of allergies, assume that the final nutrition plan should exclude foods "
                 f"that cause these allergies. The number of calories per day should be about {number_of_calories}. "
                 "Write down the number of calories for each meal, as well as the total amount for the day."
            }
        ]
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {YANDEX_GPT_API}",
    }

    response = requests.post(url, headers=headers, json=prompt)

    response_json = response.json()

    text = response_json['result']['alternatives'][0]['message']['text']

    return text