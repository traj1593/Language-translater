'''
Program: Language Translater
Filename: languageTranslater-tRaj-01.py
Author: Tushar Raj
Description: Translating from one language to another
Revisions: 00 - Because of case sensetive search of list word was not properly searched in the list, new word which is converted to lowercase as it solves search issue and meaning remains
                the same weather it is written in caps or small.
'''

#There is no import statement
english = ['chicken','salt','apple','earth','bean','water','milk']
french = ['poulet','sel','pomme','terre','haricot','eau','lait']
#There are no class defined

def inputdata(number): #checks the user input is correct
    '''
    This function accepts the input from the user and checks if the value contains any special character,digits.
    Input: user input from the console which is string type
    output: returns strings data type
    '''
    special = "!@#$%^&*()+?_=,<>/"
    while True:
        if(number.isdigit() == True): #checks if the value entered in number variable is having any character or not
            print("****Entered value can not be a digit****\n") #prints the error message
            progress = input("Please enter if you want to continue with Language Translater(y/n): ") #ask users if he wants to continue with program
            if( progress.lower() == 'y'):#checks the response of the user if its yes, asks to enter the diameter again
                number = input("\nEnter the last input again: ")
            if( progress.lower() == 'n'):#exits the program if response in no
                exit()
            continue
        elif (any( i in special for i in number)): #picks up each character from the number variable and then checks in special variable if it is present, if present run this elif
            print("****Input cant have special character. Please Enter the valid entry****\n")
            progress = input("Please enter if you want to continue with Language Translater(y/n): ")
            if( progress.lower() == 'y'):
                number = input("\nEnter the last input again: ")
            if( progress.lower() == 'n'):
                exit()
            continue
        else:
            return number

print("Language Translater") # printing the opening line
print("Program to translate words from English to French and vice versa") #Indicating what program is all about
while True: #Starting the while loop
    userInput=input("\nEnter a English or French word you are looking for: ") #accepting the input from user for the word which need to be converted
    userInput_check = inputdata(userInput) #calling the function to check valid input was provided or not
    userInput_lower = userInput_check.lower() #converting the checked data to lower format as to preserve user input format
    if(userInput_lower in english): #checking if it is english word or not
        print(f"The English word '{userInput_lower}' is '{french[english.index(userInput_lower)]}' in French")
    elif(userInput_lower in french): #checking if it is a french word or not
        print(f"The French word '{userInput_lower}' is '{english[french.index(userInput_lower)]}' in English")
    else: #if it is not in the list perform below statements
        if(userInput == ""): #exit when no value was entered by user
            print("Exiting...")
            quit()
        print(f"The word {userInput_check} was not found in English or French word list.")
        addWord = input(f"Would you like to add {userInput_lower} to the list? <y>es or <n>o: ")
        if(addWord.lower() == "y"): #checking if user want to add word in list if it present or not
            lang = input(f"what language the {userInput_check} in? <E>nglish or <F>rench: ")
            if(lang.lower() == "e"): 
                lang_french = input(f"what is the French word for '{userInput_check}'? ").lower()
                lang_french_check = inputdata(lang_french) #check data entered is appropriate
                english.append(userInput_lower) #add in english list
                french.append(lang_french) #add word in french list
                continue
            elif(lang.lower() == "f"):
                lang_english = input(f"what is the french word for '{userInput_check}'? ").lower()
                lang_english_check = inputdata(lang_english)
                french.append(userInput_lower) #add in french list
                english.append(lang_english_check) #add word in english list
                continue
            else:
                print("Please enter the valid input to add data to the list.\n")
            
