def print_cur_list(t_list):
    print("To-do list:")
    for x in t_list:
        print(x)
def print_done(d_list):
    print("Done list:")
    for x in d_list:
        print(x)
def add_item(t_list):
    t_list.append(input("What do you need to do:\n"))
def done_item(t_list, done_list):
    done = input("Which task did you complete?\n")
    t_list.remove(done)
    done_list.append(done)

def todo_list():
    print("Welcome to your To-do list!")
    to_do_list = []
    done_list = []
    for _ in range(10000):
        print("Options: \n\
    - Check your to-do list [1]\n\
    - Check your done list [2]\n\
    - Add item to do [3]\n\
    - Mark item as done [4]\n\
    - Exit [5]")
        match int(input()):
            case 1:
                print_cur_list(to_do_list)
            case 2:
                print_done(done_list)
            case 3:
                add_item(to_do_list)
            case 4:
                done_item(to_do_list, done_list)
            case 5:
                exit()

todo_list()