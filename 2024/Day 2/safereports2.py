def is_report_increasing(levels):
    for i in range(len(levels) - 1):
        difference = levels[i + 1] - levels[i]
        if not (1 <= difference <= 3):
            return False
    return True

def is_report_decreasing(levels):
    for i in range(len(levels) - 1):
        difference = levels[i] - levels[i + 1]
        if not (1 <= difference <= 3):
            return False
    return True

def is_report_safe(levels):
    return is_report_increasing(levels) or is_report_decreasing(levels)

def is_report_safe_with_dampener(levels):
    for i in range(len(levels)):
        modified_report = levels[:i] + levels[i + 1:]
        if is_report_increasing(modified_report) or is_report_decreasing(modified_report):
            return True
    return False

def count_safe_reports(file_path):
    safe_report_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            levels = list(map(int, line.strip().split()))
            if is_report_safe(levels) or is_report_safe_with_dampener(levels):
                safe_report_count += 1

    return safe_report_count

def main():
    file_path = "day2data.txt"
    num_safe_reports = count_safe_reports(file_path)
    print(f"Number of safe reports: {num_safe_reports}")

if __name__ == "__main__":
    main()
