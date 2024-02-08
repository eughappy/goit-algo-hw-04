def get_cats_info(path):
    list_of_cats = []
    try:
        with open(path, 'r') as file:
            for line in file.readlines():
                line = line.split(',')
                list_of_cats.append({"id":line[0], "name":line[1], "age":int(line[2])})
        return list_of_cats
    except:
        print("No such file in directory\\file is damaged. Try one more time.")
    



cats_info = get_cats_info("cats_file.txt")
print(cats_info)