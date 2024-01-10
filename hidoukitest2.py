import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def download_pages(urls):
    tasks = [fetch(url) for url in urls]
    # 複数の非同期タスクを並行して実行
    return await asyncio.gather(*tasks)

if __name__ == "__main__":
    urls = [
        "https://freestyles.jp/",
        "https://flora-inc.co.jp/"

    ]

    # 非同期で複数のウェブページをダウンロード
    results = asyncio.run(download_pages(urls))

    # 結果を表示
    for i, result in enumerate(results, 1):
        print(f"Page {i}:\n{result[:680]}...\n")
