from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Borrar datos existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Crear usuarios
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        spiderman = User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)

        # Crear actividades
        Activity.objects.create(user=ironman, type='run', duration=30)
        Activity.objects.create(user=spiderman, type='cycle', duration=45)
        Activity.objects.create(user=batman, type='swim', duration=60)
        Activity.objects.create(user=superman, type='run', duration=50)

        # Crear leaderboard
        Leaderboard.objects.create(user=ironman, points=100)
        Leaderboard.objects.create(user=spiderman, points=80)
        Leaderboard.objects.create(user=batman, points=90)
        Leaderboard.objects.create(user=superman, points=95)

        # Crear workouts
        Workout.objects.create(name='Full Body', description='Entrenamiento completo', duration=60)
        Workout.objects.create(name='Cardio', description='Entrenamiento cardiovascular', duration=45)

        self.stdout.write(self.style.SUCCESS('La base de datos octofit_db ha sido poblada con datos de prueba.'))
