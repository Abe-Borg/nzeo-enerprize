import pandas as pd
from lxml import etree

input_file_path = 'intervals_10203040_interval_block.xml'

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
        interval_start_time_unix = int(time_period.find('{http://naesb.org/espi}start').text)
        interval_duration = int(time_period.find('{http://naesb.org/espi}duration').text)
        interval_timezone = time_period.find('{http://naesb.org/espi}timezone').text
        interval_value = int(reading.find('{http://naesb.org/espi}value').text)
        interval_stop_time = interval_start_time_unix + interval_duration
        
        # Append the extracted data to the list
        data.append({
            'interval_starttime_unix': interval_start_time_unix,
            'interval_stop_time': interval_stop_time,
            'interval_timezone': interval_timezone,
            'interval_value': interval_value
        })
    
    # Create a DataFrame from the extracted data
    df = pd.DataFrame(data, index=[f'IntervalReading_{i}' for i in range(1, len(data) + 1)])
    return df

# test call.
df = xml_to_dataframe(input_file_path)
print(df)
