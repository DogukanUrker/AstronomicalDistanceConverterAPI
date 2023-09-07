from fastapi import APIRouter

lm = APIRouter()


@lm.get("/lm/km/{lm}")
async def LMtoKM(lm: int):
    return lm * 17987547


@lm.get("/lm/au/{lm}")
async def LMtoAU(lm: int):
    return lm * 0.12023933


@lm.get("/lm/ls/{lm}")
async def LMtoLS(lm: int):
    return lm * 60


@lm.get("/lm/ly/{lm}")
async def LMtoLY(lm: int):
    return lm * 0.0000019012853


@lm.get("/lm/mi/{lm}")
async def LMtoMI(lm: int):
    return lm * 11176944


@lm.get("/lm/pc/{lm}")
async def LMtoPC(lm: int):
    return lm * 0.00000058293671
