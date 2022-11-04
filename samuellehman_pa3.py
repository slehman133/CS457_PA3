# Samuel Lehman
# CS457
# 31 October 2022
# Project 3 for CS457
# History:

import os
import sys
import subprocess
from SamQLTable import SamQLTable

activeDB = "."
quit = False


def main() -> None:
    """
    entry point of the program
    """
    if (len(sys.argv) > 1):
        handle_prog_args()

    while (quit == False):
        args = input("SamQLite> ").split(";")
        for arg in args:
            handle_args(arg)


def handle_prog_args() -> None:
    """
    takes the second argument as the file name and reads
    that file then sends that to the handle_args fucntion
    """
    fileName = sys.argv[1]
    if (os.path.exists(fileName)):
        fileInput = []
        with open(fileName, "r") as file:
            for line in file:
                fileInput.append(line)
        args = "".join(fileInput).strip().split(";")
        for arg in args:
            handle_args(arg.strip())
    else:
        print(f"ERROR: File {fileName} does not exist")


def handle_args(arg) -> None:
    """
    takes the commands and arguments from input and sends them
    to the corresponding function
    """
    # database functions
    if (arg.__contains__("CREATE DATABASE")):
        create_database(arg.removeprefix("CREATE DATABASE").strip())
    elif (arg.__contains__("DROP DATABASE")):
        drop_database(arg.removeprefix("DROP DATABASE").strip())
    elif (arg.__contains__("USE")):
        use_database(arg.removeprefix("USE").strip())
    # table functions
    elif (arg.__contains__("CREATE TABLE")):
        create_table(arg.removeprefix("CREATE TABLE").strip())
    elif (arg.__contains__("DROP TABLE")):
        drop_table(arg.removeprefix("DROP TABLE ").strip())
    elif (arg.__contains__("SELECT")):
        select_from_table(arg.removeprefix("SELECT").strip())
    elif (arg.__contains__("ALTER")):
        alter_table(arg.removeprefix("ALTER").strip())
    # tuple functions
    elif (arg.__contains__("select")):
        select_from_tuple(arg.strip())
    elif (arg.__contains__("insert into")):
        insert_into(arg.removeprefix("insert into").strip())
    elif (arg.__contains__("update")):
        update_tuple(arg.removeprefix("update").strip())
    elif (arg.__contains__("delete")):
        delete_tuple(arg.removeprefix("delete").strip())
    # other
    else:
        if (arg.__contains__("EXIT") or arg.__contains__(".EXIT")):
            global quit
            quit = True
            print("All done.")
        elif (arg != ""):
            print(f"Unknown command: {arg}")


def create_database(data):
    """
    handles the creation of databases
    """
    if (os.path.exists(data) == True):
        print(f"ERROR: Database {data} exists")
    else:
        subprocess.run(["mkdir", data])
        print(f"Created database {data}")


def drop_database(data):
    """
    handles the deletion of databases
    """

    if (os.path.exists(data) == True):
        subprocess.run(["rm", "-r", data])
        print(f"Dropped database {data}")
    else:
        print(f"ERROR: No database named {data}")


def use_database(data):
    """
    sets the current working database
    """
    if (os.path.exists(data) == True):
        global activeDB
        activeDB = os.path.abspath(data)
        print(f"Active database: {data}")
    else:
        print(f"ERROR: No database named {data} exists")


def create_table(data):
    """
    handles table creation
    """
    tableName = data.split()[0].strip()
    # parses the data between ( )
    args = data[data.find('(')+1:data.rfind(')')]
    table = SamQLTable(activeDB, tableName, args)
    del table


def drop_table(data):
    """
    handles table deletion
    """
    tableName = data
    table = SamQLTable(activeDB, tableName)
    table.drop_table()
    del table


def select_from_table(data):
    """
    handles getting data from tables
    """
    tableName = data.removeprefix("* FROM").strip()
    table = SamQLTable(activeDB, tableName)
    table.print_table()
    del table


def alter_table(data):
    """
    handles altering data in tables
    """
    tableName = data.split()[1]
    fileInput = "|" + " ".join(data.split()[3:])
    print(fileInput)
    table = SamQLTable(activeDB, tableName)
    table.alter_table(fileInput)
    del table


def select_from_tuple(data):
    """
    handles getting data from tables
    """
    # gets tableName from data
    tableName = data.split()[data.split().index("from")+1].capitalize()
    table = SamQLTable(activeDB, tableName)
    if (data.__contains__("*")):
        table.print_table()
    else:
        table.select_from_table(data.replace("\n", ""))
    del table


def insert_into(data):
    """
    inserts values into table
    """
    tableName = data.split()[0]
    inputData = "|".join(
        data[data.find('(')+1:data.rfind(')')].split(",")).strip()
    table = SamQLTable(activeDB, tableName)
    table.insert_into(inputData)
    del table


def update_tuple(data):
    """
    updates a tables data
    """
    tableName = data.split()[0]
    table = SamQLTable(activeDB, tableName)
    table.update_table(data.replace("\n", "").replace(tableName, "").strip())
    del table


def delete_tuple(data):
    """
    deletes data in table
    """
    tableName = data.split()[1].capitalize()
    table = SamQLTable(activeDB, tableName)
    table.delete_from_table(data.replace(
        "\n", "").replace("from product", "").strip())
    del table


# execute the main function only if the file is run directly
if __name__ == "__main__":
    main()
