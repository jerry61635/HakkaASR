from os import walk
from os.path import join
import shutil

# 指定要列出所有檔案的目錄
mypath = ".\\originalAudio"
output = open('nameAndText.txt', 'w',encoding='utf-8')

# 遞迴列出所有檔案的絕對路徑
for root, dirs, files in walk(mypath):
  for f in files:
    fullpath = join(root, f)
    if fullpath.find('問題')>0 or fullpath.find('desktop.ini')>0:
        continue
    if fullpath.find('txt')<0:
        continue
    f = open(fullpath, 'r',encoding='utf-8')
    lines = f.readlines()
    temp=fullpath.split('\\')[:-1]
    from_url = temp[0]+'/'+temp[1]+'/'+temp[2]+'/'+temp[3]+'/split/'
    for line in lines:
        line = line.replace('  ',' ')
        print(line)
        if len(line)>1:
            if line.find('\n')>=0:
                line = line.split('\n')[0]
            if line[-1]==' ':
                line = line[:-1]

            line_list = line.split(' | ')
            output.write(line_list[0]+' '+line_list[2]+'\n')
            # print(from_url+line_list[0]+'.wav')
            shutil.copyfile(from_url+line_list[0]+'.wav','./audioFile/'+line_list[0]+'.wav')
    f.close()

output.close()