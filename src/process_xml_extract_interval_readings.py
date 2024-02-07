import pandas as pd
from lxml import etree

input_file_path = 'path_to_your_xml_file.xml'

def xml_to_dataframe(input_file_path):
    """
    Reads XML data from a file, parses it to extract IntervalReading information, and 
    converts it into a pandas DataFrame.
    Parameters:
    - input_file_path: Path to the XML file.
    Returns:
    - A pandas DataFrame with IntervalReading data.
    """

    # Parse the XML file
    tree = etree.parse(input_file_path)
    root = tree.getroot()
    # Initialize an empty list to store extracted data
    data = []

    # Extract IntervalReading elements
    interval_readings = root.findall('.//{http://naesb.org/espi}IntervalReading')
    
    # Process each IntervalReading
    for i, reading in enumerate(interval_readings, start=1):
        time_period = reading.find('{http://naesb.org/espi}timePeriod')
        start = int(time_period.find('{http://naesb.org/espi}start').text)
        duration = int(time_period.find('{http://naesb.org/espi}duration').text)
        timezone = time_period.find('{http://naesb.org/espi}timezone').text
        value = int(reading.find('{http://naesb.org/espi}value').text)
        stop = start + duration
        
        # Append the extracted data to the list
        data.append({
            'start': start,
            'stop': stop,
            'timezone': timezone,
            'value': value
        })
    
    # Create a DataFrame from the extracted data
    df = pd.DataFrame(data, index=[f'IntervalReading_{i}' for i in range(1, len(data) + 1)])
    return df

df = xml_to_dataframe(input_file_path)
print(df)
