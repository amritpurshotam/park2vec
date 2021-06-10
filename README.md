# park2vec

## Getting started

```shell
$ docker-compose up
```

## Map Setup

### Download Location

Downloaded the PBF file from https://download.geofabrik.de/africa/south-africa.html

### Setup PostGIS database

https://registry.hub.docker.com/r/postgis/postgis
https://gist.github.com/leopoldodonnell/b0b7e06943bd389560184d948bdc2d5b

### Importing

https://osm2pgsql.org/

```shell
$ .\osm2pgsql.exe --host=localhost --username=postgres --password --port=5432 F:\OSM\south-africa-latest.osm.pbf
```

```
2021-06-09 21:03:28  osm2pgsql version 1.5.0
Password:
2021-06-09 21:03:37  Database version: 13.3 (Debian 13.3-1.pgdg100+1)
2021-06-09 21:03:37  PostGIS version: 3.1
2021-06-09 21:03:37  Setting up table 'planet_osm_point'
2021-06-09 21:03:37  Setting up table 'planet_osm_line'
2021-06-09 21:03:37  Setting up table 'planet_osm_polygon'
2021-06-09 21:03:37  Setting up table 'planet_osm_roads'
2021-06-09 21:05:00  Reading input files done in 83s (1m 23s).
2021-06-09 21:05:00    Processed 36319226 nodes in 4s - 9080k/s
2021-06-09 21:05:00    Processed 2897844 ways in 57s - 51k/s
2021-06-09 21:05:00    Processed 32282 relations in 22s - 1k/s
2021-06-09 21:05:05  Clustering table 'planet_osm_line' by geometry...
2021-06-09 21:05:05  Clustering table 'planet_osm_point' by geometry...
2021-06-09 21:05:05  Clustering table 'planet_osm_polygon' by geometry...
2021-06-09 21:05:05  Clustering table 'planet_osm_roads' by geometry...
2021-06-09 21:05:09  Creating geometry index on table 'planet_osm_point'...
2021-06-09 21:05:13  Analyzing table 'planet_osm_point'...
2021-06-09 21:05:14  All postprocessing on table 'planet_osm_point' done in 8s.
2021-06-09 21:05:14  Creating geometry index on table 'planet_osm_roads'...
2021-06-09 21:05:15  Analyzing table 'planet_osm_roads'...
2021-06-09 21:05:19  Creating geometry index on table 'planet_osm_polygon'...
2021-06-09 21:05:28  Creating geometry index on table 'planet_osm_line'...
2021-06-09 21:05:29  Analyzing table 'planet_osm_polygon'...
2021-06-09 21:05:46  Analyzing table 'planet_osm_line'...
2021-06-09 21:05:46  All postprocessing on table 'planet_osm_line' done in 41s.
2021-06-09 21:05:46  All postprocessing on table 'planet_osm_polygon' done in 23s.
2021-06-09 21:05:46  All postprocessing on table 'planet_osm_roads' done in 10s.
2021-06-09 21:05:46  osm2pgsql took 129s (2m 9s) overall.
```