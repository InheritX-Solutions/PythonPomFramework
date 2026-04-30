class RegisterLocators:
    FIRST_NAME = "//input[@placeholder='First Name']"
    LAST_NAME = "//input[@placeholder='Last Name']"
    ADDRESS = "//textarea[@ng-model='Adress']"
    EMAIL = "//input[@type='email']"
    PHONE = "//input[@type='tel']"

    GENDER = "//input[@value='Male']"
    HOBBY = "//input[@id='checkbox1']"

    LANGUAGE_BOX = "//div[@id='msdd']"
    LANGUAGE_LIST = "//li[@class='ng-scope']"
    CLOSE_LANGUAGE = "//div[@class='row ']"

    SKILL_DROPDOWN = "//select[@id='Skills']"
    SKILL_OPTIONS = "//select[@id='Skills']/option"

    COUNTRY_BOX = "//span[@class='select2-selection select2-selection--single']"
    COUNTRY_LIST = "//li[contains(@class,'select2-results__option')]"

    YEAR = "//select[@id='yearbox']"
    MONTH = "//select[@ng-model='monthbox']"
    DAY = "//select[@id='daybox']"

    PASSWORD = "//input[@id='firstpassword']"
    REPASSWORD = "//input[@id='secondpassword']"
    SUBMIT = "//button[@id='submitbtn']"