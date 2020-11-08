import pandas as pd


def get_teams_aggregates(data_path, teams_data_path, palyers_team_aggregates):

    players = pd.read_csv(data_path)
    teams = pd.read_csv(teams_data_path)
    teams_data = pd.read_csv("data/equipos.csv")

    players = players.fillna(value=0)
    teams = teams.fillna(value=0)


    try:
        players.loc[players.heridas != 0, 'value'] = 0

        players.loc[players.heridas == -1, 'muertos'] = 1

    except Exception:
        pass

    teams = teams.set_index('raza').join(teams_data.set_index('raza'))

    teams = teams.reset_index()

    teams['value1'] = teams['factor_inchas']*10 + \
        teams['so'] * teams['valor_so'] + 50 * teams['medico']

    teams = teams.rename(columns={'nombre': 'equipo'}, inplace=False)

    teams = teams.set_index('equipo')

    print(teams)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

    results = pd.concat([palyers_team_aggregates, teams], axis=1, join='outer')
    results['valor_calculado'] = results['value1'] + results['value']

    print('\n *** STATS EQUIPOS ***\n')
    team_aggregates = players.groupby('equipo').sum()

    print(team_aggregates)

    pd.options.display.float_format = '{:,.0f}'.format

    columns_ordered = [
        'raza',
        'entrendor',
        'so',
        'valor_so',
        'factor_inchas',
        'medico',
        'valor_calculado',
    ]

    columns_ordered_stats = [
        'raza',
        'touchdowns',
        'passes',
        'casualties',
        'interceptions',
        'mvp',
        'actions',
        'PE'

    ]

    team_aggregates_values = results[columns_ordered]

    team_aggregates_stats = results[columns_ordered_stats]
    team_aggregates_stats = team_aggregates_stats.sort_values(
        by=['PE'], ascending=False)
    return team_aggregates_values, team_aggregates_stats
