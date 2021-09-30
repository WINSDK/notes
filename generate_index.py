from pathlib import Path

PWD = Path('.')

def is_markdown(entry: Path) -> bool:
    if entry.is_file():
        # if it's the top level README
        if entry.name == "README.md" and PWD == Path('.'):
            return False
        if entry.suffix == ".md":
            return True
    return False

def is_dir(entries) -> list[Path]:
    return [entry for entry in entries if entry.is_dir() and entry.name[0] != "."]

def is_file(entries) -> list[Path]:
    return [entry for entry in entries if entry.is_file() and entry.name[0] != "."]

def sort_path_len(entries) -> list[Path]:
    entries = [entry for entry in entries]
    lengths = [(len(entry.stem), idx) for idx, entry in enumerate(entries)]
    return [entries[idx] for _, idx in sorted(lengths)]

def path_to_relative(path: Path) -> Path:
    parts = len(Path(PWD).parts)
    new_path = Path('')
    for part in path.parts[parts:]:
        new_path /= part
    return new_path

def replace_underscore(path: Path) -> Path:
    sum = ""
    for char in path.name:
        if char == "_":
            sum += "-"
        else:
            sum += char 
    return path.with_name(sum)


def generate_markdown_subsection(dir: Path) -> str:
    index = ""

    if not dir.is_dir():
        raise NotADirectoryError

    for entry in sort_path_len(dir.iterdir()):
        if is_markdown(entry):
            entry = replace_underscore(entry)
            entry = path_to_relative(entry)
            index += f"[{entry.stem}](./{entry}) <br>\n"
    return index


def main():
    handle = open("README.md", 'w')
    for dir in is_dir(Path('.').iterdir()):
        handle.write(f"## {dir.name}\n")
        handle.write(f"{generate_markdown_subsection(dir)}\n")

    handle.write("## Individual\n")

    for file in is_file(Path('.').iterdir()):
        if is_markdown(file):
            handle.write(f"[{file.stem}](./{file}) <br>\n")

if __name__ == "__main__":
    main()
