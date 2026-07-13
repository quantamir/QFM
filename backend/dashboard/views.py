from django.shortcuts import render

# Create your views here.

DASHBOARD_STATS = [
    {"icon": "🏥", "title": "تجهیزات", "value": 125},
    {"icon": "🛠", "title": "دستور کارها", "value": 18},
    {"icon": "👨‍🔧", "title": "پرسنل", "value": 42},
    {"icon": "📊", "title": "گزارشها", "value": 9},
]


def home(request):
    return render(request, "dashboard/home.html", {"stats": DASHBOARD_STATS})
