from fastapi import APIRouter

pc = APIRouter()


@pc.get("/pc/pc/{pc}")
@pc.get("/parsec/parsec/{pc}")
async def PCtoPC(pc: float):
    return pc


@pc.get("/pc/km/{pc}")
@pc.get("/parsec/kilometer/{pc}")
async def PCtoKM(pc: float):
    return pc * 30856775814913.672789139383


@pc.get("/pc/lm/{pc}")
@pc.get("/parsec/light-minute/{pc}")
async def PCtoLM(pc: float):
    return pc * 1715452.084238983356


@pc.get("/pc/ls/{pc}")
@pc.get("/parsec/light-second/{pc}")
async def PCtoLS(pc: float):
    return pc * 102927125.054339001381


@pc.get("/pc/ly/{pc}")
@pc.get("/parsec/light-year/{pc}")
async def PCtoLY(pc: float):
    return pc * 3.261563777167


@pc.get("/pc/mi/{pc}")
@pc.get("/parsec/miles/{pc}")
async def PCtoMI(pc: float):
    return pc * 19173511576713.041331834203


@pc.get("/pc/au/{pc}")
@pc.get("/parsec/astronomical-unit/{pc}")
async def PCtoAU(pc: float):
    return pc * 206264.806247096355
