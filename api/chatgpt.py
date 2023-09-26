import os
import openai

from dotenv import load_dotenv


class ChatGPT:
    def clear_text(self, text):
        a = text.replace("\n", " ")
        b = a.split()
        c = " ".join(b)

        return c

    def get_answer(self, question):
        prompt = self.clear_text(question)

        load_dotenv()

        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            temperature=0.8,
            messages=[{"role": "user", "content": prompt}],
        )

        return response.choices[0].message.content
