import requests
from config import YANDEX_CLOUD, YANDEX_GPT_API


def get_advice(goal, preferences, ban_products, allergy, number_of_calories, timeline):
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
                "text": "You're an experienced nutritionist. Your goal is to create personal food rations based on all user requests. Russian is the only language that the user understands, so translate everything into Russian."
            },
            {
                "role": "user",
                "text": f"Make a comprehensive nutrition plan consistent with the principles of {goal}. "
                        f"The plan should be designed for a {timeline} days, each day should include breakfast, lunch, dinner and "
                        "two snacks. Each meal should be balanced, nutritious and comply with dietary recommendations "
                        f"{goal}. (Breakfast, lunch, dinner and two snacks should be about {number_of_calories} calories.) "
                        "Specify the number of grams of each product in the dish."
                        f"You can use these products: {preferences}, and others. But don't use these products: {ban_products}."
                        f"Also pay attention to the presence of my allergies: {allergy}."
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