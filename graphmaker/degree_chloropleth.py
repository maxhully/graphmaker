import os
import geopandas as gp
import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt

from main import load_graph
from geospatial import reprojected

def shapefile_path(fips):
    return '/'.join(['.', 'tiger_data', fips, 'tl_2012_' + fips + '_vtd10.shp'])


def graph_paths(fips):
    return ('/'.join(['.', 'graphs', fips, 'rook.json']),
            '/'.join(['.', 'graphs', fips, 'queen.json']))


def degree(graph, node):
    return graph.degree[node]


def degree_chloropleth(fips, id_column='GEOID10'):
    rook_path, queen_path = graph_paths(fips)

    rook = load_graph(rook_path)
    queen = load_graph(queen_path)

    df = gp.read_file(shapefile_path(fips))
    df = reprojected(df)

    rook_degrees = [degree(rook, df.iloc[i][id_column]) for i in df.index]
    queen_degrees = [degree(queen, df.iloc[i][id_column]) for i in df.index]

    df['rook_degree'] = rook_degrees
    df['queen_degree'] = queen_degrees

    plt.axis('off')

    df.plot(column='rook_degree')
    rook_png_path = './graphs/' + fips + '/rook.png'
    if os.path.isfile(rook_png_path):
        os.remove(rook_png_path)
    plt.savefig(rook_png_path)

    df.plot(column='queen_degree')
    queen_png_path = './graphs/' + fips + '/queen.png'
    if os.path.isfile(queen_png_path):
        os.remove(queen_png_path)
    plt.savefig(queen_png_path)


def main():
    states = [fips for fips in os.listdir('./graphs/') if fips.isdigit()]
    for fips in states:
        degree_chloropleth(fips)


if __name__ == '__main__':
    main()
