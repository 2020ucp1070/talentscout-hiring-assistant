import os
import time
import openai
from openai import OpenAI
from openai._exceptions import RateLimitError, APIConnectionError, APIError, OpenAIError

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,
        )
        return response.choices[0].message.content.strip()

    except RateLimitError:
        print("⚠️ Rate limit exceeded. Retrying in 60 seconds...")
        time.sleep(60)
        return ask_llm(prompt)

    except APIConnectionError as e:
        print(f"❌ API connection error: {e}. Retrying in 30 seconds...")
        time.sleep(30)
        return ask_llm(prompt)

    except APIError as e:
        print(f"🚨 API error: {e}. Retrying in 20 seconds...")
        time.sleep(20)
        return ask_llm(prompt)

    except OpenAIError as e:
        print(f"❗ OpenAI error: {e}")
        return "An error occurred while generating the response."

    except Exception as e:
        print(f"💥 Unexpected error: {e}")
        return "Something went wrong. Please try again later."
