import openai
import yaml
import requests
import os

# Read the config.yaml file
with open("config.yaml", "r") as yaml_file:
    config = yaml.safe_load(yaml_file)

# Set up the OpenAI API client
openai.api_key = config["openai"]["api_key"]

# Read the prompts from prompts.txt
with open("prompts.txt", "r") as prompts_file:
    prompts = prompts_file.readlines()

# Set the parameters from config.yaml
params = config["params"]

# Iterate through the prompts and call the OpenAI API
for prompt in prompts:
    response = openai.Completion.create(
        engine=config["openai"]["engine"],
        prompt=prompt.strip(),
        temperature=params["temperature"],
        max_tokens=params["max_tokens"],
        top_p=params["top_p"],
        frequency_penalty=params["frequency_penalty"],
        presence_penalty=params["presence_penalty"],
    )
    #print(f"Response: {response}")

    # Print the prompt and the generated response
    print(f"Prompt: {prompt.strip()}")
    print(f"Response: {response.choices[0].text.strip()}")
    print("\n" + "=" * 80 + "\n")
