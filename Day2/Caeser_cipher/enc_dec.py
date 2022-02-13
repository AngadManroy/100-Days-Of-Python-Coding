alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caeser(message_, mode_):
    step = int(input("Pick the shift value"))
    evaluated_message=''
    for letter in message_:
        if letter in alphabet:
            pos = alphabet.index(letter)
            evaluated_message += alphabet[ (pos + step)%26 if (mode_.lower() == 'encode') else (pos-step)%26 ]
        else:
            evaluated_message += letter
    return evaluated_message