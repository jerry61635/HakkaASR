import os

with open(f'./data/all/wav.scp', 'w')as file:
    ls = os.listdir('./audio/0.2.1/ImTong')
    ls.sort()
    for audio in ls:
        abspath = os.path.abspath(f'audio/0.2.1/ImTong/{audio}')
        utteranceID = audio[:-4]
        file.write(f'{utteranceID} {abspath}\n')

mode = ['test', 'train']

for m in mode:
    with open(f'./data/{m}/wav.scp', 'w') as testFile:
        ls = os.listdir(f'./audio/{m}')
        ls.sort()
        for audio in ls:
            utteranceID = audio[:-4]
            abspath = os.path.abspath(f'./audio/{m}/{audio}')
            testFile.write(f'{utteranceID} {abspath}\n')
