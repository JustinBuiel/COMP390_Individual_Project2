""" This module contains all sql interactions with the database"""

import sqlite3


def _trim_bounding_box():
    """ """

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

    africa_coords = bound_box_dict["Africa_MiddleEast_Meteorites"]
    europe_coords = bound_box_dict["Europe_Meteorites"]
    up_asia_coords = bound_box_dict["Upper_Asia_Meteorites"]
    low_asia_coords = bound_box_dict["Lower_Asia_Meteorites"]
    australia_coords = bound_box_dict["Australia_Meteorites"]
    north_am_coords = bound_box_dict["North_America_Meteorites"]
    south_am_coords = bound_box_dict["South_America_Meteorites"]

    return africa_coords, europe_coords, up_asia_coords, low_asia_coords, australia_coords, north_am_coords, south_am_coords


def _make_table_1(db_cursor):
    """ """

    db_cursor.execute('''CREATE TABLE IF NOT EXISTS Africa_MiddleEast_Meteorites(
                        name TEXT,
                        mass TEXT,
                        reclat TEXT,
                        reclong TEXT);''')
    db_cursor.execute('''DELETE FROM Africa_MiddleEast_Meteorites''')


def _make_table_2(db_cursor):
    """ """

    db_cursor.execute('''CREATE TABLE IF NOT EXISTS Europe_Meteorites(
                        name TEXT,
                        mass TEXT,
                        reclat TEXT,
                        reclong TEXT);''')
    db_cursor.execute('''DELETE FROM Europe_Meteorites''')


def _make_table_3(db_cursor):
    """ """

    db_cursor.execute('''CREATE TABLE IF NOT EXISTS Upper_Asia_Meteorites(
                        name TEXT,
                        mass TEXT,
                        reclat TEXT,
                        reclong TEXT);''')
    db_cursor.execute('''DELETE FROM Upper_Asia_Meteorites''')


def _make_table_4(db_cursor):
    """ """

    db_cursor.execute('''CREATE TABLE IF NOT EXISTS Lower_Asia_Meteorites(
                        name TEXT,
                        mass TEXT,
                        reclat TEXT,
                        reclong TEXT);''')
    db_cursor.execute('''DELETE FROM Lower_Asia_Meteorites''')


def _make_table_5(db_cursor):
    """ """

    db_cursor.execute('''CREATE TABLE IF NOT EXISTS Australia_Meteorites(
                        name TEXT,
                        mass TEXT,
                        reclat TEXT,
                        reclong TEXT);''')
    db_cursor.execute('''DELETE FROM Australia_Meteorites''')


def _make_table_6(db_cursor):
    """ """

    db_cursor.execute('''CREATE TABLE IF NOT EXISTS North_America_Meteorites(
                        name TEXT,
                        mass TEXT,
                        reclat TEXT,
                        reclong TEXT);''')
    db_cursor.execute('''DELETE FROM North_America_Meteorites''')


def _make_table_7(db_cursor):
    """ """

    db_cursor.execute('''CREATE TABLE IF NOT EXISTS South_America_Meteorites(
                        name TEXT,
                        mass TEXT,
                        reclat TEXT,
                        reclong TEXT);''')
    db_cursor.execute('''DELETE FROM South_America_Meteorites''')


def _put_in_africa(name, mass, lat_str, long_str, db_cursor):
    """ """

    try:
        db_cursor.execute('''INSERT INTO Africa_MiddleEast_Meteorites VALUES(?, ?, ?, ?)''',
                          (name,
                           mass,
                           lat_str,
                           long_str))
    except sqlite3.Error as db_error:
        print(f'A database error has occurred: {db_error}')


def _put_in_europe(name, mass, lat_str, long_str, db_cursor):
    """ """

    try:
        db_cursor.execute('''INSERT INTO Europe_Meteorites VALUES(?, ?, ?, ?)''',
                          (name,
                           mass,
                           lat_str,
                           long_str))
    except sqlite3.Error as db_error:
        print(f'A database error has occurred: {db_error}')


def _put_in_up_asia(name, mass, lat_str, long_str, db_cursor):
    """ """

    try:
        db_cursor.execute('''INSERT INTO Upper_Asia_Meteorites VALUES(?, ?, ?, ?)''',
                          (name,
                           mass,
                           lat_str,
                           long_str))
    except sqlite3.Error as db_error:
        print(f'A database error has occurred: {db_error}')


def _put_in_low_asia(name, mass, lat_str, long_str, db_cursor):
    """ """

    try:
        db_cursor.execute('''INSERT INTO Lower_Asia_Meteorites VALUES(?, ?, ?, ?)''',
                          (name,
                           mass,
                           lat_str,
                           long_str))
    except sqlite3.Error as db_error:
        print(f'A database error has occurred: {db_error}')


def _put_in_australia(name, mass, lat_str, long_str, db_cursor):
    """ """

    try:
        db_cursor.execute('''INSERT INTO Australia_Meteorites VALUES(?, ?, ?, ?)''',
                          (name,
                           mass,
                           lat_str,
                           long_str))
    except sqlite3.Error as db_error:
        print(f'A database error has occurred: {db_error}')


def _put_in_north_am(name, mass, lat_str, long_str, db_cursor):
    """ """

    try:
        db_cursor.execute('''INSERT INTO North_America_Meteorites VALUES(?, ?, ?, ?)''',
                          (name,
                           mass,
                           lat_str,
                           long_str))
    except sqlite3.Error as db_error:
        print(f'A database error has occurred: {db_error}')


def _put_in_south_am(name, mass, lat_str, long_str, db_cursor):
    """ """

    try:
        db_cursor.execute('''INSERT INTO South_America_Meteorites VALUES(?, ?, ?, ?)''',
                          (name,
                           mass,
                           lat_str,
                           long_str))
    except sqlite3.Error as db_error:
        print(f'A database error has occurred: {db_error}')


def set_up_database():
    """ """

    db_connection = None

    try:
        db_name = 'important_meteorites.db'
        db_connection = sqlite3.connect(db_name)
        db_cursor = db_connection.cursor()

        _make_table_1(db_cursor)
        _make_table_2(db_cursor)
        _make_table_3(db_cursor)
        _make_table_4(db_cursor)
        _make_table_5(db_cursor)
        _make_table_6(db_cursor)
        _make_table_7(db_cursor)

        return db_connection, db_cursor
    except sqlite3.Error as db_error:
        print(f'A database error has occurred: {db_error}')


def filter_data_into_tables(name, mass, lat_str, long_str, lat, long, db_cursor):
    """ """

    africa_coords, europe_coords, up_asia_coords, low_asia_coords, \
        australia_coords, north_am_coords, south_am_coords = _trim_bounding_box()

    if africa_coords[0] <= long <= africa_coords[2]:
        if africa_coords[1] <= lat <= africa_coords[3]:
            _put_in_africa(name, mass, lat_str, long_str, db_cursor)

    if europe_coords[0] <= long <= europe_coords[2]:
        if europe_coords[1] <= lat <= europe_coords[3]:
            _put_in_europe(name, mass, lat_str, long_str, db_cursor)

    if up_asia_coords[0] <= long <= up_asia_coords[2]:
        if up_asia_coords[1] <= lat <= up_asia_coords[3]:
            _put_in_up_asia(name, mass, lat_str, long_str, db_cursor)

    if low_asia_coords[0] <= long <= low_asia_coords[2]:
        if low_asia_coords[1] <= lat <= low_asia_coords[3]:
            _put_in_low_asia(name, mass, lat_str, long_str, db_cursor)

    if australia_coords[0] <= long <= australia_coords[2]:
        if australia_coords[1] <= lat <= australia_coords[3]:
            _put_in_australia(name, mass, lat_str, long_str, db_cursor)

    if north_am_coords[0] <= long <= north_am_coords[2]:
        if north_am_coords[1] <= lat <= north_am_coords[3]:
            _put_in_north_am(name, mass, lat_str, long_str, db_cursor)

    if south_am_coords[0] <= long <= south_am_coords[2]:
        if south_am_coords[1] <= lat <= south_am_coords[3]:
            _put_in_south_am(name, mass, lat_str, long_str, db_cursor)


def shut_down_data_base(db_connection):
    """ """

    db_connection.commit()
    db_connection.close()
