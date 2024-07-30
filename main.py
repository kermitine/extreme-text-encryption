version = 0.1

text_input = input('\n' + ' Enter text!' + ' \n')



def encryption(text_input):
    vowels = ['a', 'e', 'i', 'o', 'u']
    broken_list = []
    consonants = []
    current_string = ''
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





encryption(text_input)