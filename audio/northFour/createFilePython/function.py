consonant       = ['ngi', 'bb', 'ch', 'ji', 'li', 'ng', 'qi', 'rh', 'sh', 'xi', 'zh', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 'r', 's', 't', 'v', 'x', 'z']
vowel           = ['iang', 'iong', 'iung', 'uang', 'ang', 'iab', 'iad', 'iag', 'iam', 'ian', 'iau', 'ieb', 'ied', 'iem', 'ien', 'ieu', 'iib', 'iid', 'iim', 'iin', 'iod', 'iog', 'ioi', 'ion', 'iud', 'iug', 'iui', 'iun', 'ong', 'uad', 'uag', 'uai', 'uan', 'ued', 'uen', 'ung', 'ab', 'ad', 'ag', 'ai', 'am', 'an', 'au', 'eb', 'ed', 'em', 'en', 'eu', 'ia', 'ib', 'id', 'ie', 'ii', 'im', 'in', 'io', 'iu', 'ng', 'od', 'og', 'oi', 'on', 'ua', 'ud', 'ue', 'ug', 'ui', 'un', 'a', 'e', 'i', 'm', 'n', 'o', 'u']
tone            = ['24', '11', '31', '55', '2', '5']

#把音轉換成音節
def to_tone(s):
    for t in tone:
        if s.find(t)!=-1:
            syllable=s.split(t)[0]
            # print(syllable[-1*len(v):])
            for v in vowel:
                if syllable[-1*len(v):]==v:
                    con = syllable.split(v)[0]
                    if con == '':
                        return[v+t]
                    else:
                        for c in consonant:
                            if c == con:
                                return[c,v+t]
    return 'Error Word'

