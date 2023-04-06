import openai
import yaml
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
    prompt = prompt.strip()
    if not prompt:
        continue

    generated_text = ''
    new_prompt = prompt

    # Generate tokens one at a time
    while len(generated_text) < params["max_tokens"]:
        response = openai.Completion.create(
            engine=config["openai"]["engine"],
            prompt=new_prompt,
            temperature=params["temperature"],
            max_tokens=10,
            top_p=params["top_p"],
            frequency_penalty=params["frequency_penalty"],
            presence_penalty=params["presence_penalty"],
        )

        token = response.choices[0].text.strip()
        #print(f"Response: {response}")
        #print(f"Token: {token}")
        generated_text += token

        # Append the generated token to the new prompt
        new_prompt = f"{new_prompt}{token}"

        # Break the loop if there's no more output or a newline is reached
        if not token or token == '\n':
            break

    # Print the prompt and the generated response
    print(f"Prompt: {prompt}")
    print(f"Response: {generated_text}")
    print("\n" + "=" * 80 + "\n")

