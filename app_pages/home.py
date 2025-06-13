from api_client import get_charts_data
import streamlit as st
from typing import TypedDict, Dict
from streamlit_apexjs import st_apexcharts

data = get_charts_data()[1]

housing_prices = data["housing_prices"]
if not housing_prices:
    st.error("Brak danych do wyświetlenia.")
else:
    st.subheader("Ceny mieszkań")

    # housing_prices = {"2011-Q1":{"OGÓŁEM":27500,"indywidualne":18191,"sprzedaż lub wynajem":7964,"spółdzielcze":414,"pozostałe":931},"2011-Q2":{"OGÓŁEM":27068,"indywidualne":15848,"sprzedaż lub wynajem":9920,"spółdzielcze":640,"pozostałe":660},"2011-Q3":{"OGÓŁEM":32271,"indywidualne":17688,"sprzedaż lub wynajem":11778,"spółdzielcze":1246,"pozostałe":1559},"2011-Q4":{"OGÓŁEM":44115,"indywidualne":21826,"sprzedaż lub wynajem":19152,"spółdzielcze":1486,"pozostałe":1651},"2012-Q1":{"OGÓŁEM":36292,"indywidualne":20534,"sprzedaż lub wynajem":13521,"spółdzielcze":1147,"pozostałe":1090},"2012-Q2":{"OGÓŁEM":31551,"indywidualne":17070,"sprzedaż lub wynajem":13119,"spółdzielcze":985,"pozostałe":377},"2012-Q3":{"OGÓŁEM":36962,"indywidualne":19523,"sprzedaż lub wynajem":15341,"spółdzielcze":876,"pozostałe":1222},"2012-Q4":{"OGÓŁEM":48099,"indywidualne":23923,"sprzedaż lub wynajem":21605,"spółdzielcze":1186,"pozostałe":1385},"2013-Q1":{"OGÓŁEM":37155,"indywidualne":21172,"sprzedaż lub wynajem":14287,"spółdzielcze":1047,"pozostałe":649},"2013-Q2":{"OGÓŁEM":30807,"indywidualne":18839,"sprzedaż lub wynajem":10779,"spółdzielcze":531,"pozostałe":658},"2013-Q3":{"OGÓŁEM":34140,"indywidualne":19295,"sprzedaż lub wynajem":12539,"spółdzielcze":1081,"pozostałe":1225},"2013-Q4":{"OGÓŁEM":43034,"indywidualne":21922,"sprzedaż lub wynajem":18842,"spółdzielcze":834,"pozostałe":1436},"2014-Q1":{"OGÓŁEM":35562,"indywidualne":20399,"sprzedaż lub wynajem":13204,"spółdzielcze":1012,"pozostałe":947},"2014-Q2":{"OGÓŁEM":30856,"indywidualne":17420,"sprzedaż lub wynajem":12397,"spółdzielcze":380,"pozostałe":659},"2014-Q3":{"OGÓŁEM":33724,"indywidualne":17598,"sprzedaż lub wynajem":13646,"spółdzielcze":1152,"pozostałe":1328},"2014-Q4":{"OGÓŁEM":43024,"indywidualne":20712,"sprzedaż lub wynajem":19818,"spółdzielcze":946,"pozostałe":1548},"2015-Q1":{"OGÓŁEM":31703,"indywidualne":19698,"sprzedaż lub wynajem":11182,"spółdzielcze":244,"pozostałe":579},"2015-Q2":{"OGÓŁEM":32263,"indywidualne":18844,"sprzedaż lub wynajem":12714,"spółdzielcze":267,"pozostałe":438},"2015-Q3":{"OGÓŁEM":37365,"indywidualne":19256,"sprzedaż lub wynajem":16469,"spółdzielcze":684,"pozostałe":956},"2015-Q4":{"OGÓŁEM":46380,"indywidualne":21960,"sprzedaż lub wynajem":22055,"spółdzielcze":920,"pozostałe":1445},"2016-Q1":{"OGÓŁEM":37423,"indywidualne":18911,"sprzedaż lub wynajem":17319,"spółdzielcze":629,"pozostałe":564},"2016-Q2":{"OGÓŁEM":36318,"indywidualne":18079,"sprzedaż lub wynajem":17450,"spółdzielcze":387,"pozostałe":402},"2016-Q3":{"OGÓŁEM":38276,"indywidualne":18147,"sprzedaż lub wynajem":18562,"spółdzielcze":753,"pozostałe":814},"2016-Q4":{"OGÓŁEM":51308,"indywidualne":22925,"sprzedaż lub wynajem":25829,"spółdzielcze":938,"pozostałe":1616},"2017-Q1":{"OGÓŁEM":40587,"indywidualne":20616,"sprzedaż lub wynajem":18959,"spółdzielcze":569,"pozostałe":443},"2017-Q2":{"OGÓŁEM":37792,"indywidualne":18800,"sprzedaż lub wynajem":18546,"spółdzielcze":234,"pozostałe":212},"2017-Q3":{"OGÓŁEM":45964,"indywidualne":19901,"sprzedaż lub wynajem":23838,"spółdzielcze":735,"pozostałe":1490},"2017-Q4":{"OGÓŁEM":53915,"indywidualne":23362,"sprzedaż lub wynajem":28474,"spółdzielcze":838,"pozostałe":1241},"2018-Q1":{"OGÓŁEM":44634,"indywidualne":18041,"sprzedaż lub wynajem":25548,"spółdzielcze":489,"pozostałe":556},"2018-Q2":{"OGÓŁEM":38152,"indywidualne":14614,"sprzedaż lub wynajem":22480,"spółdzielcze":515,"pozostałe":543},"2018-Q3":{"OGÓŁEM":46966,"indywidualne":15511,"sprzedaż lub wynajem":29726,"spółdzielcze":771,"pozostałe":958},"2018-Q4":{"OGÓŁEM":55311,"indywidualne":18054,"sprzedaż lub wynajem":34563,"spółdzielcze":1249,"pozostałe":1444},"2019-Q1":{"OGÓŁEM":47417,"indywidualne":17251,"sprzedaż lub wynajem":28768,"spółdzielcze":667,"pozostałe":731},"2019-Q2":{"OGÓŁEM":47059,"indywidualne":15846,"sprzedaż lub wynajem":30002,"spółdzielcze":287,"pozostałe":924},"2019-Q3":{"OGÓŁEM":51240,"indywidualne":16690,"sprzedaż lub wynajem":32401,"spółdzielcze":556,"pozostałe":1593},"2019-Q4":{"OGÓŁEM":61709,"indywidualne":19439,"sprzedaż lub wynajem":40264,"spółdzielcze":657,"pozostałe":1349},"2020-Q1":{"OGÓŁEM":49577,"indywidualne":17938,"sprzedaż lub wynajem":30737,"spółdzielcze":404,"pozostałe":498},"2020-Q2":{"OGÓŁEM":47495,"indywidualne":14730,"sprzedaż lub wynajem":31896,"spółdzielcze":257,"pozostałe":612},"2020-Q3":{"OGÓŁEM":59200,"indywidualne":19933,"sprzedaż lub wynajem":38471,"spółdzielcze":334,"pozostałe":462},"2020-Q4":{"OGÓŁEM":64559,"indywidualne":21390,"sprzedaż lub wynajem":41587,"spółdzielcze":503,"pozostałe":1079},"2021-Q1":{"OGÓŁEM":53066,"indywidualne":21441,"sprzedaż lub wynajem":30515,"spółdzielcze":521,"pozostałe":589},"2021-Q2":{"OGÓŁEM":52378,"indywidualne":20898,"sprzedaż lub wynajem":30131,"spółdzielcze":732,"pozostałe":617},"2021-Q3":{"OGÓŁEM":58652,"indywidualne":21225,"sprzedaż lub wynajem":36565,"spółdzielcze":124,"pozostałe":738},"2021-Q4":{"OGÓŁEM":70584,"indywidualne":24566,"sprzedaż lub wynajem":44730,"spółdzielcze":642,"pozostałe":646},"2022-Q1":{"OGÓŁEM":54667,"indywidualne":23893,"sprzedaż lub wynajem":29610,"spółdzielcze":568,"pozostałe":596},"2022-Q2":{"OGÓŁEM":54528,"indywidualne":20953,"sprzedaż lub wynajem":33148,"spółdzielcze":175,"pozostałe":252},"2022-Q3":{"OGÓŁEM":57808,"indywidualne":20368,"sprzedaż lub wynajem":36858,"spółdzielcze":201,"pozostałe":381},"2022-Q4":{"OGÓŁEM":71487,"indywidualne":25520,"sprzedaż lub wynajem":44355,"spółdzielcze":569,"pozostałe":1043},"2023-Q1":{"OGÓŁEM":55051,"indywidualne":23521,"sprzedaż lub wynajem":30417,"spółdzielcze":427,"pozostałe":686},"2023-Q2":{"OGÓŁEM":56809,"indywidualne":22026,"sprzedaż lub wynajem":34082,"spółdzielcze":152,"pozostałe":549},"2023-Q3":{"OGÓŁEM":48983,"indywidualne":15274,"sprzedaż lub wynajem":32436,"spółdzielcze":270,"pozostałe":1003},"2023-Q4":{"OGÓŁEM":60416,"indywidualne":18544,"sprzedaż lub wynajem":40648,"spółdzielcze":157,"pozostałe":1067},"2024-Q1":{"OGÓŁEM":48286,"indywidualne":18087,"sprzedaż lub wynajem":29106,"spółdzielcze":56,"pozostałe":1037},"2024-Q2":{"OGÓŁEM":47329,"indywidualne":16573,"sprzedaż lub wynajem":29556,"spółdzielcze":244,"pozostałe":956},"2024-Q3":{"OGÓŁEM":49499,"indywidualne":16854,"sprzedaż lub wynajem":30729,"spółdzielcze":574,"pozostałe":1342},"2024-Q4":{"OGÓŁEM":54817,"indywidualne":18267,"sprzedaż lub wynajem":34956,"spółdzielcze":386,"pozostałe":1208}}

    columns = ["ogółem", "rynek pierwotny", "rynek wtórny"]
    series = []
    for column in columns:
        sub_series = []
        for key in housing_prices:
            sub_series.append(housing_prices[key][column])

        series.append({
            "name": column,
            "data": sub_series,
        })

    labels = list(housing_prices.keys())

    st_apexcharts(
        {
            "chart": {
                "toolbar": {
                    "show": False
                }
            },
            "labels": labels,
            "legend": {
                "show": True,
                "position": "bottom",
            },
            "stroke": {
                "curve": 'smooth',
            },
            "tooltip": {
                "theme": "dark",
                "y": {
                    "formatter": "(val) => val + '%'"
                }
            }
        },
        series,
        'line',
        '600',
        "Zmiany cen mieszkań w poszczególnych kwartałach (%)"
    )

building_statistics = data["building_statistics"]
if not building_statistics:
    st.error("Brak danych do wyświetlenia.")
else:
    st.subheader("Dostępność mieszkań")

    # building_statistics = {"2011-Q1":{"OGÓŁEM":27500,"indywidualne":18191,"sprzedaż lub wynajem":7964,"spółdzielcze":414,"pozostałe":931},"2011-Q2":{"OGÓŁEM":27068,"indywidualne":15848,"sprzedaż lub wynajem":9920,"spółdzielcze":640,"pozostałe":660},"2011-Q3":{"OGÓŁEM":32271,"indywidualne":17688,"sprzedaż lub wynajem":11778,"spółdzielcze":1246,"pozostałe":1559},"2011-Q4":{"OGÓŁEM":44115,"indywidualne":21826,"sprzedaż lub wynajem":19152,"spółdzielcze":1486,"pozostałe":1651},"2012-Q1":{"OGÓŁEM":36292,"indywidualne":20534,"sprzedaż lub wynajem":13521,"spółdzielcze":1147,"pozostałe":1090},"2012-Q2":{"OGÓŁEM":31551,"indywidualne":17070,"sprzedaż lub wynajem":13119,"spółdzielcze":985,"pozostałe":377},"2012-Q3":{"OGÓŁEM":36962,"indywidualne":19523,"sprzedaż lub wynajem":15341,"spółdzielcze":876,"pozostałe":1222},"2012-Q4":{"OGÓŁEM":48099,"indywidualne":23923,"sprzedaż lub wynajem":21605,"spółdzielcze":1186,"pozostałe":1385},"2013-Q1":{"OGÓŁEM":37155,"indywidualne":21172,"sprzedaż lub wynajem":14287,"spółdzielcze":1047,"pozostałe":649},"2013-Q2":{"OGÓŁEM":30807,"indywidualne":18839,"sprzedaż lub wynajem":10779,"spółdzielcze":531,"pozostałe":658},"2013-Q3":{"OGÓŁEM":34140,"indywidualne":19295,"sprzedaż lub wynajem":12539,"spółdzielcze":1081,"pozostałe":1225},"2013-Q4":{"OGÓŁEM":43034,"indywidualne":21922,"sprzedaż lub wynajem":18842,"spółdzielcze":834,"pozostałe":1436},"2014-Q1":{"OGÓŁEM":35562,"indywidualne":20399,"sprzedaż lub wynajem":13204,"spółdzielcze":1012,"pozostałe":947},"2014-Q2":{"OGÓŁEM":30856,"indywidualne":17420,"sprzedaż lub wynajem":12397,"spółdzielcze":380,"pozostałe":659},"2014-Q3":{"OGÓŁEM":33724,"indywidualne":17598,"sprzedaż lub wynajem":13646,"spółdzielcze":1152,"pozostałe":1328},"2014-Q4":{"OGÓŁEM":43024,"indywidualne":20712,"sprzedaż lub wynajem":19818,"spółdzielcze":946,"pozostałe":1548},"2015-Q1":{"OGÓŁEM":31703,"indywidualne":19698,"sprzedaż lub wynajem":11182,"spółdzielcze":244,"pozostałe":579},"2015-Q2":{"OGÓŁEM":32263,"indywidualne":18844,"sprzedaż lub wynajem":12714,"spółdzielcze":267,"pozostałe":438},"2015-Q3":{"OGÓŁEM":37365,"indywidualne":19256,"sprzedaż lub wynajem":16469,"spółdzielcze":684,"pozostałe":956},"2015-Q4":{"OGÓŁEM":46380,"indywidualne":21960,"sprzedaż lub wynajem":22055,"spółdzielcze":920,"pozostałe":1445},"2016-Q1":{"OGÓŁEM":37423,"indywidualne":18911,"sprzedaż lub wynajem":17319,"spółdzielcze":629,"pozostałe":564},"2016-Q2":{"OGÓŁEM":36318,"indywidualne":18079,"sprzedaż lub wynajem":17450,"spółdzielcze":387,"pozostałe":402},"2016-Q3":{"OGÓŁEM":38276,"indywidualne":18147,"sprzedaż lub wynajem":18562,"spółdzielcze":753,"pozostałe":814},"2016-Q4":{"OGÓŁEM":51308,"indywidualne":22925,"sprzedaż lub wynajem":25829,"spółdzielcze":938,"pozostałe":1616},"2017-Q1":{"OGÓŁEM":40587,"indywidualne":20616,"sprzedaż lub wynajem":18959,"spółdzielcze":569,"pozostałe":443},"2017-Q2":{"OGÓŁEM":37792,"indywidualne":18800,"sprzedaż lub wynajem":18546,"spółdzielcze":234,"pozostałe":212},"2017-Q3":{"OGÓŁEM":45964,"indywidualne":19901,"sprzedaż lub wynajem":23838,"spółdzielcze":735,"pozostałe":1490},"2017-Q4":{"OGÓŁEM":53915,"indywidualne":23362,"sprzedaż lub wynajem":28474,"spółdzielcze":838,"pozostałe":1241},"2018-Q1":{"OGÓŁEM":44634,"indywidualne":18041,"sprzedaż lub wynajem":25548,"spółdzielcze":489,"pozostałe":556},"2018-Q2":{"OGÓŁEM":38152,"indywidualne":14614,"sprzedaż lub wynajem":22480,"spółdzielcze":515,"pozostałe":543},"2018-Q3":{"OGÓŁEM":46966,"indywidualne":15511,"sprzedaż lub wynajem":29726,"spółdzielcze":771,"pozostałe":958},"2018-Q4":{"OGÓŁEM":55311,"indywidualne":18054,"sprzedaż lub wynajem":34563,"spółdzielcze":1249,"pozostałe":1444},"2019-Q1":{"OGÓŁEM":47417,"indywidualne":17251,"sprzedaż lub wynajem":28768,"spółdzielcze":667,"pozostałe":731},"2019-Q2":{"OGÓŁEM":47059,"indywidualne":15846,"sprzedaż lub wynajem":30002,"spółdzielcze":287,"pozostałe":924},"2019-Q3":{"OGÓŁEM":51240,"indywidualne":16690,"sprzedaż lub wynajem":32401,"spółdzielcze":556,"pozostałe":1593},"2019-Q4":{"OGÓŁEM":61709,"indywidualne":19439,"sprzedaż lub wynajem":40264,"spółdzielcze":657,"pozostałe":1349},"2020-Q1":{"OGÓŁEM":49577,"indywidualne":17938,"sprzedaż lub wynajem":30737,"spółdzielcze":404,"pozostałe":498},"2020-Q2":{"OGÓŁEM":47495,"indywidualne":14730,"sprzedaż lub wynajem":31896,"spółdzielcze":257,"pozostałe":612},"2020-Q3":{"OGÓŁEM":59200,"indywidualne":19933,"sprzedaż lub wynajem":38471,"spółdzielcze":334,"pozostałe":462},"2020-Q4":{"OGÓŁEM":64559,"indywidualne":21390,"sprzedaż lub wynajem":41587,"spółdzielcze":503,"pozostałe":1079},"2021-Q1":{"OGÓŁEM":53066,"indywidualne":21441,"sprzedaż lub wynajem":30515,"spółdzielcze":521,"pozostałe":589},"2021-Q2":{"OGÓŁEM":52378,"indywidualne":20898,"sprzedaż lub wynajem":30131,"spółdzielcze":732,"pozostałe":617},"2021-Q3":{"OGÓŁEM":58652,"indywidualne":21225,"sprzedaż lub wynajem":36565,"spółdzielcze":124,"pozostałe":738},"2021-Q4":{"OGÓŁEM":70584,"indywidualne":24566,"sprzedaż lub wynajem":44730,"spółdzielcze":642,"pozostałe":646},"2022-Q1":{"OGÓŁEM":54667,"indywidualne":23893,"sprzedaż lub wynajem":29610,"spółdzielcze":568,"pozostałe":596},"2022-Q2":{"OGÓŁEM":54528,"indywidualne":20953,"sprzedaż lub wynajem":33148,"spółdzielcze":175,"pozostałe":252},"2022-Q3":{"OGÓŁEM":57808,"indywidualne":20368,"sprzedaż lub wynajem":36858,"spółdzielcze":201,"pozostałe":381},"2022-Q4":{"OGÓŁEM":71487,"indywidualne":25520,"sprzedaż lub wynajem":44355,"spółdzielcze":569,"pozostałe":1043},"2023-Q1":{"OGÓŁEM":55051,"indywidualne":23521,"sprzedaż lub wynajem":30417,"spółdzielcze":427,"pozostałe":686},"2023-Q2":{"OGÓŁEM":56809,"indywidualne":22026,"sprzedaż lub wynajem":34082,"spółdzielcze":152,"pozostałe":549},"2023-Q3":{"OGÓŁEM":48983,"indywidualne":15274,"sprzedaż lub wynajem":32436,"spółdzielcze":270,"pozostałe":1003},"2023-Q4":{"OGÓŁEM":60416,"indywidualne":18544,"sprzedaż lub wynajem":40648,"spółdzielcze":157,"pozostałe":1067},"2024-Q1":{"OGÓŁEM":48286,"indywidualne":18087,"sprzedaż lub wynajem":29106,"spółdzielcze":56,"pozostałe":1037},"2024-Q2":{"OGÓŁEM":47329,"indywidualne":16573,"sprzedaż lub wynajem":29556,"spółdzielcze":244,"pozostałe":956},"2024-Q3":{"OGÓŁEM":49499,"indywidualne":16854,"sprzedaż lub wynajem":30729,"spółdzielcze":574,"pozostałe":1342},"2024-Q4":{"OGÓŁEM":54817,"indywidualne":18267,"sprzedaż lub wynajem":34956,"spółdzielcze":386,"pozostałe":1208}}

    columns = ["OGÓŁEM", "indywidualne", "sprzedaż lub wynajem"]

    series = []
    for column in columns:
        sub_series = []
        for key in building_statistics:
            sub_series.append(building_statistics[key][column])

        series.append({
            "name": column,
            "data": sub_series,
        })

    labels = list(building_statistics.keys())

    st_apexcharts(
        {
            "chart": {
                "id": "lol3",
                "toolbar": {
                    "show": False
                }
            },
            "tooltip": {
                "theme": "dark"
            },
            "labels": labels,
            "legend": {
                "show": True,
                "position": "bottom",
            },
            "stroke": {
                "curve": 'smooth',
            },
            "yaxis": {
                "min": 0  # <-- dodaj tę linię, aby oś Y zaczynała się od zera
            },
        },
        series,
        'line',
        '600',
        "Liczba mieszkań w poszczególnych kwartałach"
    )

    st.subheader("Dostępność mieszkań")

    # building_statistics = {"2011-Q1":{"OGÓŁEM":27500,"indywidualne":18191,"sprzedaż lub wynajem":7964,"spółdzielcze":414,"pozostałe":931},"2011-Q2":{"OGÓŁEM":27068,"indywidualne":15848,"sprzedaż lub wynajem":9920,"spółdzielcze":640,"pozostałe":660},"2011-Q3":{"OGÓŁEM":32271,"indywidualne":17688,"sprzedaż lub wynajem":11778,"spółdzielcze":1246,"pozostałe":1559},"2011-Q4":{"OGÓŁEM":44115,"indywidualne":21826,"sprzedaż lub wynajem":19152,"spółdzielcze":1486,"pozostałe":1651},"2012-Q1":{"OGÓŁEM":36292,"indywidualne":20534,"sprzedaż lub wynajem":13521,"spółdzielcze":1147,"pozostałe":1090},"2012-Q2":{"OGÓŁEM":31551,"indywidualne":17070,"sprzedaż lub wynajem":13119,"spółdzielcze":985,"pozostałe":377},"2012-Q3":{"OGÓŁEM":36962,"indywidualne":19523,"sprzedaż lub wynajem":15341,"spółdzielcze":876,"pozostałe":1222},"2012-Q4":{"OGÓŁEM":48099,"indywidualne":23923,"sprzedaż lub wynajem":21605,"spółdzielcze":1186,"pozostałe":1385},"2013-Q1":{"OGÓŁEM":37155,"indywidualne":21172,"sprzedaż lub wynajem":14287,"spółdzielcze":1047,"pozostałe":649},"2013-Q2":{"OGÓŁEM":30807,"indywidualne":18839,"sprzedaż lub wynajem":10779,"spółdzielcze":531,"pozostałe":658},"2013-Q3":{"OGÓŁEM":34140,"indywidualne":19295,"sprzedaż lub wynajem":12539,"spółdzielcze":1081,"pozostałe":1225},"2013-Q4":{"OGÓŁEM":43034,"indywidualne":21922,"sprzedaż lub wynajem":18842,"spółdzielcze":834,"pozostałe":1436},"2014-Q1":{"OGÓŁEM":35562,"indywidualne":20399,"sprzedaż lub wynajem":13204,"spółdzielcze":1012,"pozostałe":947},"2014-Q2":{"OGÓŁEM":30856,"indywidualne":17420,"sprzedaż lub wynajem":12397,"spółdzielcze":380,"pozostałe":659},"2014-Q3":{"OGÓŁEM":33724,"indywidualne":17598,"sprzedaż lub wynajem":13646,"spółdzielcze":1152,"pozostałe":1328},"2014-Q4":{"OGÓŁEM":43024,"indywidualne":20712,"sprzedaż lub wynajem":19818,"spółdzielcze":946,"pozostałe":1548},"2015-Q1":{"OGÓŁEM":31703,"indywidualne":19698,"sprzedaż lub wynajem":11182,"spółdzielcze":244,"pozostałe":579},"2015-Q2":{"OGÓŁEM":32263,"indywidualne":18844,"sprzedaż lub wynajem":12714,"spółdzielcze":267,"pozostałe":438},"2015-Q3":{"OGÓŁEM":37365,"indywidualne":19256,"sprzedaż lub wynajem":16469,"spółdzielcze":684,"pozostałe":956},"2015-Q4":{"OGÓŁEM":46380,"indywidualne":21960,"sprzedaż lub wynajem":22055,"spółdzielcze":920,"pozostałe":1445},"2016-Q1":{"OGÓŁEM":37423,"indywidualne":18911,"sprzedaż lub wynajem":17319,"spółdzielcze":629,"pozostałe":564},"2016-Q2":{"OGÓŁEM":36318,"indywidualne":18079,"sprzedaż lub wynajem":17450,"spółdzielcze":387,"pozostałe":402},"2016-Q3":{"OGÓŁEM":38276,"indywidualne":18147,"sprzedaż lub wynajem":18562,"spółdzielcze":753,"pozostałe":814},"2016-Q4":{"OGÓŁEM":51308,"indywidualne":22925,"sprzedaż lub wynajem":25829,"spółdzielcze":938,"pozostałe":1616},"2017-Q1":{"OGÓŁEM":40587,"indywidualne":20616,"sprzedaż lub wynajem":18959,"spółdzielcze":569,"pozostałe":443},"2017-Q2":{"OGÓŁEM":37792,"indywidualne":18800,"sprzedaż lub wynajem":18546,"spółdzielcze":234,"pozostałe":212},"2017-Q3":{"OGÓŁEM":45964,"indywidualne":19901,"sprzedaż lub wynajem":23838,"spółdzielcze":735,"pozostałe":1490},"2017-Q4":{"OGÓŁEM":53915,"indywidualne":23362,"sprzedaż lub wynajem":28474,"spółdzielcze":838,"pozostałe":1241},"2018-Q1":{"OGÓŁEM":44634,"indywidualne":18041,"sprzedaż lub wynajem":25548,"spółdzielcze":489,"pozostałe":556},"2018-Q2":{"OGÓŁEM":38152,"indywidualne":14614,"sprzedaż lub wynajem":22480,"spółdzielcze":515,"pozostałe":543},"2018-Q3":{"OGÓŁEM":46966,"indywidualne":15511,"sprzedaż lub wynajem":29726,"spółdzielcze":771,"pozostałe":958},"2018-Q4":{"OGÓŁEM":55311,"indywidualne":18054,"sprzedaż lub wynajem":34563,"spółdzielcze":1249,"pozostałe":1444},"2019-Q1":{"OGÓŁEM":47417,"indywidualne":17251,"sprzedaż lub wynajem":28768,"spółdzielcze":667,"pozostałe":731},"2019-Q2":{"OGÓŁEM":47059,"indywidualne":15846,"sprzedaż lub wynajem":30002,"spółdzielcze":287,"pozostałe":924},"2019-Q3":{"OGÓŁEM":51240,"indywidualne":16690,"sprzedaż lub wynajem":32401,"spółdzielcze":556,"pozostałe":1593},"2019-Q4":{"OGÓŁEM":61709,"indywidualne":19439,"sprzedaż lub wynajem":40264,"spółdzielcze":657,"pozostałe":1349},"2020-Q1":{"OGÓŁEM":49577,"indywidualne":17938,"sprzedaż lub wynajem":30737,"spółdzielcze":404,"pozostałe":498},"2020-Q2":{"OGÓŁEM":47495,"indywidualne":14730,"sprzedaż lub wynajem":31896,"spółdzielcze":257,"pozostałe":612},"2020-Q3":{"OGÓŁEM":59200,"indywidualne":19933,"sprzedaż lub wynajem":38471,"spółdzielcze":334,"pozostałe":462},"2020-Q4":{"OGÓŁEM":64559,"indywidualne":21390,"sprzedaż lub wynajem":41587,"spółdzielcze":503,"pozostałe":1079},"2021-Q1":{"OGÓŁEM":53066,"indywidualne":21441,"sprzedaż lub wynajem":30515,"spółdzielcze":521,"pozostałe":589},"2021-Q2":{"OGÓŁEM":52378,"indywidualne":20898,"sprzedaż lub wynajem":30131,"spółdzielcze":732,"pozostałe":617},"2021-Q3":{"OGÓŁEM":58652,"indywidualne":21225,"sprzedaż lub wynajem":36565,"spółdzielcze":124,"pozostałe":738},"2021-Q4":{"OGÓŁEM":70584,"indywidualne":24566,"sprzedaż lub wynajem":44730,"spółdzielcze":642,"pozostałe":646},"2022-Q1":{"OGÓŁEM":54667,"indywidualne":23893,"sprzedaż lub wynajem":29610,"spółdzielcze":568,"pozostałe":596},"2022-Q2":{"OGÓŁEM":54528,"indywidualne":20953,"sprzedaż lub wynajem":33148,"spółdzielcze":175,"pozostałe":252},"2022-Q3":{"OGÓŁEM":57808,"indywidualne":20368,"sprzedaż lub wynajem":36858,"spółdzielcze":201,"pozostałe":381},"2022-Q4":{"OGÓŁEM":71487,"indywidualne":25520,"sprzedaż lub wynajem":44355,"spółdzielcze":569,"pozostałe":1043},"2023-Q1":{"OGÓŁEM":55051,"indywidualne":23521,"sprzedaż lub wynajem":30417,"spółdzielcze":427,"pozostałe":686},"2023-Q2":{"OGÓŁEM":56809,"indywidualne":22026,"sprzedaż lub wynajem":34082,"spółdzielcze":152,"pozostałe":549},"2023-Q3":{"OGÓŁEM":48983,"indywidualne":15274,"sprzedaż lub wynajem":32436,"spółdzielcze":270,"pozostałe":1003},"2023-Q4":{"OGÓŁEM":60416,"indywidualne":18544,"sprzedaż lub wynajem":40648,"spółdzielcze":157,"pozostałe":1067},"2024-Q1":{"OGÓŁEM":48286,"indywidualne":18087,"sprzedaż lub wynajem":29106,"spółdzielcze":56,"pozostałe":1037},"2024-Q2":{"OGÓŁEM":47329,"indywidualne":16573,"sprzedaż lub wynajem":29556,"spółdzielcze":244,"pozostałe":956},"2024-Q3":{"OGÓŁEM":49499,"indywidualne":16854,"sprzedaż lub wynajem":30729,"spółdzielcze":574,"pozostałe":1342},"2024-Q4":{"OGÓŁEM":54817,"indywidualne":18267,"sprzedaż lub wynajem":34956,"spółdzielcze":386,"pozostałe":1208}}

    columns = ["spółdzielcze", "pozostałe"]

    series = []
    for column in columns:
        sub_series = []
        for key in building_statistics:
            sub_series.append(building_statistics[key][column])

        series.append({
            "name": column,
            "data": sub_series,
        })

    labels = list(building_statistics.keys())

    st_apexcharts(
        {
            "chart": {
                "id": "lol3",
                "toolbar": {
                    "show": False
                },
            },
            "tooltip": {
                "theme": "dark"
            },
            "labels": labels,
            "legend": {
                "show": True,
                "position": "bottom",
            },
            "stroke": {
                "curve": 'smooth',
            },
            "yaxis": {
                "min": 0  # <-- dodaj tę linię, aby oś Y zaczynała się od zera
            },
        },
        series,
        'line',
        '600',
        "Liczba mieszkań w poszczególnych kwartałach"
    )
