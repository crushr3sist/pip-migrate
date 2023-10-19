import os
import pathlib
import sys

req_file_path = pathlib.Path("pip_reqs.txt")

package_records = req_file_path if req_file_path.is_file() else None


def create():
    try:
        with open(req_file_path, "x") as f:
            f.close()
        os.system(f"pip freeze > {req_file_path}")
    except Exception as e:
        print(e)


def parse():
    with open(req_file_path, "r") as pip_file:
        pip_lines = pip_file.readlines()
        filtered_strs = map(lambda x: x.split("==")[0], pip_lines)
        formatted_strs = map(lambda x: "pip install {}".format(x), filtered_strs)
    return (list(formatted_strs), list(filtered_strs))


def migrate():
    try:
        parsed_txt = parse()
        for package in parsed_txt[0]:
            os.system(str(package))
        print(
            "The following packages were migrated:\n{}".format("\n".join(parsed_txt[1]))
        )
    except Exception as e:
        raise Exception("There was an error iterating over your commands")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "before":
            if package_records:
                print(f"Your backup already exists at {req_file_path}")
                print("Please do not move or touch that file !!")
                print(
                    'Continue to install your new version of Python and run "pip-migrate after"'
                )
            else:
                create()
        elif sys.argv[1] == "after":
            migrate()
        else:
            print("Please use either 'before' or 'after' to migrate.")
            print("'pip-migrate before'  -> to backup your packages")
            print(
                "'pip-migrate after'  -> to migrate your packages after a new install"
            )
    else:
        print("Usage: pip-migrate [before|after]")
