import re

def total_salary(path: str) -> tuple[:]:
    try:
        salaries = []
        with open(path, 'r', encoding="utf-8") as file:
            for line in file:
                line = re.sub(r'\D', "", line)
                if int:
                    salaries.append(int(line))
            total = sum(salaries)
            average = total // len(salaries)
        return total, average
    except FileNotFoundError:
        print('File not found!')

total, average = total_salary("salary_info.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")












