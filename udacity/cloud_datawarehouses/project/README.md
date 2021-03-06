# Sparkify Data Warehouse


Sparkify is an imaginary music streaming startup seeking to develop a database model that makes querying data from users song plays easy. This document shows how a Data Warehouse can be built and which files to run for immediate use.


- [Requirements](#requirements)
- [Quick use](#quick-use)
- [The database](#the-database)
- [Database schema design](#database-schema-design)
- [Tables and data types](#tables-and-data-types)
  * [Fact table](#fact-table)
  * [Dimension tables](#dimension-tables)
- [ETL pipeline](#etl-pipeline)

## Requirements

- Python 3.x.
- psycopg2.
- pandas.
- configparser
- AWS account
- IAM role
- Redshift Cluster

## Quick use

- Launch a Redshift Cluster and set parameters in ```dwh.cfg``` with your AWS credentials;

- Run in terminal:

1. ```python create_tables.py```

2. ```python etl.py```


## The database

Two datasets feed records to the Data Warehouse: the first dataset is a subset from the well known [Million Song Dataset](http://millionsongdataset.com/), that gathers a bunch of json files about songs. In the second there are log files, also in JSON format, generated by [an event simulator](https://github.com/Interana/eventsim) based on the songs in the first dataset. Data is in S3 buckets.

Five tables are used to build the Data Warehouse, that will be named after sparkifydb from now on: ```songplays```, ```users```, ```songs```, ```artists``` and ```time```. Details about the schema are explained right up next.


## Database schema design

A [star schema](https://en.wikipedia.org/wiki/Star_schema) is used to split sparkifydb in fact and dimension tables. The songplays table is the fact table and the other tables are the dimension tables. In that configuration foreign keys aren't really necessary, it's easy to explain how the schema works to someone interested in the data and queries will be faster.

Data types were chosen based on data from the S3 buckets, for example: usually someone would pick ```int``` for a primary key like ```artist_id```, but ```s3://udacity-dend/song_data``` files show that it would make more sense for ```artist_id``` to have ```text``` or ```varchar``` as a data type.

To create or drop tables, run in terminal:

```python create_tables.py```


The create/drop table statements can be found in ```sql_queries.py```. For more details about data types check below.


## Tables and data types


* "pk" stands for primary key

### Fact table

```songplays``` - songplay_id (auto incremented pk), start_time text, user_id text, level text, song_id text, artist_id text, session_id int, location text, user_agent text.

### Dimension tables

```users``` - user_id text (pk) , first_name text, last_name text, gender varchar(1), level text.

```songs``` - song_id text (pk), title text, artist_id text, year int, duration float.

```artists``` - artist_id text (pk) , name text, location text, latitude float, longitude float.

```time``` - start_time text (pk), hour int, day int, week int, month int, year int, weekday text.


## ETL pipeline

The ETL pipeline consists in copying data from S3 buckets and staging them to a Redshift Cluster. It starts inserting data from ```s3://udacity-dend/song_data``` into ```songs``` and ```artists``` tables, and after that inserts filtered data from ```s3://udacity-dend/log_data``` into the remaining tables.

Tables ```songplays```, ```users``` and ```time``` only receive data where ```page``` keys from ```s3://udacity-dend/song_data``` files equals to ```"NextSong"```. Records added to ```time``` table are made by splitting the timestamp obtained in ```data/log_data``` into the columns specification given by the schema above. Two columns, ```artistid``` and ```songid``` from ```Songplays```, are obtained by combining data from ```artists``` and ```songs```, where a select statement on ```sql_queries.py``` does the job of finding the ids.


The insert statements are in ```sql_queries.py``` and some of them were written with constraints to avoid duplicate data from halting the pipeline flow. Here is an example:

```
artist_table_insert = ("""
    INSERT INTO artists (artist_id, name, location, latitude, longitude)
    SELECT DISTINCT artist_id, name, location, latitude, longitude
    FROM staging_songs
""")
```

To execute the ETL pipeline, you need first to launch a Redshift cluster and set parameters in ```dwh.cfg```. After that, type the command below in terminal(but remember to check if create_tables.py was already executed):

```
python etl.py
```

You will see the entire process being executed, and if something goes wrong an elucidative message will be displayed on screen.


#### Warning


This project is part of Udacity's Nanodegree in Data Engineering. Some parts of the text do take significant inspiration on the project overview and its instructions.
