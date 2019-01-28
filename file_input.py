import json
import sys

# parse a json file for given commands
def parse_file(filepath):
        data = []
        with open(filepath, 'r') as file_obj:
                file_data = json.load(file_obj)

                # conc = concurrent set of commands
                for conc in file_data:
                        row = []

                        # key being pressed
                        if conc["type"] == "key":
                                for keys in conc["cmd"]:
                                        row.append([ keys["dur"], keys["key"] ])
                                data.append([ conc["type"], row, conc["num"] ])

                        # comment being printed on console
                        elif conc["type"] == "comment":
                                data.append([conc["type"], conc["cmd"]])

                        else:
                                sys.exit("invalid input: json error")

        return data
