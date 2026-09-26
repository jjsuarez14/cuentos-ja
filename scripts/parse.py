import re, json, sys
def parse(path):
    out=[]
    for block in open(path,encoding='utf-8').read().split('=== ')[1:]:
        head, body = block.split('\n',1)
        f=[x.strip() for x in head.split('|')]
        paras=[p.strip() for p in body.strip().split('\n\n') if p.strip()]
        words=sum(len(re.findall(r"[\wÁÉÍÓÚáéíóúñÑüÜ.]+", p)) for p in paras)
        out.append(dict(id=f[0],semana=int(f[1]),dia=f[2],momento=f[3],tipo=f[4],titulo=f[5],tema=f[6],fuente=f[7],palabras=words,p=paras))
    return out
if False:
    for c in parse('semana1.txt'):
        t=750 if c['momento']=='siesta' else 1200
        print(f"{c['id']:16} {c['palabras']:5} obj {t} ({(c['palabras']-t)/t:+.0%}) {c['tipo']}")
