import yaml
import json


with open("test1.json") as json_file:
    with open("test_yaml.yaml", "w") as yaml_file:
        json_data = str(json.load(json_file))

        yaml_data = yaml.safe_load(json_data)
        convert_yaml = yaml.dump(yaml_data)

        yaml_file.write(convert_yaml)
