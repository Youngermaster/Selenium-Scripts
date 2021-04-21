from create_account import click_element_by_xpath, create_account, skip_tutorial
from utils import DRIVER as driver
from utils import create_club_name


def create_a_club():
    create_account()

    skip_tutorial()

    # * Clicks the Club Section
    click_element_by_xpath(
        '/html/body/genesys-root/genesys-master-page/genesys-toolbar/section/div/div/div[2]/div/a[2]')

    # * Clicks MY LOUNGES
    click_element_by_xpath(
        '/html/body/genesys-root/genesys-game-clubs-page/section/div/div/div[1]/ul/li[2]/a')

    # * Clicks CREATE A CLUB
    click_element_by_xpath(
        '/html/body/genesys-root/genesys-game-clubs-page/section/div/div/div[2]/div/div/div[1]/button')

    # * Clicks SELECT A SHIELD
    click_element_by_xpath(
        '/html/body/genesys-root/genesys-game-clubs-page/section/div[2]/div/div/div[2]/genesys-clubs-create-club-page/section/form/div/div[1]/div/div/button')

    # * Select a SHIELD
    click_element_by_xpath(
        '/html/body/genesys-root/genesys-game-clubs-page/section/div[2]/div/div/div[2]/genesys-clubs-create-club-page/section/genesys-gallery-form/section/div/div[3]/div[1]/div/img'
    )

    driver.find_element_by_xpath(
        '/html/body/genesys-root/genesys-game-clubs-page/section/div[2]/div/div/div[2]/genesys-clubs-create-club-page/section/form/div/div[2]/input'
    ).send_keys('TheSeleniumClub')

    driver.find_element_by_xpath(
        '/html/body/genesys-root/genesys-game-clubs-page/section/div[2]/div/div/div[2]/genesys-clubs-create-club-page/section/form/div/div[3]/input'
    ).send_keys(create_club_name())

    driver.find_element_by_xpath(
        '/html/body/genesys-root/genesys-game-clubs-page/section/div[2]/div/div/div[2]/genesys-clubs-create-club-page/section/form/div/div[3]/input'
    ).send_keys('Youngermaster')

    driver.find_element_by_xpath(
        '/html/body/genesys-root/genesys-game-clubs-page/section/div[2]/div/div/div[2]/genesys-clubs-create-club-page/section/form/div/div[4]/input'
    ).send_keys('The amazing Selenium')

    # * Creates the club
    click_element_by_xpath(
        '/html/body/genesys-root/genesys-game-clubs-page/section/div[2]/div/div/div[2]/genesys-clubs-create-club-page/section/form/div/div[5]/button'
    )

    # * Clicks success message
    click_element_by_xpath(
        '/html/body/div[3]/div[4]/div/mat-dialog-container/genesys-ctrl-notification/div/button'
    )

    # * Clicks error message
    click_element_by_xpath(
        '/html/body/div[3]/div[2]/div/mat-dialog-container/genesys-ctrl-notification/div/button'
    )


if __name__ == "__main__":
    create_a_club()
