## The following code is part of the program sla_report_qr.py. Some sensitive and unnecessary parts of the program are omitted.

import configparser
import datetime
import pandas as pd
import os


def read_config():
    """This part of code is omitted."""
    config = configparser.ConfigParser()  ## <class 'configparser.ConfigParser'> object
    config.read(config_path)  ## <class 'list'>
    return config  ## <class 'configparser.ConfigParser'> object


## pandas.ExcelWriter() class for writing DataFrame objects into excel sheets.
def create_writer(excel_file_type):
    report_month = datetime.datetime.now().replace(month=datetime.datetime.now().month-1).strftime("%b")
    report_year = datetime.datetime.now().strftime("%Y")
    return pd.ExcelWriter(os.path.join(config['sla_report_qr']['output_path'], "QR_SLA_Report_{0:s}_{1:s}-{2:s}.xlsx".format(excel_file_type, report_month, report_year)))

writer_cbd = create_writer(excel_file_type = "CBD")
writer_ctf = create_writer(excel_file_type = "CTF")