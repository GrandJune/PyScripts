# -*- coding: utf-8 -*-
# @Time     : 1/17/2024 15:26
# @Author   : Junyi
# @FileName: Integrate_Reference_Lists.py
# @Software  : PyCharm
# Observing PEP 8 coding style
import re


def parse_bib_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        bib_entries = file.read()
    # Split the entries based on '@'
    entries = re.split(r'(?<=})\s*\n*\s*@', bib_entries)
    # Filter out empty strings
    entries = [entry.strip() for entry in entries if entry.strip()]
    return entries


def get_unique_identifier(entry):
    # Extract DOI or title as the unique identifier
    doi_match = re.search(r'\bdoi\s*=\s*{([^}]+)}', entry, re.IGNORECASE)
    title_match = re.search(r'\btitle\s*=\s*{([^}]+)}', entry, re.IGNORECASE)

    if doi_match:
        return doi_match.group(1)
    elif title_match:
        return title_match.group(1)
    else:
        # If neither DOI nor title is found, return the whole entry
        return entry


def integrate_references(file1_path, file2_path):
    # Parse reference lists
    entries1 = parse_bib_file(file1_path)
    entries2 = parse_bib_file(file2_path)

    # Create a set to store unique identifiers
    unique_identifiers = set()

    # Filter out duplicates and print integrated references
    integrated_references = []
    for entry in entries1 + entries2:
        identifier = get_unique_identifier(entry)
        if identifier not in unique_identifiers:
            unique_identifiers.add(identifier)
            integrated_references.append(entry)

    # Save the integrated references to a new file
    with open('references.bib', 'w', encoding='utf-8') as file:
        file.write('@' + '\n@'.join(integrated_references))


if __name__ == '__main__':
    file_1 = r"C:\Users\workshop\Music\Collective_Innovation.bib"
    file_2 = r"C:\Users\workshop\Music\My_Library.bib"
    # Replace 'file1.bib' and 'file2.bib' with the actual file paths
    integrate_references(file_1, file_2)
