def time_convert(spend_time):
    temp = spend_time
    second = temp % 60
    temp = temp // 60
    minute = temp % 60
    temp = temp // 60
    hour = temp % 24
    temp = temp // 24
    day = temp
    format_str = ""
    if day > 0:
        format_str += "{}天".format(day)
    if hour > 0:
        format_str += "{}小时".format(hour)
    if minute > 0:
        format_str += "{}分钟".format(minute)
    format_str += "{}秒".format(second)
    return format_str
