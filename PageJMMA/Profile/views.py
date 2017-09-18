from django.views.generic import TemplateView
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template.loader import get_template
from pprint import pprint
from .forms import ContactForm
from django.template import RequestContext, Context

pprint(globals())
pprint(locals())

# Create your views here.
def emailHome(request):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = 'PageJMMA '  + from_email + '   ' + form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['juanmacedoal@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return render(request, "index.html", {'form': form})

def email(request):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = 'PageJMMA '  + from_email + '   ' + form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['juanmacedoal@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return render(request, "curriculum.html", {'form': form})

def pri(request):
    value = request.GET.get('value', '1')
    if value == "1":
        print('1')
        return render(request, "language_articles.html", {'content':["10 Most Popular Programming Languages Today",
         "1. Java is top pick as one of the most popular programming languages, used for building server-side applications"             +
         "to video games and mobile apps. Its also the core foundation for developing Android apps, making it a favorite of"            +
         "many programmers. With its WORA mantra (write once, run anywhere), its designed to be portable and run happily across"        +
          "multiple software platforms. I first got started with Java server programming back in 1999--it was so exciting," + 
          "I actually wrote a few books about it. Java is everybodys pal!",
         "2. Python is a one-stop shop. There's a Python framework for pretty much anything, from web apps to data analysis. In fact, " +
          "WordStream is written in Python! You're the best bud. Python is often heralded as the easiest programming language to learn,"+
          "with its simple and straightforward syntax. Python has risen in popularity due to Google's investment in it over the past "  +
          "decade (in fact, one recent study has shown Python to be the most commonly taught programming language in U.S. schools)."    + 
          "Other applications built with Python include Pinterest and Instagram.",
          "3. C. If you saw C on a report card, you'd be pretty bummed. Maybe a bit confused, too (is it actually a B-?). However,"     +
          "C is not the bizarrely bad grade it seems to be. It's often the first programming language taught in college (well, "        +
          "it was for me 10 years ago). I thought it was a nice "'in-between'" language in that it was object oriented without having"  +
           "to be fanatical about it. It was also low level enough to be close to hardware, but no so low level that you had to do"     +
           "everything manually. Because there are so many C compilers, you can write stuff in C and have it run pretty much anywhere.",
           "4. Ruby (also known as Ruby on Rails) is a major supplier of web apps. Ruby is popular due to its ease of learning "        +
           "(it's very straightforward) and power. Ruby knowledge is in high demand these days!",
           "5. JavaScript (which, confusingly, is not at all related to Java) is another favorite programming language because it's "   +
           "so ubiquitous on the web--it's basically everywhere. JavaScript allows developers to add interactive elements to their "    +
           "website, and its presence is felt across the internet. At WordStream, we use a JavaScript library called JQuery to make our"+
           "JavaScript work even easier.",
           "6. C# (pronounced C-sharp, not C-hashtag for you Twitter fans) is the language used in order to develop Microsoft apps. C#" +
           "is syntactically nearly identical to Java. I've spent much time training with C#, but if you're good at Java, you'll likely"+
           "have an easy time jumping onto C#. If you're looking to work on Microsoft apps, C# is the way to go. C# opens a lot of "    +
           "Windows (har-har).",
           "7. PHP (which stands for Hypertext Preprocessor, if you care to know) is often used in conjunction with dynamic data-heavy" + 
           "websites and app development. It provides a ton of power and is the beating heart of monster sites like WordPress and "     +
           "Facebook. What's really cool about PHP is that it's an open-source language, so there are tons of free pre-built modules"   +
           "that you can grab and modify to get your ideal results. PHP is also on the easy end of the learning spectrum, simply"       + 
           "requiring you to embed the code within HTML. PHP is a must-learn language for aspiring web developers.",
           "8. Objective-C is the programming language behind iOS apps. Apple's new language Swift is rising in the ranks, but"         +
           "Objective-C is still the recommended starting point for those looking to craft Apple apps for iPhones and iPads. Next"      + 
           "stop--the iOS App Store!",
           "9. SQL is a database query language (SQL stands for Structured Query Language) that's ideal when talking big data. SQL lets"+
           "you siphon helpful data from massive databases. Nearly every app has a backend database, and SQL is the language that helps"+
           "you interact with that sweet data. In terms of software development, SQL isn't ever used alone--rather, you invoke SQL from"+
           "some other programming knowledge and you have yourself a nice package deal.",
           "10. C is the predecessor to more complex programming languages like Java and C#. C is best when you want to work small and" + 
           "when dealing with low-level applications. It's widely used for embedded systems like the firmware of your television or the"+ 
           "operating system of an airplane, as well as computer operating systems like Windows. For me personally, C was more of an"   + 
           "academic language. It was nice to learn how to write a kernel back in college, and you gain a more solid understanding of " +
           "how newer languages work under the covers, but it's rare for most application developers to ever have to use this today."   +

           "There you have it--the king languages of coding. What's your programming language of choice and why? If you're a newbie "   +
           "looking to dive into coding, take a look at these nine spots on the web where you can learn to code (for free)! You'll be a"+
           "code master in no time."

          ]})
    elif value == "2":
        print('2')
        return render(request, "language_articles.html", {'content':["7 Best Frameworks For Web Development in 2017",
         "segundo"]})
        levels = '2'
    elif value == "3":
        print('3')
        levels = '3'
        return render(request, "language_articles.html", {'content':["ultimo comom", "segundo"]})
    elif value == "4":
        print('4')
        levels = '4'
        return render(request, "language_articles.html", {'content':["ultimo", "segundo"]})
    


class ProjectsPageView(TemplateView):
    template_name = 'projects.html'

class TutorialsPageView(TemplateView):
    template_name = 'tutorials.html'

class ArticlesPageView(TemplateView):
    template_name = 'articles.html'

class LanguagesPageView(TemplateView):
    template_name = 'languages.html'

class VideosPageView(TemplateView):
    template_name = 'videos.html'

class Languages_ArticlePageView(TemplateView):
    template_name = 'language_articles.html'

    



