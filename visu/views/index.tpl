<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>CitizenWatt</title>
        <link rel="stylesheet" href="{{ get_url('static', filename='css/normalize.css') }}">
        <link rel="stylesheet" href="{{ get_url('static', filename='css/style.css') }}">
    </head>

    <body>
        <div id="page">
            <header>
                <a href="index.html"><img src="{{ get_url('static', filename='img/logo.png') }}" alt="Logo CitizenWatt"/></a>

                <div id="menu">
                    <ul>
                        <li><a href="index.html">Accueil</a></li>
                        <li><a href="">Ma conso</a></li>
                        <li><a href="">Archives</a></li>
                        <li><a href="">Guides</a></li>
                        <li><a href="">À propos</a></li>
                    </ul>
                </div>
            </header>

            <main>
                <div id="overview">
                    <div>
                        <p id="now" class="blurry red">---W</p>
                        <p>Consommation actuelle</p>
                    </div>
                    <div>
                        <p id="day" class="blurry orange">---kWh (---€)</p>
                        <p>Consommation totale</p>
                    </div>
                    <!--
                    <div>
                        <p id="week" class="blurry yellow">80W</p>
                        <p>Moyenne cette semaine</p>
                    </div>
                    -->
                </div>

                <div id="graph">
                    <div id="graph_vertical_axis"></div>
                    <hr style="bottom:33.3%"/>
                    <hr style="bottom:66.7%"/>
                    <div id="graph_values">
                    </div>
                </div>

                <p style="text-align: center;">Abonnement EDF Tarif Bleu 06 kVA.</p>
            </main>

            <footer>
                <p>Licence GNU GPL | <a href="http://citoyenscapteurs.net/">Citoyens Capteurs</a></p>
            </footer>
        </div>

        <script src="{{ get_url('static', filename='js/graph.js') }}"></script>
    </body>
</html>

