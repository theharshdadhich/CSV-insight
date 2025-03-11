from fastapi import APIRouter, HTTPException
from models.plot import PlotRequest
from services.plot_service import generate_plot

router = APIRouter()

@router.post("/plot/")
async def plot_graph(request: PlotRequest):
    try:
        return generate_plot(request.x_column, request.y_column, request.plot_type)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))