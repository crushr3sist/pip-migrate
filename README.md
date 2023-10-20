# pip-migrate

**pip-migrate** is a Python command-line tool that simplifies the process of backing up and migrating Python packages. This tool allows you to create a backup of your installed packages, and later, after installing a new Python environment, restore those packages with ease.

![GitHub](https://img.shields.io/github/license/crushr3sist/pip-migrate)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/crushr3sist/pip-migrate)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/crushr3sist/pip-migrate/CI)
![Repo Stars](https://img.shields.io/github/stars/crushr3sist/pip-migrate?style=social)

## Features

- **Backup Packages**: Create a backup of your currently installed Python packages.
- **Migrate Packages**: Restore your packages on a new Python environment.
- **Clean Up**: Remove the backup and list the migrated packages.
- **Progress Bar**: Visualize the backup and migration progress with a progress bar.
- **Better Logging**: Improved logging with error messages and successes recorded in a log file.
- **Backup Location Customization**: Customize the backup file location.
- **Dependency Resolution**: Handle package dependencies during migration.
- **Append Migration Packages**: Append packages to migrate by providing a comma-separated list.

## Installation

You can install **pip-migrate** using pip:

```bash
pip install pip-migrate
```

## Usage

### Create a Backup

Before installing a new version of Python or making major changes, create a backup of your existing packages.

```bash
pip-migrate before
```

### Migrate Packages

After setting up your new Python environment, use the following command to migrate your packages from the backup:

```bash
pip install pip-migrate

pip-migrate after

pip-migrate cleanup # optional
```

You can also append additional packages to migrate:

```bash
pip-migrate after package1,package2,package3
```

### Cleanup

If you want to remove the backup and list the migrated packages, you can use the following command:

```bash
pip-migrate cleanup
```

## Contributing

If you would like to contribute to this project, please check the CONTRIBUTING.md file for guidelines.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
