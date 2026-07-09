from fastapi  import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.responses import FileResponse
import joblib
import numpy as np
#  py -3.11 -m venv venv
#  venv\Scripts\activate
#  pip install "fastapi[standard]" pydantic joblib numpy
#  pip install scikit-learn
#  fastapi dev main.py
app = FastAPI()

model = joblib.load("milk_quality_rf.pkl")

scaler = joblib.load("scaler.pkl")
app.mount("/assets", StaticFiles(directory="dist/assets"), name="assets")
@app.get("/{full_path:path}")
async def serve_react(full_path: str):
    return FileResponse("dist/index.html")
class MilkData(BaseModel):
    pH: float
    Temprature: float
    Taste: int
    Odor: int
    Fat: int
    Turbidity: int
    Colour: int
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Cho phép tất cả các nguồn truy cập
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
def predict(data: MilkData):

    x = np.array([[
        data.pH,
        data.Temprature,
        data.Taste,
        data.Odor,
        data.Fat,
        data.Turbidity,
        data.Colour
    ]])

    x = scaler.transform(x)

    pred = model.predict(x)[0]

    label_map = {
        0: "Low",
        1: "Medium",
        2: "High"
    }

    return {
        "prediction": int(pred),
        "grade": label_map[int(pred)]
    }