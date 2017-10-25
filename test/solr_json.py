#!/usr/bin/env python

import json

with open('select.json') as jf:
    data=json.load(jf)
jf.close()

#print (json.dumps(data,indent=2,sort_keys=False))

articles=data['response']['docs']

fout=open('live_affil_test.txt','w')
for a in articles:
    bibcode=a['bibcode']
    ia=0
    try:
        a['aff']
    except KeyError:
        pass
    else:
        for x,y in zip(a['aff'],a['author']):
            z=x.split(';')
            iw=0
            for w in z:
                p=w.strip().encode('ascii','xmlcharrefreplace')
                q=y.strip().encode('ascii','xmlcharrefreplace')
                pos=str(ia)+'/'+str(iw)
                fout.write("%s\t%s\t%s\t%s\n"%(bibcode,p,q,pos))
                iw+=1
            ia+=1
fout.close()
        
    
