def get_lat_lon(pc_df, postcode, suburb = None):
    """Return average latitutde and longitude for given postcode"""
    # todo #
    # get lon/lat using address lookup (googlemaps API?)
    import numpy as np
    
    if suburb is not None:
        return pc_df[(pc_df['suburb'] == suburb)  & (pc_df['postcode'] == postcode)].tolist()
    else:
        pc = pc_df[pc_df['postcode'] == postcode]
        lat = pc['lat'].tolist()
        lon = pc['lon'].tolist()
        return (np.mean(lat), np.mean(lon))
        

        
def add_cluster_markers(outbreak_df, pc_df, map_):
    """add a marker for every record in the data, use a clustered view"""
    # todo #
    # have marker options (colour, size, etc.) as dict with default values
    # passed to function

    import folium
    
    # cluster group
    marker_cluster = folium.MarkerCluster("Hospital cluster").add_to(map_) 
    for index, row in outbreak_df.iterrows():
        # retrieve latitude and longitude using postcode
        # pass suburb as third argument if possible marker formatting
        # is most easily done by passing the function html code
        lat, lon = get_lat_lon(pc_df, row['Postcode'], None)
        html = "<h3>%s, %s</h3><br>%s" % (
            row['Species'], row['Strain type'],
            row['Date of sample collection - time stamp']) 
        # used to display html
        iframe = folium.element.IFrame(html=html, width=300, height=200) 
        popup = folium.Popup(iframe, max_width=2000)
        folium.CircleMarker(location = (lat, lon), radius=10,
                            color='#FF0000', fill_color='#FF0000',
                            popup=popup).add_to(marker_cluster)
