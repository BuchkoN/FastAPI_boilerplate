from fastapi import FastAPI


def start_app() -> FastAPI:
    app = FastAPI(
        title="Simple FastAPI Chat",
        docks_url="/api/docs/",
        debug=True
    )
    return app
