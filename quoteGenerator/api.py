from fastapi import APIRouter, Query
from quoteGenerator.ai import generate_quote
from quoteGenerator.db import save_quote, get_recent_quotes

router = APIRouter()

@router.get("/generate")
async def generate(theme: str = Query("inspirational")):
    quote = await generate_quote(theme)
    save_quote(quote)
    return {"quote": quote}

@router.get("/history")
def history():
    return get_recent_quotes()
