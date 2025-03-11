from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from services.csv_service import read_csv

router = APIRouter()

@router.post("/upload/")
async def upload_csv(file: UploadFile = File(...)):
    try:
        read_csv(file)
        return JSONResponse(content={"message": "File uploaded successfully"})
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing CSV file: {str(e)}")