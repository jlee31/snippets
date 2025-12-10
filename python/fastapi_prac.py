from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World from joe"}

# run with source fastapi_prac/bin/activate
