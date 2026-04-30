from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    # 🔥 CLICK ACTIONS
    def click(self, locator):
        self.page.locator(locator).click()

    def double_click(self, locator):
        self.page.locator(locator).dblclick()

    def right_click(self, locator):
        self.page.locator(locator).click(button="right")

    def click_force(self, locator):
        self.page.locator(locator).click(force=True)

    # 🔥 INPUT ACTIONS
    def fill(self, locator, value):
        self.page.locator(locator).fill(value)

    def type(self, locator, value):
        self.page.locator(locator).type(value)

    def clear(self, locator):
        self.page.locator(locator).fill("")

    def press_key(self, locator, key):
        self.page.locator(locator).press(key)

    # 🔥 TEXT METHODS
    def get_text(self, locator):
        return self.page.locator(locator).inner_text()

    def get_all_texts(self, locator):
        return self.page.locator(locator).all_inner_texts()

    def get_text_content(self, locator):
        return self.page.locator(locator).text_content()

    # 🔥 ATTRIBUTE METHODS
    def get_attribute(self, locator, attr):
        return self.page.locator(locator).get_attribute(attr)

    def get_input_value(self, locator):
        return self.page.locator(locator).input_value()

    # 🔥 VISIBILITY / STATE
    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def is_enabled(self, locator):
        return self.page.locator(locator).is_enabled()

    def is_checked(self, locator):
        return self.page.locator(locator).is_checked()

    # 🔥 WAIT METHODS
    def wait_for_selector(self, locator):
        self.page.wait_for_selector(locator)

    def wait_for_visible(self, locator):
        self.page.locator(locator).wait_for(state="visible")

    def wait_for_hidden(self, locator):
        self.page.locator(locator).wait_for(state="hidden")

    def wait_for_timeout(self, time):
        self.page.wait_for_timeout(time)

    def wait_for_url(self, url):
        self.page.wait_for_url(url)

    def wait_for_load(self):
        self.page.wait_for_load_state("load")

    # 🔥 DROPDOWN
    def select_by_value(self, locator, value):
        self.page.locator(locator).select_option(value=value)

    def select_by_label(self, locator, label):
        self.page.locator(locator).select_option(label=label)

    def select_by_index(self, locator, index):
        self.page.locator(locator).select_option(index=index)

    # 🔥 MOUSE ACTIONS
    def hover(self, locator):
        self.page.locator(locator).hover()

    def drag_and_drop(self, source, target):
        self.page.locator(source).drag_to(self.page.locator(target))

    # 🔥 SCREENSHOT
    def take_screenshot(self, path):
        self.page.screenshot(path=path)

    def element_screenshot(self, locator, path):
        self.page.locator(locator).screenshot(path=path)

    # 🔥 NAVIGATION
    def open_url(self, url):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()

    def get_url(self):
        return self.page.url

    def refresh(self):
        self.page.reload()

    def go_back(self):
        self.page.go_back()

    def go_forward(self):
        self.page.go_forward()

    # 🔥 SCROLL
    def scroll_to_element(self, locator):
        self.page.locator(locator).scroll_into_view_if_needed()

    def scroll_page(self):
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    # 🔥 FRAME
    def switch_to_frame(self, frame_locator):
        return self.page.frame_locator(frame_locator)

    # 🔥 ALERT
    def accept_alert(self):
        self.page.on("dialog", lambda dialog: dialog.accept())

    def dismiss_alert(self):
        self.page.on("dialog", lambda dialog: dialog.dismiss())

    # 🔥 COUNT ELEMENTS
    def get_count(self, locator):
        return self.page.locator(locator).count()