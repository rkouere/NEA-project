import sqlite3

path = "D:/NEA-project/API/mysite/db.sqlite3"


# ID's: ROSA - 0, VGG-16 - 1
# Gets the accuracy rate of neural network specified through the "name" parameter
def get_accuracy_rate(name):
    database_name = name.format('"', '"')
    database = sqlite3.connect(path)
    c = database.cursor()
    correct_query = "SELECT count(*) from api_results where result={} and network_id={}"
    total_query = "SELECT count(*) from api_results where network_id={}"
    network_id_query = "SELECT id from api_network where name={}"
    c.execute(network_id_query.format(database_name))
    network_id = c.fetchall()
    network_id = network_id[0][0] - 1

    c.execute(correct_query.format("true", str(network_id)))
    correct = c.fetchall()
    c.execute(total_query.format(str(network_id)))
    total = c.fetchall()
    # print(correct[0][0], total[0][0])
    return str(name.format("", ":")), str(round(((correct[0][0] / total[0][0]) * 100), 1))  # str(correct/total)


# Adds a result to the ROSA6 fields in results database
def rosa_add_result(result):
    database = sqlite3.connect(path)
    c = database.cursor()
    query = "INSERT INTO api_results(network_id, result) VALUES(0, {})"
    c.execute(query.format(str(result)))
    database.commit()
    # return c.fetchall()


# Adds a result to the VGG-16 fields in results database
def vgg_add_result(result):
    database = sqlite3.connect(path)
    c = database.cursor()
    query = "INSERT INTO api_results(network_id, result) VALUES(1, {})"
    c.execute(query.format(str(result)))
    database.commit()


# Gets all the data from the tables, this is mainly for debugging purposes
def get_tables():
    database = sqlite3.connect(path)
    c = database.cursor()
    c.execute("SELECT * from api_results")
    return c.fetchall()
