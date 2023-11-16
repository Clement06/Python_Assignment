import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def driver():
    # Setup: Start the WebDriver
    driver = webdriver.Chrome()
    yield driver
    # Teardown: Quit the WebDriver
    driver.quit()


def test_scenario_1(driver):
    # Launch URL and verify the Title
    url = "https://automationpanda.com/2021/12/29/want-to-practice-test-automation-try-these-demo-sites/"
    driver.get(url)
    assert "Want to practice test automation? Try these demo sites! | Automation Panda" in driver.title

    # Click on Speaking and verify the title of the Page
    time.sleep(3)
    speaking_link = driver.find_element(By.XPATH, "//a[normalize-space()='Speaking']")
    speaking_link.click()
    assert "Speaking | Automation Panda" in driver.title

    # Verify Keynote Addresses is present or not and if present verify the text
    keynote = driver.find_element(By.XPATH, "//h2[contains(text(),'Keynote Addresses')]")
    assert keynote, "Keynote Addresses found"
    assert f"Keynote Addresses" in keynote.text, "Message match"

    # Verify Conference Talks is present or not and if present verify the text
    conference_talks = driver.find_element(By.XPATH, "//h2[contains(text(),'Conference Talks')]")
    assert conference_talks, "Conference Talks found"
    assert f"Conference Talks" in conference_talks.text, "Message match"


def test_scenario_2(driver):
    # Launch URL and verify the Login button is present
    url = "https://www.flipkart.com/"
    driver.get(url)
    time.sleep(3)
    driver.find_element("xpath", "//span[@role='button']").click()
    assert driver.find_element("xpath", "//a[normalize-space()='Login']"), "Login button found"

    # Click on Login button
    login_button = driver.find_element("xpath", "//a[normalize-space()='Login']")
    login_button.click()

    # Enter Phone Number and click on Request OTP button
    phone_number = "7358927710"
    phone_input = driver.find_element("xpath", "//input[@class='_2IX_2- VJZDxU']")
    phone_input.send_keys(phone_number)

    request_otp_button = driver.find_element("xpath", "//button[text()='Request OTP']")
    request_otp_button.click()
    time.sleep(2)
    driver.find_element("xpath", "//button[@class='_2KpZ6l _2HKlqd _3AWRsL']").click()
    time.sleep(6)
    # Verify message in pop up
    message_popup = driver.find_element("xpath", "//span[normalize-space()='OTP sent to Mobile']")
    assert f"OTP sent to Mobile" in message_popup.text, "Message match"
