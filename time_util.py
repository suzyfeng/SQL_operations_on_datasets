import datetime
import re


# 01.02.2019 01:00:00.014 GMT+0800
def str_to_timestamp(time_str):
    pattern = r"(\d{2}).(\d{2}).(\d{4}) (\d{2}):(\d{2}):(\d{2}).(\d{3}) GMT\+0800"
    match_obj = re.match(pattern, time_str)
    day = int(match_obj.group(1))
    month = int(match_obj.group(2))
    year = int(match_obj.group(3))
    hour = int(match_obj.group(4))
    minute = int(match_obj.group(5))
    second = int(match_obj.group(6))
    millisecond = int(match_obj.group(7))

    timestamp = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second).timestamp()
    timestamp = str(timestamp)[:10] + str(millisecond).zfill(3) + "000000"
    return int(timestamp)


if __name__ == "__main__":
    print(str_to_timestamp("01.02.2019 11:12:23.114 GMT+0800"))
