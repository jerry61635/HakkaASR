import os

ls = os.listdir("./audio/0.2.1/ImTong")
ls.sort()

with open(f'./data/all/utt2spk', 'w', encoding='UTF-8') as file:
    for utt in ls:
        utteranceID = utt[:-4]
        speaker = utt[:-9]
        file.write(f'{utteranceID} {speaker}\n')

ls = os.listdir("./audio/test")
ls.sort()
with open(f'./data/test/utt2spk', 'w') as file:
    for utt in ls:
        utteranceID = utt[:-4]
        speaker = utt[:-9]
        file.write(f'{utteranceID} {speaker}\n')

ls = os.listdir("./audio/train")
ls.sort()
with open(f'./data/train/utt2spk', 'w') as file:
    for utt in ls:
        utteranceID = utt[:-4]
        speaker = utt[:-9]
        file.write(f'{utteranceID} {speaker}\n')
