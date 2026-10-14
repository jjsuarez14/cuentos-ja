import re

TIPOS = {'ja', 'clasico', 'original', 'en', 'spidey'}
NO_IMPRIMIBLE = {'spidey'}  # personajes con derechos de autor: solo en la app


def parse(path):
    """Lee un archivo de cuentos.

    Cabecera: === id | semana | dia | momento | tipo | titulo | tema | fuente
    semana 0 = no se ubica por semana; su fecha se asigna en cuentos/ajustes.json.
    Un bloque '@@ Para papá' al final del cuento contiene notas para el adulto (una por línea).
    """
    out = []
    for block in open(path, encoding='utf-8').read().split('=== ')[1:]:
        head, body = block.split('\n', 1)
        f = [x.strip() for x in head.split('|')]
        assert f[4] in TIPOS, f'tipo desconocido {f[4]} en {f[0]}'
        nota = []
        if '\n@@ ' in body:
            body, extra = body.split('\n@@ ', 1)
            lineas = [l.strip() for l in extra.strip().split('\n') if l.strip()]
            nota = lineas[1:]  # la primera línea es el título del recuadro
        paras = [p.strip() for p in body.strip().split('\n\n') if p.strip()]
        words = sum(len(re.findall(r"[\wÁÉÍÓÚáéíóúñÑüÜ.'’]+", p)) for p in paras)
        c = dict(id=f[0], semana=int(f[1]), dia=f[2], momento=f[3], tipo=f[4], titulo=f[5], tema=f[6],
                 fuente=f[7], palabras=words, p=paras, lang='en' if f[4] == 'en' else 'es',
                 imprimible=f[4] not in NO_IMPRIMIBLE)
        if nota:
            c['nota'] = nota
        out.append(c)
    return out
