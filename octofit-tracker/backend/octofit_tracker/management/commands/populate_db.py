from django.core.management.base import BaseCommand

from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Drop collections directly using PyMongo for a clean slate
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']
        for collection in ['activity', 'leaderboard', 'workout', 'user', 'team']:
            db[collection].drop()

        # Create teams
        marvel = Team.objects.create(name='Marvel', universe='Marvel')
        dc = Team.objects.create(name='DC', universe='DC')

        # Create users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel, is_superhero=True)
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team=marvel, is_superhero=True)
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc, is_superhero=True)
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team=dc, is_superhero=True)

        # Create workouts
        workout1 = Workout.objects.create(name='Super Strength', description='Strength training', difficulty='Hard')
        workout2 = Workout.objects.create(name='Flight Training', description='Aerial maneuvers', difficulty='Medium')
        workout1.suggested_for.add(marvel, dc)
        workout2.suggested_for.add(dc)

        # Create activities
        Activity.objects.create(user=tony, activity_type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, activity_type='Swimming', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce, activity_type='Martial Arts', duration=60, date=timezone.now().date())
        Activity.objects.create(user=clark, activity_type='Flying', duration=50, date=timezone.now().date())

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, total_points=200, rank=1)
        Leaderboard.objects.create(team=dc, total_points=180, rank=2)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
