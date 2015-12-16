import names
Bnames = ""
Cnames = ""
def Bfunc():
    global Bnames
    Bnames = ""
    while Bnames == "":
        name = names.get_first_name()
        if name[0] == "B":
            Bnames = name

def Cfunc():
    global Cnames
    Cnames = ""
    while Cnames == "":
        name = names.get_first_name()
        if name[0] == "C":
            Cnames = name

def NameBasedOneActor():
    Bfunc()
    Cfunc()
    print Bnames, Cnames

import random
import string

vowels = list('aeiou')

def gen_first(min, max):
    word = ''
    syllables = min + int(random.random() * (max - min))
    word += first_name_syllable()
    for i in range(0, syllables):
    	word += gen_syllable()
    return word.capitalize()

def gen_second(min, max):
    word = ''
    syllables = min + int(random.random() * (max - min))
    word += second_name_syllable()
    for i in range(0, syllables):
    	word += gen_syllable()
    return word.capitalize()

def first_name_syllable():
    return 'B' + word_part('v')

def second_name_syllable():
    return 'C' + word_part('v')

def gen_syllable():
	ran = random.random()
	if ran < 0.333:
		return word_part('v') + word_part('c')
	if ran < 0.666:
		return word_part('c') + word_part('v')
	return word_part('c') + word_part('v') + word_part('c')


def word_part(type):
	if type is 'c':
		return random.sample([ch for ch in list(string.lowercase) if ch not in vowels], 1)[0]
	if type is 'v':
		return random.sample(vowels, 1)[0]



def ThatOneActor():
    print gen_first(2,4), gen_second(2,4)
