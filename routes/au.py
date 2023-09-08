from fastapi import APIRouter

au = APIRouter()


@au.get("/au/km/{au}")
@au.get("/astronomical-unit/kilometer/{au}")
async def AUtoKM(au: int):
    return au * 149597870.7


@au.get("/au/lm/{au}")
@au.get("/astronomical-unit/light-minute/{au}")
async def AUtoLM(au: int):
    return au * 8.3167464


@au.get("/au/ls/{au}")
@au.get("/astronomical-unit/light-second/{au}")
async def AUtoLS(au: int):
    return au * 499.00478


@au.get("/au/ly/{au}")
@au.get("/astronomical-unit/light-year/{au}")
async def AUtoLY(au: int):
    return au * 0.000015812507


@au.get("/au/mi/{au}")
@au.get("/astronomical-unit/miles/{au}")
async def AUtoMI(au: int):
    return au * 92955807


@au.get("/au/pc/{au}")
@au.get("/astronomical-unit/parsec/{au}")
async def AUtoPC(au: int):
    return au * 0.0000048481368
