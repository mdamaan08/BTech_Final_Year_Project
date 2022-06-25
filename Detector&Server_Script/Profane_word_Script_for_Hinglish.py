from difflib import SequenceMatcher
from jellyfish import soundex
from nltk.corpus import stopwords


from nltk.tokenize import word_tokenize
f = open('Hinglish_Profanity_List.csv', "r")

dic=[]
sen=[]
abusive_sent={}
profaneSubstitutes = {
    '1': 'i',
    '$': 's',
    '@': 'a',
    '3': 'e',
    '0': 'o',
    '5': 's',
    '#':'h'
}
Words1 = [
    'cuntfucker', 'assfucker', 'nigga', 'fuckface', 'ballsack', 'cuntlick',
    'negro', 'dickweed', 'camslut', 'dyke', 'biatch', 'pussy', 'boner',
    'Goddamn', 'clitoris', 'flange', 'muff', 'dickless', 'twat', 'knobend',
    'negroes', 'coon', 'labia', 'feck', 'balllicker', 'smegma', 'gangbang',
    'dicksucker', 'slutty', 'pussylover', 'butt', 'bugger', 'boob', 'bastard',
    'whore', 'anus', 'horseshit', 'bitch', 'fellate', 'fuck', 'bum',
    'mothafucka', 'bollock', 'asspacker', 'sex', 'bloody', 'prick', 'blowjob',
    'piss', 'fudgepacker', 'meatbeater', 'vagina', 'dick', 'buttplug',
    'dammit', 'shit', 'crap', 'clit', 'felching', 'fuckbag', 'dildo', 'wank',
    'fucking', 'wanker', 'cocklover', 'ass', 'homo', 'damn', 'turd',
    'fellatio', 'asshat', 'fucker', 'cocksucker', 'bullcrap', 'jerk', 'tosser',
    'cunt', 'nigger', 'shag', 'titjob', 'slut', 'cumslut', 'motherfucking',
    'shithead', 'cockblock', 'scrotum', 'bollok', 'spunk', 'orgy', 'jizz',
    'hell', 'anal', 'poop', 'arse', 'cock', 'balls', 'asswhore', 'fag',
    'bullshit',"mad"
]



profaneSubstitutes_keys=profaneSubstitutes.keys()
for x in f:
    f1=x.split(",")
    for l in f1[:-1]:
        dic.append(l)

f.close()
f= open('Hindi.csv', "r")
for x in f:
    dic.append(x[:-1])
words=dic+Words1
dic={}
for j in words:
    dic[j]=soundex(j)
#print(dic)


def free_from_substitutes(inp_word):
    new_inp_word=""
    for letter in inp_word:
        if(letter in profaneSubstitutes_keys):
            new_inp_word+=profaneSubstitutes[letter]
        else:
            new_inp_word+=letter
    #print(new_inp_word,inp_word)
    global Binary_Profanity_Detector
    if(similar2(new_inp_word)):
        Binary_Profanity_Detector.append("1")
    if(new_inp_word==inp_word):
        return False
    else:
        return True


def similar_sound(word):
    #print(word)
    global sen
    global abusive_sent
    #print(sen)
    print(word,soundex(word))

    if(soundex(word) in sen):
        match=similar(word,abusive_sent[soundex(word)])
        if("1" in match):
            return True
        else:
            return False
    else:
        return False

def similar(a,many):
    threshold=0.7
    matcher=[]
    match=[]
    #print(many)
    for b in many:
        dop=SequenceMatcher(None,a, b).ratio()
        matcher.append(dop)
        if(dop>=threshold):
            match.append("1")

    #print(matcher)
    return match

def similar2(a):
    global words
    threshold=0.7
    match=[]
    for word in words:
        dop=SequenceMatcher(None,a,word).ratio()
        #print(dop)

        if(dop>=threshold):
            match.append("1")
            return True


for word in words:
    sound=soundex(word)
    sen.append(sound)
    if(sound in abusive_sent.keys()):
        abusive_sent[sound].append(word)
    else:
        abusive_sent[sound]=[]
        abusive_sent[sound].append(word)



text=input()
text_tokens = word_tokenize(text)
input_sentence = [word for word in text_tokens if not word in stopwords.words()]
print(input_sentence)






Binary_Profanity_Detector=[]
for word in input_sentence:
    if(similar_sound(word)):

        #print("1")
        Binary_Profanity_Detector.append("1")
    elif(free_from_substitutes(word)):
        pass
    elif(similar2(word)):
        Binary_Profanity_Detector.append("1")
    else:
        Binary_Profanity_Detector.append("0")
print(Binary_Profanity_Detector)
