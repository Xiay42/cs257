#!/usr/bin/env python3
'''
    psycopg2-sample.py
    Jeff Ondich, 23 April 2016

    A very short, demo of how to use psycopg2 to connect to
    and query a PostgreSQL database. This demo assumes a "books"
    database like the one I've used in CS257 for the past few years,
    including an authors table with fields

        (id, given_name, surname, birth_year, death_year)

    You might also want to consult the official psycopg2 tutorial
    at https://wiki.postgresql.org/wiki/Psycopg2_Tutorial.

    Also, SEE THE NOTE BELOW ABOUT config.py. It's important.
'''
import numbers
import sys
import psycopg2
import argparse


# We're also going to import our postgres username, password,
# and database from a file named config.py, like so: 
import config

# Here are steps you should take to make this "import config" work properly.
#
# 1. DO THIS IMMEDIATELY, DON'T WAIT! Create a .gitignore file in the
#    directory containing your python program (I've already done so for this
#    sample directory). Your .gitignore file should contain this line:
#
#     config.py
#
# 2. Create a config.py file in this directory, containing three
#    assignment statements:
#
#     database = 'YOUR_DATABASE_NAME'  (whatever your database name is, like 'books')
#     user = 'YOUR_POSTGRES_USER_NAME'
#     password = 'YOUR_POSTGRES_PASSWORD_IF_ANY'
#
# 3. That's it, congratulations! You have now made your postgres login information
#    available to your python program, but you've prevented that information from
#    getting accidentally pushed to your git repository. Keeping your login info
#    out of your public repos (or your private ones, for that matter) will go a long
#    way towards avoiding one of the most obvious and bone-headed security problems.
#

def get_connection():
    ''' Returns a database connection object with which you can create cursors,
        issue SQL queries, etc. This function is extremely aggressive about
        failed connections--it just prints an error message and kills the whole
        program. Sometimes that's the right choice, but it depends on your
        error-handling needs. '''
    try:
        return psycopg2.connect(database=config.database,
                                user=config.user,
                                password=config.password)
    except Exception as e:
        print(e, file=sys.stderr)
        exit()

def get_NOC_athelets(NOC):
    ''' Returns a list of the full names of all the athletes
        in the NOC, ordered by first name. '''
    athletes = []
    try:
        # Create a "cursor", which is an object with which you can iterate
        # over query results.
        connection = get_connection()
        cursor = connection.cursor()
        query = '''SELECT DISTINCT athletestable.name
                FROM athletestable, linkstable, nocstable
                WHERE athletestable.id = linkstable.athleteID
                AND nocstable.id = linkstable.nocID
                AND nocstable.noc = %s'''
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (NOC,))

        # Iterate over the query results to produce the list of author names.
        for row in cursor:
            athletes.append(f'{row[0]}')

    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    return athletes

def get_NOCs_GM():
    ''' Returns a list of the full names of all authors in the database
        whose surnames are equal to the specified search string.

        This function introduces an important security issue. Suppose you
        have information provided by your user (e.g. a search string)
        that needs to become part of your SQL query. Since you can't trust
        users not to be malicious, nor can you trust them not to do weird and
        accidentally destructive things, you need to be very careful about
        how you use any input they provide. To avoid the very common and
        very dangerous security attack known as "SQL Injection", we will use
        the parameterized version of cursor.execute whenever we're using
        user-generated data. See below for how that goes. '''
    nocs = []
    try:
        query = '''SELECT gmtable.nocID, nocstable.region, gmtable.gm
                   FROM gmtable, nocstable
                   WHERE nocstable.id = gmtable.nocID
                   ORDER BY gmtable.gm DESC;'''
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor:
            nocs.append(f'{row[1]},{row[2]}')

    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    return nocs

def get_NOC_GM(ath):
    ''' Returns the number of GMs a NOC has won '''
    nocGM= []
    try:
        # Create a "cursor", which is an object with which you can iterate
        # over query results.
        connection = get_connection()
        cursor = connection.cursor()
        query = '''SELECT gmTable.gm
                   FROM gmTable, nocsTable
                   WHERE gmTable.nocID = nocsTable.id
                   AND nocstable.noc = %s;'''
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (ath,))

        # Iterate over the query results to produce the list of author names.
        for row in cursor:
            nocGM.append(row[0])

    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    return nocGM


def get_parsed_arguments():
    parser = argparse.ArgumentParser(description='NOCs!')
    parser.add_argument('function', metavar='function', help='sepcify the function you want this program to perform')
    parser.add_argument('--searchWord', metavar='searchWord', help='search the title that contains this word')
    parser.add_argument('--Help', '-H', action='store_const', const=True, help='want help?')
    parsed_arguments = parser.parse_args()
    return parsed_arguments

def main():
    arguments = get_parsed_arguments()
    search_text = arguments.searchWord


    if arguments.Help:
        with open("usage.txt") as helptext:
            help = helptext.read()
            print(help)        
    elif (arguments.function).lower() == 'noc_athletes':
        # Example #1: get a list of author names
        print('========== All athletes ==========')
        athletes = get_NOC_athelets(search_text)
        for athlete in athletes:
            print(athlete)
        print()
    elif (arguments.function).lower() == 'nocs_gmedals':
        #Example #2: get a list of authors whose surnames equal a search string
        print(f'========== All NOCS with Gmedal ==========')
        nocs = get_NOCs_GM()
        for noc in nocs:
            print(noc)
        print()
    elif (arguments.function).lower() == 'noc_gmedals':
        # Example #3: get a list of authors whose surnames contain a search string
        print(f'========== GMs won by NOC "{search_text}" ==========')
        GMnum = get_NOC_GM(search_text)
        if len(GMnum) == 0:
            print(0)
        else:
            print(GMnum[0])
    else:
        with open("usage.txt") as helptext:
            help = helptext.read()
            print(help) 



if __name__ == '__main__':
    main()

