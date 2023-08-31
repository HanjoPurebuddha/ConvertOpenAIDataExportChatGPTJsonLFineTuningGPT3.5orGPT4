# Convert OpenAI DataExport Chat GPT JsonL FineTuning Converter GPT3.5orGPT4
This a repository for converting your OpenAI data exports into jsonL format for fine-tuning a 3.5 model. These jsonL scripts can be used following the OpenAI API fine-tuning docs.  https://platform.openai.com/docs/guides/fine-tuning  

**OpenAI Data Export Conversion Tool**

This tool converts a set of conversation.json files (downloaded from OpenAI Data Export) into a single jsonl file that can be used for fine-tuning GPT-3.5.

**Why is this useful?**

By converting your OpenAI Data Export files into a single jsonl file, you can use this data to fine-tune GPT-3.5 and generate models that are closer to your experience. This allows you to take back power by using your data to create your own models that suit you.

**How does it work?**

This tool uses a Python script to automatically convert all conversation.json files in a specified data folder into a single jsonl file. The resulting jsonl file can then be used as input for fine-tuning GPT-3.5.

**Installation**
To use this tool, you will need to have Python installed on your computer. You can download and install Python from the official Python website.

Once you have Python installed, you can download or clone this repository to your computer.

**Super beginniner guide**
To use this tool, navigate to the directory where you downloaded or cloned this repository and run the following command:

_python main.py_

This will convert all conversation.json files in the specified data folder into a single jsonl file named output.jsonl. You can run commands by opening the command line (cmd) and navigating to the folder where main.py is using CD (in Windows) 
_
cd "location_of_main.py_"

If it's on another drive like the D drive and you're on the C drive, you have to type that in separately

_D:_



**Contributing**
Contributions are welcome! If you have any ideas for improving this tool or adding new features, please feel free to submit a pull request or open an issue.

I hope this GitHub open source project meets your needs. Let me know if you have any questions or if there’s anything else I can help with. 😊
