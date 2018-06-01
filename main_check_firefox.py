import os.path
import requests
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium import webdriver

proxy = {'http': 'http://10.48.48.65:13128', 'https': 'http://10.48.48.65:13128'}
certificate = 'cert.pem'
# opts = Options()
# opts.set_headless()
# # opts.add_argument("--headless")
# assert opts.headless  # operating in headless mode
# browser = Firefox(options=opts)
# browser.get('https://duckduckgo.com')
# path_to_firefox = '/Applications/Firefox.app/Contents/MacOS/firefox'
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options, executable_path="/Users/mzieba/PycharmProjects/NASK/geckodriver", proxy=proxy)
print("Firefox Headless Browser Invoked")
driver.get('https://cisco.com/')
driver.quit()

file = 'BLOCK_PL.csv'
# files = ('BLOCK_PL.csv', 'BLOCK_EN.csv', 'ALLOW_PL.csv', 'ALLOW_EN.csv')
# working_dir = "."
# output_file = '_results_.txt'
#
#
# def write_results(url, result, file_name):
#     with open(output_file, 'a') as f:
#         f.write("File: {} URL: {} ACTION: {}\n".format(file_name, url, result))
#
#
# #request via proxy:
# def ask_wsa(url, file):
#     proxy = {'http': 'http://10.48.48.65:13128', 'https': 'http://10.48.48.65:13128'}
#     certificate = 'cert.pem'
#     result = requests.get(url, proxies=proxy, verify=certificate)
#     write_results(url, result.status_code, file)
#
#
# #Open NASK xmls
# for file in files:
#     try:
#         with open(os.path.join(working_dir, file)) as wyniki:
#             for lines in wyniki:  # reads each line
#                 try:
#                     line_entry = lines.strip().split(';')
#                     url = str(line_entry[1])
#                     ask_wsa(url, file)
#                 except ValueError:
#                     pass
#     except OSError as e:
#         print(e, type(e))
#

