from fastapi import APIRouter

ls = APIRouter()


@ls.get("/ls/km/{ls}")
async def LStoKM(ls: int):
    return ls * 299792.458


@ls.get("/ls/lm/{ls}")
async def LStoLM(ls: int):
    return ls * 0.016666666667


@ls.get("/ls/au/{ls}")
async def LStoAU(ls: int):
    return ls * 0.0020039888


@ls.get("/ls/ly/{ls}")
async def LStoLY(ls: int):
    return ls * 0.000000031688088


@ls.get("/ls/mi/{ls}")
async def LStoMI(ls: int):
    return ls * 186282.397051220870


@ls.get("/ls/pc/{ls}")
async def LStoPC(ls: int):
    return ls * 0.0000000097156119
