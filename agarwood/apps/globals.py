from agarwood.apps.models import *
from django.db.models import Avg, F, Count


def get_menu():
    return Menu.objects.all()


def get_total_score_of_dispensary(store_id):
    return ReviewStore.objects.filter(store_id=store_id).aggregate(Avg('score'))


def get_dispensaries():
    all_stores = Store.objects.annotate(score_avg=Avg('reviewstore__score'), total_review=Count('reviewstore__store_id'))
    if len(all_stores) > 10:
        return all_stores[:10]
    return all_stores
