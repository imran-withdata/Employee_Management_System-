from fastapi import FastAPI




app = FastAPI(title="Employee Management System(EMS)")



# .................connect routers/heath.py.......... 
from app.routers.health import router as health_router
# Added a health router with the /api/v1 prefix
app.include_router(health_router, prefix = "/api/v1")



