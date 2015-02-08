import requests
import psycopg2
import re
import json


from create_table_insert_values_module import *
from reddit_bsoup import get_data as reddit
from linkedin_channel_selenium import get_data as linkedin
from list_of_links import list_of_links

list_of_links = list_of_links

"""
Methods:

export_json - prints data in json
check_table_exists
delete_table
view_all_tables
which_table_type - checks for table template
url_source - checks for data retrieval template
view_table
backbone - main logic


"""

def export_json(database, name):
    """
    Accepts database, table name, returns json
    List of 3 items, name, headers, data
    [name, {headers : [title, link, votes]}, {data : ['argbar', 'www.com', 23]}]
    """

    #collecting column names
    conn = psycopg2.connect("dbname={0} user=postgres password=feliks".format(database))
    cur = conn.cursor()  #cursor to database established here
    cur.execute("SELECT column_name "
                "FROM information_schema.columns "
                "WHERE table_schema = 'public' "
                "AND table_name = '{0}'".format(name))
    a = cur.fetchall()
    a.pop(0)  # removes index
    headers = []
    for i in a:
        headers.append(i[0])

    #collecting data
    cur.execute('SELECT * FROM {0};'.format(name))
    a = cur.fetchall()
    #fetchall returns one list of tuples
    list_of_lists = []
    for tuple in a:
        temp_list = []
        for item in tuple:
            temp_list.append(item)
        temp_list.pop(0)  # remove index
        list_of_lists.append(temp_list)
    conn.close()
    print json.dumps([name, {'columns': headers}, {'data': list_of_lists}])



def check_table_exists(database, name):
    """checks if table exists. Returns True or false"""
    conn = psycopg2.connect("dbname={0} user=postgres password=feliks".format(database))
    cur = conn.cursor()  #cursor to database established here
    cur.execute("SELECT * "
                "FROM information_schema.tables "
                "WHERE table_name = '{0}' ".format(name))
    a = cur.fetchall()
    conn.close()
    if a == []:  #fetchall returns an empty list for nonexistent tables
        return False
    else:
        return True

def delete_table(database, name):
    conn = psycopg2.connect("dbname={0} user=postgres password=feliks".format(database))
    cur = conn.cursor()  #cursor to database established here
    try:
        cur.execute("DROP TABLE {0}".format(name))
    except:
        print name, "not present."
    conn.commit()
    conn.close()

def view_all_tables(database):
    """Prints public tables in give database."""

    conn = psycopg2.connect("dbname={0} user=postgres password=feliks".format(database))
    cur = conn.cursor()  #cursor to database established here
    cur.execute("SELECT * "
                "FROM information_schema.tables "
                "WHERE table_schema = 'public' ")

    a = cur.fetchall()
    print "Here are the tables:"
    for i in a:
        print i

    conn.close()

def which_table_type(name):
    """
    Determines which template of table creation is used.
    Takes a table name and returns a template code.
    For new sites
    """
    list_of_template_1 = ['reddit'
                          ''
                          '']
    list_of_template_2 = ['linkedin'
                          ''
                          '']
    list_of_template_3 = []

    for i in list_of_template_1:
        if i in name:
            return 1
    for i in list_of_template_2:
        if i in name:
            return 2
    for i in list_of_template_3:
        if i in name:
            return 3
    else:
        print "Error: Table name doesn't coincide with a present template." \
              "Edit which_table_type"

def url_source(url):
    """
    This functions accepts a url from the list of links. It checks what the source website is,
    such as reddit, quora, or linkedin. Then it sends that url to its get data script
    Accepts URL, returns
    """

    if "reddit" in url:  # connects to the reddit_bsoup.py
        return reddit
    if "linkedin" in url:
        return linkedin

def view_table(database, name):
    conn = psycopg2.connect("dbname={0} user=postgres password=feliks".format(database))
    cur = conn.cursor()  #cursor to database established here
    cur.execute('SELECT * FROM {0};'.format(name))
    a = cur.fetchall()
    print "Here is the table {0}:".format(name)
    for i in a:
        print i
    conn.close()

def backbone():
    """Main Logic"""

    database = 'newdatabase'  # databases are created manually
    for link in list_of_links:
        get_data = url_source(link)  # sets get_data to the correct handle
        url = link
        name = re.sub('[a-z]+://', "", link).replace("/", "_").replace(".", "_")

        check = check_table_exists(database, name)  # where name is the prospective or
                                                    # existing name of the table
        if check is True:  # if true, we go to inserting values
            pass
        if check is False:  # we check table type. Needs to be updated for new table types.
            table = which_table_type(name)  # which table returns 1, 2, 3 et cetra
            if table == 1:
                create_table_1(database, name)
                print "table type 1 created"
            if table == 2:
                create_table_2(database, name)
                print "table type 2 created"
            if table == 3:
                create_table_3(database, name)
            else:
                print "Error: Table code in 'if name == main' does not" \
                      "coincide with a available table template. " \
                      "Add a table template or update 'if name == main'"

        # get_data(url) # returns list of list: title, link, votes, and comments
        table = which_table_type(name)  #reusing which table rather than using global variable
        if table == 1:
            insert_values_1(database, name, reddit(url))
        if table == 2:
            insert_values_2(database, name, linkedin(url))
        if table == 3:
            pass
        export_json('newdatabase', name)


if __name__ == "__main__":
    backbone()
    # delete_table('newdatabase', 'www_linkedin_com_channels_206www_linkedin_com_channels_200')
    # view_all_tables('newdatabase')
    # export_json('newdatabase', name)
    # view_table('newdatabase', 'www_reddit_com_r_worldnews')



##################################### kimono API - expired code
def get_json(link):
    """
    retrieves json data from kimono link
    expired code for kimono
    """
    global name  #define global so variables
    # can be picked up elsewhere
    link = link
    a = requests.get('{0}'.format(link))
    a = a.json()
    name = a['name']
    results = a['results']
    collection = results['collection1']

######################################
