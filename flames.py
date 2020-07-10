# global variables

name1 = None
name2 = None
names_length = 0
flames_list = ['Friend', 'Lover', 'Affectionate',
               'Marriage', 'Enemy', 'Sister']

# function to ask name


def ask_names():
    global name1, name2
    name1 = input("Enter your name: ").lower()
    name2 = input("Enter another name: ").lower()
    return name1, name2


# function to format the names
def format_names():
    global name1, name2
    name1 = name1.replace(" ", "")
    name2 = name2.replace(" ", "")
    return name1, name2


# function to find the same characters in the name and strike it out
def find_similar_char():
    global name1, name2
    for i in name1:
        for j in name2:
            if i == j:
                name1 = name1.replace(i, "", 1)
                name2 = name2.replace(j, "", 1)
                break
    print(name1)
    print(name2)
    return name1, name2


# function to find length of combination of name1 and name2
def find_length_of_names():
    global name1, name2, names_length
    names_length = len(name1 + name2)
    print(names_length)


# function to iterate over flames
def put_flames():
    global name1, name2, names_length, flames_list
    if names_length > 0:
        while len(flames_list) > 1:
            count = names_length % len(flames_list)
            remove_index = count - 1
            if remove_index >= 0:
                left = flames_list[:remove_index]
                right = flames_list[remove_index+1:]
                flames_list = right + left
            else:
                flames_list = flames_list[:len(flames_list)-1]
        print(f'Relationship between {name1} and {name2}:{flames_list[0]}')
    else:
        print("Enter different names")


ask_names()
format_names()
find_similar_char()
find_length_of_names()
put_flames()
