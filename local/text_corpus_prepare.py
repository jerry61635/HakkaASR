import pandas as pd
import numpy as np
import os

df = pd.read_csv('./audio/0.2.1/SuiSiann.csv')

data = df.to_numpy()

ls = os.listdir("./audio/0.2.1/ImTong")
ls.sort()

j = 0

for i in ls:
    ls[j] = i[:-4]
    j += 1

j = 0

with open(f'./data/all/text', 'w', encoding = 'UTF-8') as file:
    with open(f'./data/test/text', 'w', encoding = 'UTF-8') as testFile:
        with open(f'./data/train/text', 'w', encoding = 'UTF-8') as trainFile:
            for i in data[...,3]:
                file.write(f'{ls[j]} {i}\n')
                if j < 999:
                    testFile.write(f'{ls[j]} {i}\n')
                else:
                    trainFile.write(f'{ls[j]} {i}\n')
                j += 1

with open(f'./data/local/corpus.txt', 'w', encoding = 'UTF-8') as file:
    for corpus in data[...,3]:
        file.write(f'{corpus}\n')
