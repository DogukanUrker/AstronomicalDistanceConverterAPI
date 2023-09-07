from fastapi import APIRouter

km = APIRouter()


@km.get("/km/au/{km}")
async def KMtoAU(km: int):
    return km * 0.0000000066845871


@km.get("/km/lm/{km}")
async def KMtoLM(km: int):
    return km * 0.000000055594016


@km.get("/km/ls/{km}")
async def KMtoLS(km: int):
    return km * 0.0000033356410


@km.get("/km/ly/{km}")
async def KMtoLY(km: int):
    return km * 0.00000000000010570008


@km.get("/km/mi/{km}")
async def KMtoMI(km: int):
    return km * 0.62137119


@km.get("/km/pc/{km}")
async def KMtoPC(km: int):
    return km * 0.000000000000032407793
