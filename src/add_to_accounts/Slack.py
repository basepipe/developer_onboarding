import json
import requests
import logging
import sys
from app_config import config

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
url = "https://slack.com/api"


def get_user(email):
    """Checks for existence of user and fetches the user id

    :param email: The pre-existing users email address
    :return: The users id number
    """
    check = requests.get("{}/users.lookupByEmail?token={}&email={}".format(url, config()['slack']['main_token'], email))
    log.info(check.content)
    return_dict = json.loads(check.content)
    return return_dict


def add_to_channel(user):
    """Adds the specified user to the Basepipe channels in Slack

    :param user: The users unique id number
    :return: 1 if successful; 0 if failure
    """
    on = requests.post("{}/channels.invite?token={}&channel=CFE5E2J1H&user={}".format(url,
                                                                                      config()['slack']['main_token'],
                                                                                      user))
    gen = requests.post("{}/channels.invite?token={}&channel=C3M0Z9UP6&user={}".format(url,
                                                                                       config()['slack']['main_token'],
                                                                                       user))
    temp1 = json.loads(on.content)
    check1 = temp1['ok']
    temp2 = json.loads(gen.content)
    check2 = temp2['ok']
    if check1 and check2:
        return 1
    else:
        return 0


def add_to_workspace(email):
    """Adds user to the Basepipe workspace from their email. Requires unique token given to this application

    :param email:
    :return: 1 if successful, 0 if failure
    """
    status = requests.post("{}/users.admin.invite?token={}&email={}".format(url,
                                                                            config()['slack']['main_token'], email))
    test1 = json.loads(status.content)
    check3 = test1['ok']
    log.info(status.content)                                # Prints "ok: true" if successful, else prints error msg
    if check3:
        return 1
    else:
        return 0


def add_user_to_slack(email):
    add_to_workspace(email)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        user = sys.argv[1]
    elif len(sys.argv) == 1:
        user = input("Enter Email Address: ")
    add_to_workspace(user)
"""
new_dict = get_user(user)
testing = new_dict['ok']
if testing:
    log.info("got it")
else:
    log.error("Need existing user")
    quit()

user_id = new_dict['user']
new_id = user_id['id']

if add_to_channel(new_id) == 0:
    log.error("User Already in Channels")
"""


