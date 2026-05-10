from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        self.user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=self.team, is_superhero=True)
        self.workout = Workout.objects.create(name='Web Swing', description='Swinging through the city')
        self.activity = Activity.objects.create(user=self.user, activity_type='Swing', duration=30, date='2023-01-01')
        self.leaderboard = Leaderboard.objects.create(team=self.team, total_points=100, week=1)
        self.workout.suggested_for.add(self.user)

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.user.name, 'Spider-Man')

    def test_team_creation(self):
        self.assertEqual(Team.objects.count(), 1)
        self.assertEqual(self.team.name, 'Marvel')

    def test_activity_creation(self):
        self.assertEqual(Activity.objects.count(), 1)
        self.assertEqual(self.activity.activity_type, 'Swing')

    def test_workout_creation(self):
        self.assertEqual(Workout.objects.count(), 1)
        self.assertEqual(self.workout.name, 'Web Swing')

    def test_leaderboard_creation(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
        self.assertEqual(self.leaderboard.total_points, 100)
