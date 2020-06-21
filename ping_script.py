import pythonping as pp
import datetime as dt
import pandas as pd
import time

# Define parameters
url = '8.8.8.8'  # IP Address or Hostname
log_path = ''  # 'C:/Users/{yourusername}/Downloads/ping_log.csv'
MAX_TIMEOUT_SECS = 1.00  # Amount of time to wait before response time out (1.0 seconds = 1000ms)
PING_COUNT = 4  # If you change this, add/remove the appropriate amount of columns to the CSV.

# Ping
try:
    # Ping url number of times specified by PING_COUNT
    # print("Pinging {}".format(url))
    responses = pp.ping(url, MAX_TIMEOUT_SECS, PING_COUNT)._responses
    
    response_dict = {'ping{}'.format(i+1): response.time_elapsed_ms for i, response in enumerate(responses)}
    response_dict['datetime'] = dt.datetime.now().strftime("%Y-%m-%d %H:%M")

    # # DEBUG: Print out responses
    # for response in responses:
    #     print(response.time_elapsed_ms)

    # File i/o and update
    df_ping_log = pd.read_csv(log_path)
    df_ping_log = df_ping_log.append(response_dict, ignore_index=True)
    df_ping_log.to_csv(log_path, index=False)

except:
   print("Error pinging {} - no log entry added".format(url))
