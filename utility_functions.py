"""
This module assists with converting a string to an int or float.
Only the convert_string_to_numerical() function is available to outside files
"""

import requests


def _string_is_int(in_string):
    """ returns True if the incoming parameter is an int, returns False otherwise """
    try:
        int(in_string)
        return True
    except TypeError:
        return False
    except ValueError:
        return False


def _string_is_float(in_string):
    """ returns True if the incoming parameter is a float, returns False otherwise """
    try:
        float(in_string)
        return True
    except TypeError:
        return False
    except ValueError:
        return False


def convert_string_to_numerical(in_string):
    """ this function converts a string to a numerical value (to either an int or float)
        'None' is returned if the incoming string is not in the form of an int or float """

    if _string_is_int(in_string):
        return int(in_string)
    elif _string_is_float(in_string):
        return float(in_string)
    return None


def get_request(target_url: str):
    """ This function issues a GET request using the url passed in as the single parameter.
    The response and status code are printed whether there is an error or the request is successful.
    The program exits if there is an error. """

    try:
        response_object: requests.Response = requests.get(target_url)
        if response_object.status_code != 200:
            raise Exception
        print(f"GET request successful\n{response_object.status_code}: [{response_object.reason}]")
    except Exception as error:
        print(f"A get request error has occurred: {error} \n{response_object.status_code}: {response_object.reason} ")
    finally:
        return response_object


def convert_content_to_json(response_object: requests.Response):
    """ This function accepts a requests response object as it's single parameter and tries to
    convert the object to a JSON object
    'None' is returned if the conversion was unsuccessful. """
    try:
        json_object = response_object.json()
        print("Content has been successfully converted to a json object")
    except requests.exceptions.JSONDecodeError as error:
        print(f"A decoding error has occurred, cannot convert content to JSON object: {error}")
    finally:
        return json_object
