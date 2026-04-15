#!/usr/bin/env python3
"""
Frontend Screenshot Tool
Takes screenshots of the running frontend for visual inspection
"""

import asyncio
import sys
from datetime import datetime
from pathlib import Path
from playwright.async_api import async_playwright
import argparse


async def take_screenshot(url: str = "http://localhost:5173", output_path: str = None):
    """Take a screenshot of the frontend"""

    if output_path is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f"frontend_screenshot_{timestamp}.png"

    print(f"📸 Taking screenshot of {url}")
    print(f"   Output: {output_path}")

    async with async_playwright() as p:
        try:
            # Launch browser
            browser = await p.chromium.launch(
                headless=True,
                args=['--no-sandbox', '--disable-dev-shm-usage']
            )
            context = await browser.new_context(
                viewport={'width': 1920, 'height': 1080}
            )
            page = await context.new_page()

            # Navigate to the page
            print(f"🌐 Navigating to {url}...")
            response = await page.goto(url, wait_until='networkidle', timeout=10000)

            if response.status != 200:
                print(f"⚠️  Warning: HTTP {response.status} received")

            # Wait for content to load
            print("⏳ Waiting for content to load...")
            await page.wait_for_timeout(2000)  # Wait 2 seconds for animations/loading

            # Try to wait for main content
            try:
                await page.wait_for_selector('main', timeout=5000)
                print("✅ Main content loaded")
            except:
                print("⚠️  Main content selector not found, proceeding anyway")

            # Take screenshot
            print("📷 Capturing screenshot...")
            await page.screenshot(
                path=output_path,
                full_page=True,
                type='png'
            )

            # Get page title
            title = await page.title()
            print(f"📄 Page title: {title}")

            await browser.close()

            print(f"✅ Screenshot saved to: {output_path}")
            print(f"🖼  File size: {Path(output_path).stat().st_size} bytes")

            return output_path

        except Exception as e:
            print(f"❌ Error taking screenshot: {e}")
            return None


async def analyze_frontend_visual():
    """Take screenshot and provide basic analysis"""

    # Check if server is running first
    import aiohttp
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('http://localhost:5173') as resp:
                if resp.status != 200:
                    print(f"⚠️  Frontend server returned HTTP {resp.status}")
    except Exception as e:
        print(f"❌ Frontend server not accessible: {e}")
        print("💡 Make sure the frontend server is running: cd frontend && npm run dev")
        return None

    # Take screenshot
    screenshot_path = await take_screenshot()

    if screenshot_path:
        print("\n🎨 VISUAL INSPECTION READY")
        print("=" * 40)
        print(f"Screenshot location: {Path(screenshot_path).absolute()}")
        print("\n📋 Next steps:")
        print("1. Open the screenshot file to see current frontend appearance")
        print("2. Compare with desired modern chat UI design")
        print("3. Identify specific visual improvements needed")
        print("4. Use frontend-improver agent with specific visual requirements")

        return screenshot_path

    return None


def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='Take screenshot of frontend')
    parser.add_argument('--url', default='http://localhost:5173',
                       help='URL to screenshot (default: http://localhost:5173)')
    parser.add_argument('--output', help='Output path for screenshot')
    parser.add_argument('--analyze', action='store_true',
                       help='Analyze frontend and provide recommendations')

    args = parser.parse_args()

    if args.analyze:
        asyncio.run(analyze_frontend_visual())
    else:
        asyncio.run(take_screenshot(args.url, args.output))


if __name__ == "__main__":
    main()