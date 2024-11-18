import requests
from config import YANDEX_CLOUD, YANDEX_GPT_API


def get_advice(goal, ban_products, number_of_calories):
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
                "text": "Ты опытный диетолог. Твоя цель - составлять персональные рационы питания учитывая все запросы пользователя"
            },
            {
                "role": "user",
                "text": f"generate a varied meal plan for the week for {goal}. Diet products should not include: {ban_products}. The number of calories per day should be about {number_of_calories}. The number of calories for each day should be calculated)"
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

    # Извлечение текста из ответа
    text = response_json['result']['alternatives'][0]['message']['text']

    return text
