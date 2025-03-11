import polars as pl
import io
import state  # ✅ Import the global df storage

def read_csv(file):
    file_bytes = file.file.read()
    state.df = pl.read_csv(io.BytesIO(file_bytes))  # ✅ Save to global storage

def get_columns():
    if state.df is None:
        raise ValueError("No CSV file uploaded.")
    return state.df.columns