# def spell_check():
    
#     return None

# def lev_dist(str1, str2):
#     arr = [[999999]*(len(str1) + 2)]*(len(str2) + 2) #intialising array with abusrd high value. The value 99999 won't create an issue while finding a minimum value
    
#     for i in range(0, len(str1)+1):
#         arr[i][0] = i
    
#     for j in range(0, len(str2)+1):
#         arr[0][j]= j
    
#     print(arr)

# lev_dist('cat', 'fat')

def LevenshteinD(word1, word2):
    """Dynamic programming solution"""
    m = len(word1)
    n = len(word2)
    table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        table[i][0] = i
    for j in range(n + 1):
        table[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
                
    return table[-1][-1]

print(LevenshteinD("computer","computers"))

