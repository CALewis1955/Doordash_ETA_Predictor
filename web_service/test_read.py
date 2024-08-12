import os

print(os.getcwd())


def read_text(file):
    with open(file, "r", encoding="utf-8") as f_in:
        return f_in.read().strip()


print(read_text("./web_service/LOGGED_MODEL.txt"))
