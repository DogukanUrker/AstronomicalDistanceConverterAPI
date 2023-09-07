from fastapi import APIRouter

pc = APIRouter()


@pc.get("/pc/km/{pc}")
async def PCtoKM(pc: int):
    return pc * 30856775814913.672789139383


@pc.get("/pc/lm/{pc}")
async def PCtoLM(pc: int):
    return pc * 1715452.084238983356


@pc.get("/pc/ls/{pc}")
async def PCtoLS(pc: int):
    return pc * 102927125.054339001381


@pc.get("/pc/ly/{pc}")
async def PCtoLY(pc: int):
    return pc * 3.261563777167


@pc.get("/pc/mi/{pc}")
async def PCtoMI(pc: int):
    return pc * 19173511576713.041331834203


@pc.get("/pc/au/{pc}")
async def PCtoAU(pc: int):
    return pc * 206264.806247096355
