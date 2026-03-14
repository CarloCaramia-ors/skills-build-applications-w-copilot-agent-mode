from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', universe='Marvel')
        self.user = User.objects.create(email='tony@stark.com', name='Tony Stark', team=self.team, is_superhero=True)
        self.workout = Workout.objects.create(name='Super Strength', description='Strength training', difficulty='Hard')
        self.workout.suggested_for.add(self.team)
        self.activity = Activity.objects.create(user=self.user, activity_type='Running', duration=30, date=timezone.now().date())
        self.leaderboard = Leaderboard.objects.create(team=self.team, total_points=100, rank=1)

    def test_user_str(self):
        self.assertEqual(str(self.user), 'Tony Stark')

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Marvel')

    def test_activity_str(self):
        self.assertIn('Tony Stark', str(self.activity))

    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Super Strength')

    def test_leaderboard_str(self):
        self.assertIn('Marvel', str(self.leaderboard))
