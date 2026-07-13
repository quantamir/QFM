from django.shortcuts import render

# Create your views here.

DASHBOARD_STATS = [
    {"icon": "🏥", "title": "Assets", "value": 125},
    {"icon": "🛠", "title": "Work Orders", "value": 18},
    {"icon": "👨‍🔧", "title": "Staff", "value": 42},
    {"icon": "📊", "title": "Reports", "value": 9},
]


def home(request):
    return render(request, "dashboard/home.html", {"stats": DASHBOARD_STATS})
