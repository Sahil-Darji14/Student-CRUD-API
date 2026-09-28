from fastapi import FastAPI
from routes.student_routes import router

app = FastAPI(
    title="University Student CRUD API",
    description="FastAPI CRUD API using in-memory storage",
    version="1.0.0"
)

app.include_router(router)