from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Hello from GitHub Actions"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/employee/{employee_id}")
def get_employee(employee_id: int):
    return {
        "id": employee_id,
        "name": "Amith",
        "role": "DevOps Engineer"
    }
