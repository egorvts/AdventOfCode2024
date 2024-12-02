from sys import stdin


def is_report_safe(report: list[int]):

    if (report != sorted(report)
            and report != sorted(report, reverse=True)):
        return False

    for i in range(len(report) - 1):
        if not (1 <= abs(report[i] - report[i+1]) <= 3):
            return False

    return True


def count_safe_reports(reports: list[list[int]]):
    return sum(is_report_safe(report) for report in reports)

reports = []
for line in stdin:
    reports.append(list(map(int, line.split())))

print(count_safe_reports(reports))
