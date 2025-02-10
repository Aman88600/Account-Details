import json

# New Entry
def new_entry():
    sections = {}
    entry_name = 'entry_name'#input("Entry Name : ")
    entry_sections = int(input("How many sections in entry :"))
    for i in range(entry_sections):
        section_name = f'section_name{i}'#input("Enter Section Name :")
        section_data = f'section_data{i}'#input("Enter Section Data :")
        sections[section_name] = section_data
    return sections, entry_name

def put_data(entry_name, entry):
    file = open('data.json', 'r')
    data = json.load(file)
    file.close()
    file = open('data.json', 'w')
    data[entry_name] = entry
    json.dump(data, file, indent=4)
    file.close()