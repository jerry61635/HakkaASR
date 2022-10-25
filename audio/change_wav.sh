for i in test train
do
	for j in $i/*.wav; do echo $j; sox "$j" -e signed -r 16000 -b 16 ${j%%.wav}.new.wav; rm $j; done
	for j in $i/*.new.wav; do echo $j; mv $j ${j%%.new.wav}.wav; done
done
