import os
import shutil
import asyncio
from langchain_openai import ChatOpenAI
from browser_use import BrowserConfig, Browser, Agent
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import subprocess
load_dotenv()
api_key = "YOUR_OPENAI_API_KEY"
gorq_key="YOUR_GROQ_API_KEY"
async def main():
    # Initialize the LLM
    llm = ChatOpenAI(
        model="gpt-3.5-turbo", #use gpt-4o or gpt 3.5turbo
        temperature=0.0,
        openai_api_key=api_key
    )
    config = BrowserConfig(
        window_size=(1920, 1080),
        # browser_binary_path=r"C:\Users\User\Desktop\Crawl4AI\chromedriver.exe",
        headless=False,
        disable_security=False,
        extra_chromium_args=[r"--user-data-dir='C:\Users\User\Desktop\Crawl4AI\chromedriver.exe'"],
    )
    browser = Browser(config=config)
    task_description = """
    Open https://www.myreddy247.com
    2. Click the 'Log In' button.
    3. Enter the following credentials:
    - Username:  YourUsername
    - Password: YourPassword123
    4. Submit the login form and wait for the dashboard to load.
    
    Wait 5 seconds.  
    5. Click the 'Deposit' button like Deposit.  
    7.  Enter the deposit amount Click ' Continue Deposition '.
    8. Wait for the payment confirmation page to load (e.g., QR code or UPI details).
    9. Take a full-page screenshot and save it as deposit_confirmation.png.
    10. Close the browser.
    """    
    llm_cheaper = ChatGroq(
        groq_api_key="YOUR_GROQ_API_KEY",
        model_name="meta-llama/llama-4-scout-17b-16e-instruct",
        # model_name="llama-3.3-70b-versatile",
        temperature=0.0
    )
    llm_cheaper02 = ChatGroq(
        groq_api_key="YOUR_GROQ_API_KEY",
        model_name="gemma-7b-it",
        # model_name="meta-llama/llama-4-scout-17b-16e-instruct",
        # model_name="llama-3.3-70b-versatile",
        temperature=0.0
    )
    agent = Agent(
        browser=browser,
        task=task_description,
        llm=llm,
        planner_llm=llm_cheaper,
        page_extraction_llm=llm_cheaper02,
        use_vision=False,
        # use_vision=True,
        max_input_tokens=4000,
        max_failures=4,
        max_actions_per_step=3)
    history = await agent.run(
            max_steps=15
        )
        # Handle screenshots
    print("token used ==> ", history.total_input_tokens())

    # Run agent
    # history = await agent.run()
    print("Visited URLs:", history.urls())
    print("Actions taken:", history.action_names())
    print("Actions taken:", history.extracted_content())

    import os
    import base64
    screenshots = history.screenshots()
    import os
    import base64
    screenshots = history.screenshots()
    print(history.final_result())
    print(history.extracted_content())
    if screenshots:
        # Get the latest Base64 screenshot
        screenshot_data = screenshots[-1]  # This should be a Base64 string, not a file path
        destination_path = os.path.join(r"C:\Users\Acer\OneDrive - Pixeltruth\Desktop\Pixeltruth Codes\Agentic_Ai", "deposit_confirmation.png")
        try:
            # Decode the Base64 data into binary
            decoded_data = base64.b64decode(screenshot_data)
            # Save the decoded binary data as an image file
            with open(destination_path, 'wb') as f:
                f.write(decoded_data)
            print(f" Saved screenshot as '{destination_path}'")
        except Exception as e:
            print(f" Error: {e}")
    await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
 