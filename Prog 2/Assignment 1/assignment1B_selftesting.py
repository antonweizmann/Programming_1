import mini_proj_2 as asgmt

def test_read_database():
    f = open("test.txt", "w")
    f.write("\"movie1\" 1 11\n\"Movie2\" 2.2 22\n\"MoVie3\" 0.3 333")
    f.close()

    correct_answer = {'movie1': (1.0, 11), 
                      'Movie2': (2.2, 22), 
                      'MoVie3': (0.3, 333)}

    if asgmt.read_database("test.txt") == correct_answer:
        print("Passed test_read_database")
    else:
        print("Failed test_read_database")

def test_read_database_long_name():
    f = open("test.txt", "w")
    f.write("\"movie1 movie1PartA wow\" 1 11\n\"Movie2\" 2.2 22\n\"MoVie3\" 0.3 333")
    f.close()

    correct_answer = {'movie1 movie1PartA wow': (1.0, 11), 
                      'Movie2': (2.2, 22), 
                      'MoVie3': (0.3, 333)}

    if asgmt.read_database("test.txt") == correct_answer:
        print("Passed test_read_database_long_name")
    else:
        print("Failed test_read_database_long_name")
        
def test_read_database_invalid_filename():
    if asgmt.read_database("not_existing.txt") is None:
        print("Passed test_read_database_invalid_filename")
    else:
        print("Failed test_read_database_invalid_filename")
        

def test_read_database_same_movie():
    f = open("test.txt", "w")
    f.write("\"movie\" 1 111\n\"movie\" 2 22")
    f.close()
    
    correct_result = {'movie' : (1.0, 111)}
    
    if asgmt.read_database("test.txt") == correct_result:
        print("Passed test_read_database_same_movie")
    else:
        print("Failed test_read_database_same_movie")
        
def test_read_database_same_movie2():
    f = open("test.txt", "w")
    f.write("\"movie\" 1 11\n\"movie\" 2 22")
    f.close()

    correct_result = {'movie' : (2.0, 22)}
    
    if asgmt.read_database("test.txt") == correct_result:
        print("Passed test_read_database_same_movie2")
    else:
        print("Failed test_read_database_same_movie2")
        
def test_read_database_tuple_types():
    f = open("test.txt", "w")
    f.write("\"movie\" 1 11\n\"movie\" 2 22")
    f.close()
    
    if (type(asgmt.read_database("test.txt")['movie'][0]) == float and
        type(asgmt.read_database("test.txt")['movie'][1]) == int):
        print("Passed test_read_database_tuple_types")
    else:
        print("Failed test_read_database_tuple_types")
        
##########################################################################################

def test_movie_title_list():
    test_dict =  {'movie1' : (1.0, 11), 
                  'Movie2' : (2.2, 22), 
                  "MoVie3" : (0.3, 333)}
    
    if asgmt.movie_title_list(test_dict) == ['movie1', 'Movie2', 'MoVie3']:
        print("Passed test_movie_title_list")
    else:
        print("Failed test_movie_title_list")
##########################################################################################

def test_avg_duration1():
    test_dict =  {'movie1' : (1.0, 11), 
                  'Movie2' : (2.2, 22), 
                  "MoVie3" : (0.3, 333)}
    
    if asgmt.avg_duration(test_dict, 1) == 22:
        print("Passed test_avg_duration1")
    else:
        print("Failed test_avg_duration1")

def test_avg_duration2():
    test_dict =  {'movie1' : (1.0, 11), 
                  'Movie2' : (2.2, 22), 
                  "MoVie3" : (0.3, 333)}
    
    if asgmt.avg_duration(test_dict, 0.9) == 16.5:
        print("Passed test_avg_duration2")
    else:
        print("Failed test_avg_duration2")

def test_avg_duration_none():
    test_dict =  {'movie1' : (1.0, 11), 
                  'Movie2' : (2.2, 22), 
                  "MoVie3" : (0.3, 333)}
    
    if asgmt.avg_duration(test_dict, 3) is None:
        print("Passed test_avg_duration_none")
    else:
        print("Failed test_avg_duration_none")


def test_avg_duration_zero():
    test_dict =  {'movie1' : (1.0, 11), 
                  'Movie2' : (2.2, 0), 
                  "MoVie3" : (0.3, 333)}
    
    if asgmt.avg_duration(test_dict, 0) == 172:
        print("Passed test_avg_duration_zero")
    else:
        print("Failed test_avg_duration_zero")

##########################################################################################

def test_best_rated_movie():
    test_dict =  {'movie1' : (1.0, 85), 
                  'Movie2' : (2.2, 0), 
                  "MoVie3" : (0.3, 130), 
                  'Movie4' : (2.5, 55), 
                  "MoVie5" : (2.2, 120)}

    assert asgmt.best_rated_movie(test_dict, 56, 135, True) == "MoVie5"

def test_best_rated_movie_shortest():
    test_dict =  {'movie1' : (1.0, 85), 
                  'Movie2' : (2.2, 0), 
                  "MoVie3" : (2.2, 128), 
                  'Movie4' : (2.5, 55), 
                  "MoVie5" : (2.2, 129)}

    assert asgmt.best_rated_movie(test_dict, 56, 135, True) == "MoVie3"

def test_best_rated_movie_longest():
    test_dict =  {'movie1' : (1.0, 85), 
                  'Movie2' : (2.2, 0), 
                  "MoVie3" : (2.2, 128), 
                  'Movie4' : (2.5, 55), 
                  "MoVie5" : (2.2, 129)}

    assert asgmt.best_rated_movie(test_dict, 56, 135, False) == "MoVie5"

def test_best_rated_movie_none():
    test_dict =  {'movie1' : (1.0, 85), 
                  'Movie2' : (2.2, 0), 
                  "MoVie3" : (2.2, 128), 
                  'Movie4' : (2.5, 55), 
                  "MoVie5" : (2.2, 129)}

    assert asgmt.best_rated_movie(test_dict, 130, 135, False) == None


def main():
    
    print("Testing add_entry() function")
    try:
        test_read_database()
    except Exception as e:
        print("Ran into an issue while running: test_read_database")
        print(e)
    try:
        test_read_database_same_movie()
    except Exception as e:
        print("Ran into an issue while running: test_read_database_same_movie")
        print(e)

    try:
        test_read_database_tuple_types()
    except Exception as e:
        print("Ran into an issue while running: test_read_database_tuple_types")
        print(e)
    print(".................................")

    print("Testing change_entry() function")
    try:
        test_avg_duration1()
    except Exception as e:
        print("Ran into an issue while running: test_avg_duration1")
        print(e)

    try:
        test_avg_duration_none()
    except Exception as e:
        print("Ran into an issue while running: test_avg_duration_none")
        print(e)

    try:
        test_avg_duration_zero()
    except Exception as e:
        print("Ran into an issue while running: test_avg_duration_zero")
        print(e)

    print(".................................")
    
    print("Testing movie_title_list() function")
    try:
        test_movie_title_list()
    except Exception as e:
        print("Ran into an issue while running: test_avg_duration_zero")
        print(e)
    print(".................................")
    
if __name__ == "__main__":
    main()
