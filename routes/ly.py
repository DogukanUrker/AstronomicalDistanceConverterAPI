from fastapi import APIRouter

ly = APIRouter()


@ly.get("/ly/km/{ly}")
async def LYtoKM(ly: int):
    return ly * 9460730472580.8


@ly.get("/ly/lm/{ly}")
async def LYtoLM(ly: int):
    return ly * 525960


@ly.get("/ly/ls/{ly}")
async def LYtoLS(ly: int):
    return ly * 31557600


@ly.get("/ly/au/{ly}")
async def LYtoAU(ly: int):
    return ly * 63241.07708426628


@ly.get("/ly/mi/{ly}")
async def LYtoMI(ly: int):
    return ly * 5878625373183.607730851825


@ly.get("/ly/pc/{ly}")
async def LYtoPC(ly: int):
    return ly * 0.306601393786
