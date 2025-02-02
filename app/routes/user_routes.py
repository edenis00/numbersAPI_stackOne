from fastapi import APIRouter, HTTPException
from app.schema import NumberResponse
from app.utils import is_prime, is_perfect, digit_sum, properties, get_fun_fact

router = APIRouter()


@router.get("/api/classify-number", response_model=NumberResponse)
async def classify_number(number: str):

    try:
        number = int(number)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail={"number": number, "error": True}
        )

    fun_fact = await get_fun_fact(number)

    return {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties(number),
            "digit_sum": digit_sum(number),
            "fun_fact": fun_fact
        }
