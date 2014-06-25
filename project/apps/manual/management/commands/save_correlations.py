from django.core.management.base import BaseCommand

from manual.utils import save_correlations


class Command(BaseCommand):

    def handle(self, *args, **options):
        print "Saving...",
        save_correlations()
        print " done."
