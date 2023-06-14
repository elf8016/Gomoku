import os


def change_terminal_size():  # 改變目前視窗的大小
    command = f"printf '\\033[8;99999;99999t'"
    os.system(command)


def split_string(string: str):  # 拆出字體和大小
    if len(string) >= 2:
        front = string[:-2]
        back = string[-2:]
    else:
        front = string
        back = ""

    return front, back


def get_terminal_font():
    # 得到目前的Profile ID
    profile_id_cmd = "gsettings get org.gnome.Terminal.ProfilesList default"
    profile_id_output = os.popen(profile_id_cmd).read().strip().strip("'")

    # 得到目前的字體和大小
    font_cmd = "gsettings get org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:{}/ font".format(
        profile_id_output
    )
    font_output = os.popen(font_cmd).read().strip().strip("'")

    return font_output


def screen_change():
    current_font, current_font_size = split_string(get_terminal_font())
    set_size = "2"

    os.system(
        "gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:b1dcc9dd-5262-4d8d-a863-c897e6d979b9/ font '{}'".format(
            current_font + " " + set_size
        )
    )
    change_terminal_size()


def screen_back():
    current_font, current_font_size = split_string(get_terminal_font())
    set_size = "16"
    os.system(
        "gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:b1dcc9dd-5262-4d8d-a863-c897e6d979b9/ font '{}'".format(
            current_font + " " + set_size
        )
    )
