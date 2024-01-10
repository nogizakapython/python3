import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')
    print("finish1")

async def second():
  for i in range(0,2):
    print(i)
    await asyncio.sleep(0.5)
  print("finish2")

asyncio.run(main())
asyncio.run(second())
