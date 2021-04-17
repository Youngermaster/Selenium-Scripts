from create_account import click_element_by_xpath, create_account, skip_tutorial
import enum
# Using enum class create enumerations


class Languages(enum.Enum):
    Spanish = 'spanish'
    English = 'english'


def change_language(language):
    create_account()

    skip_tutorial()

    # * Clicks the settings icon
    click_element_by_xpath(
        '/html/body/genesys-root/genesys-master-page/genesys-toolbar/section/div/div/div[3]/div/div[2]/div/a[3]')

    # * Clicks the language selector
    click_element_by_xpath(
        '/html/body/genesys-root/genesys-settings-page/section/div/div/div/div[1]/div')

    if language == 'spanish':
        # * Clicks the Spanish language
        click_element_by_xpath(
            '/html/body/genesys-root/genesys-settings-page/section/div/div/div/div[2]/div[2]')

    if language == 'english':
        # * Clicks the English language
        click_element_by_xpath(
            '/html/body/genesys-root/genesys-settings-page/section/div/div/div/div[2]/div[1]')


if __name__ == "__main__":
    change_language(Languages.Spanish.value)
