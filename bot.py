import os
import asyncio
from aiohttp import web
from playwright.async_api import async_playwright

ACCESS_TOKEN = os.getenv("MUTOLAA_ACCESS_TOKEN", "")
DEVICE_ID = os.getenv("MUTOLAA_DEVICE_ID", "")
BOOK_URL = os.getenv("MUTOLAA_BOOK_URL", "https://mutolaa.com/uz/reader/orzular-ortidan-quvib")

async def handle_ping(request):
    return web.Response(text="Bot faol ishlamoqda!")

async def start_web_server():
    app = web.Application()
    app.router.add_get('/', handle_ping)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", 10000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"Veb-server {port}-portda ishga tushdi.", flush=True)

async def run_single_session():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu",
                "--disable-extensions",
                "--js-flags=--max-old-space-size=128",
                "--renderer-process-limit=1"
            ]
        )
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
            timezone_id="Asia/Tashkent",
            locale="uz-UZ"
        )
        
        if ACCESS_TOKEN and DEVICE_ID:
            await context.add_cookies([
                {"name": "access_token", "value": ACCESS_TOKEN, "domain": ".mutolaa.com", "path": "/"},
                {"name": "mutolaa_device_id", "value": DEVICE_ID, "domain": ".mutolaa.com", "path": "/"}
            ])

        page = await context.new_page()
        
        # RAM tejash: faqat rasm va video to'xtatiladi, shrift va scriptlar faol qoladi
        await page.route("**/*", lambda route: route.abort() if route.request.resource_type in ["image", "media"] else route.continue_())

        print("Sahifa darhol ochilmoqda...", flush=True)
        await page.goto(BOOK_URL, wait_until="networkidle", timeout=60000)
        
        # Sahifa ochilishi bilanoq darhol o'qish harakatlari boshlandi
        print("Sahifa ochildi! Darhol o'qish harakatlari boshlandi...", flush=True)
        await page.mouse.click(200, 300)
        await page.keyboard.press("PageDown")
        await page.mouse.wheel(0, 150)

        # 25 daqiqa davomida uzluksiz o'qish sikli
        for _ in range(50):
            await asyncio.sleep(15)
            await page.keyboard.press("PageDown")
            await page.mouse.wheel(0, 120)
            await asyncio.sleep(15)
            await page.keyboard.press("ArrowDown")
            await page.mouse.wheel(0, -50)

        print("Sessiya yakunlandi. Xotirani tozalab qayta ulanadi...", flush=True)
        await browser.close()

async def run_mutolaa_bot():
    while True:
        try:
            await run_single_session()
            await asyncio.sleep(3)
        except Exception as e:
            print(f"Kutilmagan xatolik: {e}, 5 soniyadan so'ng qayta ochiladi...", flush=True)
            await asyncio.sleep(5)

async def main():
    await start_web_server()
    await run_mutolaa_bot()

if __name__ == "__main__":
    asyncio.run(main())
