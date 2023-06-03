from starlette.applications import Starlette
from starlette.routing import Route
from controllers.user_controller import register
from database import SessionLocal


# Init application.
app = Starlette()
routes = [
    Route("/register", endpoint=register, methods=["POST"])
]

app = Starlette(routes=routes)
app.state.db = SessionLocal()

# Run application.
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
