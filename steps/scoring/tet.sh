#usr/bin/env bash

dir=../../exp/mono/decode_test
text="123"
files=($dir/scoring_kaldi/test_filt.txt)
for wip in $(echo $word_ins_penalty | sed 's/,/ /g'); do
  for lmwt in $(seq $min_lmwt $max_lmwt); do
    files+=($dir/scoring_kaldi/penalty_${wip}/${lmwt}.txt)
  done
done
#cat $temp

for f in "${files[@]}" ; do
  fout=${f%.txt}.chars.txt
  if [ -x local/character_tokenizer ]; then
    cat $f |  local/character_tokenizer > $fout
  else
#    echo "123"
#    cat $f | perl -CSDA -ane '
#      {
#        print $F[0];
#	print "\n";
#      }
#    '
    python3 func.py $f
  fi
done

