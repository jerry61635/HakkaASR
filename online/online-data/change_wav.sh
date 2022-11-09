for j in audio/*.wav; do echo $j; sox "$j" -e signed -r 16000 -b 16 ${j%%.wav}.new.wav; rm $j; done
for j in audio/*.new.wav; do echo $j; mv $j ${j%%.new.wav}.wav; done
