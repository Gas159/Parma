import django_filters
from statuses.models import Status

class TaskFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    # class Meta:
    #     model = Status
    #     fields = ['status', 'executor']#,'labels'


# <!--<div class="card">-->
# <!--    <div class="card-body bg-light">-->
# <!--        <form method="GET" class="form-inline justify-content-center">-->
# <!--            {% bootstrap_form filter.form %}-->
# <!--            {% buttons %}-->
# <!--            <button type="submit" class="btn btn-primary ml-4">-->
# <!--                {% trans 'Show' %}-->
# <!--            </button>-->
# <!--            {% endbuttons %}-->
# <!--        </form>-->
# <!--    </div>-->
# <!--    </div>-->