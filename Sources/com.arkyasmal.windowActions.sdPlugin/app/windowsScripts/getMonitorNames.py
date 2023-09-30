import functools
import os
import json
import pywintypes
from win32api import EnumDisplayMonitors, GetMonitorInfo, EnumDisplayDevices
from win32com.client import GetObject
from difflib import SequenceMatcher
from pathlib import Path
def create_json_file(data, app_data_directory):
    new_data_json = json.dumps(data)
    directory_path = Path(f'{os.getenv("APPDATA")}\\{app_data_directory}')
    if not directory_path.exists():
        os.makedirs(directory_path)
    path_to_file = directory_path / 'currentMonitors.json'
    path_to_file = path_to_file.resolve()
    try:
        f = open(path_to_file, "x")
        f.write(new_data_json)
        return new_data_json
    except FileExistsError:
        f = open(path_to_file, "w")
        f.write(new_data_json)
        return new_data_json
    except: 
        print("An error occured")
def convert_unit16_to_str(arr):
    chr_list = [chr(x) for x in arr]
    filtered_list = list(filter( lambda char: len(char)<=1, chr_list))
    new_str = functools.reduce(lambda a,b: a+b, filtered_list)
    return new_str.rstrip('\x00')
def get_monitor_names(app_data_directory):
    names = [GetMonitorInfo(x[0])["Device"] for x in EnumDisplayMonitors()] 
    monitor_ids = [EnumDisplayDevices( names[x],0, 1).DeviceID.replace("#", "\\") for x in range(len(names))]
    obj_wmi = GetObject('winmgmts:\\\\.\\root\\WMI').InstancesOf('WmiMonitorID')  # WmiMonitorConnectionParams
    instance_names = [dict(instance_name = item.InstanceName, name = convert_unit16_to_str(item.UserFriendlyName)) for item in obj_wmi]
    for instance in instance_names:
        highest_match = {"match":"", "idx": 0}
        for idx in range(len(monitor_ids)):
            pattern = instance['instance_name'].replace("\\", " ")
            test_str = monitor_ids[idx].replace("\\", " ")
            sequence = SequenceMatcher(None, pattern, test_str).find_longest_match(0, len(pattern), 0, len(test_str))
            matching_str = test_str[sequence.a:sequence.a + sequence.size]
            if len(matching_str) > len(highest_match['match']):
                highest_match.update({'match': matching_str, "idx": idx})
            print(pattern, test_str, matching_str)
        # we want the idx to be 1-indexed
        instance.update({"idx": highest_match["idx"] + 1})
    create_json_file(instance_names, app_data_directory)
    return instance_names