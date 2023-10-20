import os
import pathlib
import sys
import subprocess
import logging
from progress.bar import IncrementalBar

# Set up logging
logging.basicConfig(filename="pip-migrate.log", level=logging.INFO)

req_file_path = pathlib.Path("pip_reqs.txt").absolute()


def create():
    try:
        with open(req_file_path, "x") as f:
            f.close()
        # Use subprocess to capture the output and log it
        with subprocess.Popen(["pip", "freeze"], stdout=subprocess.PIPE) as proc:
            with open(req_file_path, "wb") as f:
                bar = IncrementalBar("Creating backup", max=100)
                for line in proc.stdout:
                    f.write(line)
                    bar.next()
                bar.finish()
        logging.info("Backup completed successfully.")
        print("Backup completed successfully.")
    except Exception as e:
        logging.error(f"Error during backup: {e}")
        print(f"Error during backup: {e}")


def parse():
    try:
        with open(req_file_path, "r") as pip_file:
            pip_lines = pip_file.readlines()
            filtered_strs = list(map(lambda x: x.split("==")[0], pip_lines))
            formatted_strs = list(map(lambda x: f"pip install {x}", filtered_strs))
            return formatted_strs, filtered_strs
    except Exception as e:
        logging.error(f"Error during parsing: {e}")
        print(f"Error during parsing: {e}")
        return [], []


def fix():
    try:
        os.system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
        os.system("python get-pip.py")
        os.system("python -m pip install -U pip")

    except Exception as e:
        print(e)


def migrate(packages_to_install=None):
    try:
        parsed_txt = parse()
        packages = parsed_txt[0]
        if packages_to_install:
            packages.extend(packages_to_install)
        bar = IncrementalBar("Migrating packages", max=len(packages))
        for package in packages:
            os.system(str(package))
            bar.next()
        bar.finish()
        print("Packages have been migrated successfully:")
        print("\n".join(packages))
        logging.info("Migration completed successfully.")
    except Exception as e:
        logging.error(f"Error during migration: {e}")
        print(f"Error during migration: {e}")


def cleanup():
    try:
        parsed_txt = parse()
        os.remove(req_file_path)
        print("Cleanup completed successfully.")
        print("Packages that were migrated:")
        print("\n".join(parsed_txt[1]))
        logging.info("Cleanup completed successfully.")
    except Exception as e:
        logging.error(f"Error during cleanup: {e}")
        print(f"Error during cleanup: {e}")


def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == "before":
            if req_file_path.is_file():
                print(f"Backup already exists at {req_file_path}")
                print("Please do not move or touch that file.")
                print(
                    'Continue to install your new version of Python and run "pip-migrate after" to migrate packages.'
                )
            else:
                create()
        elif sys.argv[1] == "after":
            migrate()
        elif sys.argv[1] == "cleanup":
            cleanup()
        elif sys.argv[1] == "fix":
            fix()
        else:
            print("Please use 'before', 'after', or 'cleanup' to manage your packages.")
            print("Usage:")
            print("'pip-migrate before'  -> to create a backup of your packages")
            print(
                "'pip-migrate after'   -> to migrate your packages after a new Python install"
            )
            print(
                "'pip-migrate cleanup' -> to remove the backup and list migrated packages"
            )
    elif len(sys.argv) == 3:
        if sys.argv[1] == "after":
            packages_to_install = sys.argv[2].split(",")
            migrate(packages_to_install)
    else:
        print("Usage: pip-migrate [before|after|cleanup] [packages_to_install]")


if __name__ == "__main":
    main()
