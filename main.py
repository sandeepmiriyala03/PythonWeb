from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.employee_controller import router as employee_router
from api.department_controller import router as department_router

app = FastAPI(
    title="YuktishaalaaAI API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    employee_router
)

app.include_router(
    department_router
)