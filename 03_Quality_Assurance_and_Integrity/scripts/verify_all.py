#!/usr/bin/env python3
from pathlib import Path
import csv, itertools, collections, math, json, hashlib

ROOT = Path(__file__).resolve().parents[2]
CANON = ROOT / "01_Historical_GA_Results" / "100Job" / "Ta100x20_Canonical_595"

def rows(path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def close(a,b,tol=1e-10):
    return abs(float(a)-float(b)) <= tol

def as_bool(x):
    return str(x).strip().lower() in {"true","1","yes"}

def cmax(matrix, perm_1based):
    m=len(matrix[0]); c=[0]*m
    for jj in perm_1based:
        j=jj-1
        c[0]+=matrix[j][0]
        for k in range(1,m):
            c[k]=max(c[k],c[k-1])+matrix[j][k]
    return c[-1]

# ---------- manuscript-critical summary checks ----------
HIST = ROOT/"01_Historical_GA_Results"/"Current_Manuscript_Historical_Anchor_Summary.csv"
PROS = ROOT/"02_Prospective_24_Target_Results"/"Prospective_24_Target_Summary.csv"
PROTOCOL = ROOT/"04_Protocol_and_Data_Dictionaries"/"Prospective_Protocol_Prespecified_v1.1_2026-08-27.json"
for p in (HIST,PROS,PROTOCOL):
    assert p.exists(), p
h=rows(HIST); anchors=[r for r in h if r["anchor"].strip().upper()!="OVERALL"]
expected={
"20x5":(749,840,89.17,9000),"20x10":(775,840,92.26,8000),"20x20":(720,840,85.71,8000),
"50x5":(824,840,98.10,2000),"50x10":(656,840,78.10,9000),"50x20":(613,840,72.98,9000),
"100x5":(837,840,99.64,9000),"100x10":(814,840,96.90,9000),"100x20":(595,840,70.83,17000)}
assert len(anchors)==9
for r in anchors:
    ec,en,er,eg=expected[r["anchor"]]
    assert int(r["safe_count"])==ec and int(r["comparisons"])==en and close(r["safe_rate_pct"],er,0.0051) and int(r["G"])==eg
hist_safe=sum(int(r["safe_count"]) for r in anchors); hist_n=sum(int(r["comparisons"]) for r in anchors)
assert (hist_safe,hist_n)==(6583,7560)
protocol=json.loads(PROTOCOL.read_text(encoding="utf-8")); pt=json.dumps(protocol,ensure_ascii=False)
for x in [749,775,720,824,656,613,837,814,595]: assert str(x) in pt
p=rows(PROS); assert len(p)==24
actions={a:sum(r["action"]==a for r in p) for a in ("GREEN","AMBER","RED")}; assert actions=={"GREEN":8,"AMBER":12,"RED":4}
assert sum(as_bool(r["policy_safe"]) for r in p)==21
assert sum(as_bool(r["center_safe"]) for r in p)==21

# ---------- canonical 595 raw reconstruction ----------
neh_rows=rows(CANON/"Ta100x20_NEH_reference.csv")
NEH={int(r["instance"]):int(r["NEH_Cmax"]) for r in neh_rows}
assert [NEH[i] for i in range(1,11)] == [6541,6523,6639,6557,6695,6664,6632,6739,6677,6677]

# matrices and independent standard-NEH verification
# Standard NEH: jobs sorted by descending total processing time; sequential best insertion; earliest position breaks ties.
def neh_cmax(matrix):
    order=sorted(range(len(matrix)), key=lambda j:(-sum(matrix[j]), j))
    seq=[]
    for job in order:
        best=None; bestv=None
        for pos in range(len(seq)+1):
            cand=seq[:pos]+[job]+seq[pos:]
            v=cmax(matrix,[x+1 for x in cand])
            if bestv is None or v<bestv:
                bestv=v; best=cand
        seq=best
    return bestv

MATS={}
for i in range(1,11):
    mp=CANON/"matrices"/f"Ta100x20_{i:02d}.csv"
    with mp.open("r",encoding="utf-8-sig",newline="") as f:
        mat=[[int(x) for x in rr] for rr in csv.reader(f) if rr]
    assert len(mat)==100 and all(len(rr)==20 for rr in mat)
    MATS[i]=mat
    assert neh_cmax(mat)==NEH[i], (i,neh_cmax(mat),NEH[i])

config_order=[(pop,pc,pm) for pop in [1,2,3,4,5] for pc in [0.85,0.8875,0.925,0.9625,1.0] for pm in [0.025,0.05,0.075,0.10,0.125]]
rank={k:i for i,k in enumerate(config_order)}
main_means={}; main_cmax_checks=0
for i in range(1,11):
    rr=rows(CANON/"main"/f"Ta100x20_inst{i:02d}_main_G17000_R10_complete.csv")
    assert len(rr)==1250
    by=collections.defaultdict(list); keys=set()
    for r in rr:
        assert int(r["instance"])==i and int(r["G"])==17000
        assert int(r["Ps"])==int(r["pop_mult"])*100
        assert int(r["seed"])==2230000201+i*100000+int(r["rep"])*1009
        k=(int(r["pop_mult"]),float(r["pc"]),float(r["pm"]))
        by[k].append(int(r["best_cmax"])); keys.add((k,int(r["rep"])))
        perm=[int(x) for x in r["best_perm_1based"].split("-")]
        assert len(perm)==100 and len(set(perm))==100 and min(perm)==1 and max(perm)==100
        assert cmax(MATS[i],perm)==int(r["best_cmax"])
        main_cmax_checks+=1
    assert len(by)==125 and len(keys)==1250 and all(len(v)==10 for v in by.values())
    main_means[i]={k:sum(v)/len(v) for k,v in by.items()}

oracle={i:min(main_means[i].items(),key=lambda kv:(kv[1],rank[kv[0]])) for i in range(1,11)}

# 120 policies
calc=[]
for sid,cal in enumerate(itertools.combinations(range(1,11),3),start=1):
    rg={}
    for k in config_order:
        vals=[(main_means[i][k]-oracle[i][1])/NEH[i]*100 for i in cal]
        rg[k]=(sum(vals)/3,max(vals))
    best=min(v[0] for v in rg.values())
    adm=[k for k,v in rg.items() if v[0] <= best+0.25+1e-12]
    chosen=min(adm,key=lambda k:(rg[k][1],rg[k][0],rank[k]))
    holdouts=[i for i in range(1,11) if i not in cal]
    calc.append((sid,cal,holdouts,chosen,best,rg[chosen][0],rg[chosen][1],len(adm)))
fr=rows(CANON/"Ta100x20_120split_policies_prespecified.csv"); assert len(fr)==120
for a,b in zip(calc,fr):
    sid,cal,hold,chosen,best,cmean,cworst,nadm=a
    assert sid==int(b["split_id"])
    assert cal==(int(b["cal1"]),int(b["cal2"]),int(b["cal3"]))
    assert "-".join(map(str,hold))==b["holdouts"]
    assert chosen==(int(b["pop_mult"]),float(b["pc"]),float(b["pm"]))
    assert close(best,b["best_mean_regret_pp"]) and close(cmean,b["chosen_mean_regret_pp"]) and close(cworst,b["chosen_worst_regret_pp"])
    assert nadm==int(b["admissible_count"])

# fresh runs and 840 comparisons
fresh=rows(CANON/"Ta100x20_fresh_validation_complete_790.csv"); assert len(fresh)==790
by=collections.defaultdict(list); fresh_cmax_checks=0
for r in fresh:
    i=int(r["instance"]); rep=int(r["rep"])
    assert int(r["G"])==17000 and int(r["Ps"])==int(r["pop_mult"])*100
    assert int(r["seed"])==2330000201+i*100000+rep*1009
    k=(i,int(r["pop_mult"]),float(r["pc"]),float(r["pm"]))
    by[k].append(int(r["best_cmax"]))
    perm=[int(x) for x in r["best_perm_1based"].split("-")]
    assert len(perm)==100 and len(set(perm))==100
    assert cmax(MATS[i],perm)==int(r["best_cmax"])
    fresh_cmax_checks+=1
assert len(by)==79 and all(len(v)==10 for v in by.values())
fmeans={k:sum(v)/10 for k,v in by.items()}

hold=rows(CANON/"Ta100x20_3to7_holdout_observations_840.csv"); assert len(hold)==840
near=0
for r in hold:
    i=int(r["target"])
    tk=(i,int(r["transfer_pop_mult"]),float(r["transfer_pc"]),float(r["transfer_pm"]))
    ok=(i,int(r["oracle_pop_mult"]),float(r["oracle_pc"]),float(r["oracle_pm"]))
    tm=fmeans[tk]; om=fmeans[ok]; se=(tm-om)/NEH[i]*100; clip=max(0.0,se); flag=se<=0.25
    assert close(tm,r["transfer_mean_cmax"]) and close(om,r["oracle_mean_cmax"]) and close(se,r["signed_excess_pp"]) and close(clip,r["clipped_regret_pp"])
    assert flag==as_bool(r["near_optimal"])
    near += flag
assert near==595
ov=rows(CANON/"Ta100x20_transfer_overall_summary.csv"); assert len(ov)==1
assert int(ov[0]["holdouts"])==840 and int(ov[0]["near_opt_count"])==595 and int(ov[0]["fresh_real_GA_runs"])==790

print("PASS — manuscript-critical summary verification")
print(f"Historical anchors: {hist_safe}/{hist_n} = {100*hist_safe/hist_n:.2f}%")
print("PASS — Ta100x20 canonical 595/840 raw reconstruction")
print("Main rows verified:", sum(1250 for _ in range(10)))
print("Main independent Cmax checks:", main_cmax_checks)
print("Split policies reproduced: 120/120")
print("Fresh rows verified: 790/790")
print("Fresh independent Cmax checks:", fresh_cmax_checks)
print("Holdout comparisons reproduced: 840/840")
print("Near-optimal result: 595/840 = 70.833333%")
