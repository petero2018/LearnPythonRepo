def return_method(log_line, return_type):
    split = log_line.split(" ")
    (ip_address, datetime, http_path, http_code, user_agent) = split[0], split[3].replace('[', '').replace(']', ''), \
                                                               split[4], split[5], split[6]
    r = {"log": [ip_address, datetime, http_path, http_code, user_agent],
         "csv": ','.join([ip_address, datetime, http_path, http_code, user_agent])}
    return r[return_type]
