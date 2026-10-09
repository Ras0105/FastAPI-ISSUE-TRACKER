from fastapi import FastAPI
from app.routes.issues import router as issues_router
 
app=FastAPI()

@app.get("/health")
def health_check():
    return{"status":"ok"}

app.include_router(issues_router)