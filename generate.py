import os
import re
import gpt_util


def read_from_file(path, as_dict=True):
    with open(path, 'r') as f:
        output = f.read()
        if as_dict:
            output = convert_to_dict(output)
        return output


def convert_to_dict(input_text):
    # This pattern matches the section names and the content between them
    pattern = r'\[\[(.*?)\]\](.*?)\n(?=\[\[|\Z)'

    # Find all matches and clean the content
    matches = re.findall(pattern, input_text, flags=re.DOTALL)

    output_dict = {}
    for section, content in matches:
        # Clean up the content by removing leading/trailing whitespace and ensuring proper newline handling
        content = content.strip() + '\n'
        # Replace sequences of newlines with a single newline
        content = re.sub(r'\n+', '\n\n', content)
        # Add to the dictionary
        output_dict[section] = content

    return output_dict


#
example_endeavor = read_from_file('examples/endeavor.txt', as_dict=False)
example_response_1 = read_from_file('examples/response_1.txt')
example_response_2 = read_from_file('examples/response_2.txt')
example_response_3 = read_from_file('examples/response_3.txt')

#
client_endeavor = read_from_file('data/endeavor.txt', as_dict=False)

#
# project_path = 'data/project_1.txt'
project_path = 'data/project_2.txt'
client_project = read_from_file(project_path)

# prompt_template = read_from_file(
#     'prompts/technical_summary.txt', as_dict=False)
# prompt = prompt_template.format(
#     example_response_1_name=example_response_1['Project Name'],
#     example_response_1_technical_summary=example_response_1['Technical Summary of Work'],
#     example_response_2_name=example_response_2['Project Name'],
#     example_response_2_technical_summary=example_response_2['Technical Summary of Work'],
#     example_response_3_name=example_response_3['Project Name'],
#     example_response_3_technical_summary=example_response_3['Technical Summary of Work'],
#     client_project_name=client_project['Project Name'],
#     client_project_paper1=client_project['Paper 1'],
#     client_project_paper2=client_project['Paper 2'],
#     client_project_paper3=client_project['Paper 3'],
# )

# prompt_template = read_from_file(
#     'prompts/plain_summary.txt', as_dict=False)
# prompt = prompt_template.format(
#     example_response_1_name=example_response_1['Project Name'],
#     example_response_1_technical_summary=example_response_1['Technical Summary of Work'],
#     example_response_1_plain_summary=example_response_1['Plain Language Summary of Work'],
#     example_response_2_name=example_response_2['Project Name'],
#     example_response_2_technical_summary=example_response_2['Technical Summary of Work'],
#     example_response_2_plain_summary=example_response_2['Plain Language Summary of Work'],
#     example_response_3_name=example_response_3['Project Name'],
#     example_response_3_technical_summary=example_response_3['Technical Summary of Work'],
#     example_response_3_plain_summary=example_response_3['Plain Language Summary of Work'],
#     client_project_name=client_project['Project Name'],
#     client_project_technical_summary=client_project['Technical Summary of Work'],
# )


prompt_template = read_from_file(
    'prompts/significance_summary.txt', as_dict=False)
prompt = prompt_template.format(
    example_endeavor=example_endeavor,
    example_response_1_name=example_response_1['Project Name'],
    example_response_1_technical_summary=example_response_1['Technical Summary of Work'],
    example_response_1_plain_summary=example_response_1['Plain Language Summary of Work'],
    example_response_1_significance=example_response_1['Summary of the Significance of the Work'],
    example_response_2_name=example_response_2['Project Name'],
    example_response_2_technical_summary=example_response_2['Technical Summary of Work'],
    example_response_2_plain_summary=example_response_2['Plain Language Summary of Work'],
    example_response_2_significance=example_response_2['Summary of the Significance of the Work'],
    example_response_3_name=example_response_3['Project Name'],
    example_response_3_technical_summary=example_response_3['Technical Summary of Work'],
    example_response_3_plain_summary=example_response_3['Plain Language Summary of Work'],
    example_response_3_significance=example_response_3['Summary of the Significance of the Work'],
    client_endeavor=client_endeavor,
    client_project_name=client_project['Project Name'],
    client_project_technical_summary=client_project['Technical Summary of Work'],
    client_project_plain_summary=client_project['Plain Language Summary of Work'],
    client_project_context=client_project['Industry Context'],
)

print(prompt)

print('========================================')
response = gpt_util.request_gpt(messages=[prompt])
print(response)
