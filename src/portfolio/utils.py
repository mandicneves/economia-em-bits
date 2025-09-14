import plotly.express as px
import pandas as pd
from portfolio.projects.forecasting.data_loader import load_inflation_data

def generate_forecast_plot():
    data = load_inflation_data()
    fig = px.line(data, x="data", y="valor", title="Inflação Real vs Prevista")
    return fig.to_html(full_html=False)

    #     "inflacao_real": [0.3, 0.4, 0.25, 0.35, 0.45, 0.4, 0.5, 0.55, 0.6, 0.58, 0.62, 0.65],
    #     "inflacao_prevista": [0.28, 0.38, 0.3, 0.36, 0.43, 0.41, 0.48, 0.54, 0.61, 0.6, 0.63, 0.66]
    # })
    # fig = px.line(data, x="mes", y=["inflacao_real", "inflacao_prevista"], title="Inflação Real vs Prevista")
    # return fig.to_html(full_html=False)
