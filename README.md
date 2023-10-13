# Cannonicalize JSON

This repository provides two Python scripts that manipulate JSON files:

1. `cannonicalize.py`: Formats a JSON file with sorted keys and an indentation of 4 spaces.
2. `compactify.py`: Converts a JSON file into its most compact representation by removing
  unnecessary whitespace.

## Prerequisites

- Python 3.x

## Usage

**Important Note: ** Both scripts modify the JSON files **in place**. This means
that the original content of the file will be replaced with the formatted
or compactified version. Make sure to back up your data or use version control
before running these scripts if you want to keep the original format.

### `cannonicalize.py`

To canonicalize a JSON file, run:

```
$ ./cannonicalize.py <path_to_json_file>
```

Example:

```
$ ./cannonicalize.py sample.json
```

This will format the content of `sample.json` with sorted keys and an indentation of 4 spaces.

### `compactify.py`

To compactify a JSON file, run:

```
$ ./compactify.py [path_to_json_file]
```

Example:

```
$ ./compactify.py sample.json
```

This will convert the content of `sample.json` into its most compact representation.

## Contributing

If you wish to contribute, report bugs, or suggest improvements, feel free to open an issue
or create a pull request.

## License

This project is open-source and available under the MIT License.
