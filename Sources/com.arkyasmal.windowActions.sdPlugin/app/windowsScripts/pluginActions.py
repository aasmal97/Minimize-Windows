import sys
from windowActions import move_windows_to_new_monitor, maximize_window, minimize_window, close_window, resize_window
from virtualDesktopActions import create_new_virtual_desktop, move_windows_to_new_desktop, move_virtual_desktop, toggle_through_virtual_desktops
from getMonitorNames import get_monitor_names
from determineActiveWindows import get_active_windows
if __name__ == "__main__":
    cmd_args = sys.argv
    action = cmd_args[cmd_args.index("--action") + 1]
    match action: 
        case 'create_desktop': 
            num_of_desktops= cmd_args[cmd_args.index("--numOfNewDesktops") + 1]
            create_new_virtual_desktop(int(num_of_desktops))
        case 'move_window':
            desktop_num = cmd_args[cmd_args.index("--newDesktop") + 1]
            desktop_num = int(desktop_num)
            win_id = cmd_args[cmd_args.index("--winId") + 1]
            win_id_type = cmd_args[cmd_args.index("--winIdType") + 1]
            move_windows_to_new_desktop(desktop_num, win_id_type, win_id)
        case 'move_virtual_desktop': 
            desktop_num = cmd_args[cmd_args.index("--newDesktop") + 1]
            #we expect this input to be 1-indexed (so we correct for 0-index)
            desktop_num = int(desktop_num) - 1
            move_virtual_desktop(desktop_num)
        case 'move_window_to_monitor': 
            monitor_num = cmd_args[cmd_args.index("--newMonitor") + 1]
            #we expect this input to be 1-indexed
            monitor_num = int(monitor_num) - 1
            win_id = cmd_args[cmd_args.index("--winId") + 1]
            win_id_type = cmd_args[cmd_args.index("--winIdType") + 1]
            move_windows_to_new_monitor(monitor_num, win_id_type, win_id)
        case 'get_monitor_info':
            app_data_directory = cmd_args[cmd_args.index("--appDataDirectory") + 1]
            get_monitor_names(app_data_directory)
        case 'move_by_one_virtual_desktop':
            direction = cmd_args[cmd_args.index("--direction") + 1]
            toggle_through_virtual_desktops(int(direction))
        case 'minimize_window':
            win_id = cmd_args[cmd_args.index("--winId") + 1]
            win_id_type = cmd_args[cmd_args.index("--winIdType") + 1]
            minimize_window(win_id_type, win_id)
        case 'maximize_window':
            win_id = cmd_args[cmd_args.index("--winId") + 1]
            win_id_type = cmd_args[cmd_args.index("--winIdType") + 1]
            maximize_window(win_id_type, win_id)
        case 'close_window': 
            win_id = cmd_args[cmd_args.index("--winId") + 1]
            win_id_type = cmd_args[cmd_args.index("--winIdType") + 1]
            close_window(win_id_type, win_id)
        case 'resize_window':
            win_id = cmd_args[cmd_args.index("--winId") + 1]
            win_id_type = cmd_args[cmd_args.index("--winIdType") + 1]
            size = cmd_args[cmd_args.index("--size") + 1].strip('][').split(',')
            coordinates = cmd_args[cmd_args.index("--coordinates") + 1].strip('][').split(',')
            resize_window(win_id_type, win_id, size, coordinates)
        case 'get_active_windows':
            active_windows= []
            app_data_directory = cmd_args[cmd_args.index("--appDataDirectory") + 1]
            if "--filterDup" in cmd_args: 
                active_windows = get_active_windows(app_data_directory, True) 
            else:
                active_windows = get_active_windows(app_data_directory, False)
