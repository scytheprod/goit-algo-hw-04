import re

def total_salary(path: str) -> tuple[:]:
    try:
        salaries= []
        with open(path, 'r', encoding="utf-8") as file:
            for lines in file:
                line = lines.split(',')
                line1 = re.sub(r"\D+,","",line[1])
                salaries.append(float(line1))
            total = sum(salaries)
            average = (total / len(salaries))
        return total, average
    except FileNotFoundError:
        print('File not found!')

total, average = total_salary("salary_info.txt")
print(f"Загальна сума заробітної плати: {total:.2f}, Середня заробітна плата: {average:.2f}")












