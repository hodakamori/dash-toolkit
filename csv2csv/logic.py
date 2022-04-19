import os 
import pandas as pd

def main(args):

    df = pd.read_csv(os.path.join("./uploads", args['upload_id'], args['fileNames'][0]))

    os.makedirs(os.path.join('./downloads', args['upload_id']), exist_ok=True)
    output_name = os.path.join('./downloads', args['upload_id'], args['fileNames'][0] + "_result.csv")
    df.to_csv(output_name)

    return output_name
