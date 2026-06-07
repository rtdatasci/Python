import asyncio

from langchain_ollama import ChatOllama
from browser_use import Agent, Browser, BrowserConfig
from pydantic import SecretStr
from dotenv import load_dotenv
load_dotenv()


# Configure the browser to connect to your Chrome instance
browser = Browser(
    config=BrowserConfig(
        # Specify the path to your Chrome executable
        chrome_instance_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',  # macOS path

        # browser_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',  # macOS path
        # For Windows, typically: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
        # For Linux, typically: '/usr/bin/google-chrome'
    )
)

# Create the agent with your configured browser
agent = Agent(
    # task="Search for coffee company called happymug",
    task="Compose a test email with message hi and subject line test and send to jjcamper74@gmail.com",
    llm=ChatOllama(model="deepseek-r1:latest", num_ctx=32000),    
    browser=browser,
)

async def main():
    await agent.run()

    input('Press Enter to close the browser...')
    await browser.close()

if __name__ == '__main__':
    asyncio.run(main())


