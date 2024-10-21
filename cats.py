def get_cats_info(path: str) -> list[:]:
    try:
        with open(path, 'r', encoding="utf-8") as file:
            cats_info_list = []
            for line in file:
                line = line.split(",")
                cats = {}
                cats["id"] = line[0]
                cats["name"] = line[1]
                cats["age"] = line[2].replace("\n", '')
                cats_info_list.append(cats)
    except FileNotFoundError:
        print("File not found!")
    return cats_info_list
print(get_cats_info("cats_file.txt"))




