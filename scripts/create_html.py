from clasificacion import get_classification
from team_value import get_teams_aggregates
from calendario import get_calendario
from stats import get_stats


data_path = "tiburon_negro/partidos.csv"
players_path = "tiburon_negro/jugadores.csv"
teams_data_path = "tiburon_negro/equipos.csv"

(
    touchdowns,
    passes,
    interceptions,
    mvp,
    casualities,
    pe,
    actions,
    palyers_team_aggregates
) = get_stats(data_path=players_path)

calendario, html_calendario_equipos = get_calendario(partidos_path=data_path)
classification_table = get_classification(partidos_path=data_path)
team_aggregates_values, team_aggregates_stats = get_teams_aggregates(
    data_path=players_path,
    teams_data_path=teams_data_path,
    palyers_team_aggregates=palyers_team_aggregates
)

styles = '''

body {
    color: white;
    background-color:black;
    margin:40px;
    # padding:40px;
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

html_web = f'''

<html>
<head>
<title>Tiburon Negro</title>
<style>
    {styles}
</style>
</head>


<body>
    <div>
        <h1>La liga del tiburón negro</h1>
        <span>Septiembre - Octubre 2020</span>
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

<h4> Casualities </h4>
{ casualities.head(5).to_html(index=False)}

<h4> MVPs </h4>
{ mvp.head(5).to_html(index=False)}

<h4> interceptions </h4>
{ interceptions.head(5).to_html(index=False)}

<h4> Most improved </h4>
{ pe.head(5).to_html(index=False)}


<h4> Most actions </h4>
{ actions.head(5).to_html(index=False)}

</div>


</html></body>
'''

with open('docs/index.html', 'w') as web:
    web.write(html_web)
