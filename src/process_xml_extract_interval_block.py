from lxml import etree

input_file = 'intervals_10203040.xml'
output_file = 'intervals_10203040_processed.xml'

def extract_interval_block(input_file_path, output_file_path):
    """
    Extracts specific <entry> sections from an input XML file and saves them to an output file,
    focusing specifically on entries that contain IntervalBlock data.

    Parameters:
    - input_file_path: Path to the input XML file.
    - output_file_path: Path where the output XML content should be saved.
    """
    # Parse the input XML file
    tree = etree.parse(input_file_path)
    root = tree.getroot()

    # Define the Atom and ESPI namespaces
    namespaces = {
        'atom': 'http://www.w3.org/2005/Atom',
        'espi': 'http://naesb.org/espi'
    }

    # Initialize a list to hold entries that contain IntervalBlock
    interval_entries = []

    # Iterate over all entry elements
    for entry in root.findall('.//atom:entry', namespaces=namespaces):
        # Check if entry contains an IntervalBlock
        if entry.find('.//espi:IntervalBlock', namespaces=namespaces) is not None:
            interval_entries.append(entry)

    # Check if IntervalBlock entries are found; if not, print a message
    if not interval_entries:
        print("No IntervalBlock entries found. Check namespaces and XML structure.")

    # Convert each filtered entry to a string and concatenate
    entries_xml = "".join([etree.tostring(entry, pretty_print=True, encoding="UTF-8").decode() for entry in interval_entries])

    # Write the concatenated entry elements to the output file
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(entries_xml)


# run script
extract_interval_block(input_file, output_file)
