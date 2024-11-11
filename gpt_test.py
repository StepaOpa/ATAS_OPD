import requests

# b1gignv1fqqv4i0feomd

# AQVNwk7s-5kcJcHpzAIJX5kGCGhuDcTQ8886PSmb


def get_answer(target, ban_products, number_of_calories):
    prompt = {
        "modelUri": "gpt://b1gignv1fqqv4i0feomd/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.5,
            "maxTokens": "1000"
        },
        "messages": [
            {
                "role": "system",
                "text": "Ты опытный диетолог. Твоя цель - составлять персональные рационы питания учитывая все запросы пользователя"
            },
            {
                "role": "user",
                "text": f"generate a varied meal plan for the week for {target}. Diet products should not include: {ban_products}. The number of calories per day should be about {number_of_calories}. The number of calories for each day should be calculated)"
            }
        ]
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVNwk7s-5kcJcHpzAIJX5kGCGhuDcTQ8886PSmb",
    }

    response = requests.post(url, headers=headers, json=prompt)

    response_json = response.json()

    # Извлечение текста из ответа
    text = response_json['result']['alternatives'][0]['message']['text']

    return text


if __name__ == '__main__':
    target = input(
        "Введите цель (похудение / набор массы / поддержание здорового питания): ")
    ban_products = input("Введите запрещенные продукты (через запятую): ")
    number_of_calories = input("Введите количество калорий в день: ")

    print(get_answer(target, ban_products, number_of_calories))
