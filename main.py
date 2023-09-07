import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routes.au import au
from routes.km import km
from routes.lm import lm
from routes.ls import ls
from routes.ly import ly
from routes.mi import mi

app = FastAPI()
origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=origins,
    allow_credentials=True,
)


app.include_router(au)
app.include_router(km)
app.include_router(lm)
app.include_router(ls)
app.include_router(ly)
app.include_router(mi)

match __name__ == "__main__":
    case True:
        uvicorn.run("main:app", host="127.0.0.1", port=1818, workers=1, reload=True)
