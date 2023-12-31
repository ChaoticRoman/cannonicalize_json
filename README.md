# Cannonicalize JSON

## Motivation

Working with JSON files can often lead to various representations of the same
structural data due to differences in spacing, ordering of keys, and other
formatting nuances. The primary motivation behind these scripts is to provide
tools for:

- **Pretty Printing**: Humans often prefer well-formatted, indented JSON files
  for readability and easier understanding. `prettify.py` provides this by
  formatting the JSON in a consistent (keys in objects are sorted) and human-readable
  (indent of four and single space between JSON separators) manner.

- **Compactifying for Embedded Development**: In scenarios like embedded development
  where storage space might be at a premium, it's advantageous to have JSON data
  in the most compact form possible. `compactify.py` assists in converting
  any JSON file to this compact representation with sorted keys.

- **Diffing between JSONs**: When dealing with multiple JSON files of the same structure
  but with different data, it's often essential to see the differences. Having a canonical
  representation allows for more meaningful `diff` operations, emphasizing the data changes
  rather than format variations.

This repository provides two Python scripts that manipulate JSON files:

1. `prettify.py`: Formats a JSON file with sorted keys and an indentation of 4 spaces.
2. `compactify.py`: Converts a JSON file into its most compact representation by removing
  unnecessary whitespace.

## Prerequisites

- Python 3.x

## Usage

**Important Note:** Both scripts modify the JSON files **in place**. This means
that the original content of the file will be replaced with the formatted
or compactified version. Make sure to back up your data or use version control
before running these scripts if you want to keep the original format.

### `prettify.py`

To canonicalize a JSON file to pretty human readable form suitable for line based diff, run:

```
$ ./prettify.py <path_to_json_file>
```

This will format the content of the file with sorted keys and an indentation of 4 spaces.

### `compactify.py`

To compactify a JSON file, run:

```
$ ./compactify.py [path_to_json_file]
```

This will convert the content of the file into its most compact representation.

## Contributing

If you wish to contribute, report bugs, or suggest improvements, feel free to open an issue
or create a pull request.

## License

This project is open-source and available under the MIT License.
