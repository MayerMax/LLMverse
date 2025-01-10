from openai import OpenAI
import os

def basic_response_generation(system_message, prompt, utt_id, output_dir, api_key, model_name, skip_if_exist=True) -> str:
    """
    simple wrapper around openAI client to generate response
    """
    client = OpenAI(api_key=api_key)
    assert os.path.exists(output_dir), f'Proivded output dir, {output_dir} should exist'
    output_path = f'{output_dir}/{utt_id}.txt'

    if skip_if_exist and os.path.exists(output_path):
        with open(output_path, 'r') as f:
            return f.read()
    else:
        completion = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "developer", "content": system_message},
                {"role": "user","content": prompt}
                ])
        with open(output_path, 'w') as f:
            f.write(completion.choices[0].message.content)
        return completion.choices[0].message.content
