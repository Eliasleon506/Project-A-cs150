import pandas as pd
import plotly.express as px

from dash import Dash, dcc, html, Input, Output


df = pd.read_csv("WildFires.CSV")

df["Date"] = pd.to_datetime(df["Date"])

df = pd.DataFrame({
    "Date": df["Date"],
    "PM2.5": df["Daily Mean PM2.5 Concentration"],
    "AQI": df["Daily AQI Value"],
    "Location": df["Local Site Name"],
})

app = Dash(__name__)

app.layout = html.Div([
    html.Div(html.H1("Air Pollution related to the Thomas Fire", style={"textAlign": "center"})),
    html.Div(dcc.Graph(id="line-chart", figure = {})),

    ## Drop down from tweeter_app.py
    html.Div(
        dcc.Dropdown(
            id="my-dropdown",
            multi=True,
            options=[
                {"label": x, "value": x}
                for x in sorted(df["Location"].unique())
            ],
            value=["Santa Barbara"],
        )
    )
])

@app.callback(
    Output(component_id="line-chart", component_property="figure"),
    [Input(component_id="my-dropdown", component_property="value")],
)
##
## function from tweeter_app.py
def update_graph(value):
    if len(value) == 0:
        return {}
    else:
        df_filtered = df[df["Location"].isin(value)]
        fig = px.line(
            data_frame=df_filtered,
            x="Date",
            y="AQI",
            color="Location",
            labels={
                "AQI": "AQI",
                "Date": "Date",
                "PM2.5": "PM2.5",
            },
        )

        fig.add_shape(
        type = "line",
        x0="2017-12-04",
        x1="2017-12-04",
        y0=df["AQI"].min(),
        y1=df["AQI"].max(),
        line = dict(color="Orange", width=2, dash="dot"),
        name = "Thomas Fire starts")

        fig.add_annotation(
            x= "2017-12-04",
            y=df["AQI"].max(),
            text = "Start of Thomas Fire",
            arrowhead = 1
        )

        return fig







if __name__ == "__main__":
    app.run_server(debug=True)