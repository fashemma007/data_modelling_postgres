# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = ("""create table songplays (songplay_id SERIAL, 
start_time TIMESTAMP NOT NULL,user_id INT NOT NULL,
level VARCHAR NOT NULL, song_id VARCHAR(18),
artist_id VARCHAR(18),session_id INT NOT NULL, 
location VARCHAR NOT NULL, user_agent VARCHAR NOT NULL, 
PRIMARY KEY (songplay_id))""")

user_table_create = ("""create table users (user_id INT, 
first_name VARCHAR not NULL, 
last_name VARCHAR not NULL, 
gender CHAR(1) not NULL, 
level VARCHAR not NULL,
PRIMARY KEY (user_id))
""")

song_table_create = ("""
create table if not exists songs(song_id VARCHAR(18), 
title VARCHAR not NULL, 
artist_id VARCHAR not NULL, 
year INT not NULL, 
duration float NOT NULL, 
primary key (song_id))
""")

artist_table_create = ("""
create table if not exists artists(artist_id VARCHAR(18),
    name VARCHAR NOT NULL,
    location VARCHAR NOT NULL,
    latitude FLOAT,
    longitude FLOAT,
    PRIMARY KEY (artist_id))
""")

time_table_create = ("""CREATE TABLE time (
    start_time TIMESTAMP NOT NULL,
    hour int NOT NULL,
    day int NOT NULL,
    week int NOT NULL,
    month int NOT NULL,
    year int NOT NULL,
    weekday int NOT NULL)
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT into songplays(start_time,user_id,level,
song_id,artist_id,session_id,location, user_agent)
values(%s,%s,%s,%s,%s,%s,%s,%s)""")

user_table_insert = ("""INSERT into users (user_id,first_name,last_name,gender,level)
values (%s,%s,%s,%s,%s) 
ON CONFLICT (user_id) DO UPDATE 
SET level = excluded.level
""")

song_table_insert = ("""INSERT into songs (song_id,title,artist_id,year,duration)
values
    (%s,%s,%s,%s,%s) 
    ON CONFLICT(song_id) DO NOTHING
""")

artist_table_insert = (""" INSERT into artists(artist_id,name,location,latitude,longitude)
values(%s,%s,%s,%s,%s) ON CONFLICT(artist_id) DO NOTHING""")


time_table_insert = ("""
INSERT INTO time
    (start_time, hour, day, week, month, year, weekday)
VALUES
    (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""
SELECT
    s.song_id, s.artist_id
FROM
    songs s
        JOIN artists a ON s.artist_id = a.artist_id
WHERE
    s.title = %s
    AND a.name = %s
    AND s.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]