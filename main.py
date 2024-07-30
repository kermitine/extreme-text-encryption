version = 0.3

text_input = input('\n' + ' Enter text!' + ' \n')



def encryption(text_input):
    vowels = ['a', 'e', 'i', 'o', 'u']
    broken_list = []
    consonants = []
    current_string = ''
    final_word = ''
    for x in text_input: # break up word into list
        broken_list.append(x)




    for x in broken_list: # extract consonants
        if x not in vowels:
            consonants.append(x)
        if x in vowels:
            break

    if consonants:
        cut_list = broken_list[len(consonants):]
        for x in range(len(consonants)):
            current_string = consonants[x]
            cut_list.append(current_string)
        cut_list.append('a')
        cut_list.append('y')
        final_word = "".join(cut_list)
    if not consonants:
        broken_list.append('y')
        broken_list.append('a')
        broken_list.append('y')
        final_word = "".join(broken_list)
    return final_word

def wholesentence(sentence):
    final_sentence = []
    words = sentence.split()
    for x in range(len(words)):
        final_sentence.append(encryption(words[x]))
    joined_sentence = " ".join(final_sentence)
    return joined_sentence


print(wholesentence(text_input))

exitCode = input('\n' + 'Press any key + enter to exit' + '\n')
exit(exitCode)

def exit(exitCode):
    if exitCode:
        return None