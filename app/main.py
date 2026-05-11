def copy_file(command: str) -> None:
    file_name = command.split()
    try:
        if (file_name[1] != file_name[2]) and file_name[0] == "cp":
            with (open(file_name[1], "r") as file_in,
                  open(file_name[2], "w") as file_out):
                read_content = file_in.read()
                file_out.write(read_content)
    except FileNotFoundError:
        print(f"File {file_name[1]} does not exist")
    except IndexError as e:
        print(f"An error occured {e}")
