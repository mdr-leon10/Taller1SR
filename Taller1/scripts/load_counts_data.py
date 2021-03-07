import csv

from api.models import User, Interactions, Songs

def run():
    csv_file = open('./ImportData/interactions-data.csv')
    reader = csv.reader(csv_file)
    #Skip header
    next(reader, None)

    for row in reader:
        u = User.objects.get(user_id=row[0])
        s, created = Songs.objects.get_or_create(
            artist_id=row[3],
            artist_name=row[4],
            track_id=row[1],
            track_name=row[2]
        )

        inter = Interactions(from_song=s, from_user=u, count=row[5])
