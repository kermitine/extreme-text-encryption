import time

version = str('4.0.1')

print('''                                                                                                       
                                                    ###%%%#*                                           
                                                  #%%%%%%%%%%*                                         
                                               +%%%%%%%%%%%%%%%#=                                      
                                            =#%%%%%%%%%%%%%%%%%%%%*                                    
                                          *%%%%%%%%%%%%%%%%%%%%%%@%%*                                  
                                      =*#%%%%%%%%%%%%%%%%%%%%%@@%%@@%#                                 
                                    *%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@%                                
      -----                       #%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@+                              
    -=++*#+=-                  +#@@@@@@@@@@@@@@@@@@%%%%%@@@@@@@@@@@@@@@@@*                             
    -+#+:=#*=-               *%@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%@%%@@@@@@@@@@*                            
    -=*#=:-##+-            *@@@@@@@@@%%%%%%%%%%%@@@@@@@@@@%%%%%@@@@@@@@@@@@#                           
      =*#=:-*#+-          @@@@@@@@%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@%                          
       =*#+::*#+-        #@@@@@@@%%%#####%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@%*                        
        =*#+::*#+-      *@@@@@@@%%#########%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@%+                       
         -+#+::+#*=     %@@@@@@%%##*****#####%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@+                      
          -+#*::+#*=   #@@@@@@@%#******#####%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@%                      
           -+#*-:=#*= +%@@@@@@@%#*****######%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@+                      
            -+#*-:=#*=#@@@@@@@@@##**######%%%%%%%%%@@@@%%%%%%@@@@@@@@@@@@@@@@@@@+                      
             -=##-:-###%@@@@@@@%#@@@%%%%@@@@@@%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@*                     
              -=*#=:-###%@@@@@@%#**####%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@%-                    
               -=*#=:-###%@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@#                    
                -=*#+::*##%@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@*                   
                  =##+::*##%@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@%-                  
                   ###*::+###@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@%                  
                  +@%##*::+###@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@*                 
                  =@@%##*-:=###@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@%+                
                  *@@@%###-:=###%@@@@@@@@%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@#                
                  %@@@@%###-:-###%@@@@@@@@%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@%                
                  %@@@@@%###=:-###%@@@@@@@@@@@@%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#               
                  @@@@@@@%###=:-###%@@@@@@@@@@@@%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-              
                  %@@@@@@@@###+::*##%@@@@@@@@@@%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#              
                  %@@@@@@@@@###+::*##%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*             
                  *@@@@@@@@@@%##*::+###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=            
                  +@@@@@@@@@@@%##*::+###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*             
                  =@@@@@@@@@@@@%###-:=###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%              
                   #@@@@@@@@@@@@%###-.=###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*             
                   #@@@@@@@@@@@@@%###=-+*#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#             
                    ##@@@@@@@@@@@@@##*%#**@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#            
                        +@@@@@@@@@@@%%#%*##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#            
                       *@@@@@@@@@@@@@@@%%@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#           
                                                                                                       
                                                                                                       
                                                                                                       ''')


print(''' __                             .__   __   .__                 
|  | __  ____  _______   _____  |__|_/  |_ |__|  ____    ____  
|  |/ /_/ __ \ \_  __ \ /     \ |  |\   __\|  | /    \ _/ __ \ 
|    < \  ___/  |  | \/|  Y Y  \|  | |  |  |  ||   |  \\  ___/ 
|__|_ \ \___  > |__|   |__|_|  /|__| |__|  |__||___|  / \___  >
     \/     \/               \/                     \/      \/ ''')

vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
punctuation = ['!', '?', '.', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '#', '/', ':', ';',
                    '<', '=', '>', '"', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
full_stop_punc = punctuation[:3]
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

print('Encryptor V' + version)

text_input = input(str('\n' + 'Enter text for encryption:' + ' \n'))


def encryption(text_input):
    broken_list = []
    consonants = []
    popList = []
    final_word = ''
    editPunc = ''
    current_string = ''
    final_word = ''
    for x in text_input: # break up word into list
        broken_list.append(x)




    for x in broken_list: # extract consonants
        if x in nums: # detects numbers and leaves them unchanged
            final_word = "".join(broken_list)
            return final_word # immediately return number
        if x not in vowels: # add all sequential consonants to a list
            consonants.append(x)
        if x in vowels: # stop once first vowel is reached
            break

    if consonants:
        cut_list = broken_list[len(consonants):] # cuts broken_list so the vowels at the start are deleted
        for x in range(len(consonants)): # moves consonants to the back
            current_string = consonants[x]
            cut_list.append(current_string)
        cut_list.append('ay')
        for x in range(len(cut_list)): # moves punctuation to the back of word, but keeps og punc to maintain indexes
            if cut_list[x] in punctuation:
                editPunc = cut_list[x]
                cut_list.append(editPunc)
                popList.append(x)   # adds index of og punctuation to popList, to be removed outside of loop
        for y in popList:
            cut_list.pop(y) # pops og indexes outside of loop
        cut_list = [item.lower() for item in cut_list]
        final_word = "".join(cut_list) # joins list into string and returns
    if not consonants:
        broken_list.append('yay')
        for x in range(len(broken_list)): # moves punctuation to the back of word, but keeps og punc to maintain indexes
            if broken_list[x] in punctuation:
                editPunc = broken_list[x]
                broken_list.append(editPunc)
                popList.append(x)   # adds index of og punctuation to popList, to be removed outside of loop
        for y in popList:
            broken_list.pop(y) # pops og indexes outside of loop
        broken_list = [item.lower() for item in broken_list]
        final_word = "".join(broken_list)
    return final_word

def wholesentence(sentence):
    final_sentence = []
    words = sentence.split()
    for x in range(len(words)):
        final_sentence.append(encryption(words[x]))
    final_sentence[0] = final_sentence[0].capitalize() # capitalizes first letter of first word

    for x in range(1, len(final_sentence)-1): # corrects capitalization
        for letter in final_sentence[x]:
            if letter in full_stop_punc:
                final_sentence[x+1] = final_sentence[x+1].capitalize()


    joined_sentence = " ".join(final_sentence)
    return joined_sentence


def loopStart(text_input):
    print('\n' + '\n' + '\n' + '\n' + 'Encrypted Result:' + '\n' + wholesentence(text_input) + '\n' + '\n')
    exitCode = input(str('\n' + 'Enter t to translate another sentence. Enter any other key to exit.' + '\n'))
    return exitCode






exitCode1 = str(loopStart(text_input))


while True:
    if exitCode1 in ['t', 'T']:
        text_input = input(str('\n' + 'Enter text for encryption:' + ' \n'))
        exitCode1 = loopStart(text_input)
    elif exitCode1 is None:
        print('Program Terminating...')
        time.sleep(1.5)
        break
    else:
        print('Program Terminating...')
        time.sleep(1.5)
        break








