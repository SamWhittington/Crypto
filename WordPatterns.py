def word_pattern(word):
    lis, lout, loutn,f = list(word.lower()), [], [], []
    { lout.append(lis[i]) for i in range(0, len(lis)) if lis[i] not in lis[:i] }
    { loutn.append(i) for i in range(0, len(lout)) }
    d = dict(zip(lout, loutn))
    [ f.append(str(d.get(lis[i]))) for i in range(0, len(lis)) if lis[i] in d ]
    return '.'.join(f)
