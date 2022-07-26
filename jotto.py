

# H(X) = H(p1,...pn)= -sum(pi*log2(pi))

import math

badL = []
word = "eagle"
a = open("candidates.txt", "r")
b = a.read()
c = b.replace("\n", "")
guess = []
for i in range(len(c)//5):
    guess += [c[5*i:5*i+5]]
print("Generated list of guesses called 'guess'")

def score(word, g):
    """Scores a Jotto guess
    word = string you are tryng to guess
    guess = string you are guessing"""

    score = 0
    for x in word:
        if x in g:
            score += 1
    return score

def makeDictionary(word, guesses):
    """word = string you are trying to guess
    guesses = list of string you want to guess
    creates dictionary
    keys = words (guesses)
    values = score"""

    d = {}
    for x in guesses:
        d[x] = score(word, x)
    
    return d

def bruteSolve(d):
    """takes dictionary as input
    keys = words (guesses)
    values = score
    returns list of letters NOT in word
    and list of letters IN word""" 

    badL = []

    for key in d.keys():
        if d[key] == 0:
            for letter in key:
                if letter not in badL:
                    badL += [letter]

    allLetters = "qwertyuiopasdfghjklzxcvbnm"
    goodL = [x for x in allLetters if x not in badL]
    return badL, goodL

def count(letter, word):
    """Returns number of times a letter appears in a word"""

    count = 0
    for x in word:
        if x == letter:
            count += 1
    return count

def step(pg):
    """Based on previous guess, suggests next best guess"""

    global badL
    global guess

    print()
    print(f"'{pg}' gets a score of {score(word,pg)}")

    s1 = score(word, pg)
    modG = []
    if s1 == 0:
        for y in guess:
            if score(pg, y) == 0:
                # print(f"'{pg}' and '{y}' have a score of {score(pg,y)} - REMOVING")
                modG += [y]
            # else:
                # print(f"'{pg}' and '{y}' have a score of {score(pg,y)}")

        ng = modG[0]
        print(f"Next guess recommendation is '{ng}' which has {score(pg, ng)} letters in common with '{pg}'")
        guess = modG
        print(f"There are {len(guess)} candidates left")
        return ng

    else:
        bestNG = ""
        for ng in guess:
            s2 = score(ng, pg)
            if s2 >= s1:
                modG += [ng]
            if s2 == 0:
                bestNG = ng

        if len(guess) > 1000:
            modG += [bestNG]
            ng = bestNG

        else:
            ng = modG[0]

        print(f"Next guess recommendation is '{ng}' which has {score(ng,pg)} letters in common with '{pg}'")
        guess = modG
        print(f"There are {len(guess)} candidates left")

        return ng
    
def wholeGame():
    """Runs whole game of jotto"""

    end = False
    print(f"The secret word is {word}")
    g0 = guess[42]

    steps = 0
    while end == False:

        ng = step(g0)
        steps += 1
        g0 = ng

        if ng == word:
            print(f"Found in {steps} steps")
            return steps

        if steps == 50:
            print("Probably did not find it")
            return steps

        guess.remove(ng)
        
    
# dict = makeDictionary(word, guess)
# print("Generated dictionary of scores called 'dict'")
# bad, good = bruteSolve(dict)
# print("Generated list of letters IN word called 'good'")
# print("Generated list of letters NOT in word called 'bad'")

# t1 = "knife"
# t2 = "maple"
# test = cross(word, t1, t2)
# print(f"The word is {word}")
# print(f"Crossing {t1} and {t2}")
# print(f"{t1} has a score of {score(word, t1)}")
# print(f"{t2} has a score of {score(word, t2)}")
# print(f"{t2} contribution: {test}")

    
    




    
