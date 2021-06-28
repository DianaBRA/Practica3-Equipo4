e5rfrom fastapi  import  FasAPI
from fastapi.responses import HTMLResponse

app = FastAPI ()

@app.get("/", response_class=HTMLResponse)
async def mostrar_inicio() :
	 contenido_html = """
	 <html>
	 <head>
	     <title>EquipoX</title>
	  </head>
	  <body>
	      <h3>Bienvenidos</h3>
	      <p>Este sitio pertenece al EquipoX y mostrara los datos de los integrantes</p>
	      <a href="wilber.html"> wilber</a>
	   </body>
	   </html>
	   """
	   return HTMLResponse(content=contenido_html, Status_code=200)