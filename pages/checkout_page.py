"""Page Object for the Sauce Demo checkout flow (info + overview)."""


class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.error_message = page.locator("[data-test='error']")
        self.page_title = page.locator(".title")

    def fill_info(self, first_name: str, last_name: str, postal_code: str):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)
        self.continue_button.click()

    def finish_order(self):
        self.finish_button.click()

    def get_error_text(self) -> str:
        return self.error_message.inner_text()

    def get_page_title(self) -> str:
        return self.page_title.inner_text()
