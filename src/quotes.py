import random

game_quote = "default_quote"
game_person = "stupid nobody"

def give_quote_call(all_quotes):
    global game_quote, game_person
    position = random.randint(0, 3)
    curr_channel = all_quotes[position]
    quote = curr_channel[random.randint(0, len(curr_channel) - 1)]
    print(quote)
    game_quote = quote
    game_person = curr_channel[0]
    return quote

def check_answer_call():
    global game_quote, game_person
    print(game_person)
    return game_person