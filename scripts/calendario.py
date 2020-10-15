import pandas as pd


def get_calendario(partidos_path):

    partidos = pd.read_csv(partidos_path)
    partidos = partidos.fillna(value='-')
    equipos = set(partidos['equipo1'].values)

    partidos_reducido = partidos[[
        'jornada',
        'equipo1',
        'equipo2',
        'resultado'
    ]]

    jornadas = range(1, 7)

    html = ''

    for jornada in jornadas:

        html += f'<div><h3> JORNADA {jornada}</h3>'
        partidos_de_la_jornda = partidos_reducido[partidos_reducido['jornada'] == jornada]

        partidos_de_la_jornda = partidos_de_la_jornda[[
            'equipo1',
            'equipo2',
            'resultado'
        ]]

        html += f'{partidos_de_la_jornda.to_html()} </div>'

    html_calendario_equipos = ''

    for equipo in equipos:
        partidos_equipo = partidos[
            (partidos['equipo1'] == equipo) |
            (partidos['equipo2'] == equipo)
        ]

        html_calendario_equipos += f'<div><h3> EQUIPO {equipo}</h3>'
        html_calendario_equipos += f' {partidos_equipo.to_html()} </div>'

    return html, html_calendario_equipos