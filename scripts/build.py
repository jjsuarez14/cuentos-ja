"""Convierte cuentos/semanaN.txt en public/cuentos.json. Uso: python3 scripts/build.py"""
import json, glob, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from parse import parse
raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cuentos = []
for f in sorted(glob.glob(os.path.join(raiz, 'cuentos', 'semana*.txt'))):
    cuentos += parse(f)
json.dump({'inicio': '2026-09-25', 'cuentos': cuentos},
          open(os.path.join(raiz, 'public', 'cuentos.json'), 'w', encoding='utf-8'), ensure_ascii=False)
for c in cuentos:
    obj = 750 if c['momento'] == 'siesta' else 1200
    print(f"{c['id']:16} {c['palabras']:5}  {(c['palabras']-obj)/obj:+.0%}")
print(len(cuentos), 'cuentos')
