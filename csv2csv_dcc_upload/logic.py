import os 
import io
import base64
import pandas as pd
import uuid
import time

wait_time = 5 # second

def main(args):

    _, content_string = args['contents'].split(',')    
    decoded = base64.b64decode(content_string)

    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
    dir_name = str(uuid.uuid4())
    os.makedirs(os.path.join('./uploads', dir_name), exist_ok=True)
    os.makedirs(os.path.join('./downloads', dir_name), exist_ok=True)
    input_name = os.path.join('./uploads', dir_name, args['fileNames'] + ".csv")
    output_name = os.path.join('./downloads', dir_name, args['fileNames'] + "_result.csv")

    df.to_csv(input_name)
    df.to_csv(output_name)
    time.sleep(wait_time)
    return output_name
