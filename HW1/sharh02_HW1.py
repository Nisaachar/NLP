import re

def process_regex (inputFile):
    print("Processing file...")

    text = open(inputFile, 'r', encoding = 'utf-8')
    regexFile = open("regex.txt", 'a') #creating a new file / appending existing one

    while True:
        next_line = text.readline()

        if not next_line:
            break
        
        #creating lists for salutation removal.
        eng_brit = ['Mr\.', 'Mrs\.', 'Ms\.', 'Dr\.']
        eng_amer = ['Mister', 'Misses', 'Miss', 'Doctor']

        for i in range(4):
            next_line= re.sub(r'' + eng_brit[i], '' + eng_amer[i], next_line) #using + oprator for combining list/variables in regex
           
        regexFile.write(next_line) #writing the end result to file regex.txt

    text.close()    #closing all the files safely
    regexFile.close()
    print("Output stored to \"regex.txt\"")

def normalize_text(toNormalize):
    regexFile = open(toNormalize, 'r', encoding = 'windows-1252')
    dictFile = open("dictionary.txt", 'a') 

    #normalization starts
    next_line = regexFile.read()
    noNumber = re.sub(r'\d+', '',next_line) #Removing all the numbers from the text to normalize it.
    noUnder = re.sub(r'_', '', noNumber) #Removing underscores. There were many instances of words with '_' in the text.
    strLower = noUnder.lower() #lower casing the text
    strPunch = re.sub(r'[^\w\s]', '', strLower)  #removing all the puntuations like commas, fullstops, brackets, etc. Anything ie, other than a word or space.
    strWhite = " ".join(strPunch.split()) #removing all the white spaces, newlines, or tabs. 
    
    #Forming dictionary to get unique tokens
    unique = {}
    for word in strWhite.split():
        if word not in unique:
            unique[word] = ""

    #sorting alphabetically
    keyList = list(unique.keys())
    keyList.sort()
    sortDict = {i: unique[i] for i in keyList} #referred to geeks for geeks. https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/

    #writing dictionary to text file called as "dictionary.txt"
    for key,value in sortDict.items():
        dictFile.write(key + "\t" + value + "\n")

    regexFile.close() #closing all the files safely
    dictFile.close()


#functions call.
inputFile = input("Enter the path of the file to be processed: ")
process_regex(inputFile)


toNormalize = input("Enter the path of the file to be Normalized: ")
normalize_text(toNormalize)
