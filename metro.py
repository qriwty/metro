import map
# import datetime
import math
import re
import time
import pandas
import numpy


class Metro:
    def __init__(self, setup_environment=False):
        self.metro_map = map.metro
        self.language_pack = map.language_pack
        self.service_pack = map.service_language_pack
        self.language = "UKR"

        self.metro_matrix = []

        self.metro_stations = []
        self.metro_length = 0

        self.INF = math.inf

        self.metro_distance_map = []

        self.path_map = {}

        if setup_environment:
            self.set_metro_stations()
            self.create_metro_matrix()
            self.explore_path()
            self.create_distance_map()

    def get_station_name(self, station, language=None):
        if language is None:
            language = self.language
        if isinstance(station, int):
            station = self.metro_stations[station]
            return self.language_pack[station][language]
        if isinstance(station, str):
            return self.language_pack[station][language]

    def get_service_name(self, service, language=None):
        if language is None:
            language = self.language
        return self.service_pack[service][language]

    def get_sort_key(self, id):
        m = re.match("M([0-9]+)_S([0-9]+)", id)
        return int(m.group(1)), int(m.group(2))

    def set_language(self, language):
        self.language = language

    def find_station(self, name):
        if name in self.metro_stations:
            return name, self.metro_stations.index(name)

        for station in self.metro_stations:
            for language in self.language_pack[station]:
                if name == self.language_pack[station][language]:
                    return station, self.metro_stations.index(station)

        return None

    def explore_path(self):
        for station in range(self.metro_length):
            dist, path = self.dijkstra(station)

            self.path_map[station] = {
                "DIST": dist,
                "PATH": path
            }

        return self.path_map

    def find_path(self, source, destination):
        if len(self.path_map.keys()) != self.metro_length:
            self.explore_path()

        source, source_id = self.find_station(source)
        destination, destination_id = self.find_station(destination)

        distance = self.path_map[source_id]["DIST"][destination_id]
        path = self.path_map[source_id]["PATH"][destination_id]

        return distance, path

    def set_metro_stations(self):
        self.metro_stations = [station for station in self.metro_map.keys()]
        self.metro_stations.sort(key=self.get_sort_key)
        self.metro_length = len(self.metro_stations)

    def create_metro_matrix(self):
        metro_matrix = [[self.INF for _ in range(self.metro_length)] for _ in range(self.metro_length)]

        for row in range(self.metro_length):
            for column in range(self.metro_length):
                if row == column:
                    metro_matrix[row][column] = 0

        for station in self.metro_stations:
            station_index = self.metro_stations.index(station)

            for neighbour in self.metro_map[station]["CONNECTIONS"]:
                neighbour_index = self.metro_stations.index(neighbour[0])

                time_to_station = neighbour[1].total_seconds()

                metro_matrix[station_index][neighbour_index] = time_to_station

            if self.metro_map[station]["TYPE"] == "TRANSFER":
                for transfer in self.metro_map[station]["TRANSFER"]:
                    transfer_index = self.metro_stations.index(transfer[0])

                    time_to_station = transfer[1].total_seconds()

                    metro_matrix[station_index][transfer_index] = time_to_station

        self.metro_matrix = metro_matrix

        return metro_matrix

    def create_distance_map(self):
        self.metro_distance_map = self.floyd()
        return self.metro_distance_map

    def export_file(self, filename="exported", extension="xlsx", matrix=None):
        if matrix is None:
            if len(self.metro_distance_map) != self.metro_length:
                self.metro_distance_map = self.create_distance_map()

            matrix = self.metro_distance_map

        matrix = [[time.strftime("%M:%S", time.gmtime(seconds)) if seconds != 0 else "X" for seconds in row] for row in matrix]

        stations = [""] + [self.get_station_name(station) for station in self.metro_stations]
        matrix.insert(0, stations)
        for row in range(1, len(stations)):
            matrix[row].insert(0, stations[row])

        arr = numpy.asarray(matrix)

        if extension is "xlsx":
            pandas.DataFrame(arr).to_excel(f"{filename}.{extension}", index=False, header=False)
        if extension is "csv":
            pandas.DataFrame(arr).to_csv(f"{filename}.{extension}", index=False, header=False)

    def print_matrix(self, matrix=None):
        matrix = matrix
        if matrix is None:
            matrix = self.metro_matrix
        matrix_length = len(matrix)
        row_format = "{:>25}" * (matrix_length + 1)
        print(row_format.format("", *[self.get_station_name(vertex) for vertex in range(matrix_length)]))
        for edge, vertices in zip([vertex for vertex in range(matrix_length)], matrix):
            arr = []
            for vertex in vertices:
                if vertex is self.INF:
                    arr.append("∞")
                elif vertex is 0:
                    arr.append("X")
                else:
                    arr.append(time.strftime("%M:%S", time.gmtime(vertex)))
            print(row_format.format(self.get_station_name(edge), *arr))

    def print_path_map(self, dist, path):
        source = path[0][0]
        print("{} - {}\n".format(self.get_service_name("INITIAL"),
                                 self.get_station_name(source)))
        print("{:>25} {:>11} {:>31}".format(self.get_service_name("TERMINUS"),
                                            self.get_service_name("TIME"),
                                            self.get_service_name("PATH")))
        for node in range(self.metro_length):
            station_name = self.get_station_name(node)
            travel_time = time.strftime("%M:%S", time.gmtime(dist[node])) if dist[node] != self.INF else "∞"
            path_array = []
            prev = path[node][0] - 1
            for station in path[node]:
                if abs(station - prev) != 1:
                    path_array.append(f"{self.get_station_name(station)} ({self.get_service_name('TRANSFER')})")
                else:
                    path_array.append(self.get_station_name(station))
                prev = station
            print("{:>25} {:>11} {:>31}".format(station_name,
                                                travel_time,
                                                " -> ".join(path_array)))

    def print_path(self, dist, path):
        print("{:>25} {:>25} {:>11} {:>31}".format(self.get_service_name("INITIAL"),
                                                   self.get_service_name("TERMINUS"),
                                                   self.get_service_name("TIME"),
                                                   self.get_service_name("PATH")))
        source = path[0]
        destination = path[-1]

        source_name = self.get_station_name(source)
        destination_name = self.get_station_name(destination)
        travel_time = time.strftime("%M:%S", time.gmtime(dist)) if dist != self.INF else "∞"

        path_array = []
        prev = path[0] - 1
        for station in path:
            if abs(station - prev) != 1:
                path_array.append(f"{self.get_station_name(station)} ({self.get_service_name('TRANSFER')})")
            else:
                path_array.append(self.get_station_name(station))
            prev = station

        print("{:>25} {:>25} {:>11} {:>31}".format(source_name,
                                                   destination_name,
                                                   travel_time,
                                                   " -> ".join(path_array)))

    def dijkstra(self, src):
        dist = [self.INF] * self.metro_length
        dist[src] = 0

        visited = [False] * self.metro_length

        path = {}
        for i in range(self.metro_length):
            path[i] = [src]

        for _ in range(self.metro_length):
            u = self.__extract_min(dist, visited)
            visited[u] = True
            for v in range(self.metro_length):
                delay = self.metro_map[self.metro_stations[u]]["DELAY"].total_seconds()
                alt = dist[u] + self.metro_matrix[u][v] + delay
                if dist[v] > alt and visited[v] is False:
                    dist[v] = alt
                    path[v] = path[u] + [v]

        return [dist, path]

    def __extract_min(self, dist, visited):
        min_value = self.INF
        min_index = -1
        for u in range(self.metro_length):
            if dist[u] < min_value and visited[u] is False:
                min_value = dist[u]
                min_index = u

        return min_index

    def floyd(self):
        dist = self.metro_matrix.copy()

        for k in range(self.metro_length):
            for i in range(self.metro_length):
                for j in range(self.metro_length):
                    delay = self.metro_map[self.metro_stations[i]]["DELAY"].total_seconds()
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j] + delay)

        self.metro_distance_map = dist

        return dist
