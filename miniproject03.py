GLOBAL_CONFIG_VERSION = "1.0.0"

def demonstrate_scope():
    local_counter = 0
    local_counter += 1
    global GLOBAL_CONFIG_VERSION
    return f"Local Counter: {local_counter}, Global Version: {GLOBAL_CONFIG_VERSION}"

def add_record(student_id, name, marks):
    if not student_id or not isinstance(student_id, str):
        return {"error": "Invalid Student ID"}
    if not name or not isinstance(name, str):
        return {"error": "Invalid Name"}
    if not isinstance(marks, list) or not all(isinstance(m, (int, float)) for m in marks):
        return {"error": "Marks must be a list of numbers"}
    
    return {
        "student_id": student_id,
        "name": name,
        "marks": marks
    }

def calculate_total(marks):
    return sum(marks)

def calculate_average(marks):
    if not marks:
        return 0.0
    return sum(marks) / len(marks)

def get_grade(average):
    if average >= 75:
        return "Distinction"
    elif average >= 60:
        return "First Division"
    elif average >= 40:
        return "Pass"
    else:
        return "Fail"

def build_report(student_record):
    marks = student_record["marks"]
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = get_grade(average)
    
    return {
        "name": student_record["name"],
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

def get_top_students(records_dict):
    reports = [build_report(rec) for rec in records_dict.values()]
    high_performers_filter = filter(lambda r: r["average"] >= 75, reports)
    top_student_names = list(map(lambda r: r["name"], high_performers_filter))
    return top_student_names

def calculate_flexible_average(*args):
    if not args:
        return 0.0
    return sum(args) / len(args)

def generate_class_summary_options(**kwargs):
    title = kwargs.get("title", "Class Report")
    passing_mark = kwargs.get("passing_mark", 40)
    return f"--- {title} (Passing Mark: {passing_mark}) ---"

def display_student_info(student_id, name, grade="Pass"):
    return f"ID: {student_id} | Name: {name} | Grade: {grade}"

def recursive_sum(n):
    if n <= 1:
        return max(0, n)
    return n + recursive_sum(n - 1)

def main():
    print("===== STUDENT PERFORMANCE REPORT =====")
    
    records = {}
    
    rec1 = add_record("S101", "Uzma", [78, 65, 88])
    rec2 = add_record("S102", "Saniya", [35, 72, 61])
    
    if "error" not in rec1:
        records[rec1["student_id"]] = rec1
    if "error" not in rec2:
        records[rec2["student_id"]] = rec2
        
    for s_id, record in records.items():
        report = build_report(record)
        print(f"{s_id} | {report['name']} | Marks: {report['marks']}")
        print(f"Total: {report['total']} | Average: {report['average']:.2f} | Grade: {report['grade']}\n")
        
    top_performers = get_top_students(records)
    print(f"High performers (average >= 75): {top_performers}")
    
    print(generate_class_summary_options(title="Class Report", passing_mark=40))
    class_avg = calculate_flexible_average(78, 65, 88, 35, 72, 61)
    print(f"class average: {class_avg:.2f}")
    
    print(f"Recursive sum from 1 to 5: {recursive_sum(5)}")
    print(f"Recursive sum from 1 to 3: {recursive_sum(3)}")
    print(f"Recursive sum from 1 to 10: {recursive_sum(10)}")
    
    print("\n----- Argument Styles Demonstration -----")
    print("1. positional argument call:", display_student_info("s103", "Bilal", "Distinction"))
    print("2. keyword argument call:", display_student_info(name="Sofiya", student_id="s104", grade="First Division"))
    print("3. default argument call:", display_student_info("s105", "Faisal"))

if __name__ == "__main__":
    main()