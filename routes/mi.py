from fastapi import APIRouter

mi = APIRouter()


@mi.get("/mi/km/{mi}")
async def MItoKM(mi: int):
    return mi * 1.609344


@mi.get("/mi/lm/{mi}")
async def MItoLM(mi: int):
    return mi * 0.000000089469896


@mi.get("/mi/ls/{mi}")
async def MItoLS(mi: int):
    return mi * 0.0000053681938


@mi.get("/mi/ly/{mi}")
async def MItoLY(mi: int):
    return mi * 0.00000000000017010780


@mi.get("/mi/au/{mi}")
async def MItoAU(mi: int):
    return mi * 0.0000000107578


@mi.get("/mi/pc/{mi}")
async def MItoPC(mi: int):
    return mi * 0.000000000000052155287
