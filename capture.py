import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as pb:
        browser = await pb.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1280, "height": 800})
        await page.goto("http://localhost:3000")
        
        # Wait for the page to load and animations to set
        await page.wait_for_timeout(2000)
        
        # Screenshot the hero section
        await page.screenshot(path="screenshot-hero.png")
        
        # Screenshot dark mode
        await page.click("#theme-toggle")
        await page.wait_for_timeout(1000)
        await page.screenshot(path="screenshot-hero-dark.png")
        
        # Scroll down to skills section
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight/2)")
        await page.wait_for_timeout(1000)
        await page.screenshot(path="screenshot-middle.png")

        await browser.close()

asyncio.run(run())
