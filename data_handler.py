def read_date_file(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


def write_date_file(file_path, data):
    with open(file_path, "a") as file:
        file.writelines(f"{line}\n" for line in data)
