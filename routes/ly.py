from fastapi import APIRouter

ly = APIRouter()


@ly.get("/ly/ly/{ly}")
@ly.get("/light-year/light-year/{ly}")
async def LYtoLY(ly: float):
    return ly


@ly.get("/ly/km/{ly}")
@ly.get("/light-year/kilometer/{ly}")
async def LYtoKM(ly: float):
    return ly * 9460730472580.8


@ly.get("/ly/lm/{ly}")
@ly.get("/light-year/light-minute/{ly}")
async def LYtoLM(ly: float):
    return ly * 525960


@ly.get("/ly/ls/{ly}")
@ly.get("/light-year/light-second/{ly}")
async def LYtoLS(ly: float):
    return ly * 31557600


@ly.get("/ly/au/{ly}")
@ly.get("/light-year/astronomical-unit/{ly}")
async def LYtoAU(ly: float):
    return ly * 63241.07708426628


@ly.get("/ly/mi/{ly}")
@ly.get("/light-year/miles/{ly}")
async def LYtoMI(ly: float):
    return ly * 5878625373183.607730851825


@ly.get("/ly/pc/{ly}")
@ly.get("/light-year/parsec/{ly}")
async def LYtoPC(ly: float):
    return ly * 0.306601393786
