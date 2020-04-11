from selenium import webdriver
from time import sleep
from random import randint

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
sleep(3)
# driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://www.instagram.com/')
# username = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
sleep(3)
# driver.implicitly_wait(5)
username = driver.find_element_by_name('username')
username.send_keys('_sachin_7979_g')
# password = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
driver.implicitly_wait(5)
password = driver.find_element_by_name('password')
password.send_keys('Instagram7979$')
sleep(3)
# driver.implicitly_wait(5)
loginButton = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')
loginButton.click()
sleep(3)
# driver.implicitly_wait(5)
notnow = driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
notnow.click()

hashtag_list = ['food', 'cars', 'badminton']
# hashtag_list = ['sachingor']
prev_user_list = []
new_users_followed = 0
likes = 0

for hashtag in hashtag_list:
    driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
    driver.implicitly_wait(10)
    first_thumbnail = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
    first_thumbnail.click()
    sleep(5)
    # driver.implicitly_wait(5)

    for post in range(1,5):
        user_name = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a').text
        if user_name not in prev_user_list:
            if driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':
                driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                print(f'You Followed {user_name}', end= " : ")
                prev_user_list.append(user_name)
                new_users_followed += 1
                sleep(5)
                # driver.implicitly_wait(5)
                likeButton = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
                likeButton.click()
                likes += 1
                # random_number = randint(1,10)
                print(f'Hashtag -> {hashtag} , Post -> {post} , UserName -> {user_name}')
                sleep(5)
                # driver.implicitly_wait(5)
                # comment = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')

                comment = driver.find_element_by_class_name('Ypffh')
                # comment = ui.WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.Ypffh")))
                comment.click()
                driver.implicitly_wait(5)
                comment = driver.find_element_by_class_name('Ypffh')
                comment.click()

                # wait = WebDriverWait(driver, 10)
                # comment = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')))
                # ActionChains(driver).move_to_element(comment).click(comment).perform()

                comment.send_keys("Nice Pic")
                comment.send_keys(Keys.ENTER)
                sleep(3)
                # driver.implicitly_wait(3)
                next_post = driver.find_element_by_link_text('Next')
                next_post.click()
                sleep(3)
                # driver.implicitly_wait(5)

            else:
                print(f'You are Already Following {user_name}')
                # sleep(2)
                # next_post = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')
                # next_post = driver.find_element_by_class_name('_65Bje  coreSpriteRightPaginationArrow')
                next_post = driver.find_element_by_link_text("Next")
                next_post.click()
                driver.implicitly_wait(5)

print(f'New Users Followed by You = {new_users_followed}')
print(f'Number of Posts you liked = {likes}')
print(f'Previous User List = {prev_user_list}')
