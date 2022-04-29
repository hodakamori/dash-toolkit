import os 
import pandas as pd

options = ("name", "age", "job")

def main(args):

    # df = pd.read_csv(os.path.join("./uploads", args['upload_id'], args['fileNames'][0]))

    # os.makedirs(os.path.join('./downloads', args['upload_id']), exist_ok=True)
    # output_name = os.path.join('./downloads', args['upload_id'], args['fileNames'][0] + "_result.csv")
    # df.to_csv(output_name)
    output_name = args['option']
    return output_name
