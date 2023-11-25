from string_path import shortest_string_path
from pprint import pprint

pprint(shortest_string_path("cat", "latest", {"cat": True, "cate": True, "cates": True, "cato": True, "lates": True, "lutes": True}))