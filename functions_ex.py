## WARMUP SECTION ##
####################

def lesser_of_two_evens(a, b):
    if a%2!=0 or b%2!=0:
        if a > b:
            return a
        else:
            return b
    else:
        if a < b:
            return a
        else:
            return b

#print(lesser_of_two_evens(2,4))
#print(lesser_of_two_evens(2,5))

def animal_crackers(text):
    words = text.split()
    return words[0][0] == words[1][0]


#print(animal_crackers('Levelheaded Llama'))
#print(animal_crackers('Crazy Kangaroo'))

def makes_twenty(a, b):
    if a == 20 or b == 20:
        return True
    elif a+b == 20:
        return True
    else:
        return False

#print(makes_twenty(20, 10))
#print(makes_twenty(12, 8))
#print(makes_twenty(2, 3))

##### SECTION 1 #####
#####################

def old_macdonald(name):
    return name[0].upper() + name[1:3] + name[3].upper() + name[4::]

#print(old_macdonald('macdonald'))
#print(old_macdonald('lucsobral'))

def master_yoda(text):
    words = text.split()
    i = -1
    answer = ''
    for _ in words:
        answer += words[i]
        answer += ' '
        i -= 1
    return answer

def master_yoda_v2(text):
    words = text.split()
    words.reverse()
    return " ".join(words)

#print(master_yoda_v2('I am home'))
#print(master_yoda_v2('We are ready'))

def almost_there(n):
    n -= 100
    if abs(n) <= 10:
        return True
    n -= 100
    if abs(n) <= 10:
        return True
    return False

#print(almost_there(90))
#print(almost_there(104))
#print(almost_there(150))
#print(almost_there(209))


##### SECTION 2 #####
#####################

def has_33(numlist):
    j = 0
    for i in numlist:
        if j == i == 3:
            return True
        j = i
    return False

#print(has_33([3, 1, 2, 4, 3, 3]))
#print(has_33([1, 3, 3]))
#print(has_33([1, 3, 1, 3]))
#print(has_33([3, 1, 3]))

def paper_doll(s):
    result = ''
    for letter in s:
        result += letter*3
    return result

#print(paper_doll('Hello'))
#print(paper_doll('Mississipi'))

def blackjack(a, b, c):
    elevCount = 0
    for num in (a, b, c):
        if num == 11:
            elevCount+=1

    total = a+b+c
    while total>21 and elevCount>0:
        total -= 10
        elevCount -= 1
    if total > 21: return 'BUST'
    else: return total

#print(blackjack(5, 6, 7))
#print(blackjack(9, 9, 9))
#print(blackjack(9, 9, 11))

def summer_69(arr):
    flag = True
    total = 0
    for num in arr:
        if flag and num == 6:
            flag = False
            continue
        elif not flag and num == 9:
            flag = True
            continue

        if flag:
            total += num
    return total

#print(summer_69([1, 3, 5]))
#print(summer_69([4, 5, 6, 7, 8, 9]))
#print(summer_69([2, 1, 6, 9, 11]))

def unique_list(mylist):
    myset = set(mylist)
    return list(myset)

#print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

import string

def isPangram(text, alphabet=string.ascii_lowercase):
    textLetters = set(text)
    for letter in alphabet:
        if not letter in textLetters:
            return False
    return True

#print(isPangram('The quick brown fox jumps over the lazy dog'))
#print(isPangram('abcdefg hijklmnopqrstuv wxyz'))
#print(isPangram('abcdefg hijklmnopqrstuv wxy'))