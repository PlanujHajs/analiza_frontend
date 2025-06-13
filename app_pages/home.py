from api_client import get_charts_data
import streamlit as st
from streamlit_apexjs import st_apexcharts

data = get_charts_data()[1]

housing_prices = data["housing_prices"]
if not housing_prices:
    st.error("Brak danych do wyświetlenia.")
else:
    st.subheader("Ceny mieszkań")

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
                "min": 0
            },
        },
        series,
        'line',
        '600',
        "Liczba mieszkań w poszczególnych kwartałach"
    )

    st.subheader("Dostępność mieszkań")

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
                "min": 0
            },
        },
        series,
        'line',
        '600',
        "Liczba mieszkań w poszczególnych kwartałach"
    )
