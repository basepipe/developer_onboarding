import requests
import sys
import logging
import json
import hashlib

logging.basicConfig(level=logging.INFO)
auth = "a6416f0279b825c0c434ba0c5e043b0e-us14"
log = logging.getLogger("Check:")
url = "https://us14.api.mailchimp.com/3.0"
authorize = ("Username", "a6416f0279b825c0c434ba0c5e043b0e-us14")


def get_info():
    tester = requests.get("{}/lists/472f5e896c/members".format(url), auth=authorize)
    log.info(tester.content)
    new_dict = tester.content
    return new_dict


def make_json(email, first, last, git):
    diction = {
        "email_address": email,
        "status": "subscribed",
        "merge_fields": {
            "FNAME": first,
            "LNAME": last,
            "GITHUB": git,
            "ONBOARDED": 1
        }
    }
    return diction


def mail_chimp():
    diction = json.loads(get_info())
    new = diction["members"]
    for key in new:
        if key["merge_fields"]["ONBOARDED"]:
            log.info("ONBOARDED")
            fname = "null"
            lname = "null"
            git = "null"
            on = 1
        else:
            email = key["email_address"]
            temp_hash = hashlib.md5(email.encode())
            email_hash = temp_hash.hexdigest()
            log.info(email_hash)
            fname = key["merge_fields"]["FNAME"]
            lname = key["merge_fields"]["LNAME"]
            git = key["merge_fields"]["GITHUB"]
            on = key["merge_fields"]["ONBOARDED"]
            stag = {
                "FNAME": fname,
                "LNAME": lname,
                "GITHUB": git,
                "EMAIL": email
            }
            info = make_json(email, fname, lname, git)
            req = requests.patch("{}/lists/472f5e896c/members/{}".format(url, email_hash), data=json.dumps(info),
                                 auth=authorize)
            log.info(req.content)
            log.info(stag)
            return stag
    return 0


if __name__ == "__main__":
    log.info(mail_chimp())
    get_info()
