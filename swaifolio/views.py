from django.shortcuts import render
from django.template import Context, Template
from .form import ContactForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile, Portfolio, Services, Skill


def index(request):

    c = {}

    #user and specific user whose name appears to be 'swai'
    us_er = User.objects.filter(username = 'swai')
    user_specific = us_er.first()
    c["user"] = user_specific

    #swai's profile
    profile_all = Profile.objects.all()
    profile_specific = Profile.objects.first()
    c["profile"] = profile_specific

    #swai's cv 
    his_cv = profile_specific.cv
    c["cv"] = his_cv

    #swai's about
    his_about = profile_specific.about
    c["about"] = his_about

    #swai's many portfolios
    pf = Portfolio.objects.filter(fk=user_specific)
    pf_count = 0
    for swaipf in pf:
        swai_pf_name = swaipf.name
        swai_pf_image = swaipf.image

        c["portfolio_name"+str(pf_count)] = swai_pf_name
        c["portfolio_image"+str(pf_count)] = swai_pf_image

        pf_count += 1
        
    #his many services
    sv = Services.objects.all()
    spec_sv = sv.filter(fk_serv = user_specific)
    s_count = 0
    for swaiserv in spec_sv:
        swv = swaiserv
        service_name = swv.name
        service_image = swv.image
        service_description = swv.description

        c["service_name"+str(s_count)] = service_name
        c["service_image"+str(s_count)] = service_image
        c["service_description"+str(s_count)] = service_description

        print(service_name , service_image)
        print(c)

        s_count += 1

    #his skill
    sk = Skill.objects.all()
    sk_count = 0
    for hs in sk:
        skill_name = hs.name
        skill_image = hs.image
        skill_score = hs.score

        c["skill_name"+str(sk_count)] = skill_name
        c["skill_image"+str(sk_count)] = skill_image
        c["skill_score"+str(sk_count)] = skill_score

        sk_count += 1

    print(c["portfolio_image0"])
    print(c["portfolio_image1"])
    print(' \n')
    

    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            name = form.cleaned_data.get('name')
            messages.success(request, f'{ name } your message has been sent')
            print('wazi!!!! '+ str(name))
    else:
        form = ContactForm()

    c['form'] = form

    return render(request, 'swaifolio/index.html', {'c': c})

def anim(request):

    return render(request, 'swaifolio/anim.html')