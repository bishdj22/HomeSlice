def result_getter():
    connection = engine.connect()
    query = "select first-name from user_data where first-name = " + firstname + ";"
    result = connection.execute(query)
    for i in result:
        results = i
    return results
    results = result_getter(firstname)
    print("query finished")
    print(results[0])
    print("Success")