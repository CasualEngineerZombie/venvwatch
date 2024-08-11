# VenvWatch

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/VenvWatch)
![PyPI](https://img.shields.io/pypi/v/VenvWatch)
![GitHub License](https://img.shields.io/github/license/CasualEngineerZombie/venvwatch)
![GitHub issues](https://img.shields.io/github/issues/CasualEngineerZombie/venvwatch)
![GitHub stars](https://img.shields.io/github/stars/CasualEngineerZombie/venvwatch?style=social)

VenvWatch is a lightweight Python package that continuously monitors your virtual environment and automatically updates your `requirements.txt` file whenever you install or uninstall a package. No more manually managing dependencies—VenvWatch does it for you in real-time!


## Features

- **Automatic Sync**: Detects changes in your virtual environment and updates `requirements.txt` instantly.
- **Continuous Monitoring**: Runs in the background, listening for any modifications to your installed packages.
- **Simple CLI**: Easy-to-use command-line interface to start and manage the watcher.
- **Configurable Options**: Customize how VenvWatch handles changes, such as removing unused dependencies.

## Installation

Install VenvWatch using pip:

```bash
pip install venvwatch
```

## Usage

### Basic Usage

To start monitoring your virtual environment, navigate to your project directory and run:

```bash
venvwatch watch
```

VenvWatch will monitor your virtual environment for any changes and update the `requirements.txt` file accordingly.

### Configuration Options

VenvWatch can be customized with a variety of command-line options:

- **`--venv`**: Specify the path to your virtual environment.
  ```bash
  venvwatch watch --venv /path/to/your/venv
  ```

- **`--interval`**: Set the interval (in seconds) for how often VenvWatch checks for changes.
  ```bash
  venvwatch watch --interval 5
  ```

- **`--no-remove`**: Disable automatic removal of dependencies that are no longer in the environment.
  ```bash
  venvwatch watch --no-remove
  ```

### Example

Start watching your virtual environment and update `requirements.txt` in real-time:

```bash
venvwatch watch --venv ./venv --interval 5
```

VenvWatch will run in the background, keeping your `requirements.txt` file perfectly synced with your installed packages.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or find any bugs, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## License

VenvWatch is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Support

If you encounter any issues or have questions, please open an issue on [GitHub](https://github.com/yourusername/VenvWatch/issues).

---

**Happy Coding!**
