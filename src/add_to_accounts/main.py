import github
import sprintly
import Slack
from app_config import config
import requests
import os
import logging
import MailChimp



def onboarding_email(type_='welcome', subject='Generic Subject', message='This is a message', attachments=None):
    email = config()['email']
    from_name = ''
    if type_ == 'bugs':
        from_name = 'Lumbermill Bugs'
    elif type_ == 'reviews':
        from_name = 'Review Requested'
    files_ = None
    if attachments:
        files_ = {}
        count = 0
        for a in attachments:
            with open(a, 'rb') as f:
                files_['attachment['+str(count)+']'] = (os.path.basename(a), f.read())
            count += 1
    logging.info('sending email...')
    return requests.post(email['lj_domain'],
                         auth=("api", email['mailgun_key']),
                         files=files_,
                         data={"from": "%s <%s>" % (from_name, email['from']),
                               "to": [email[type_]],
                               "subject": subject, "text": message},
                         )


def add_new_developer(first_name=None, last_name=None, email=None, github_user=None,
                      add_github=True, add_sprintly=True, add_slack=True, send_onboard_email=True):

    # Add user to slack
    if add_slack:
        Slack.add_to_workspace(email)
    # Add user to github - allow me to input comma seperated ids for repos i want
    if add_github:
        github.add_user_to_github(github_user, config()['github']['org'], config()['github']['repos'])
    # add user to sprint.ly allow me to input comma seperated ids for projets to add them too.
    if add_sprintly:
        if sprintly.is_user_registered(product_id=config()['sprintly']['product_id'], email=email,
                                       first_name=first_name, last_name=last_name):
            print("User already registered")
        else:
            sprintly.add_to_sprintly(product_id=config()['sprintly']['product_id'], email=email, first_name=first_name,
                                     last_name=last_name, admin=False)


def run():
    info = MailChimp.mail_chimp()
    print("IN RUN")
    print(info)
    add_new_developer(info["FNAME"], info["LNAME"], info["EMAIL"], info["GITHUB"])


if __name__ == "__main__":
    #run()
    add_new_developer('Siena', 'mikota', 'siena.mikota@gmail.com', 'smikota')
