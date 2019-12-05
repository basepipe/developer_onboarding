#!/usr/bin/env python3

import requests
import json
import argparse
import logging
import sys
from app_config import config

log = logging.getLogger('Sprint.ly')

sprintly_api = config()['sprintly']['api']
token = (config()['sprintly']['user'], config()['sprintly']['token'])


def list_products(token):
    """List products accessible by the auth key, their archive status, and their id's

    :param auth: auth (email, token) needed to access the Sprint.ly API
    :return: list of each project's (archived_status, name, product_id)
    """
    products = requests.get('{}/products.json'.format(sprintly_api), auth=token)

    if not products.status_code == 200:
        log.exception('Failed to get products, status {}'.format(products.status_code))
        return []
    else:
        return [(product['archived'], product['name'], product['id']) for product in products.json()]


def is_user_registered(product_id, email, first_name, last_name, auth=token):
    """Check if a user is already registered with a Sprint.ly product

    :param product_id:
    :param email: The email address to send an invite to and register a user under
    :param first_name: The first name to be used by Sprint.ly for the user
    :param last_name: The last name to be used by Sprint.ly for the user
    :param auth: API (email, token), which does not need to be an admin, to read the user list
    :return:
    """
    people = requests.get('{}/products/{}/people.json'.format(sprintly_api, product_id), auth=auth)

    if not people.status_code == 200:
        log.exception('Product {} not found'.format(product_id))
        return False

    for person in people.json():
        if email.lower() == person['email'].lower():
            log.debug('Duplicate user found by email {}'.format(email.lower()))
            if not (first_name, last_name) == (person['first_name'], person['last_name']):
                log.warning(
                    'Person found with same email ({}) but differing names: expected {} {}, found {} {}'
                    .format(email, first_name, last_name, person['first_name'], person['last_name'])
                )
            return True

    return False


def create_post_json(email, first_name, last_name, admin=False):
    """Create the json formatted post which adds the user to the product

    :param email: The email address to send an invite to and register a user under
    :param first_name: The first name to be used by Sprint.ly for the user
    :param last_name: The last name to be used by Sprint.ly for the user
    :param admin: Add the user with admin access to the product
    :return: A json dump which can be used to add a user to a product
    """
    post = {
        'admin': admin,
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
    }

    return json.dumps(post)


def add_to_sprintly(product_id, email, first_name, last_name, auth=token, admin=False):
    """Add a user to a Sprint.ly product

    :param product_id: The product to add the user to
    :param email: The email address to send an invite to and register a user under
    :param first_name: The first name to be used by Sprint.ly for the user
    :param last_name: The last name to be used by Sprint.ly for the user
    :param auth: The API (email, token) required to access Sprint.ly, must be an admin of the product
    :param admin: Add the user with admin access to the product
    :return: true if the user was successfully added, false otherwise
    """
    url = "{}/products/{}/people.json".format(sprintly_api, product_id)
    payload = create_post_json(email, first_name, last_name, admin=admin)
    added = requests.post(url, payload, auth=auth)

    if not added.status_code == 200:
        log.exception('Adding user {} to product {} failed with status {}'.format(email, product_id, added.status_code))
        return False
    # Check to see if the response has the same email as a hack to confirm that they were added
    if added.json()['email'] != email:
        log.exception('Failed adding user to {}: {}'.format(product_id, added.json()))
        return False
    else:
        log.info('User {} successfully added to {}'.format(email, product_id))
        return True


def run(email='', first_name='', last_name='', product_id=None):
    if product_id:
        products = list_products(token)
        print products
        if len(products) > 0:
            for (archived, name, product_id) in products:
                if not archived:
                    print('{} => {}'.format(name, product_id))
            print('Select a product ID')
            product_id = int(input(">> "))
        else:
            sys.exit(2)
    else:
        product_id = product_id

    if is_user_registered(product_id, email, first_name, last_name, token):
        print("User already registered")
    else:
        add_to_sprintly(product_id, email, first_name, last_name, token)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("email", help="Email address of the new user")
    parser.add_argument("first_name", help="First name of the new user")
    parser.add_argument("last_name", help="Last name of the new user")
    parser.add_argument("api_token", nargs=2, help="The <api_user> <api_key> used to access sprintly")
    parser.add_argument("-i", "--product_id", help="id for the sprintly product we want to add the user to")

    args = parser.parse_args()

    token = tuple(args.api_token)

    product_id = None

    if not args.product_id:
        products = list_products(token)
        if len(products) > 0:
            for (archived, name, product_id) in products:
                if not archived:
                    print('{} => {}'.format(name, product_id))
            print('Select a product ID')
            product_id = int(input(">> "))
        else:
            sys.exit(2)
    else:
        product_id = args.product_id

    if is_user_registered(product_id, args.email, args.first_name, args.last_name, token):
        print("User already registered")
    else:
        add_to_sprintly(product_id, args.email, args.first_name, args.last_name, token)
