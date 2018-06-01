from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

certificate = './Certs/cert_nask.pem'

#files = ('BLOCK_PL.csv', 'BLOCK_EN.csv') #, 'ALLOW_PL.csv', 'ALLOW_EN.csv')
files = ('ALLOW_PL.csv', 'ALLOW_EN.csv')
working_dir = "./Reports"
timestr = time.strftime("%d%m%Y-%H%M%S")
output_file = './Outputs/chrome_{}.log'.format(timestr)

def write_logs(result, file_name):
    with open(output_file, 'a') as f:
        f.write("File: {} Result: {}\n".format(file_name, result))


def simulate_chrome_request(url_s):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--proxy-server=10.48.48.65:13128')
    chrome_options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
    # setting drivers parameter
    driver = webdriver.Chrome('/Users/mzieba/PycharmProjects/Additions/chromedriver',  chrome_options=chrome_options,
                              service_args=["--verbose", "--log-path=./Outputs/simulate_chrome_requests.txt"])
    driver.get(url_s)
    a = driver.page_source
    driver.close()
    return a

# simulate_chrome_request('https://cisco.com')

# Open NASK xmls
for file in files:
    try:
        with open(os.path.join(working_dir, file)) as wyniki:
            for lines in wyniki:  # reads each line
                try:
                    line_entry = lines.strip().split(';')
                    url = str(line_entry[1])
                    write_logs(simulate_chrome_request(url), file)
                except ValueError:
                    pass
    except OSError as e:
        print(e, type(e))

