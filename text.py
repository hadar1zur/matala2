# -*- coding: utf-8 -*-

def revword(word:str) -> str:
    j=len(word)-1
    word_correctly=''
    for i in range(0,len(word)):
        word_correctly=word_correctly+word[j]
        j=j-1
    return word_correctly


def countword()->int:
    num=1
    i=0
    sentence=''
    fhand = open('text.txt')
    word_1= fhand.readline()
    word_1=word_1.strip()
    for line in fhand:
        sentence=line+' '
        while (i<len(sentence)):
            word_2=revword(sentence[i:sentence.find(' ')])
            word_2=word_2.strip()
            if word_2.lower()==word_1.lower():
                num=num+1
            j=len(word_2)+1
            sentence=sentence[j:len(sentence)]  
    return num
     
    


