import sys
import os

srcpath=sys.argv[1]
print(srcpath)
path="audio/text"

os.remove(path)

ls = os.listdir(srcpath)
ls.sort()
ls.remove("問題音檔")
first=True

for ph in ls:
    with open(f'{srcpath}/{ph}/{ph}.txt', 'r') as srcfile:
        data = srcfile.readlines()
        mode = True

        with open(f'{path}','a') as dirfile:
            if first == True:
                print("change")
                first=False
            else:
                dirfile.write(f'\n')
            for filedata in data:
                if filedata != "\n":
                    for index in filedata:
                        if index == '|':
                            mode = not mode
                            continue
                        if mode == True:
                            print(index, end='')
                            dirfile.write(f'{index}')
