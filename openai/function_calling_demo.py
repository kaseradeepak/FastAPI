# Function Calling Example - get_weather(city)
from openai import OpenAI
import json

client = OpenAI()

def get_weather(city: str):
    fake_weather_data = {
        "bangalore" : {"temperature" : 25, "condition" : "Cloudy"},
        "hyderabad" : {"temperature" : 35, "condition" : "Sunny"},
        "delhi" : {"temperature" : 40, "condition" : "polluted"},
        "mumbai" : {"temperature" : 23, "condition" : "rainy"},
    }

    # strip function removes any unnecessary (leading or trailing) spaces.
    city = city.strip().lower()
    if city not in fake_weather_data:
        return {"temperature" : "unknown", "condition" : "unknown"}

    return fake_weather_data.get(city)

tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get the current weather for a given city.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "Name of the city to get weather for"
                }
            },
            "required": ["city"]
        }
    }
]

response = client.responses.create(
    model = "gpt-5.4",
    input = "What is the weather of Bangalore ?",
    tools = tools
)

print(response)

# for item in response.output:
#     if item.type == "function_call":
#         print("Tool name: ", item.name)
#         print("Arguments: ", item.arguments)

#         args = json.loads(item.arguments)

#         print(args)