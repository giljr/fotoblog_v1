# fotoblog_v1 Episodes List DjangoSeries 🤓️
Hi, this is all about [Django](https://www.djangoproject.com/) , a web framework for perfectionists with deadlines!

Django is a full-stack, open-source Python framework designed for efficient web development.

This is learning by doing: I am using openclassrooms, a leading E-learning Platform!:rocket:

Go to 
[django-web-app Site Course](https://openclassrooms.com/en/courses/6967196-create-a-web-application-with-django)
```	
A photography collective is looking for 
a way to share its work with the world. 
They want to be able to upload their photos 
online and also create blog posts about them. 

They have asked you, a Django developer, 
to build a web application that allows them to do just that. 
They need to have two tiers of users - subscribers and creators - 
and ensure that only the creators can create content. 
This content then needs to be shared in a social feed,
with subscribers choosing which creators they want to follow.
```

The material, to understand Django framework,
is envisaged as follows:

```
Epi #1 - Environment setup; Deploy proj/apps; git repo init.
	
Epi #2 - soon...
```

I versioned every advance I made during the course (Episode.01, Episode.02 and so on).

Go to tags and download each working code package.

BTW, You're more then welcome to visit my Web Pages: 

🤩️[Jungletronics](https://medium.com/jungletronics)🤩️ (Python, C, Arduino, RasPi, PIC, Eagle, Blender, and more) 😍️[KidsTronics](https://medium.com/kidstronics)😍️ (MIT App Inventor, Geogebra, LEGO, Pixy, Unity3D, Arduino For Kids, and more)

## HOW TO Install on VSCode (Version 1.76.1)

Go to your command propt and paste this mini-script:

```
mkdir fotoblog
cd fotoblog
python -m venv ENV
source ENV/bin/activate
pip install django
pip freeze > requirement.txt
code .
exit
```
Open a Teminal inside VS Code, type:

```
git branch -M dev

source /home/j3/fotoblog/ENV/bin/activate

python -m pip install pillow

python -m pip install -U mypy

```

Now in Source Control Tag (Ctlr+Shift+G) clone from:

```
git@github.com:giljr/fotoblog_v1.git

```
Again open the Terminal, type:

```
python manage.py migrate

```
Congratulations!
You Django Project is up and running!

For a quick start Django Vscode lesson, go to this [post](https://medium.com/jungletronics/a-django-blog-in-vs-code-fb23335d919). 

## FotoBlog: Episodes & A List of sites visited for This Project:

### [Episode.01](/../../tags/) from http://jungletronics.com

FotoBlog v1.0 - [Episode #01](https://medium.com/jungletronics/a-django-fotoblog-in-vs-code-quick-start-8e6b944c13a)
```
Step-by-Step list of tasks:

	1- Environment setup;

	2 -Deploy Project & Apps;

	3 -Git repo init.

```
### [Episode.02](/../../tags/) from http://jungletronics.com

FotoBlog - v1.0: [Episode #02](https://medium.com/jungletronics/a-django-fotoblog-in-vs-code-custom-user-model-83611e2888d3)
```
Step-by-step list of tasks:

	1-Use Custom Model;

	2-Config Django to use Custom User;

	3-Run the Migration.
```
### [Episode.03](/../../tags/) from http://jungletronics.com: 

FotoBlog - v1.0: [Episode #03](https://medium.com/jungletronics/a-django-fotoblog-in-vs-code-self-service-password-reset-b7729588001d) 
```      
Step-by-step list of tasks:

	1-Explaining how password reset functionality works;

	2-Modifying fotoblog/urls.py file;

	3-Modifying fotoblog/settings.py file

	4-Creating 5 htmls file at templates/registration;

	3-Routing at localhost:800/accounts/ dirs.
```
### [Episode.04](/../../tags/): soon...
