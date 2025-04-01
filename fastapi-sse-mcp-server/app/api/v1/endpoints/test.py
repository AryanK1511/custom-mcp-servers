from fastapi import APIRouter, Response
from fastapi import Request as ServerRequest

from app.utils.logger import CustomLogger
from app.utils.response import success_response

router = APIRouter()


@router.get("/test")
async def test(req: ServerRequest, res: Response):
    try:
        CustomLogger.create_log("info", "Test successful")
        return success_response("Test successful", 200, res, "Test successful")
    except Exception as e:
        CustomLogger.create_log("error", f"Error testing: {str(e)}")
        raise e
