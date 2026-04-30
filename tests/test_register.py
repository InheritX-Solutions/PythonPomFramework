from pages.register_page import RegisterPage
from utils.google_sheet_utils import GoogleSheetUtils
from utils.config import Config


def test_register(page):
    page.goto(Config.BASE_URL)

    sheet_id = "1ec2cfCbV_nd9OLpqmRo8SHCy1mHaGyLmDCquH1jnEwU"

    data = GoogleSheetUtils.get_data(sheet_id)

    for row in data:
        register = RegisterPage(page)

        register.fill_form(
            row["first_name"],
            row["last_name"],
            row["address"],
            row["email"],
            row["phone"]
        )

        register.select_language()
        register.select_skill()
        register.select_country()
        register.select_dob()

        register.set_password(row["password"])
        register.submit_form()