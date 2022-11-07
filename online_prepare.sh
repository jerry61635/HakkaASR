#!/usr/bin/env bash

./prepare_online_decoding.sh \
	--feature-type mfcc \
	--add-pitch true \
	data/lang_chain \
	exp/nnet3/extractor \
	exp/chain/tdnn_1d_sp \
	online/prepare || exit 1;
