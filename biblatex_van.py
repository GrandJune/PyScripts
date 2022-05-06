# -*- coding: utf-8 -*-
# @Time     : 5/6/2022 19:55
# @Author   : Junyi
# @FileName: biblatex_van.py
# @Software  : PyCharm
# Observing PEP 8 coding style

# Transfer the two-word surname into correct format of {von Hippel}

file_name = "references.bib"
data = []
with open("references.bib", "r", encoding="utf-8") as infile:
    reader = infile.readlines()
    for each in reader:
        data.append(each)

for index, each in enumerate(data):
    if "author = " in each:
        print("original string: ", each)
        each = each.replace("    author = {", "").replace("},\n", "")
        persons = each.split(" and ")
        print("persons: ", persons)  # ['Franke, Nikolaus', 'Keinz, Peter', 'Klausberger, Katharina']
        first_names = [person.split(",")[0] for person in persons]
        second_names = [person.split(",")[1] for person in persons]
        print("first name before", first_names)  # ['Franke', 'Keinz', 'Klausberger']
        for index_2, surname in enumerate(first_names):
            if " " in surname:
                surname_2 = list(surname)
                surname_2[0] = surname_2[0].lower()
                first_names[index_2] = "{" + "".join(surname_2) + "}"
        print("first name after: ", first_names)  # ['Franke', 'Keinz', 'Klausberger']
        persons = [first_name + "," + second_name for first_name, second_name in zip(first_names, second_names)]
        data[index] = "    author = {" + " and ".join(persons) + "},\n"
        print("person after: ", data[index])

# print("result: ", data)
with open("references_final.bib", "w", encoding="utf-8") as outfile:
    writer = outfile.writelines(data)
