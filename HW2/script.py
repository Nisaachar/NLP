import re

def LevenshteinD(word1, word2):
    m = len(word1)
    n = len(word2)

    table = [[0] * (n + 1) for _ in range(m + 1)] #defining the matrix as per the lenghts of the two strings

    for i in range(m + 1):      #initiating values from 0 to length of string to use for the levenshtein formula
        table[i][0] = i
    for j in range(n + 1):
        table[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
    return table[-1][-1]        #returning the diagonal final value or levenshtein distance.


def spell_check():

    #loading the file and creating a dictionary from it.
    file = open("dictionary.txt", 'r', encoding = 'windows-1252')
    dictionary = {}
    tolerance = 2 #defining a tolernace for the spell check.
    
    while True:
        content = file.readline()
        content = re.sub(r'\t\n', '', content) #removing tabs and newlines to form a dictionary. 
        content = content.lower() #lowercasing the text, in case if it wasn't.
        dictionary[content] = ""

        if not content: #braking the loop at the end of file
            break
    
    print("----------------------------------------\nWelcome to the spell checker! \nPlease enter a text to check spelling or enter quit to exit the program.\n-----------------------------------------")
    testStr = input("Enter the tet to be checked: ")
    testStr = testStr.lower() #again lowercasing the input from the user. I don't want Apple and apple to be two different words.
    testStr = re.sub(r'[^\w\s]', '', testStr) #removing all the punctuations from the user input/test string. (as mentioned by the rule of assignment)

    if testStr == 'quit':       #checking for the exit condition
        print('Goodbye!')
        exit()
    else:
        flag = 0
        noError = 0
        row = 0
        suggestions = [[0] * 50] * 20    #defining a matrix for holding the suggestions.
        totalWordsSuggested = 0
        for word in testStr.split():
            if word not in dictionary:
                noError = 1
                totalWordsSuggested = totalWordsSuggested + 1
                flag = 1
                count = 1
                for dic in dictionary:
                    suggestions[row][0] = word
                    wordTolerance = LevenshteinD(word, dic)
                    if wordTolerance <= tolerance:
                        suggestions[row][count] = dic
                        count = count + 1
                row = row + 1
        # print(suggestions)
        if noError == 1:
            print('Mispelling - Suggestion \n--------------------------------')
            for i in range(0, totalWordsSuggested):
                print(suggestions[i][0] + ' - ' + suggestions[i][1] + ' or ' + suggestions[i][2])

        if flag == 0:
            print("No misspellings detected!")    
            
spell_check()

