import json
import random
import sys


# Function to randomly select one value from each array
def random_element_selection(element_options):
    selected_elements = {}
    for key, values in element_options.items():
        selected_elements[key] = random.choice(values)
    return selected_elements


def generate_json(template_path, output_json_path):
    # Reading the template JSON file
    with open(template_path, 'r') as file:
        template_json_data = file.read()

    # Parsing the template JSON file
    template_json = json.loads(template_json_data)

    # Extracting the arrays of possible values for each element
    element_options = template_json["elements"]

    # Generating a new JSON object similar to the second file
    new_json = {
        "p": template_json["p"],
        "metaverse": template_json["metaverse"],
        "op": "mint",  # Setting 'op' to 'mint'
        "tick": template_json["tick"],
        "elements": random_element_selection(element_options)
    }

    # Writing the generated JSON to a file
    with open(output_json_path, 'w') as file:
        json.dump(new_json, file, indent=None, separators=(',', ':'))


# Example usage


# 配置
argList = sys.argv
json_template_file_path = str(argList[1])  # 读取Json template 文件, 比如 Humanoid_DragonBlood.json
number_of_json_to_generate = int(argList[2])  # 读取要生成的Json数量, 比如 10

for i in range(1, number_of_json_to_generate + 1):
    generate_json(json_template_file_path,
                  'generated_json/' + json_template_file_path.replace('.json', '') + str(i) + '.json')
