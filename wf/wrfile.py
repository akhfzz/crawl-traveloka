import pandas as pd 
import os

def file_writerow(file, data):
    df = pd.DataFrame({
        'kategori': [data[0]],
        'url': [data[1]]
    })
    if os.path.isfile(file):
        df.to_csv(file, mode='a', index=False, header=False)
    else:
        df.to_csv(file, mode='a', index=False, header=True)


def file_writerow_data(file, data):
    df = pd.DataFrame({
        'images': [data[0]], 
        'destination': [data[1]], 
        'price_normal': [data[2]], 
        'price_discount': [data[3]], 
        'rating': [data[4]], 
        'location': [data[5]]
    })
    if os.path.isfile(file):
        df.to_csv(file, mode='a', index=False, header=False)
    else:
        df.to_csv(file, mode='a', index=False, header=True)