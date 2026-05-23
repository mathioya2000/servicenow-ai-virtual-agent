import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_support_response(user_message, kb_articles):
    prompt = f"""
You are a ServiceNow AI Virtual Agent and Employee Support Assistant.

Employee message:
{user_message}

Relevant ServiceNow knowledge articles:
{kb_articles}

Give a helpful support response with:
1. Likely issue
2. Recommended troubleshooting steps
3. Related knowledge article summary
4. When to create an incident
5. Short professional employee-facing answer
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful enterprise IT support virtual agent."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content