# string_path

A simple module that returns the path between two strings through words in a given dictionary, where each step in the path has an edit distance of 1 (only adds, removes, or changes a single character).

To get started, clone this repository and run `pip install` the root directory. This will install the project's dependencies. You can then run `example.py`.

## API

Using the module means calling the method `shortest_string_path(from: str, to: str, words: Dict[str, bool])`. The parameters are as follows:

- *from* - The word to start tracing a path from.
- *to* - The word to find a path to.
- *words* - A dictionary of words that will be used to trace a path. The value of each key must be `True` or else it will be ignored.