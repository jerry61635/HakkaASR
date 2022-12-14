import random
from telnetlib import SE
from function import *
import shutil

Sentence = []
Lexicon = []

noUse=['north-lbk13_001','north-lbk06_053','north-lbk01_079','north-lbk03_132','north-lbk04_059','north-lbk10_138']

#開啟檔案 7541為全部檔案數量
f = open('nameAndText.txt', 'r', encoding='utf-8')
for i in range(7541):
# for i in range(10):
    str=f.readline().split('\n')[0]
    chk=True
    for w in noUse:
        if w==str.split(' ')[0]:
            chk=False
    if chk:
        Sentence.append(str)
f.close

for line in Sentence:
    for word in line.split(' ')[1:]:
        wordChk=True
        for L in Lexicon:
            if word == L:
                wordChk=False
                break
        if wordChk:
            if len(word)>0:
                Lexicon.append(word)

'''
L=0
for line in Sentence:
    print(Sentence[L])
    L+=1
'''

# export corpus.txt
print('export corpus.txt')
export = open('output/corpus.txt', 'w', newline='', encoding='utf-8-sig')
for line in Sentence:
    output=''
    for word in line.split(' ')[1:]:
        output = output+' '+word
    export.write(output[1:]+'\n')
export.close()
shutil.copyfile('./output/corpus.txt','../../../data/local/corpus.txt')

# export text.no_oov (for lm)
print('export text.no_oov')
export = open('output/text.no_oov', 'w', newline='', encoding='utf-8-sig')
for line in Sentence:
    output='<SPOKEN_NOISE>'
    for word in line.split(' ')[1:]:
        output = output+' '+word
    export.write(output[1:]+'\n')
export.close()
shutil.copyfile('./output/text.no_oov','../../../data/local/lm/text.no_oov')

# export train/test_text
p=0.4 #比例
L=0 #Index
print('export text_test and text_train')
export = open('output/text_train', 'w', newline='', encoding='utf-8-sig')
export2 = open('output/text_test', 'w', newline='', encoding='utf-8-sig')
for line in Sentence:
    if random.random()>=p:
        export.write(line+'\n')
        for i in range (4,15):
            if Sentence[L][i] == ' ':
                shutil.copyfile('../HakkaAudioFile/'+Sentence[L][0:i]+'.wav','../../train/'+Sentence[L][0:i]+'.wav')
                break
    else:
        export2.write(line+'\n')
        for i in range (4,15):
            if Sentence[L][i] == ' ':
                shutil.copyfile('../HakkaAudioFile/'+Sentence[L][0:i]+'.wav','../../test/'+Sentence[L][0:i]+'.wav')
                break
    L+=1
export.close()
export2.close()
shutil.copyfile('./output/text_train','../../../data/train/text')
shutil.copyfile('./output/text_test','../../../data/test/text')

# export lexicon.txt
print('export Lexicon')
export = open('output/lexicon.txt', 'w', newline='', encoding='utf-8-sig')
for L in Lexicon:
    output = L
    for syl in to_tone(L):
        output=output+' '+syl
    export.write(output+'\n')
export.close()
shutil.copyfile('./output/lexicon.txt','../../Language/lexicon.txt')

# export nonsilence_phones.txt
print('nonsilence_phones.txt')
tone=[]
for L in Lexicon:
    for syl in to_tone(L):
        toneCheck=True
        for t in tone:
            if syl==t:
                toneCheck=False
        if toneCheck:
            tone.append(syl)
tone.sort()
tone.pop(0)
# print(tone)
export = open('output/nonsilence_phones.txt', 'w', newline='', encoding='utf-8-sig')
for L in tone:
    export.write(L+'\n')
export.close()
