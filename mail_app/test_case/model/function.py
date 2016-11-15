from selenium import webdriver
import os


def insert_img(driver, file_name):
    #base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = os.getcwd()
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('/mail_app')[0]
    file_path = base + "/mail_app/report/image/" + file_name
    print(file_path)
    driver.get_screenshot_as_file(file_path)


if __name__ == '__main__':
    #insert_img("baidu.jpg")
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    insert_img(driver, 'baidu.jpg')
    driver.quit()



#
