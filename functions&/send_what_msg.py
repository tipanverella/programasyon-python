import time
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys

keyboard = Controller()


def send_whatsapp_message(msg: str):
    try:
        pywhatkit.sendwhatmsg_instantly(
            phone_no="+50947926337",
            message=msg,
            tab_close=True,
        )
        time.sleep(2)
        pyautogui.click()
        time.sleep(10)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("Message sent!")
    except Exception as e:
        print(str(e))


"""
def send_msg(msg):
    contact_number = "+50938241591"  # Replace with the desired contact number
    message = msg  # Replace with your message
    num_times = 5  # Replace with the desired number of times

    # Open the browser
    driver = webdriver.Chrome(
        "c:/User/\dedea/Dropbox/PC/Downloads/chromedriver_win32/chromedriver.exe"
    )  # Make sure you have the Chrome WebDriver installed

    # Open WhatsApp Web
    driver.get("https://web.whatsapp.com/")

    # Wait for the user to scan the QR code and log in to WhatsApp Web
    # input("Press Enter after scanning QR code and logging in to WhatsApp Web...")

    # Find the chat input field

    # chat_input = WebDriverWait(driver, 60).until(
    #    EC.visibility_of_element_located(
    #        (By.CSS_SELECTOR, "div._2_1wd.copyable-text.selectable-text")
    #    )
    # )
    chat_input = driver.find_element(
        By.CSS_SELECTOR,
        "div._2_1wd.copyable-text.selectable-text",
    )
    #
    # Send the same message multiple times
    for _ in range(num_times):
        # Clear the chat input field
        chat_input.clear()

        # Type the message
        chat_input.send_keys(contact_number, Keys.RETURN)

        time.sleep(2)

        chat_input.send_keys(message, Keys.RETURN)

        # Press Enter to send the message
        chat_input.send_keys("\n")

        # Wait for a short time between each message (adjust as needed)
        time.sleep(2)

    # Close the browser
    driver.quit()
"""

if __name__ == "__main__":
    send_whatsapp_message("I Love U *Bae* \U0001F618 \n" * 500)
