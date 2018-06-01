import os.path
import requests
import re


proxy = {'http': 'http://10.48.48.65:13128', 'https': 'http://10.48.48.65:13128'}
certificate = 'cert.pem'



# http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certificate)
# http = urllib3.ProxyManager('http://10.48.48.65:13128')
# #connect to a URL
# website = http.request('GET', 'https://www.zalando.nl/editorial-dames/inspiration/editors-pick-nike-air-max-97/')
#
# #read html code
# html = website.read().decode('utf-8')
#
# #use re.findall to get all the links
# links = re.findall('"((http|ftp)s?://.*?)"', html)
#
# for i in links:
#     print(i[0])
#
file = 'BLOCK_PL.csv'
files = ('BLOCK_PL.csv', 'BLOCK_EN.csv') #, 'ALLOW_PL.csv', 'ALLOW_EN.csv')
working_dir = "."
output_file = 'only_block2.txt'


def write_results(url, result, file_name):
    with open(output_file, 'a') as f:
        f.write("File: {} URL: {} ACTION: {}\n".format(file_name, url, result))


#request via proxy:
def ask_wsa(url, file):
    # proxy = {'http': 'http://10.48.48.65:13128', 'https': 'http://10.48.48.65:13128'}
    # certificate = 'cert.pem'
    result = requests.get(url, proxies=proxy, verify=certificate)
    #write_results(url, result.status_code, file)
    html = result.text
    #use re.findall to get all the links
    links = re.findall(r'"((http|ftp)s?://.*?)"', html)
    for link in links:
        print(link[0])
        # result2 = requests.get(link, proxies=proxy, verify=certificate)
        # print(link, result2)


def get_sub_urls(main_url):
    #connect to url
    # proxy = {'http': 'http://10.48.48.65:13128', 'https': 'http://10.48.48.65:13128'}
    # certificate = 'cert.pem'
    website = requests.get(main_url, proxies=proxy, verify=certificate)
    #read html code
    html = website.text
    #use re.findall to get all the links
    links = re.findall(r'"((http|ftp)s?://.*?)"', html)
    for link in links:
        yield link[0]

#Open NASK xmls
for file in files:
    try:
        with open(os.path.join(working_dir, file)) as wyniki:
            for lines in wyniki:  # reads each line
                try:
                    line_entry = lines.strip().split(';')
                    url = str(line_entry[1])
                    #ask_wsa(url, file)
                    for i in get_sub_urls(url):
                        web = requests.get(i, proxies=proxy, verify=certificate)
                        print(i, web.status_code)

                except ValueError:
                    pass
    except OSError as e:
        print(e, type(e))




# for i in get_sub_urls('https://www.zalando.nl/editorial-dames/inspiration/editors-pick-nike-air-max-97/'):
#     print(i)
