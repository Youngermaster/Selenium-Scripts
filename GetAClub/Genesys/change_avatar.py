from create_account import click_element_by_xpath, create_account, skip_tutorial


def change_avatar():
    create_account()

    skip_tutorial()

    # * Clicks the profile icon
    click_element_by_xpath(
        '/html/body/genesys-root/genesys-master-page/genesys-toolbar/section/div/div/div[3]/div/div[2]/div/a[2]')

    # * Clicks the image to change the avatar
    click_element_by_xpath(
        '/html/body/genesys-root/genesys-profile-page/section/div/div/div[1]/div[1]/div[2]/div/div/img')

    # * Clicks the desired new profile avatar
    click_element_by_xpath(
        '/html/body/genesys-root/genesys-profile-page/section/div/div/div/genesys-gallery-form/section/div/div[3]/div[1]/div/img')


if __name__ == "__main__":
    change_avatar()
