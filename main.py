from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route

def home(request:Request):
    return JSONResponse({'hello': 'world'})
routes = [
    Route('/', endpoint=home),
]

app = Starlette(
    debug=True,
    routes=routes,
    # middleware=middleware
)
