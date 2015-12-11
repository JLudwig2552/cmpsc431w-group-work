from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from Main.models import Page, Categories, Items
from Main.forms import UsersForm, BaseUserForm
from django.contrib.auth import authenticate, login, logout

import itertools
import MySQLdb as mdb
import sys

'''
def category(request, category_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Categories.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Categories.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'Main/index.html', context_dict)

'''

def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/Main/')

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/Main/')
                #return render (request, 'Main/index.html',{})
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your EBDB account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'Main/login.html', {})


def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = BaseUserForm(data=request.POST)
        profile_form = UsersForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = BaseUserForm()
        profile_form = UsersForm()

    # Render the template depending on the context.
    return render(request,
            'Main/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


def add_user(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = UsersForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = UsersForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'Main/add_user.html', {'form': form})

def itemdetails(request, item_name):
    try:
        con = mdb.connect('localhost', 'Admin1', 'Admin1', 'Inceptionists');

        cur = con.cursor()
        cur.execute("select i.name, u.name, description, price from user u, items i, sells s where i.itemID = s.itemID AND sellerID = u.userID and i.name = %s", [item_name])

        itemz = list(itertools.chain.from_iterable(cur))

    except mdb.Error, e:

        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)

    finally:
        if con:
            con.close()

    template = loader.get_template('Main/item.html')
    context = RequestContext(request, {
        'itemz': itemz,
    })
    return HttpResponse(template.render(context))


def category(request, category_name):
    try:
        con = mdb.connect('localhost', 'Admin1', 'Admin1', 'Inceptionists');

        cur = con.cursor()
        #cur.execute("SELECT name FROM items")
        if category_name == "all":
            cur.execute("SELECT name FROM items")
        else:
            cur.execute("SELECT name FROM items WHERE category = %s", [category_name])

        itemss = list(itertools.chain.from_iterable(cur))

    except mdb.Error, e:

        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)

    finally:
        if con:
            con.close()

    template = loader.get_template('Main/category.html')
    context = RequestContext(request, {
        'itemss': itemss,
    })
    return HttpResponse(template.render(context))
    #return HttpResponse("Category name : %s " % category_name)

def index(request):
    try:
        con = mdb.connect('localhost', 'Admin1', 'Admin1', 'Inceptionists');

        cur = con.cursor()
        cur.execute("SELECT name FROM categories")

        #categories = cur.fetchall()
        categoriess = list(itertools.chain.from_iterable(cur))  #no longer being used

    except mdb.Error, e:

        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)

    finally:

        if con:
            con.close()

    category_list = Categories.objects.all()
    #context_dict = {'categories': category_list}

    template = loader.get_template('Main/index.html')
    context = RequestContext(request, {
        'categories': category_list,
    })
    #return render(request, 'Main/index.html')
    #return HttpResponse("Database version : %s " % ver)
    #return HttpResponse(template.render(context))    <---previous working version
    return HttpResponse(template.render(context))


def about(request):
    return HttpResponse("Programmed by Fliu and Rcamp")

