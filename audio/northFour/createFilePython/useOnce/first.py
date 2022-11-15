#把原始檔案內容只提取出音檔名稱和數字調
#總共7541句


punctuation=['，','！','？','。','「','」','、','：','；','〈','〉','＜','＞','（','）','『','』','－－','—']

f = open('fullContent.txt', 'r', encoding='utf-8')
o = open('nameAndText.txt', 'w', encoding='utf-8')
for i in range(7541):
    line = f.readline().split('|')
    # print(line[0].split(' ')[0])
    # print(line[4].split(' ')[1:-1])
    output=''
    for word in line[4].split(' ')[1:-1]:
        chk=True
        for p in punctuation:
            if word==p:
                chk=False
        if chk:
            if output=='':
                output=word
            else:
                output = output+' '+word
    # print(output)
    o.write(line[0].split(' ')[0]+' '+output+'\n')
o.close()
f.close()
