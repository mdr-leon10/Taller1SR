import csv

from api.models import User

def run():
    csv_file = open('./ImportData/user_list.csv')
    reader = csv.reader(csv_file)

    #Clear in case there are leftovers from testing
    User.objects.all().delete()

    for row in reader:
        user_created = User(user_id=row[0], is_old_user=True, recommendation_frame=0)
        user_created.save()