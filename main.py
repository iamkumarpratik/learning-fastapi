from app import create_app
from uvicorn import run

app = create_app()

if __name__ == "__main__":
    run(app, port=5000)
