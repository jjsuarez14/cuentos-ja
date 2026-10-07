"""Genera public/cuentos.json con cuentos, agenda por fecha y festivos.

Uso: python3 scripts/build.py

Reglas:
- Cada cuento se ubica en su fecha según (semana, día): lunes de la semana 1 = 21/09/2026.
- Desde REGLA_SIESTA, los días lectivos (lunes a viernes no festivos) no llevan siesta;
  esas siestas pasan al banco para reutilizarlas.
- cuentos/ajustes.json fuerza asignaciones por fecha (p. ej. siestas del banco en festivos).
"""
import json, glob, os, sys
from datetime import date, timedelta
sys.path.insert(0, os.path.dirname(__file__))
from parse import parse

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LUNES0 = date(2026, 9, 21)
ARRANQUE = date(2026, 9, 25)
REGLA_SIESTA = date(2026, 10, 7)
DIAS = ['lun', 'mar', 'mie', 'jue', 'vie', 'sab', 'dom']


def cargar_festivos():
    crudo = json.load(open(os.path.join(RAIZ, 'cuentos', 'festivos.json'), encoding='utf-8'))
    fest = {}
    for k, v in crudo.items():
        if k.startswith('_'):
            continue
        if '..' in k:
            a, b = (date.fromisoformat(x) for x in k.split('..'))
            d = a
            while d <= b:
                fest[d.isoformat()] = v
                d += timedelta(days=1)
        else:
            fest[k] = v
    return fest


def main():
    cuentos = []
    for f in sorted(glob.glob(os.path.join(RAIZ, 'cuentos', 'semana*.txt'))):
        cuentos += parse(f)
    por_id = {c['id']: c for c in cuentos}
    festivos = cargar_festivos()

    agenda = {}
    for c in cuentos:
        d = LUNES0 + timedelta(days=(c['semana'] - 1) * 7 + DIAS.index(c['dia']))
        agenda.setdefault(d.isoformat(), {})[c['momento']] = c['id']

    # Regla: sin siesta en días lectivos desde REGLA_SIESTA
    for k in list(agenda):
        d = date.fromisoformat(k)
        lectivo = d.weekday() < 5 and k not in festivos
        if d >= REGLA_SIESTA and lectivo:
            agenda[k].pop('siesta', None)

    ajustes = json.load(open(os.path.join(RAIZ, 'cuentos', 'ajustes.json'), encoding='utf-8'))
    for k, v in ajustes.items():
        if k.startswith('_'):
            continue
        for momento, cid in v.items():
            assert cid in por_id, f'ajuste con id desconocido: {cid}'
            agenda.setdefault(k, {})[momento] = cid

    usados = {cid for v in agenda.values() for cid in v.values()}
    banco = sorted(c['id'] for c in cuentos if c['id'] not in usados)

    # Validación: cobertura y duplicados
    errores = []
    vistos = {}
    for k in sorted(agenda):
        for m, cid in agenda[k].items():
            if cid in vistos:
                errores.append(f'{cid} repetido en {vistos[cid]} y {k}')
            vistos[cid] = k
    ultimo = max(date.fromisoformat(k) for k in agenda)
    d = ARRANQUE
    while d <= ultimo:
        k = d.isoformat()
        e = agenda.get(k, {})
        if 'noche' not in e:
            errores.append(f'{k}: falta noche')
        necesita_siesta = d < REGLA_SIESTA or d.weekday() >= 5 or k in festivos
        if necesita_siesta and 'siesta' not in e:
            errores.append(f'{k}: falta siesta')
        d += timedelta(days=1)

    salida = {
        'lunes_semana1': LUNES0.isoformat(),
        'arranque': ARRANQUE.isoformat(),
        'cuentos': cuentos,
        'agenda': dict(sorted(agenda.items())),
        'festivos': {k: v for k, v in festivos.items() if k <= ultimo.isoformat()},
        'banco': banco,
    }
    json.dump(salida, open(os.path.join(RAIZ, 'public', 'cuentos.json'), 'w', encoding='utf-8'), ensure_ascii=False)

    print(f'{len(cuentos)} cuentos · agenda {ARRANQUE} → {ultimo} · banco: {banco or "vacío"}')
    for c in cuentos:
        obj = 750 if c['momento'] == 'siesta' else 1200
        dv = (c['palabras'] - obj) / obj
        if abs(dv) > 0.10:
            errores.append(f"{c['id']}: {c['palabras']} palabras ({dv:+.0%})")
    if errores:
        print('ERRORES:'); [print(' -', e) for e in errores]; sys.exit(1)
    print('Validación OK')


if __name__ == '__main__':
    main()
