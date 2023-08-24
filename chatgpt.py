import openai
from tools import convert_card_codes

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




def create_question(table, heroIndex, hand):
    hand_pretty = ", ".join(convert_card_codes(hand))
    question = f"It is the {table.round}\nI am in position {table.players[heroIndex].position}\nMy hand is {hand_pretty}\nThe pot is ${table.pot}.\nIt is ${table.call_amount} to call\n"
    for player in table.players:
        if player.name == "Hero":  
            question += str(player) + "\n"
            break
        else:
            question += str(player) + "\n"
    question += "What should hero do in this case? Please give a reccomendation even if you're not confident. Please answer in the format of 'Call', 'Fold', or 'Raise to x'"
    get_chatgpt_response(question)