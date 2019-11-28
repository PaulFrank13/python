from selenium import webdriver

stealth_mode = False

options = webdriver.ChromeOptions()
options.binary_location = ""
options.add_argument('log-level=3')
options.headless = True

if stealth_mode:
    print('Запуск браузера в скрытом режими.')
else:
    print('Запуск браузера в обычном режими.')

driver = webdriver.Chrome(options=options)

driver.close()
