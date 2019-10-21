#List of expressors.
expressors = ["+", "-", "*", "/", "^", "(", ")"]

#Function that tokenizes the mathematical string.
def tokenize(exp_ressors):
    tokens = []
    number = ""
    in_number = False
    for character in exp_ressors:
        if character in expressors:
            if in_number:
                in_number = False
                tokens.append(number)
                number = ""
            tokens.append(character)
        elif character.isdecimal():
            in_number = True
            number += character 
    return tokens

def main():
    word = input("Please, enter a sentence containing some mathematical expressions to tokenize it: ")
    word = tokenize(word)
    return print("Finally, the tokens of your mathematical sentence are: ", word)
main()

#FIRST IF = Appends all expressors that stand alone.
#SECOND IF = Appends all the decimal characters into the number which previously is appended to tokens.
