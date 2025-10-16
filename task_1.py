# fh = open('text_task_1.txt', 'w+')
# text_written = fh.write("""Alex Korp,3000
# Nikita Borisenko,2000
# Sitarama Raju,1000""")
# print(text_written)
# fh.close()


def total_salary(path):
    salary_list = []
    
    with open(path, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            line = line.strip()
            line_list = line.split(',')
                
            if not line:
                break
                
            salary_list.append(int(line_list[1]))
                
    total_salary = sum(salary_list)
    average_salary = sum(salary_list) / len(salary_list)
    salary_tuple = (total_salary, average_salary)
    
    return salary_tuple
    
try:
    total, average = total_salary("text_task_1.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
except FileNotFoundError:
    # Handle the case where the file is not found
    print("Error: The specified file was not found.")    