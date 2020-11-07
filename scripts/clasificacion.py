import pandas as pd

pd.set_option('display.max_columns', None)

# partidos_path = "tiburon_negro/partidos.csv"


def get_points1(result):
    a, b = result.split('-')
    try:
        a = int(a)
        b = int(b)
    except Exception as ex:
        return 0, 'N'

    if a == b:
        return 1, 'D'
    elif a > b:
        return 3, 'W'
    else:
        return 0, 'L'


def get_points2(result):
    a, b = result.split('-')
    try:
        a = int(a)
        b = int(b)
    except Exception as ex:
        return 0, 'N'

    if a == b:
        return 1, 'D'
    elif a < b:
        return 3, 'W'
    else:
        return 0, 'L'


def boolena(a, b):
    return int(a[1] == b)


def get_goles(resultado, index):
    try:
        return int(resultado.split('-')[index])
    except:
        return 0


def get_classification(partidos_path):

    # import ipdb;ipdb.set_trace()

    partidos = pd.read_csv(partidos_path)

    partidos = partidos.fillna(value='-')

    partidos['score1'] = [get_goles(s, 0) for s in partidos['resultado']]
    partidos['score2'] = [get_goles(s, 1) for s in partidos['resultado']]

    partidos['points1'] = [get_points1(s)[0] for s in partidos['resultado']]
    partidos['points2'] = [get_points2(s)[0] for s in partidos['resultado']]

    partidos['win1'] = [boolena(get_points1(s), 'W')
                        for s in partidos['resultado']]
    partidos['win2'] = [boolena(get_points2(s), 'W')
                        for s in partidos['resultado']]

    partidos['lose1'] = [boolena(get_points1(s), 'L')
                         for s in partidos['resultado']]
    partidos['lose2'] = [boolena(get_points2(s), 'L')
                         for s in partidos['resultado']]

    partidos['draw1'] = [boolena(get_points1(s), 'D')
                         for s in partidos['resultado']]
    partidos['draw2'] = [boolena(get_points2(s), 'D')
                         for s in partidos['resultado']]

    partidos['inchas1'] = [get_goles(s, 0) for s in partidos['inchas']]
    partidos['inchas2'] = [get_goles(s, 1) for s in partidos['inchas']]

    partidos['ingresos1'] = [get_goles(s, 0) for s in partidos['ingresos']]
    partidos['ingresos2'] = [get_goles(s, 1) for s in partidos['ingresos']]

    drop_columns = [
        'points',
        'inchas',
        'ingresos',
        'win',
        'lose',
        'draw',
    ]

    en_casa = partidos.groupby('equipo1').sum()
    en_casa.rename(columns={'score2': 'score_againts1'}, inplace=True)

    drop_columns1 = [f"{col}1" for col in drop_columns] + ['jornada']
    drop_columns2 = [f"{col}2" for col in drop_columns] + ['jornada']

    en_casa = en_casa.drop(drop_columns2, axis=1)

    # print(en_casa)

    fuera = partidos.groupby('equipo2').sum()
    fuera.rename(columns={'score1': 'score_againts2'}, inplace=True)
    fuera = fuera.drop(drop_columns1, axis=1)

    results = pd.concat([en_casa, fuera], axis=1, join='outer')

    results = results.fillna(value=0)

    # print(results)

    columns = [
        'inchas',
        'ingresos',
        'score',
        'score_againts',
        'win',
        'lose',
        'draw',
        'points',
    ]

    for col in columns:
        col1 = f"{col}1"
        col2 = f"{col}2"

        results[col] = results[col1] + results[col2]

    results['score_diff'] = results['score'] - results['score_againts']
    results['partidos_jugados'] = results['win'] + \
        results['lose'] + results['draw']

    results = results.sort_values(by=['points', 'score_diff'], ascending=False)

    # print(results)
    # cols = list(results.columns.values)

    columns_order = [
        'partidos_jugados',
        'win',
        'draw',
        'lose',
        'points',
        'score',
        'score_againts',
        'score_diff'
    ]

    results = results[columns_order]

    # print(results)

    return results
