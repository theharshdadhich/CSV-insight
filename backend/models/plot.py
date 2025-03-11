from pydantic import BaseModel

class PlotRequest(BaseModel):
    x_column: str
    y_column: str
    plot_type: str