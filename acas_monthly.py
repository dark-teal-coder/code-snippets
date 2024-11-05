## The following code is part of the program acas_monthly.py. Some sensitive and unnecessary parts of the program are omitted.

import datetime
import os
import configparser
from time import strftime, localtime
import shutil
from dateutil.relativedelta import relativedelta


def read_config():
    """This part of code is omitted."""
    config = configparser.ConfigParser()  ## <class 'configparser.ConfigParser'> object
    config.read(config_path)  ## <class 'list'>
    return config  ## <class 'configparser.ConfigParser'> object


def run():
    def last_day_of_month(date):
        if date.month == 12:
            return date.replace(day=31)
        return date.replace(month=date.month + 1, day=1) - datetime.timedelta(days=1)

    def first_day_of_month(date):
        return date.replace(day=1)

    report_month = datetime.datetime.now() + relativedelta(months=-1)
    firstday_month = strftime("%Y%m%d", first_day_of_month(report_month).timetuple())
    lastday_month = strftime("%Y%m%d", last_day_of_month(report_month).timetuple())
    day_range = [firstday_month, lastday_month]

    config = read_config('config.ini')
    config_acas = read_config('acas_sla.ini')

    ## Name Excel files from airline codes sections .ini file
    filenames = []
    for i in range(len(config_acas.sections())):
        ## Make one more space before using it
        filenames.append('')
        filenames[i] = "awb_and_hawb_records_us_shpt_monthly_{sdate}-{edate}_({0}).xlsx".format(
            config_acas.sections()[i], sdate=day_range[0], edate=day_range[1])
    print("File names:", filenames, sep="\n")

    for section in config_acas.sections():
        section_keys = []
        ## config_acas.options(section) returns a list
        for key in config_acas.options(section):
            section_keys.append(key)
        print("section_keys:\n", section_keys)
        key_airlines = config_acas[section][section_keys[0]].split(",")  ## <class 'list'>
        key_sla_hour = int(config_acas[section][section_keys[1]])  ## <class 'int'>
        key_excluded_agents = config_acas[section][section_keys[2]].split(",")  ## <class 'list'>
        print("key_airlines:", key_airlines, "key_sla_hour:", key_sla_hour, "key_excluded_agents:", key_excluded_agents,
              sep="\n")
        filename = filenames[config_acas.sections().index(section)]
        ## Run these functions for each section
        get_report_from_cplus(config, day_range, key_sla_hour)
        save_as_excel(config, filename, key_airlines, key_sla_hour, key_excluded_agents)
        copy_to_share(config, filename)


"""This part of code is omitted."""


def get_report_from_cplus():
    """This part of code is omitted."""


def save_as_excel(config, filename, airlines, sla_hour, excluded_agents):
    """This part of code is omitted."""

    ## config_obj['section']['key'] returns a string
    output_path = config['ACAS']['output_path']

    ## Create directory if not existed
    if not os.path.exists(output_path):
        ## Create all the intermediate-level directories if missing
        os.makedirs(output_path)

    ## Full path of output file
    output_file_path = os.path.join(output_path, filename)

    ## Rename file if same file name already exists in 'output' directory
    if os.path.exists(output_file_path):
        new_output_file_path = output_file_path.replace(".xlsx", "_{timestamp}.xlsx".format(
            timestamp=strftime("%Y%m%d%H%M%S", localtime())))
        os.rename(output_file_path, new_output_file_path)
        print(f"Existing {output_file_path} in 'output' renamed to {new_output_file_path}")

    writer = pd.ExcelWriter(output_file_path)

    """This part of code is omitted."""

    writer.save()


def copy_to_share(config, filename):
    print(f"Copying {filename} to share directory")
    output_path = config['ACAS']['output_path']
    share_path = config['ACAS']['share_path']

    ## Create directory if not existed
    if not os.path.exists(share_path):
        ## Create all the intermediate-level directories if missing
        os.makedirs(share_path)

    output_file_path = os.path.join(output_path, filename)
    share_file_path = os.path.join(share_path, filename)

    ## Rename file if same file name already exists in 'share' directory
    if os.path.exists(share_file_path):
        new_share_file_path = share_file_path.replace(".xlsx", "_{timestamp}.xlsx".format(
            timestamp=strftime("%Y%m%d%H%M%S", localtime())))
        os.rename(share_file_path, new_share_file_path)
        print(f"Existing {share_file_path} in 'share' renamed to {new_share_file_path}")

    ## Copy the contents and metadata of the source file to the destination file or directory
    shutil.copy2(output_file_path, share_file_path)
    print(f"{output_file_path} has been copied to {share_file_path}")


if __name__ == "__main__":
    run()
