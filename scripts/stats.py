import pandas as pd

# pd.set_option('display.max_columns', None)

# data_path = "../tiburon_negro/jugadores.csv"


def get_stats(data_path):

    players = pd.read_csv(data_path)

    players = players.fillna(value=0)

    players['PE'] = players['passes']+players['touchdowns']*3 + \
        (players['interceptions']+players['casualities'])*2+players['mvp'] * 5

    players['actions'] = players['passes']+players['touchdowns'] + \
        players['interceptions']+players['casualities']

    print('\n *** TOP TOUCHDOWNS ***\n')

    touchdowns = players[players['touchdowns'] > 0].sort_values(
        by=['touchdowns', 'PE'], ascending=False)
    print(touchdowns.head(10))

    print('\n *** TOP PASSES ***\n')

    passes = players[players['passes'] > 0].sort_values(
        by=['passes', 'PE'], ascending=False)
    print(passes.head(10))

    print('\n *** TOP INTERCEPTIONS ***\n')

    interceptions = players[players['interceptions'] > 0].sort_values(
        by=['interceptions', 'PE'], ascending=False)
    print(interceptions.head(10))

    print('\n *** TOP MVPS ***\n')

    mvp = players[players['mvp'] > 0].sort_values(
        by=['mvp', 'PE'], ascending=False)
    print(mvp.head(10))

    print('\n *** TOP CASUALITIES ***\n')

    casualities = players[players['casualities'] > 0].sort_values(
        by=['casualities', 'PE'], ascending=False)
    print(casualities.head(10))

    print('\n *** TOP MOST IMPORVED ***\n')

    pe = players[players['PE'] > 0].sort_values(
        by=['PE'], ascending=False)
    print(pe.head(10))

    print('\n *** TOP MOST ACTIONS ***\n')

    actions = players[players['actions'] > 0].sort_values(
        by=['actions'], ascending=False)

    print(actions.head(10))

    print('\n *** STATS EQUIPOS ***\n')
    team_aggregates = players.groupby('equipo').sum()

    team_aggregates = team_aggregates.drop(['numero'], axis=1)

    print(team_aggregates)

    pd.options.display.float_format = '{:,.0f}'.format
    team_aggregates["touchdowns"] = pd.to_numeric(
        team_aggregates["touchdowns"], downcast='integer')

    return touchdowns, passes, interceptions, mvp, casualities, pe, actions, team_aggregates
