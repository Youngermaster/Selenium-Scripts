from create_account import click_element_by_xpath, create_account, skip_tutorial
import enum
# Using enum class create enumerations

def create_ladder_tournament():
    create_account()

    skip_tutorial()

    # * Clicks the Tournament Section
    click_element_by_xpath(
        '/html/body/genesys-root/genesys-master-page/genesys-toolbar/section/div/div/div[2]/div/a[1]')

    # * Clicks the ladder tournament button
    click_element_by_xpath(
        '/html/body/genesys-root/genesys-tournament-tab-page/section/div[1]/button[4]')

    # * Starts to find a match
    click_element_by_xpath(
        '/html/body/genesys-root/genesys-tournament-tab-page/section/div[2]/div/div/mat-tab-group/div/mat-tab-body[1]/div/div/div/genesys-tournament-ladder/section/div/div/div[2]/div/button')


if __name__ == "__main__":
    create_ladder_tournament()