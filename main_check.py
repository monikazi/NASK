import os.path
import requests
import time


file = 'BLOCK_PL.csv'
#files = ('BLOCK_PL.csv', 'BLOCK_EN.csv') #, 'ALLOW_PL.csv', 'ALLOW_EN.csv')
files = ('ALLOW_PL.csv', 'ALLOW_EN.csv')
working_dir = "./Reports"
timestr = time.strftime("%d%m%Y-%H%M%S")
output_file = './Results/chrome_{}.log'.format(timestr)
output_file = './Outputs/only_allow_final.txt'


def write_results(url_, result, file_name):
    with open(output_file, 'a') as f:
        f.write("File: {} URL: {} ACTION: {}\n".format(file_name, url_, result))


#request via proxy:
def ask_wsa(url, file):
    proxy = {'http': 'http://10.48.48.65:13128', 'https': 'http://10.48.48.65:13128'}
    certificate = 'cert_nask.pem'
    result = requests.get(url, proxies=proxy, verify=certificate)
    write_results(url, result.status_code, file)


#Open NASK xmls
for file in files:
    try:
        with open(os.path.join(working_dir, file)) as wyniki:
            for lines in wyniki:  # reads each line
                try:
                    line_entry = lines.strip().split(';')
                    url = str(line_entry[1])
                    ask_wsa(url, file)
                except ValueError:
                    pass
    except OSError as e:
        print(e, type(e))

