from fastapi import FastAPI
from service.api.api import main_router
import onnxruntime as rt

app = FastAPI(project_name = "Emotions Detection")
app.include_router(main_router)

providers = ['CPUExecutionProvider']
m_q = rt.InferenceSession(
        "Model/vit_quantized.onnx", providers=providers
    )


@app.get("/")
def root():
    return {"Human Emotions": "Detection"}