from selenium import webdriver


class Browser:
    driver = None

    @classmethod
    def get_browser(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            return cls.driver
        else:
            return cls.driver

    @classmethod
    def kill_browser(cls):
        if cls.driver is not None:
            cls.driver.close()
            cls.driver = None
