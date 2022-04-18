import datetime 
import pandas as pd

input_names = ("name", "age", "job")

def main(args):
    df = pd.DataFrame({'x':[1, 2, 3, 4 ], 'y':[2, 4, 6, 4]})
    df.to_csv('result.csv')
    return datetime.datetime.now().strftime(f'{args["name"]} {args["age"]} {args["job"]} %Y年%m月%d日 %H:%M:%S')
