# change 'assignment2C_solutions' to the name of your file
import recursive_problems_2 as asgmt
import numpy as np

def test_move_max_rec():
    try:
        test = np.array([1, 5, 3, 8, 4, 4])
        solution = np.array([1, 3, 5, 4, 4, 8])
        result = asgmt.move_max_rec(test.copy())
        if np.array_equal(result, solution): 
            print('Passed test_move_max_rec')
        else : 
            print("Failed test_move_max_rec")
            print("Expected: ", solution)
            print("Received: ", result)
    except Exception as e:
        print("Something went wrong running test_move_max_rec:")
        print(f"  {type(e).__name__}: {e}")
            
def test_move_max_rec_last():
    try:
        test = np.array([1, 5, 3, 8, 4, 4])
        solution = np.array([1, 3, 5, 4, 4, 8])
        result = asgmt.move_max_rec(test.copy())
        if np.array_equal(result[-1], solution[-1]): 
            print('Passed test_move_max_rec_last_element')
        else : 
            print("Failed test_move_max_rec_last_element")
            print("Expected: ", solution[-1])
            print("Received: ", result[-1])
    except Exception as e:
        print("Something went wrong running test_move_max_rec_last:")
        print(f"  {type(e).__name__}: {e}")
        
        
def test_move_max_rec_empty():
    try:
        test = np.array([])
        result = asgmt.move_max_rec(test.copy())
        if np.array_equal(result, np.array([])): 
            print('Passed test_move_max_rec')
        else : 
            print("Failed test_move_max_rec")
            print("Expected: ", np.array([]))
            print("Received: ", result)
    except Exception as e:
        print("Something went wrong running test_move_max_rec_empty:")
        print(f"  {type(e).__name__}: {e}")

def test_is_substring():
    try:
        if asgmt.is_substring("I love programming!", "ve p") == True : 
            print('Passed test_is_substring')
        else : 
            print("Failed test_is_substring")
            print("Expected: True")
            print("Received: ", asgmt.is_substring("I love programming!", "ve p"))
    except Exception as e:
        print("Something went wrong running test_is_substring:")
        print(f"  {type(e).__name__}: {e}")

def test_is_substring_wrong():
    try:
        if asgmt.is_substring("Work Hard, Party Hard", "rd, p") == False : 
            print('Passed test_is_substring_wrong')
        else : 
            print("Failed test_is_substring_wrong")
            print("Expected: False")
            print("Received: ", asgmt.is_substring("Work Hard, Party Hard", "rd, p"))
    except Exception as e:
        print("Something went wrong running test_is_substring_wrong:")
        print(f"  {type(e).__name__}: {e}")

def test_find_combination():
    try:
        if asgmt.find_combinations([1, 2, 3, 4, 5], 6) == 3 :
            print('Passed test_find_combination')
        else :
            print("Failed test_find_combination")
            print("Expected: 3")
            print("Received: ", asgmt.find_combinations([1, 2, 3, 4, 5], 6))
    except Exception as e:
        print("Something went wrong running test_find_combination:")
        print(f"  {type(e).__name__}: {e}")

def test_find_combination_no_combinations():
    try:
        if asgmt.find_combinations([1, 2, 3, 4, 5], 66) == 0 :
            print('Passed test_find_combination_no_combinations')
        else :
            print("Failed test_find_combination_no_combinations")
            print("Expected: 0")
            print("Received: ", asgmt.find_combinations([1, 2, 3, 4, 5], 66))
    except Exception as e:
        print("Something went wrong running test_find_combination_no_combinations:")
        print(f"  {type(e).__name__}: {e}")

def test_find_combination_empty():
    try:
        if asgmt.find_combinations([], 3) == 0 :
            print('Passed test_find_combination_empty')
        else :
            print("Failed test_find_combination_empty")
            print("Expected: 0")
            print("Received: ", asgmt.find_combinations([], 3))
    except Exception as e:
        print("Something went wrong running test_find_combination_empty:")
        print(f"  {type(e).__name__}: {e}")

def test_sort_array():
    try:
            
        test = np.array([1, 5, 3, 8, 4, 4])
        solution = np.array([1, 3, 4, 4, 5, 8])
        result = asgmt.sort_array(test.copy())
        if np.array_equal(result, solution):
            print('Passed test_sort_array')
        else :
            print("Failed test_sort_array")
            print("Expected: ", solution)
            print("Received: ", result)
    except Exception as e:
        print("Something went wrong running test_sort_array:")
        print(f"  {type(e).__name__}: {e}")
# Define different testing functions
def main():
    """
    Main function
    """
    print("Testing move_max_rec() function")
    test_move_max_rec()
    test_move_max_rec_empty()
    print(".................................")
    
    print("Testing is_substring() function")
    test_is_substring()
    test_is_substring_wrong()    
    print(".................................")
    
    print("Testing find_combination() function")
    test_find_combination()
    test_find_combination_no_combinations()
    test_find_combination_empty()
    print(".................................")
    
    print("Testing sort_array() function")
    test_sort_array()
    print(".................................")
    
if __name__=="__main__":    
    main()
