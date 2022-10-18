import random
from telnetlib import SE
from function import *
import shutil

Sentence = []
Lexicon = []

#開啟檔案 7541為全部檔案數量
f = open('nameAndText.txt', 'r', encoding='utf-8')
for i in range(7541):
# for i in range(10):
    Sentence.append(f.readline().split('\n')[0])
f.close

for line in Sentence:
    for word in line.split(' ')[1:]:
        wordChk=True
        for L in Lexicon:
            if word == L:
                wordChk=False
                break
        if wordChk:
            Lexicon.append(word)


# export corpus.txt
print('export corpus.txt')
export = open('output/corpus.txt', 'w', newline='', encoding='utf-8-sig')
for line in Sentence:
    output=''
    for word in line.split(' ')[1:]:
        output = output+' '+word
    export.write(output[1:]+'\n')
export.close()
# shutil.copyfile('./corpus.txt','../../../data/local/corpus.txt')

# export train/test_text
p=0.2 #比例
print('export text_test and text_train')
export = open('output/text_train', 'w', newline='', encoding='utf-8-sig')
export2 = open('output/text_test', 'w', newline='', encoding='utf-8-sig')
for line in Sentence:
    if random.random()>=p:
        export.write(line+'\n')
    else:
        export2.write(line+'\n')
# shutil.copyfile('../ImTong/'+Sentence[L][0]+'.wav','../../train/'+Sentence[L][0]+'.wav')
export.close()
export2.close()
# shutil.copyfile('./text_train','../../../data/train/text')
# shutil.copyfile('./text_test','../../../data/test/text')

# export lexicon.txt
print('export Lexicon')
export = open('output/lexicon.txt', 'w', newline='', encoding='utf-8-sig')
for L in Lexicon:
    output = L
    for syl in to_tone(L):
        output=output+' '+syl
    export.write(output+'\n')
export.close()
# shutil.copyfile('./lexicon.txt','../../Language/lexicon.txt')

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