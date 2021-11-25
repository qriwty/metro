from metro import *

test = Metro()

test.create_metro_matrix()

dist, path = test.dijkstra(0)

test.print_path(dist, path)

test.export_file()

