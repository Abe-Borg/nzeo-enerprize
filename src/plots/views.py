import os
from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
from django.http import HttpResponse
from io import BytesIO
from matplotlib.dates import DateFormatter, AutoDateLocator
from . forms import UploadXMLForm
from io import BytesIO
from . views import xml_to_dataframe
from lxml import etree
from django.shortcuts import get_object_or_404
from django.conf import settings


FIGSIZE = (10, 6)
HISTOGRAM_YEARLY_BINS = 100
HISTOGRAM_MONTHLY_BINS = 30


def upload_xml_file(request):
    if request.method == 'POST' and request.FILES.get('xml_file'):
        xml_file = request.FILES['xml_file']
        
        # Extract the base filename without extension
        base_filename = os.path.splitext(xml_file.name)[0]
        pickle_filename = f"{base_filename}.pkl"
        
        pickle_file_path = os.path.join(settings.MEDIA_ROOT, 'plots/data_sources', pickle_filename)
        
        # Ensure the directory exists
        os.makedirs(os.path.dirname(pickle_file_path), exist_ok=True)
        
        # Process the XML file to a DataFrame here
        # This step depends on how you're converting XML to DataFrame
        df = xml_to_dataframe(xml_file)
        
        # Pickle the DataFrame
        df.to_pickle(pickle_file_path)
        
        # Inform the user or your system that the file was processed successfully
        return HttpResponse(f"File {xml_file.name} uploaded and processed successfully.")
    else:
        form = UploadXMLForm()
        return render(request, 'district_management/school_level_analytics.html', {'form': form})

        

def get_line_plot(request):
    buf = BytesIO()
    create_line_plot(
        pkl_filepath="path/to/your/data.pkl",
        # plot_filepath="path/to/your/plot.png",
        buf = buf
    )
    buf.seek(0)
    return HttpResponse(buf.getvalue(), content_type='image/png')


def get_scatter_plot(request):
    buf = BytesIO()
    create_scatter_plot(
        pkl_filepath="path/to/your/data.pkl",
        # plot_filepath="path/to/your/plot.png",
        buf = buf
    )
    buf.seek(0)
    return HttpResponse(buf.getvalue(), content_type='image/png')


def get_histogram(request):
    buf = BytesIO()
    create_histogram(
        pkl_filepath="path/to/your/data.pkl",
        # plot_filepath="path/to/your/plot.png",
        buf = buf
    )
    buf.seek(0)
    return HttpResponse(buf.getvalue(), content_type='image/png')


def get_bar_plot(request):
    buf = BytesIO()
    create_bar_plot(
        pkl_filepath="path/to/your/data.pkl",
        # plot_filepath="path/to/your/plot.png",
        buf = buf
    )
    buf.seek(0)
    return HttpResponse(buf.getvalue(), content_type='image/png')


def get_area_plot(request):
    buf = BytesIO()
    create_area_plot(
        pkl_filepath="path/to/your/data.pkl",
        # plot_filepath="path/to/your/plot.png",
        buf = buf
    )
    buf.seek(0)
    return HttpResponse(buf.getvalue(), content_type='image/png')


def get_heatmap(request):
    buf = BytesIO()
    create_heatmap(
        pkl_filepath="path/to/your/data.pkl",
        # plot_filepath="path/to/your/plot.png",
        buf = buf
    )
    buf.seek(0)
    return HttpResponse(buf.getvalue(), content_type='image/png')



# ========== PLOTTING FUNCTIONS ==========
# for green button interval data

def create_line_plot(pkl_filepath: str, plot_filepath: str = None, buf: BytesIO = None) -> None:
    df = pd.read_pickle(pkl_filepath, compression='zip')
    df["start_time_unix"] = pd.to_datetime(df["start_time_unix"], unit='s')

    plt.figure(figsize=FIGSIZE)
    plt.plot(df["start_time_unix"], df["interval_value"], marker='o', linestyle='-')
    
    # Format the dates on the x-axis
    ax = plt.gca()  # Get the current Axes instance
    date_format = DateFormatter('%Y-%m-%d %H:%M')
    ax.xaxis.set_major_formatter(date_format)
    ax.xaxis.set_major_locator(AutoDateLocator())
    
    plt.title("Interval Energy Usage over Time")
    plt.xlabel("Start Time")
    plt.ylabel("Watt-hour")
    plt.xticks(rotation=45)
    plt.tight_layout()

    if buf:
        plt.savefig(buf, format='png')
    else:
        os.makedirs(os.path.dirname(plot_filepath), exist_ok=True)
        plt.savefig(plot_filepath) 
    plt.close()


def create_scatter_plot(pkl_filepath: str, plot_filepath: str = None, buf: BytesIO = None) -> None:
    df = pd.read_pickle(pkl_filepath, compression = 'zip')
    df["start_time_unix"] = pd.to_datetime(df["start_time_unix"], unit='s')

    plt.figure(figsize=FIGSIZE)
    plt.scatter(df["start_time_unix"], df["interval_value"])

    ax = plt.gca()  
    date_format = DateFormatter('%Y-%m-%d %H:%M')
    ax.xaxis.set_major_formatter(date_format)
    ax.xaxis.set_major_locator(AutoDateLocator())

    plt.title("Interval Energy Usage Scatter Plot")
    plt.xlabel("Start Time")
    plt.ylabel("Watt-hour")
    plt.xticks(rotation=45)
    plt.tight_layout()

    if buf:
        plt.savefig(buf, format='png')
    else:
        os.makedirs(os.path.dirname(plot_filepath), exist_ok=True)
        plt.savefig(plot_filepath)
    plt.close()


def create_histogram(pkl_filepath: str, plot_filepath: str = None, buf: BytesIO = None) -> None:
    df = pd.read_pickle(pkl_filepath, compression = 'zip')
    df["start_time_unix"] = pd.to_datetime(df["start_time_unix"], unit='s')

    plt.figure(figsize=FIGSIZE)
    plt.hist(df["interval_value"], bins=HISTOGRAM_YEARLY_BINS)

    ax = plt.gca()  
    date_format = DateFormatter('%Y-%m-%d %H:%M')
    ax.xaxis.set_major_formatter(date_format)
    ax.xaxis.set_major_locator(AutoDateLocator())

    plt.title("Distribution of Energy Usage Values")
    plt.xlabel("Watt-hour")
    plt.ylabel("Frequency")
    plt.tight_layout()

    if buf:
        plt.savefig(buf, format='png')
    else:
        os.makedirs(os.path.dirname(plot_filepath), exist_ok=True)
        plt.savefig(plot_filepath)
    plt.close()


def create_bar_plot(pkl_filepath: str, plot_filepath: str = None, buf: BytesIO = None) -> None:
    df = pd.read_pickle(pkl_filepath, compression = 'zip')
    df["start_time_unix"] = pd.to_datetime(df["start_time_unix"], unit='s')

    plt.figure(figsize=FIGSIZE)
    plt.bar(df["start_time_unix"], df["interval_value"])

    ax = plt.gca()  
    date_format = DateFormatter('%Y-%m-%d %H:%M')
    ax.xaxis.set_major_formatter(date_format)
    ax.xaxis.set_major_locator(AutoDateLocator())

    plt.title("Enery Usage per Interval")
    plt.xlabel("Start Time")
    plt.ylabel("Watt-hour")
    plt.xticks(rotation=45)
    plt.tight_layout()

    if buf:
        plt.savefig(buf, format='png')
    else:
        os.makedirs(os.path.dirname(plot_filepath), exist_ok=True)
        plt.savefig(plot_filepath)
    plt.close()


def create_area_plot(pkl_filepath: str, plot_filepath: str = None, buf: BytesIO = None) -> None:
    df = pd.read_pickle(pkl_filepath, compression = 'zip')
    df["start_time_unix"] = pd.to_datetime(df["start_time_unix"], unit='s')
    
    plt.figure(figsize=FIGSIZE)
    plt.fill_between(df["start_time_unix"], df["interval_value"], alpha=0.3)

    ax = plt.gca()  
    date_format = DateFormatter('%Y-%m-%d %H:%M')
    ax.xaxis.set_major_formatter(date_format)
    ax.xaxis.set_major_locator(AutoDateLocator())

    plt.title('Energy Usage Over Time (Area Plot)')
    plt.xlabel("Start Time")
    plt.ylabel("Watt-hour")
    plt.xticks(rotation=45)
    plt.tight_layout()

    if buf:
        plt.savefig(buf, format='png')
    else:
        os.makedirs(os.path.dirname(plot_filepath), exist_ok=True)
        plt.savefig(plot_filepath)
    plt.close()


def create_heatmap(pkl_filepath: str, plot_filepath: str = None, buf: BytesIO = None) -> None:
    df = pd.read_pickle(pkl_filepath, compression = 'zip')
    df["start_time_unix"] = pd.to_datetime(df["start_time_unix"], unit='s')

    plt.figure(figsize=FIGSIZE)
    plt.imshow(df, cmap='hot', interpolation='nearest')
    plt.title("Energy Usage Heatmap")

    if buf:
        plt.savefig(buf, format='png')
    else:
        os.makedirs(os.path.dirname(plot_filepath), exist_ok=True)
        plt.savefig(plot_filepath)
    plt.close()


# ========== DATAFRAME FUNCTIONS ==========

# def process_xml_interval_readings()


def create_pandas_df_from_csv(csv_file_path, df_filepath):
    # create padas dataframe from csv file and save to a folder location
    df = pd.read_csv(csv_file_path)
    df.to_pickle(df_filepath, compression = 'zip')
    
def pikl_q_table(df_filepath, pkl_filepath) -> None:
    df = create_pandas_df_from_csv(df_filepath)
    df.to_pickle(pkl_filepath, compression = 'zip')

