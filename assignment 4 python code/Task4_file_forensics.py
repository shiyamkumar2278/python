from pathlib import Path

def save_returns(books, log_name="returns.log"):
    with open(log_name, "a", encoding="utf-8") as log:
        for book in books:
            log.write(book.rstrip("\\n") + "\\n")

def process(day_file, log_name="returns.log", error_log="errors.log"):
    try:
        with open(day_file, encoding="utf-8") as f:
            books=f.readlines()
        save_returns(books, log_name)
    except (FileNotFoundError, PermissionError, UnicodeDecodeError) as exc:
        with open(error_log, "a", encoding="utf-8") as err:
            err.write(f"{day_file}: {type(exc).__name__}: {exc}\\n")

if __name__ == "__main__":
    for i in range(1,4):
        Path(f"day{i}.txt").write_text(f"Book returned on day {i}\\n", encoding="utf-8")
        process(f"day{i}.txt")
    print(Path("returns.log").read_text(encoding="utf-8"))
