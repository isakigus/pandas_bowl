from clasificacion import get_classification
from team_value import get_teams_aggregates
from calendario import get_calendario
from stats import get_stats
from leagues import leagues

styles = '''
a {
  color: red;
  text-decoration: none;
  text-transform: uppercase;
}

a:hover {
  background-color: #555;
}

a:active {
  background-color: black;
}

a:visited {
  background-color: #ccc;
}



table, th, td {
border: 1px solid white;
border-collapse: collapse;
text-align: right;
}


th, td {
padding: 15px;
}

.container {

    display:flex;
    align-items:space-around;
}

.container > div {
margin:10px;
}

.calendario {
    width :80%;
}
'''


def get_league_html(league):
    data_path = f"{league.folder}/partidos.csv"
    players_path = f"{league.folder}/jugadores.csv"
    teams_data_path = f"{league.folder}/equipos.csv"

    (
        touchdowns,
        passes,
        interceptions,
        mvp,
        casualties,
        pe,
        actions,
        palyers_team_aggregates
    ) = get_stats(data_path=players_path)

    calendario, html_calendario_equipos = get_calendario(
        partidos_path=data_path)
    classification_table = get_classification(partidos_path=data_path)
    team_aggregates_values, team_aggregates_stats = get_teams_aggregates(
        data_path=players_path,
        teams_data_path=teams_data_path,
        palyers_team_aggregates=palyers_team_aggregates
    )

    html_web = f'''

    <html>
    <head>
    <meta charset="utf-8"/>
    <title>{league.title}</title>
    <style>
        body {{
            color: white;
            background-color:{league.background};
            margin:40px;
        }}
        {styles}
    </style>
    </head>


    <body>
        <div>
        <a href="../index.html">Go back</a>
            <h1>{league.comment}</h1>
            <span>{league.period}</span>
            <img src="{league.img}">
        </div>

        <div>
            <h3> Equipos <h3>
            {team_aggregates_values.to_html()}
            <h4> Team stats </h4>
            {team_aggregates_stats.to_html()}
        </div>

        <div>
            <h3> Clasificacion <h3>
            {classification_table.to_html()}
        </div>

        <div class="calendario">
            <h3> Calendario <h3>
            <div class="container">
            {calendario}

            </div>

            <h3> Calendario Equipos<h3>
            <div class="container">
            {html_calendario_equipos}

            </div>
        </div>

    <div>
    <h3> Estaditicas </h3>

    <h4> Touchdowns </h4>
    { touchdowns.head(5).to_html(index=False)}

    <h4> Passes </h4>
    { passes.head(5).to_html(index=False)}

    <h4> casualties </h4>
    { casualties.head(5).to_html(index=False)}

    <h4> MVPs </h4>
    { mvp.head(5).to_html(index=False)}

    <h4> interceptions </h4>
    { interceptions.head(5).to_html(index=False)}

    <h4> Most improved </h4>
    { pe.head(5).to_html(index=False)}

    <h4> Most actions </h4>
    <span> action = touchdowns + passes + casualties + interceptions </span>
    { actions.head(5).to_html(index=False)}

    </div>

    </html></body>
    '''

    return html_web


data = ''

for league in leagues:
    data += f"""
    <a href="leagues/{league.folder}.html">
<div class="league_box">

     <h1>{league.title}</h1>
    <span>{league.period}</span>
    <img width="200px" src="leagues/{league.img}"</h1>
</div>
</a>
        """

index = f'''
<html>
<head>
<title>BB Leagues</title>
    <style>
       body {{
           background-color:#4e4858;
       }}

       .league_box {{
        border: 1px solid;
        padding: 10px;
        box-shadow: 5px 10px 18px #888888;
        height:300px;
        }}

        .league_box:hover {{
            opacity:0.6;
            background-color: yellow;
        }}

        .flexy {{
             display:flex;
        }}


        {styles}
    </style>
</head>
    <body>
    <h1>BB Leagues</h1>
        <div class="flexy">
            {data}
        </div>
    </body>
</html>
'''

for league in leagues:
    html_web = get_league_html(league)
    with open(f'docs/leagues/{league.folder}.html', 'w') as web:
        web.write(html_web)

with open('docs/index.html', 'w') as web:
    web.write(index)
