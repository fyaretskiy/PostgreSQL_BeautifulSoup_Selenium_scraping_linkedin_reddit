import psycopg2

############################################## 1 #####################################################
def create_table_1(database,name):
    """Type comments and upvotes"""
    #Are comments and upvotes enough to gauge item strength/value? No, not alone
    #Actually, yes because comments may be proportional to controversy
    #However, with reddit its a slippery slope, since comment count
    #May be random, arbitrary.
    conn = psycopg2.connect("dbname={0} user=postgres password=feliks".format(database))
    cur = conn.cursor() #can't have table names with spaces. got it
    cur.execute("CREATE TABLE {0} ("
                "id serial PRIMARY KEY,"
                "title varchar,"
                "link varchar,"
                "votes int,"
                "comments int"
                ");".format(name))
    print "Created Table Successfully"
    conn.commit()
    conn.close()


def insert_values_1(database, name, list_of_entries):
    """
    Inserts values function one. Compatibility includes:
    Categories: likes, comments
    Reddit
    Accepts database, table(name) and list of entries

    -Needs to remove values too for example, I can clear
    this whole table once the function is called
    """
    conn = psycopg2.connect("dbname={0} user=postgres password=feliks".format(database))
    cur = conn.cursor()
    #delete prior entries:
    cur.execute("DELETE FROM {0}".format(name))


    for i in list_of_entries:
        cur.execute("Insert Into {0} (title, link, votes, comments)"
                    " Values (%s, %s, %s, %s);".format(name), (i[0], i[1], i[2], i[3]))
    conn.commit()
    conn.close()
    print "Entered data for {0} successfully.".format(name)

############################################## 2 #####################################################

def create_table_2(database, name):
    """linkedin"""
    conn = psycopg2.connect("dbname={0} user=postgres password=feliks".format(database))
    cur = conn.cursor()  #  can't have table names with spaces. got it
    cur.execute("CREATE TABLE {0} ("
                "id serial PRIMARY KEY,"
                "title varchar,"
                "summary varchar," #postgres does not accept 'like', 'comment' or 'link'
                "likes int,"
                "comments int,"
                "shares int,"
                "links varchar"
                ");".format(name))
    print "Created Table Successfully"
    conn.commit()
    conn.close()


def insert_values_2(database, name, list_of_entries):
    """
    Inserts values function one. Compatibility includes:
    Categories: likes, comments
    Reddit
    Accepts database, table(name) and list of entries

    -Needs to remove values too for example, I can clear
    this whole table once the function is called
    """
    conn = psycopg2.connect("dbname={0} user=postgres password=feliks".format(database))
    cur = conn.cursor()
    #delete prior entries:
    cur.execute("DELETE FROM {0}".format(name))
    for i in list_of_entries:
        cur.execute("Insert Into {0} (title, summary, likes, comments, shares, links)"
                    " Values (%s, %s, %s, %s, %s, %s);".format(name), (i[0], i[1], i[2], i[3], i[4], i[5]))
    conn.commit()
    conn.close()
    print "Entered data for {0} successfully.".format(name)

    pass

############################################## Test #####################################################

def create_table_test(database, name):
    """test"""
    name = name.replace(" ", "_") #it seems postgres can't take spaces in the table names
    conn = psycopg2.connect("dbname={0} user=postgres password=feliks".format(database))
    cur = conn.cursor() #can't have table names with spaces. got it
    cur.execute("CREATE TABLE {0} ("
                "id serial PRIMARY KEY,"
                "num integer,"
                "data varchar"
                ");".format(name))
    print "Created Table Successfully"
    conn.commit()
    conn.close()

def insert_values_test(database):
     """test"""
     conn = psycopg2.connect("dbname={0} user=postgres password=feliks".format(database))
     cur = conn.cursor() #can't have table names with spaces. got it
     cur.execute("Insert Into reddit_world_news (num, data)"
                 "Values (21, 'abcc');")

     print "inserted Successfully"
     conn.commit()
     conn.close()



if __name__ == "__main__":
    pass
