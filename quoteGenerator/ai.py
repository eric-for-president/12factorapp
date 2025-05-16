import httpx


async def generate_quote(theme: str) -> str:
    url = "https://zenquotes.io/api/random"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            print(f"Status code: {response.status_code}")
            print(f"Response text: {response.text}")

            if response.status_code == 200:
                data = response.json()  # Remove `await` here
                if isinstance(data, list) and data:
                    quote = data[0]
                    return f"{quote['q']} — {quote['a']}"
                else:
                    return "Unexpected response format from API."
            else:
                return "Failed to fetch quote from external API."
        except Exception as e:
            return f"Exception occurred: {e}"
