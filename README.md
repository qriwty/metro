# METRO

## _Calculated and graphic work_

METRO - an [**app**][metro] for finding the shortest path between metropolitan stations

## Requirements

<a target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/python-3.7%2B-brightgreen"></a>

**No additional packages are required by default.**

To make full use of this application, you need to install additional packages.

_Export to file:_
- Numpy
- Pandas

_Visualization:_
- Matplotlib
- Networkx

## Required data

> Example in file [`map.py`][map.py]

### _Metro map_

Template of metro station 

```python
"M0_S1": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=30),
        "CONNECTIONS": [
            ["M0_S0", datetime.timedelta(minutes=2, seconds=30)],
            ["M0_S2", datetime.timedelta(minutes=2, seconds=30)]
        ]
    }
```

STATION ID:
M{line_id}_S{station_id}

TYPE:
- START -- station located at the beginning of the subway line
- END -- station located at the end of the subway line
- REGULAR -- regular subway station
- TRANSFER -- subway station with a connection to other subway stations on another line

DELAY:
Delay of current station
> DELAY -- `datetime.timedelta()`

CONNECTIONS:
Connections with other stations are written to the array. 
In the connection array [NEIGHBOUR, TIME]
> NEIGHBOUR -- `Station ID`
> TIME -- `datetime.timedelta()`

TRANSFER (optional):
Transfer connections are written in "CONNECTIONS" style.
This array contains all connections to other subway lines to get to another station.

### _Language pack (optional)_

In this app you are able to add new languages for stations name and services

```python
language_pack = {
    "STATION": {
        "M0_S0": {
            "ENG": "Khreschatyk"
        }
    },
    "SERVICE": {
        "PATH": {
            "ENG": "Way to the station"
        }
    }
}
```

STATION:
Stores stations name in different languages by Station ID

SERVICE:
Stores service name in different languages by Service NAME


## Usage

> More in [`main.py`][main.py]

To use this app you need to import and create object

```python
from metro import *
metro = Metro()
```

Description of common methods

| Method | Description |
| ------ | ------ |
| find_path(??, ??) | Finds the path between stations A and B |
| find_path_map(??) | Finds the path from station A to all stations |
| get_distance_map() | Returns the distance map between all stations |
| print_path(distance, path) | Prints the path found |


## Examples

To find path between station A and station B

```python
metro.find_path("station A", "station B", print_result=True)
```

To find path map from station A

```python
metro.find_path_map("station A", print_result=True)
```

To find path using cached values

```python
metro.get_path("station A", "station B", print_result=True)
```

To get distance map

```python
metro.get_distance_map(print_result=True)
```

To export distance map to current directory

```python
metro.export_file(filename="Exported", extension="csv")
```

## Thank you for reviewing my work

[metro]: https://github.com/qriwty/metro
[main.py]: https://github.com/qriwty/metro/blob/master/main.py
[map.py]: https://github.com/qriwty/metro/blob/master/map.py
