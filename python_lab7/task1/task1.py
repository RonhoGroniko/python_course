import json
from jsonschema import validate

def validate_json(json_file, schema_file):
    with open(json_file) as file, open(schema_file) as schema:
        try:
            validate(json.load(file), json.load(schema))
            print(f"{json_file} прошел валидацию.")
        except:
            print(f"{json_file} не прошел валидацию.")



validate_json("task1/ex_1.json", "task1/schema.json")
validate_json("task1/ex_1_invalid.json", "task1/schema.json")
