import asyncio
import time

async def say_after(delay, str1):
    await asyncio.sleep(delay)
    print(str1)

async def main():

  task1 = asyncio.create_task(
        say_after(1,'hello')
  )
  task2 = asyncio.create_task(
        say_after(2,'project')
  )
  print(f"started at {time.strftime('%X')}")
  await task1
  await task2
  print(f"started at {time.strftime('%X')}")

asyncio.run(main())


