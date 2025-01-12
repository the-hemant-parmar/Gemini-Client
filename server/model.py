import google.generativeai as genai

# import os

with open("KEY.txt") as f:
    API_KEY = f.read()
    # print(API_KEY)

# genai.configure(api_key=os.environ["API_KEY"])
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-pro")


def query(QUESTION):
    response = model.generate_content(QUESTION)
    return response.text


# print(response.text)
