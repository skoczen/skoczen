from import_export import resources
from manual.models import GutterBumper, MonthlyCheckin


class GutterBumperResource(resources.ModelResource):

    class Meta:
        model = GutterBumper


class MonthlyCheckinResource(resources.ModelResource):

    class Meta:
        model = MonthlyCheckin
