# ----------------------------------------------------------------------------------- #
# Test script
# ----------------------------------------------------------------------------------- #
# import DriverSetup
from utility.DriverSetup import *
# Inherit from scripts_default
from template import Scripts_default


class test_script(Scripts_default):
    url = "https://phptravels.com/demo/"

    def start(self, log):
        INFO = self.INFO
        log.title("luanch driver",1)
        driver = DriverSetup()
        log.title("start page",2)
        log.session_start("get website",3)
        driver.get(self.url)
        log.session_start("click log-in page",3)
        driver.find_element_then_click(By.XPATH, "//small[text()='http://www.phptravels.net/login']")
        log.session_end()

        log.title("log-in procedure",2)
        log.session_start("switch to log-in window", 3)
        # switch to log-in webpage
        handle_start_page = driver.current_window_handle
        for handle in driver.window_handles:
            if handle != handle_start_page:
                driver.switch_to.window(handle)
        log.session_start("check window",3)
        # current_window is not the start_page
        assert driver.current_window_handle != handle_start_page
        log.session_start("fill USERNAME",3)
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys(INFO["USERNAME"])
        log.session_start("fill PASSWORD",3)
        driver.find_element(By.NAME, "password").send_keys(INFO["PASSWORD"])
        log.session_start("press login",3)
        driver.find_element_then_click(By.XPATH, "//button[@type='submit']")
        log.session_end()


        
        
