from fastapi import APIRouter

ls = APIRouter()


@ls.get("/ls/ls/{ls}")
@ls.get("/light-second/light-second/{ls}")
async def LStoLS(ls: float):
    return ls


@ls.get("/ls/km/{ls}")
@ls.get("/light-second/kilometer/{ls}")
async def LStoKM(ls: float):
    return ls * 299792.458


@ls.get("/ls/lm/{ls}")
@ls.get("/light-second/light-minute/{ls}")
async def LStoLM(ls: float):
    return ls * 0.016666666667


@ls.get("/ls/au/{ls}")
@ls.get("/light-second/astronomical-unit/{ls}")
async def LStoAU(ls: float):
    return ls * 0.0020039888


@ls.get("/ls/ly/{ls}")
@ls.get("/light-second/light-year/{ls}")
async def LStoLY(ls: float):
    return ls * 0.000000031688088


@ls.get("/ls/mi/{ls}")
@ls.get("/light-second/miles/{ls}")
async def LStoMI(ls: float):
    return ls * 186282.397051220870


@ls.get("/ls/pc/{ls}")
@ls.get("/light-second/parsec/{ls}")
async def LStoPC(ls: float):
    return ls * 0.0000000097156119
