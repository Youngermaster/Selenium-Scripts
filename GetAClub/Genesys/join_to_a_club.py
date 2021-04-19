from create_account import click_element_by_xpath, create_account, skip_tutorial


def join_to_a_club():
    create_account()

    skip_tutorial()

    # * Clicks the Club Section
    click_element_by_xpath(
        '/html/body/genesys-root/genesys-master-page/genesys-toolbar/section/div/div/div[2]/div/a[2]')

    # * Request to join to the first club
    click_element_by_xpath(
        '/html/body/genesys-root/genesys-game-clubs-page/section/div/div/div[2]/div/div/div[1]/div/div/div[2]/button')

    # * Clicks confirm error button
    click_element_by_xpath(
        '/html/body/div[2]/div[4]/div/mat-dialog-container/genesys-ctrl-notification/div/button')

    click_element_by_xpath(
        '/html/body/div[2]/div[2]/div/mat-dialog-container/genesys-ctrl-notification/div/button')


if __name__ == "__main__":
    join_to_a_club()
