from django.shortcuts import render
from projects.models import SoftwareProject, MathPhysicsProject, WebProject
from resume.models import Resume, SkillGroup

# Create your views here.
def home_page(request):
    software_projects = SoftwareProject.objects.order_by('-pub_date')
    mathphysics_projects = MathPhysicsProject.objects.order_by('-pub_date')
    web_projects = WebProject.objects.order_by('-pub_date')
    resume = Resume.objects.all()[0]
    
    skill_groups = SkillGroup.objects.all()
    context = {
        'software_projects': software_projects,
        'mathphysics_projects': mathphysics_projects,
        'web_projects': web_projects,
        'resume': resume,
        'skill_groups': skill_groups
    }
    return render(request, 'home/index.html', context)
