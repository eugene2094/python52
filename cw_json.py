import json
import os

capitals = {
    "Italy": 'Rome',
    "Spain": "Madrid",
    "Germany": "Berlin"
}

print(capitals)

serialized_capitals = json.dumps(capitals)
print(f"JSON capitals: {serialized_capitals}")

deserialized_capitals = json.loads(serialized_capitals)
print(f"deserialized cap: {deserialized_capitals}")


def create_path(file_name):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(script_dir, file_name)


def json_serialized(file_name, data):
    path = create_path(file_name)
    with open(path, 'w') as file:
        json.dump(data, file,indent=4)


def json_deserialized(file_name):
    path = create_path(file_name)
    with open(path, 'r') as file:
        data = json.load(file)
    return data


try:
    file_name = "employee.json"

    employees_dict = {
        "company": "Microsoft",
        "employees": [
            {
                'name': "Bill",
                'age': 44,
                "department": "Sales"
            },
            {
                'name': "Djon",
                'age': 34,
                "department": "Manager"
            }
        ]
    }

    json_serialized(file_name, employees_dict)
    print(json_deserialized(file_name))

except Exception as e:
    print(e)
