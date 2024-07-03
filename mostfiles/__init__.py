import argparse
import os

dirs = list()

def count_files(path, recursive=False, hidden=False, count_dir=False):
    """
    Counts the number of files in a directory.
    
    Args:
        directory (str): The path of the directory.
        recursive (bool): If True, counts files in all subdirectories recursively.
    
    Returns:
        int: The number of files in the directory.
    """
    file_count = 0
    try:
        for entry in os.listdir(path):
            if entry.startswith('.') and not hidden:
                continue

            full_path = os.path.join(path, entry)
            if os.path.isfile(full_path):
                file_count += 1
            elif os.path.isdir(full_path):
                if count_dir:
                    file_count += 1
                sub_count = count_files(full_path, recursive)
                if recursive:
                    file_count += sub_count
    except PermissionError:
        pass

    dirs.append((path, file_count))
    return file_count

# Example usage:
# directory_path = "path/to/directory"
# print(count_files(directory_path, recursive=True))

__version__ = "0.0.3"

def get_args():
    parser = argparse.ArgumentParser(
        description="count files in each directory",
        epilog=None)
    
    parser.add_argument("path", default='.', nargs='?', help="path to directory")
    parser.add_argument("-r", "--recursive", default=False, action='store_true', help="recursive mode")
    parser.add_argument("-d", "--dir", default=False, action='store_true', help="directory counted as file too")
    parser.add_argument("-a", "--all", default=False, action='store_true', help="include hidden files/directories")
    parser.add_argument("-m", "--min", default=None, type=int, help="print only directories with N+ files")

    return parser.parse_args()

def main():
    global dirs
    args = get_args()
    n = count_files(path=args.path, recursive=args.recursive, hidden=args.all, count_dir=args.dir)

    dirs = sorted(dirs, key=lambda x: x[1], reverse=True)

    for d in dirs:
        if args.min is not None and d[1] < args.min:
            break
        print(f"{d[1]} {os.path.relpath(d[0])}")

if __name__ == '__main__':
    main()
