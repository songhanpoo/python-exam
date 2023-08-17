import requests
import json

def clean_json_data():
    # Perform GET request
    response = requests.get("https://coderbyte.com/api/challenges/json/json-cleaning")
    data = response.json()
    print(data)
    # Clean the JSON object
    cleaned_data = clean_object(data)

    # Print the modified object as a string
    modified_object_string = json.dumps(cleaned_data)
    print(modified_object_string)

def clean_object(obj):
    if isinstance(obj, dict):
        cleaned_dict = {}
        for key, value in obj.items():
            if is_valid_value(value):
                cleaned_value = clean_object(value)
                cleaned_dict[key] = cleaned_value
        return cleaned_dict
    elif isinstance(obj, list):
        cleaned_list = []
        for item in obj:
            if is_valid_value(item):
                cleaned_item = clean_object(item)
                cleaned_list.append(cleaned_item)
        return cleaned_list
    else:
        return obj

def is_valid_value(value):
    invalid_values = ["N/A", "-", ""]
    return value not in invalid_values

# Call the function to clean the JSON data
clean_json_data()