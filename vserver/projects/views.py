from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import ProjectForm
from .models import Project


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    #tags = projectObj.tags.all()
    print('projectObj :', projectObj)
    return render(request, 'projects/project.html', {'project': projectObj})

    # return render(request, 'projects/project.html', {'project': projectObj, 'tags': tags})


def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        # print(request.POST)
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        # print(request.POST)
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)


# projectList = [
#
#    {
#        'id': '1',
#        'title': 'Ecommerce Website',
#        'description': 'Fully functional Ecommerce website'
#    },
#
#    {
#        'id': '2',
#        'title': 'Portfolio Website',
#        'description': 'A personal website to write articles and display work'
#    },
#
#    {
#        'id': '3',
#        'title': 'Social Network',
#        'description': 'An open source project built by the community'
#    },
#
# ]
#
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
