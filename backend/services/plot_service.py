import plotly.express as px
import json
import state  # ✅ Import global df

def generate_plot(x_column, y_column, plot_type):
    if state.df is None:
        raise ValueError("No CSV file uploaded.")

    df_pandas = state.df.to_pandas()

    if x_column not in df_pandas.columns or y_column not in df_pandas.columns:
        raise ValueError("One or both column names are invalid.")

    if plot_type == "bar":
        fig = px.bar(df_pandas, x=x_column, y=y_column, title=f"Bar Chart: {x_column} vs {y_column}")
    elif plot_type == "line":
        fig = px.line(df_pandas, x=x_column, y=y_column, title=f"Line Graph: {x_column} vs {y_column}")
    elif plot_type == "scatter":
        fig = px.scatter(df_pandas, x=x_column, y=y_column, title=f"Scatter Plot: {x_column} vs {y_column}")
    elif plot_type == "histogram":
        fig = px.histogram(df_pandas, x=x_column, y=y_column, title=f"Histogram: {x_column} vs {y_column}")
    else:
        raise ValueError("Unsupported graph type.")

    return json.loads(fig.to_json())