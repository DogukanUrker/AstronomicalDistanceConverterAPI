from fastapi import APIRouter

lm = APIRouter()


@lm.get("/lm/lm/{lm}")
@lm.get("/light-minute/light-minute/{lm}")
async def LMtoLM(lm: float):
    return lm


@lm.get("/lm/km/{lm}")
@lm.get("/light-minute/kilometer/{lm}")
async def LMtoKM(lm: float):
    return lm * 17987547


@lm.get("/lm/au/{lm}")
@lm.get("/light-minute/astronomical-unit/{lm}")
async def LMtoAU(lm: float):
    return lm * 0.12023933


@lm.get("/lm/ls/{lm}")
@lm.get("/light-minute/light-second/{lm}")
async def LMtoLS(lm: float):
    return lm * 60


@lm.get("/lm/ly/{lm}")
@lm.get("/light-minute/light-year/{lm}")
async def LMtoLY(lm: float):
    return lm * 0.0000019012853


@lm.get("/lm/mi/{lm}")
@lm.get("/light-minute/miles/{lm}")
async def LMtoMI(lm: float):
    return lm * 11176944


@lm.get("/lm/pc/{lm}")
@lm.get("/light-minute/parsec/{lm}")
async def LMtoPC(lm: float):
    return lm * 0.00000058293671
