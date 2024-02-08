def total_salary(path):
    salary_mass = []
    count = 0
    try:
        with open(path, 'r') as file:
            for line in file.readlines():
                line = line.split(',')
                salary_mass.append(int(line[1]))
                count += 1
            ttl = sum(salary_mass)
            avg = sum(salary_mass) // count
        return ttl, avg
    except:
        print("blablabla")
    




total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")