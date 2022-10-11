#CS257 database design
#10.11.2022
#Mihael Xia

import csv

# Strategy:
# (1) Create a dictionary that maps athlete IDs to athlete names
#       and then save the results in athletes.csv
# (2) Create a dictionary that maps event names to event IDs
#       and then save the results in events.csv
# (3) For each row in the original athlete_events.csv file, build a row
#       for our new event_results.csv table
#
# NOTE: I'm doing these three things in three different passes through
# the athlete_events.csv files. This is not necessary--you can do it all
# in a single pass.


# (1) Create a dictionary that maps athlete_id -> athlete_name
#       and then save the results in athletes.csv
athletes = {}
with open('athlete_events.csv') as original_data_file,\
        open('athletes.csv', 'w', newline = "") as athletes_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(athletes_file)
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    for row in reader:
        athlete_id = row[0]
        athlete_name = row[1]
        if athlete_id not in athletes:
            athletes[athlete_id] = athlete_name
            writer.writerow([athlete_id, athlete_name])

# (2) Create a dictionary that maps event_name -> event_id
#       and then save the results in events.csv
events = {}
with open('athlete_events.csv') as original_data_file,\
        open('events.csv', 'w', newline = "") as events_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(events_file)
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    for row in reader:
        event_name = row[13]
        sport_name = row[12]

        if event_name not in events:
            event_id = len(events) + 1
            events[event_name] = event_id
            writer.writerow([event_id, sport_name, event_name])
# (3) Create a dictionary that maps game_name -> game_id
#       and then save the results in games.csv
games = {}
with open('athlete_events.csv') as original_data_file,\
        open('games.csv', 'w', newline = "") as games_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(games_file)
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    for row in reader:
        # noc_name = row[7]
        game_name = row[8]
        game_city = row[11]
        
        if game_name not in games:
            game_id = len(games) + 1
            games[game_name] = game_id
            writer.writerow([game_id, game_name, game_city])

nocs = {}
with open('noc_regions.csv') as original_data_file,\
        open('nocs.csv', 'w', newline = "") as noc_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(noc_file)
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    for row in reader:
        noc = row[0]
        region = row[1]
        
        if noc not in nocs:
            noc_id = len(nocs) + 1
            nocs[noc] = noc_id
            writer.writerow([noc_id, noc, region])

# (3) For each row in the original athlete_events.csv file, build a row
#       for our new event_results.csv table
with open('athlete_events.csv') as original_data_file,\
        open('event_results.csv', 'w', newline = "") as event_results_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(event_results_file)
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    for row in reader:
        athlete_id = row[0]
        event_name = row[13]
        game_name = row[8]
        noc_name = row[7]
        event_id = events[event_name] # this is guaranteed to work by section (2)
        game_id = games[game_name]
        noc_id = nocs[noc_name]
        medal = row[14]
        writer.writerow([game_id, event_id, noc_id, athlete_id, medal])
