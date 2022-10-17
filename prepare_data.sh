#!/bin/bash

. ./path.sh

echo 'Deleting old files'
rm data/test/utt2dur
rm data/train/utt2dur
rm data/test/utt2num_frames
rm data/train/utt2num_frames
rm data/train/reco2dur
rm data/train_sp/feats.scp

echo 'Preparing wav.scp'
python3 wav_prepare.py

echo 'Preparing utt2spk'
python3 utt2spk_prepare.py

echo 'Copying text & lexicon.txt'
cp audio/0.2.1/createLexicon/text_test data/test/text
cp audio/0.2.1/createLexicon/text_train data/test/train

cp audio/0.2.1/createLexicon/lexicon.txt audio/Language
