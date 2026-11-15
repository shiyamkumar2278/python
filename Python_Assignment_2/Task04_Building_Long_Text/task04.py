"""TASK 4 – Building Long Text: + or join()?
Problem Context: Monthly SMS Bill Statement
"""

import time
from io import StringIO


def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text


def build_join(parts):
    return "".join(p + ";" for p in parts)


def build_fstring(parts):
    lines = []
    for p in parts:
        lines.append(f"{p};")
    return "".join(lines)


def build_stringio(parts):
    output = StringIO()
    for p in parts:
        output.write(p)
        output.write(";")
    return output.getvalue()


def experiment():
    sizes = [1000, 10000, 200000]

    for size in sizes:
        items = [f"Item{i}:Rs{i % 50}" for i in range(size)]
        plus_times = []
        join_times = []
        fstring_times = []

        for _ in range(3):
            start = time.perf_counter()
            a = build_plus(items)
            plus_times.append(time.perf_counter() - start)

            start = time.perf_counter()
            b = build_join(items)
            join_times.append(time.perf_counter() - start)

            start = time.perf_counter()
            c = build_fstring(items)
            fstring_times.append(time.perf_counter() - start)

        print("\\nNumber of lines:", size)
        print("Plus and Join same:", a == b)
        print("Join and F-string same:", b == c)
        print("Length:", len(b))
        print("Average += time:", sum(plus_times) / 3)
        print("Average join time:", sum(join_times) / 3)
        print("Average f-string time:", sum(fstring_times) / 3)


if __name__ == "__main__":
    print("Complete Program – 200,000 Records")
    items = [f"Item{i}:Rs{i % 50}" for i in range(200_000)]

    start = time.perf_counter()
    a = build_plus(items)
    t_plus = time.perf_counter() - start

    start = time.perf_counter()
    b = build_join(items)
    t_join = time.perf_counter() - start

    start = time.perf_counter()
    c = build_fstring(items)
    t_fstring = time.perf_counter() - start

    print("Plus and Join same:", a == b)
    print("Join and F-string same:", b == c)
    print("Length:", len(b))
    print("+= time:", t_plus)
    print("join time:", t_join)
    print("f-string time:", t_fstring)

    print("\\nExperimental Investigation")
    experiment()

    print("\\nAlternative Concept – io.StringIO")
    print(build_stringio(["Tea", "Coffee", "Milk"]))

    print("\\nAlternative – Direct File Writing")
    items = ["Tea", "Coffee", "Milk"]
    with open("statement.txt", "w", encoding="utf-8") as file:
        for item in items:
            file.write(item + ";")
    print("Statement written to statement.txt")
