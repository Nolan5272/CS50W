from django.shortcuts import render
from django.shortcuts import redirect
from django import forms
import random 

from . import util 

import markdown2

class NewWikiForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content", widget=forms.Textarea)



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries() 
    })

def new(request):
    if request.method == "POST":
        form = NewWikiForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
        if title in util.list_entries():
            return render(request, "encyclopedia/new.html",{
                "form":form
            })
    
        content = (f"#{title}" + " \n" + content)
        util.save_entry(title, content)
        convert_html = markdown2.markdown(util.get_entry(title))
        
        return render(request, "encyclopedia/entry.html", {
            "content": convert_html
        })
    return render(request, "encyclopedia/new.html", {
        "form": NewWikiForm()
    })

def entry(request, title):

    entries = util.list_entries()
    matched_entry = None
    for entry_name in entries:
        if entry_name.lower() == title.lower():
            matched_entry = entry_name
            break

    if matched_entry is None:
        return render(request, "encyclopedia/none.html", {"message": title})
    else:
        convert_html = markdown2.markdown(util.get_entry(matched_entry))
        return render(request, "encyclopedia/entry.html", {
            "content": convert_html,
            "title": matched_entry
        })
    
def edit(request, title):
      form = NewWikiForm()

      if request.method == "GET":
          exsisting_entry = util.get_entry(title)
          form = NewWikiForm(initial={"title": title, "content":exsisting_entry})
          return render(request, 'encyclopedia/edit.html',{
              "form": form,
              "title": title
          })
      if request.method == "POST":
          form = NewWikiForm(request.POST)
          if form.is_valid():
              title = form.cleaned_data["title"]
              content = form.cleaned_data["content"]
            
          util.save_entry(title, content)
          convert_html = markdown2.markdown(util.get_entry(title))

          return render(request, 'encyclopedia/entry.html',{
              "content": convert_html,
              "title": title
          })
        

def search(request):
    #print("Search GET data:", request.GET)
    title = request.GET.get("q", "")
    entries = util.list_entries()
    matched_entry = None

    for entry_name in entries:
        if entry_name.lower() == title.lower():
            matched_entry = entry_name
            break
    if matched_entry is None:
        #return render(request, "encyclopedia/none.html", {"message": title})
        #make into error code instead
        search_results = []
        for entry_name in entries:
            if title.lower() in entry_name.lower():
                search_results.append(entry_name)
        if not search_results:
            return render(request, "encyclopedia/none.html", {"message": title})
        else:
            return render(request, "encyclopedia/search.html", {
                "results": search_results
            })
    else:
        convert_html = markdown2.markdown(util.get_entry(matched_entry))
        return render(request, "encyclopedia/entry.html", {
            "content": convert_html
        })
    
def random_entry(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    convert_html = markdown2.markdown(util.get_entry(random_entry))
    return redirect("encyclopedia:entry", title= random_entry)
