from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from time import sleep, strftime, localtime
import config
import csv


class WebDriver():
    def __init__(self, debug):
        self.debug = debug
        service = Service(executable_path=config.EXE_PATH)
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()

    def _log(self, info):
        if self.debug:
            with open(config.LOGFILE, 'a', encoding='utf-8') as file:
                info = strftime('[%d-%m-%Y %H:%M:%S]: ', localtime())+info
                file.writelines(info+'\n')
                print(info)

    def _get_url(self):
        return self.driver.current_url

    def _get_element(self, xpath):
        try:
            element = WebDriverWait(self.driver, config.TIMEOUT).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, xpath)
                )
            )
        except TimeoutException:
            return None
        return element

    def _get_text(self, xpath):
        if (e := self._get_element(xpath)) is not None and e.text != '':
            return str(e.text)
        return 'None'

    def _click_element(self, ele):
        try:
            self._get_element(ele).click()
            sleep(config.TIMEOUT)
        except AttributeError:
            return False
        return True

    def _click_js(self, xpath, disabled=False):
        try:
            element = self._get_element(xpath)
            sleep(config.TIMEOUT)
            id = element.get_attribute('id')
            if disabled:
                self.driver.execute_script(
                    f'document.querySelector(\'#{id}\').disabled = false;'
                )
                sleep(config.TIMEOUT)
            self.driver.execute_script(
                f'document.querySelector(\'#{id}\').click();'
            )
            sleep(config.TIMEOUT)
        except Exception:
            return False
        return True

    def quit(self):
        self._log('exiting the browser >')
        self.driver.close()


class GoogleMapsScraper(WebDriver):
    def __init__(self, debug=False):
        super().__init__(debug)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.quit()

    def _get_text_js(self, src):
        try:
            text = self.driver.execute_script(
                f'return document.querySelector("img[src*={src}]")'
                '.parentNode.parentNode.parentNode.children[1].innerText;'
            )
            if 'Add' in text or text == '':
                return 'None'
            return text
        except Exception:
            return 'None'

    def search_query(self, searchtext):
        self.driver.get(config.URL+searchtext)
        self._log('searching for url > '+searchtext)
        sleep(config.WAIT_TIME)

    def identify_url(self):
        return self._get_url().split('/')[4]

    def write_data(self, data, filename):
        with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            self._log('writing to file > '+str(data[:3]))
            csvwriter.writerow(data)

    def get_place_data(self, filename):
        name = self._get_text(config.PLACE_NAME_XPATH)
        rating = self._get_text(config.PLACE_RATING_XPATH)
        review = self._get_text(config.PLACE_REVIEWS_XPATH)
        address = self._get_text_js(config.PLACE_ADDRESS_SRC)
        contact = self._get_text_js(config.PLACE_CONTACT_SRC)
        website = self._get_text_js(config.PLACE_WEBSITE_SRC)
        pluscode = self._get_text_js(config.PLACE_PLUSCODE_SRC)
        url = self._get_url()
        result = [
            name, rating, review, address, contact, website, pluscode, url
        ]
        self.write_data(result, filename)

    def _next_page(self, prev):
        try:
            self._click_element(config.BACK_BUTTON_XPATH)
            self._click_js(config.NEXT_PAGE_XPATH, True)
            if (e := self._get_element(config.FIRST_RESULT_XPATH)) != prev:
                e.click()
            else:
                return False
        except Exception:
            return False
        return e

    def get_places_data(self, filename, querylen):
        self._click_element(config.FIRST_RESULT_XPATH)
        results_found, prev = 1, None
        while results_found <= querylen:
            if (rf := results_found % 20) == 0:
                if not self._click_element(config.BOTTOM_PANE_XPATH+'[20]'):
                    break
                self.get_place_data(filename)
                if not (prev := self._next_page(prev)):
                    break
            else:
                if not self._click_element(config.BOTTOM_PANE_XPATH+f'[{rf}]'):
                    break
                self.get_place_data(filename)
            results_found += 1
