OUTPUT_DIRECTORY = "./Output/ReadyToSend/"
NAMES_FILENAME = "./Input/Names/invited_names.txt"
TEMPLATE_FILENAME = "./Input/Letters/starting_letter.txt"
PLACEHOLDER = "[name]"

with open(NAMES_FILENAME, "r") as file1:
    names = file1.readlines()

for name in names:
    stripped_name = name.strip()
    file_name = f'{OUTPUT_DIRECTORY}letter_for_{stripped_name}.txt'

    with open(TEMPLATE_FILENAME) as file2:
        template = file2.read()
    template = template.replace(PLACEHOLDER, stripped_name)

    with open(file_name, "w") as file3:
        file3.write(template)
