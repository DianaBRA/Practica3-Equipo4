from fastapi  import  FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title = "FastAPI con Jinja2")

app.mount("/recursos", StaticFiles(directory="recursos"), name="recursos")

miPlantilla = Jinja2Templates(directory="plantillas")

@app.get("/inicio", response_class=HTMLResponse)
async def read_item(request: Request):
	return miPlantilla.TemplateResponse("index.html",{"request":request})