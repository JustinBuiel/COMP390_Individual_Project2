"""

"""

import requests
import utility_functions as util
import db_utilities as db_util


def main():

    # http get request and json conversion
    target_url_string: str = 'https://data.nasa.gov/resource/gh4g-9sfh.json'
    response_object: requests.Response = util.get_request(target_url_string)
    json_object = util.convert_content_to_json(response_object)

    # database setup with cursor for execution
    db_connection, db_cursor = db_util.set_up_database()

    # main loop to filter data into tables
    if json_object is not None:
        for list_entry in json_object:
            if list_entry.get('reclat', None) is not None\
                    and list_entry.get('reclong', None) is not None:  # check if entry has coordinate data

                # get only the important data about list entry
                name, mass, lat_str, long_str, lat, long = util.get_entry_data(list_entry)

                # pass data to the filtering function
                db_util.filter_data_into_tables(name, mass, lat_str, long_str, lat, long, db_cursor)

                # wanted this to be a progress bar but program completes too fast without sleep and takes
                # too long (16 seconds) with sleep; but I'll keep it anyway
                print(f'\rFiltering data ..... {json_object.index(list_entry)+1}/{len(json_object)}', end='')

        db_util.shut_down_data_base(db_connection)
        print('\nDatabase fully populated, ending program.')
    else:
        db_util.shut_down_data_base(db_connection)
        print('No data to operate on, exiting program...')


if __name__ == '__main__':
    main()
