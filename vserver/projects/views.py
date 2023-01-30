from django.http import HttpResponse
from django.shortcuts import render

projectList = [

    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional Ecommerce website'
    },

    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },

    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    },

]

# projectList = [
#    {
#        'id': '1',
#        'title': 'Ecommerce Website',
#        'description': 'Fully functional Ecommerce website',
#    },
#    {
#        'id': '2',
#        'title': 'Portfolio Website',
#        'description': 'Fully functional Portfolio website',
#    },
#    {
#        'id': '3',
#        'title': 'Social Website',
#        'description': 'Fully functional Social website',
#    },
# ]


def projects(request):
    msg = 'Hello you are in the projects page'
    page = 'projects'
    number = 10
    context = {'page': page, 'number': number,
               'projects': projectList}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = None
    for project in projectList:
        if project['id'] == pk:
            projectObj = project
            # break
    return render(request, 'projects/project.html', {'project': projectObj})
