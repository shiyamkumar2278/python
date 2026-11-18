from attendance.reader import read_rows
from attendance.stats import percentage
from attendance.report import write_report

if __name__ == "__main__":
    print("Attendance package is ready.")
    print("Example percentage:", percentage(18,20))
