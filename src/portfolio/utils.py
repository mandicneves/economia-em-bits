import plotly.express as px
import pandas as pd

def generate_forecast_plot():
    # Exemplo simples com dados fictícios
    data = pd.DataFrame({
        "mes": pd.date_range("2022-01-01", periods=12, freq="ME"),
        "inflacao_real": [0.3, 0.4, 0.25, 0.35, 0.45, 0.4, 0.5, 0.55, 0.6, 0.58, 0.62, 0.65],
        "inflacao_prevista": [0.28, 0.38, 0.3, 0.36, 0.43, 0.41, 0.48, 0.54, 0.61, 0.6, 0.63, 0.66]
    })
    fig = px.line(data, x="mes", y=["inflacao_real", "inflacao_prevista"], title="Inflação Real vs Prevista")
    return fig.to_html(full_html=False)
