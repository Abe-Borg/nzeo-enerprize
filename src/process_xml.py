from lxml import etree

def extract_specific_entries(input_file_path, output_file_path):
    """
    Extracts specific <entry> sections from an input XML file and saves them to an output file.

    Parameters:
    - input_file_path: Path to the input XML file.
    - output_file_path: Path where the output XML content should be saved.
    """
    # Parse the input XML file
    tree = etree.parse(input_file_path)
    root = tree.getroot()

    # Extract <entry> elements
    entries = root.findall('.//entry')  # Adjust this XPath if needed to target specific entries

    # Convert each entry to a string and concatenate
    entries_xml = "".join([etree.tostring(entry, pretty_print=True, encoding="UTF-8").decode() for entry in entries])

    # Write the concatenated entry elements to the output file
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(entries_xml)

# Example usage
input_file = 'intervals_10203040.xml'  # Update this to your input file path
output_file = 'intervals_10203040_processed.xml'  # Update this to your desired output file path
extract_specific_entries(input_file, output_file)
