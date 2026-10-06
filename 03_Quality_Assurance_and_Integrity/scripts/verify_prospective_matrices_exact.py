#!/usr/bin/env python3
from pathlib import Path
import csv, hashlib
ROOT=Path(__file__).resolve().parents[2]
META=ROOT/'02_Prospective_24_Target_Results'/'Prospective_24_Target_Design_Prespecified.csv'
MATS=ROOT/'02_Prospective_24_Target_Results'/'matrices'
def rows(p):
    with p.open('r',encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def matrix(p):
    with p.open('r',encoding='utf-8-sig',newline='') as f:return [[int(x) for x in r] for r in csv.reader(f) if r]
def cmax(P,seq):
    c=[0]*len(P[0])
    for j in seq:
        c[0]+=P[j][0]
        for k in range(1,len(c)):c[k]=max(c[k],c[k-1])+P[j][k]
    return c[-1]
def neh(P):
    order=sorted(range(len(P)),key=lambda j:(-sum(P[j]),j)); seq=[]
    for j in order:
        best=None; bestv=None
        for pos in range(len(seq)+1):
            cand=seq[:pos]+[j]+seq[pos:]; v=cmax(P,cand)
            if bestv is None or v<bestv:bestv=v; best=cand
        seq=best
    return bestv
rr=rows(META); sh=ne=0
for r in rr:
    p=MATS/r['matrix_file']; assert p.exists(),p
    h=hashlib.sha256(p.read_bytes()).hexdigest(); nv=neh(matrix(p))
    assert h==r['matrix_sha256'],(r['target_index'],'sha'); sh+=1
    assert nv==int(r['NEH']),(r['target_index'],'NEH',nv,r['NEH']); ne+=1
print(f'PASS — prospective exact matrix replay: SHA-256 {sh}/{len(rr)}, NEH {ne}/{len(rr)}')
