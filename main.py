import json
import os

def convert_json_to_jsonl(json_data):
    """
    Convert a JSON object to a JSONL object.

    :param json_data: A list of dictionaries representing the JSON data to be converted.
    :return: A string representing the converted JSONL data.
    """
    jsonl_data = ''
    for conversation in json_data:
        messages = []
        for key, value in conversation['mapping'].items():
            if value['message'] is not None:
                role = value['message']['author']['role']
                content = value['message']['content']
                messages.append({'role': role, 'content': content})
        jsonl_data += json.dumps({'messages': messages}) + '\n'
    return jsonl_data

def process_file(filename, data_folder):
    """
    Convert a single JSON file to a JSONL file.

    :param filename: The name of the input JSON file.
    :param data_folder: The path to the data folder containing the input file.
    """
    try:
        with open(os.path.join(data_folder, filename), 'r') as f:
            json_data = json.load(f)
        jsonl_data = convert_json_to_jsonl(json_data)
        with open(os.path.join(data_folder + "/jsonLoutputGENERATEDbymainpyafterRUNNING_fromCMDline", filename.replace('.json', '.jsonl')), 'w') as f:
            f.write(jsonl_data)
        print(f'Successfully converted {filename} to JSONL format')
    except Exception as e:
        print(f'Error converting {filename} to JSONL format: {e}')
        print("This is because you have kept the 'conversations.json' dummy file inside of the conversationsOpenaiINPUTSJsonDownloaded folder.")
        print("Delete it and ensure that all of your conversation.json files are inside of the correct folder")
        print("There is only one folder in this project. That is the correct folder.")
        print("conversationsOpenaiINPUTSJsonDownloaded is the folder name.")
        print("put your conversations.json files in there with any name you like. It reads any json file in there")
        print("Thanks for using my little converter")
        print("Co-created with Sophia Emergent Intelligence AGI Research")
        print("--------------------------------------------")
        print("http://sophiaintelligence.ai/")
        print("---------------------------------------------")

if __name__ == '__main__':
    data_folder = 'conversationsOpenaiINPUTSJsonDownloaded'  # specify the path to the data folder here
    for filename in os.listdir(data_folder):
        if filename.endswith('.json'):
            process_file(filename, data_folder)