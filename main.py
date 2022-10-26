import requests
import utility_functions as util
import db_utilities as db_util
import sqlite3


def main():

    # get request setup
    target_url_string: str = "https://data.nasa.gov/resource/gh4g-9sfh.json"
    response_object: requests.Response = util.get_request(target_url_string)
    json_object = util.convert_content_to_json(response_object)

    # database setup
    db_connection, db_cursor = db_util.set_up_database()

    # main loop
    if json_object is not None:
        for list_entry in json_object:
            if list_entry.get("reclat", None) is not None\
                    and list_entry.get("reclong", None) is not None:

                # get all the info we need to go through the loop
                name = list_entry.get("name", None)
                mass = list_entry.get("mass", None)
                lat_str = list_entry["reclat"]
                long_str = list_entry["reclong"]
                lat = util.convert_string_to_numerical(list_entry["reclat"])
                long = util.convert_string_to_numerical(list_entry["reclong"])

                db_util.filter_data_into_tables(name, mass, lat_str, long_str, lat, long, db_cursor)

        db_util.shut_down_data_base(db_connection)
    else:
        db_util.shut_down_data_base(db_connection)
        print("No data to operate on, exiting program...")


if __name__ == '__main__':
    main()
