from fastapi import APIRouter

mi = APIRouter()


@mi.get("/mi/km/{mi}")
@mi.get("/miles/kilometer/{lm}")
async def MItoKM(mi: float):
    return mi * 1.609344


@mi.get("/mi/lm/{mi}")
@mi.get("/miles/light-minute/{lm}")
async def MItoLM(mi: float):
    return mi * 0.000000089469896


@mi.get("/mi/ls/{mi}")
@mi.get("/miles/light-second/{lm}")
async def MItoLS(mi: float):
    return mi * 0.0000053681938


@mi.get("/mi/ly/{mi}")
@mi.get("/miles/light-year/{lm}")
async def MItoLY(mi: float):
    return mi * 0.00000000000017010780


@mi.get("/mi/au/{mi}")
@mi.get("/miles/astronomical-unit/{lm}")
async def MItoAU(mi: float):
    return mi * 0.0000000107578


@mi.get("/mi/pc/{mi}")
@mi.get("/miles/parsec/{lm}")
async def MItoPC(mi: float):
    return mi * 0.000000000000052155287
