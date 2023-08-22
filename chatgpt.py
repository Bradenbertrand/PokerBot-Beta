import openai

openai.api_key = "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"

messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]

def get_chatgpt_response(text):
    message = text
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
      
    reply = chat.choices[0].message.content
    print(f"Best course of action: {reply}")
    messages.append({"role": "assistant", "content": reply})