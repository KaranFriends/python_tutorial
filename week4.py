def orangecap(d):
    listt = {}
    for k,v in d.items():
        for kk, vv in v.items():
            if kk in listt.keys():
                listt[kk] =  listt[kk] +  vv
            else:
                listt[kk] = vv

    # for k in sorted(listt, key=listt.get, reverse=True):
    #     k, listt[k]


    listt = sorted(listt.items(), key=lambda kv: (kv[1], kv[0]))
    # return(list(listt.keys())[0])
    return listt[-1]


print(orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}}))