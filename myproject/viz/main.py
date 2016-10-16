#!/usr/bin/python

def generate_map(initial_loc, zoom, terrain):
    import folium
    map_ = folium.Map(location=initial_loc, zoom_start=zoom,
                       tiles=terrain)

    return map_
    
def main():
    import pandas as pd
    import numpy as np
    import folium
    import matplotlib.pyplot as plt
    # pd.options.display.mpl_style = 'default'

    from parse_data import *
    from map_generator import *

    # import postcode data
    pc_handle = "./data/Australian_Post_Codes_Lat_Lon.csv"
    pc_df = read_postcode_csv(pc_handle)

    # parse the outbreak data
    outbreak_handle = "./data/Outbreak.csv"
    outbreak_df = parse_outbreak(outbreak_handle)

    # generate the map
    initial_loc = [-27.46499, 153.02661366666666]
    zoom = 12
    terrain = 'Stamen terrain'
    map_ = generate_map(initial_loc, zoom, terrain)

    # add markers to our map
    add_cluster_markers(outbreak_df, pc_df, map_)

    map_.save('./brisbane.html')

    
if __name__ == "__main__":
    main()
