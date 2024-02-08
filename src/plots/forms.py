from django import forms

class UploadXMLForm(forms.Form):  
    xml_file = forms.FileField(label='XML File')
    destination_directory = forms.CharField(label='Destination Directory')
    PLOT_CHOICES = [
        ('line_plot', 'Line Plot'),
        ('scatter_plot', 'Scatter Plot'),
        ('histogram', 'Histogram'),
        ('bar_plot', 'Bar Plot'),
        ('area_plot', 'Area Plot'),
        ('heatmap', 'Heatmap'),
    ]
    plot_type = forms.ChoiceField(label='Plot Type', choices=PLOT_CHOICES)