import requests
import json
import sys
import logging
from app_config import config

authorize = (config()['github']['username'], config()['github']['token'])

url = "https://api.github.com/"
repo_params = {'pull': 'true', 'push': 'true', 'admin': 'false'}

logging.basicConfig(level=logging.INFO)


def check_user(username):
    """
    Check if user is registered with GitHub
    :param username: GitHub username
    :return:
    """
    c = requests.get("{}users/{}".format(url, username))  # no authorization needed for this request
    if c.status_code == 404:
        logging.info("Error: Invalid User")
        quit()
    elif c.status_code == 200:
        logging.info("User Found")
        return True


def in_org(username, org):
    """ Check if user is already in organization

    :param username: GitHub username
    :return:
    """
    check = requests.get("{}orgs/{}/members/{}".format(url, org, username), auth=authorize)
    if check.status_code == 204:
        logging.info("Already org member")
        quit()
    else:
        return False


def add_to_org(username,org):
    """ Add user to  GitHub organization

    :param username: GitHub username of user to be added
    :return: response object
    """
    r = requests.put("{}orgs/{}/memberships/{}".format(url,org, username), auth=authorize)
    return r


def add_to_repo(username, org, repo):
    """ Add user to the onboarding repo

    :param username: GitHub username to be added to repo
    :return: response object for request
    """
    test = requests.get('{}repos/{}/{}/collaborators/{}'.format(url, org, repo, username), auth=authorize)
    return test


def add_user_to_github(user_, org, repo):
    if check_user(user_) and not in_org(user_, org):
        add_user = add_to_org(user_, org)
        add_repo = add_to_repo(user_, org, repo)
        if add_user.status_code == 200:
            logging.info("Invitation Sent")
        elif add_user.status_code == 403:
            logging.info("Error: Authentication Needed")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        user = sys.argv[1]
    elif len(sys.argv) == 1:
        user = input("Enter Github Username: ")





