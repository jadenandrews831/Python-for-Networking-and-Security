import httpx, asyncio

async def request_http2():
  async with httpx.AsyncClient(http2=True) as client:
    response = await client.get("https://www.google.es")
    print(response)
    print(response.status_code)
    print(response.text)

asyncio.run(request_http2())