# fh = open('cats_file.txt', 'w+')
# text_written = fh.write("""60b90c1c13067a15887e1ae1,Tayson,3
# 60b90c2413067a15887e1ae2,Vika,1
# 60b90c2e13067a15887e1ae3,Barsik,2
# 60b90c3b13067a15887e1ae4,Simon,12
# 60b90c4613067a15887e1ae5,Tessi,5""")
# print(text_written)
# fh.close()


def get_cats_info(path):
    cats_list = []
    
    with open(path, 'r', encoding='utf-8') as file:
        while True:
            cat_dict = {}
            line = file.readline()
            line = line.strip()
            line_list = line.split(',')
                
            if not line:
                break
            
            cat_dict["id"] = line_list[0]   
            cat_dict["name"] = line_list[1]   
            cat_dict["age"] = line_list[2]   
            
            cats_list.append(cat_dict)
                
    return cats_list

try:
    cats_info = get_cats_info("cats_file.txt")
    print(cats_info)
except FileNotFoundError:
    # Handle the case where the file is not found
    print("Error: The specified file was not found.")    