"""
This module contains all sql interactions with the database
the supporting functions are all private including insertions into tables for security
"""

import sqlite3


def _get_bounding_box():
    """ This private function returns the bounding box dictionary that
        includes the coordinates we will test against """

    # geolocation bounding box -- (left,bottom,right,top)
    bound_box_dict = {
        'Africa_MiddleEast_Meteorites': (-17.8, -35.2, 62.2, 37.6),
        'Europe_Meteorites': (-24.1, 36, 32, 71.1),
        'Upper_Asia_Meteorites': (32.2, 35.8, 190.4, 72.7),
        'Lower_Asia_Meteorites': (58.2, -9.9, 154, 38.6),
        'Australia_Meteorites': (112.9, -43.8, 154.3, -11.1),
        'North_America_Meteorites': (-168.2, 12.8, -52, 71.5),
        'South_America_Meteorites': (-81.2, -55.8, -34.4, 12.6)
    }
    return bound_box_dict


def _trim_bounding_box():
    """ This private function reduces the bounding box dictionary into tuples for each region """

    bound_box_dict = _get_bounding_box()

    africa_coords = bound_box_dict['Africa_MiddleEast_Meteorites']
    europe_coords = bound_box_dict['Europe_Meteorites']
    up_asia_coords = bound_box_dict['Upper_Asia_Meteorites']
    low_asia_coords = bound_box_dict['Lower_Asia_Meteorites']
    australia_coords = bound_box_dict['Australia_Meteorites']
    north_am_coords = bound_box_dict['North_America_Meteorites']
    south_am_coords = bound_box_dict['South_America_Meteorites']

    return africa_coords, europe_coords, up_asia_coords, low_asia_coords, australia_coords, north_am_coords, south_am_coords


def _get_table_names():
    """ This private function returns the region names for use when creating and interacting with the tables """

    table_names = ['Africa_MiddleEast_Meteorites', 'Europe_Meteorites', 'Upper_Asia_Meteorites',
                   'Lower_Asia_Meteorites', 'Australia_Meteorites', 'North_America_Meteorites', 'South_America_Meteorites']
    return table_names


def _make_tables(db_cursor, table_name):
    """ This private function takes the database cursor object and a table name as it's
        parameters in order to create the 7 regions' tables. The table is also cleared
        out so old data doesn't affect results """

    try:
        db_cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}(
                            name TEXT,
                            mass TEXT,
                            reclat TEXT,
                            reclong TEXT);''')
        db_cursor.execute(f'''DELETE FROM {table_name}''')
    except sqlite3.Error as create_error:
        print(f'A database error has occurred: {create_error}')


def _put_data_in_tables(name, mass, lat_str, long_str, db_cursor, table_name):
    """ This private function takes the entry data, database cursor object and a table name
        as it's parameters in order to insert the meteorite data into the correct table """

    try:
        db_cursor.execute(f'''INSERT INTO {table_name} VALUES(?, ?, ?, ?)''',
                          (name,
                           mass,
                           lat_str,
                           long_str))
    except sqlite3.Error as insert_error:
        print(f'A database error has occurred: {insert_error}')


def set_up_database():
    """ This function sets up our database and then creates the tables. The function
        returns the important connection and cursor objects for use throughout the program """

    db_connection = None

    try:
        # initialize the database and its important connection/cursor objects
        db_name = 'important_meteorites.db'
        db_connection = sqlite3.connect(db_name)
        db_cursor = db_connection.cursor()

        print('Successfully connected to database')

        # create the tables by passing a table to the _make_tables function
        table_names = _get_table_names()
        for table_name in table_names:
            _make_tables(db_cursor, table_name)
        print('Successfully created all tables')

    except sqlite3.Error as db_error:
        print(f'A database error has occurred: {db_error}')
    finally:
        return db_connection, db_cursor


def filter_data_into_tables(name, mass, lat_str, long_str, lat, long, db_cursor):
    """ This function takes the entry data and the cursor object in order to filter
        the meteorites into the correct regions. It does this by comparing the bounding
        box coordinates to the numerical lat and long variables and calling the insertion function """

    table_names = _get_table_names()

    # get the tuples from the dictionary for less clutter
    africa_coords, europe_coords, up_asia_coords, low_asia_coords, \
        australia_coords, north_am_coords, south_am_coords = _trim_bounding_box()

    # the nested ifs check whether the current meteorite fits in the region
    if africa_coords[0] <= long <= africa_coords[2]:
        if africa_coords[1] <= lat <= africa_coords[3]:
            # if match is found, insert the data into the table
            _put_data_in_tables(name, mass, lat_str, long_str, db_cursor, table_names[0])

    if europe_coords[0] <= long <= europe_coords[2]:
        if europe_coords[1] <= lat <= europe_coords[3]:
            _put_data_in_tables(name, mass, lat_str, long_str, db_cursor, table_names[1])

    if up_asia_coords[0] <= long <= up_asia_coords[2]:
        if up_asia_coords[1] <= lat <= up_asia_coords[3]:
            _put_data_in_tables(name, mass, lat_str, long_str, db_cursor, table_names[2])

    if low_asia_coords[0] <= long <= low_asia_coords[2]:
        if low_asia_coords[1] <= lat <= low_asia_coords[3]:
            _put_data_in_tables(name, mass, lat_str, long_str, db_cursor, table_names[3])

    if australia_coords[0] <= long <= australia_coords[2]:
        if australia_coords[1] <= lat <= australia_coords[3]:
            _put_data_in_tables(name, mass, lat_str, long_str, db_cursor, table_names[4])

    if north_am_coords[0] <= long <= north_am_coords[2]:
        if north_am_coords[1] <= lat <= north_am_coords[3]:
            _put_data_in_tables(name, mass, lat_str, long_str, db_cursor, table_names[5])

    if south_am_coords[0] <= long <= south_am_coords[2]:
        if south_am_coords[1] <= lat <= south_am_coords[3]:
            _put_data_in_tables(name, mass, lat_str, long_str, db_cursor, table_names[6])


def shut_down_data_base(db_connection):
    """ This function actually populates the database tables and disconnects from the database """

    db_connection.commit()
    db_connection.close()
