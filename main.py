from fastapi import FastAPI
app  = FastAPI()


@app.get('/',description="this is our first route")
async def root():
    return {"message":"Hello World"}


@app.post("/")
async def root():
    return {"message":"hello from the post root"}

@app.put("/{id}")
async def root():
    return {"message":"hello from the put "}

