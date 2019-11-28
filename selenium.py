from selenium import webdriver

options = webdriver.ChromeOptions()
options.binary_location = ""
options.add_argument('log-level=3')
options.headless = True

if stealth_mode:
    printTime('Запуск браузера в скрытом режими.')
else:
    printTime('Запуск браузера в обычном режими.')

driver = webdriver.Chrome(options=options)
