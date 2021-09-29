from os import listdir, path, getcwd, chdir

PWD = getcwd()

def is_markdown(entry: str) -> bool:
    if path.isfile(entry):
        # it's the top level README
        if entry == "README.md" and getcwd() == PWD:
            return False
        if entry[len(entry)-3:] == ".md":
            return True
    return False

def is_dir(entries: list[str]) -> list[str]:
    return [entry for entry in entries if path.isdir(entry) and entry[0] != "."]

def is_file(entries: list[str]) -> list[str]:
    return [entry for entry in entries if path.isfile(entry) and entry[0] != "."]

def replace_underscore(s: str) -> str:
    sum = ""
    for char in s:
        if char == "_":
            sum += "-"
        else:
            sum += char 
    return sum


def write_markdown_index(dir: str):
    index = ""

    if path.isdir(dir):
        chdir(path.abspath(dir))
    else:
        raise NotADirectoryError

    for entry in listdir():
        if is_markdown(entry):
            name = replace_underscore(entry[:len(entry)-3])
            index += f"##### [{name}](./{entry})\n"
    open("README.md", "w").write(index)
    chdir(PWD)


def main():
    open("README.md", 'w').write("# Index\n")
    handle = open("README.md", 'a')

    handle.write("### Categories\n")

    for dir in is_dir(listdir()):
        handle.write(f"\n#### [{dir}](./{dir}/README.md)")
        write_markdown_index(dir)

    handle.write("\n\n### Individual\n")

    for file in is_file(listdir()):
        if is_markdown(file):
            handle.write(f"\n##### [{file[:len(file)-3]}](./{file})")

if __name__ == "__main__":
    main()
