from selenium import webdriver


class BrowserInterface:
    def __init__(self, config):
        self.browser_name = config.getoption('--browser_name')
        self.browser_version = config.getoption('--browser_version')
        self.hub = config.getoption('--hub')
        self.hub_port = config.getoption('--hub_port')
        self.enable_vnc = config.getoption('--enable_vnc')
        self._window_width = 1920
        self._window_height = 1080

        if self.browser_name == 'chrome':
            options = webdriver.ChromeOptions()
        elif self.browser_name == 'firefox':
            options = webdriver.FirefoxOptions()
        else:
            raise AssertionError(f'Unknown browser: {self.browser_name}')

        options.set_capability('browserName', self.browser_name)
        options.set_capability('browserVersion', self.browser_version)
        options.set_capability('selenoid:options', {
            'enableVNC': True if self.enable_vnc == 'true' else False,
            'screenResolution': f'{self._window_width}x{self._window_height}x24'
        })

        self.driver = webdriver.Remote(
            command_executor=f"http://{self.hub}:{self.hub_port}/wd/hub",
            options=options)
        self.driver.set_window_size(self._window_width, self._window_height)

    def quit(self):
        self.driver.quit()
