import os
import random



def read_data(filepath="./Data.txt"):
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
    return words

    
def run():

    data = read_data(filepath="./Data.txt")
    # print(data)
    chosen_word = random.choice(data)
    # print(chosen_word)
    chosen_word_list = [letter for letter in chosen_word]
    # print(chosen_word_list)
    chosen_word_list_underscores = ["_"] * len(chosen_word_list)
    # print(chosen_word_list_underscores)
    letter_index_dict = {}
    # print(letter_index_dict)
    for idx, letter in enumerate(chosen_word):
        if not letter_index_dict.get(letter): 
            letter_index_dict[letter] = []
            # print(letter_index_dict)
        letter_index_dict[letter].append(idx)
        # print(letter_index_dict)
    

    while True:
        os.system('clear')
        print('HANGMAN\n')

        for element in chosen_word_list_underscores:
            print(element + " ", end="")
        print("\n")

        letter = input('\nWrite a letter: ').strip().upper()
        assert letter.isalpha(), "Only letters"

        print(letter_index_dict)
        if letter in chosen_word_list:
            for idx in letter_index_dict[letter]:
                chosen_word_list_underscores[idx] = letter

        if "_" not in chosen_word_list_underscores:
            os.system("clear") # Si estás en Unix (Mac o Linux) cambia cls por clear
            print("¡Good job, the word was", chosen_word)
            break



if __name__ == '__main__':
    run()