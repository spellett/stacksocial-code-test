import plugins.twitter as twitter

from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

def index(request):
    return redirect('term_page')
    #template_vars = {}
    #return render_to_response('index.html', template_vars, context_instance=RequestContext(request))

def term_tweets(request):
    query = request.REQUEST.get('query', 'stockr')

    search_results = twitter.get_tweets_by_term(query)
  
    template_vars = {}
    template_vars['tweets'] = search_results.get('statuses')

    return render_to_response('termTweets.html', template_vars, context_instance=RequestContext(request))

def user_tweets(request, handle, **kwargs):
    template_vars = {}

    template_vars['handle'] = handle

    tweets = twitter.get_tweets_by_user(handle)
    template_vars['tweets'] = tweets

    if tweets:
        template_vars['profile_img_url'] = tweets[0].get('user').get('profile_image_url')

    return render_to_response('userTweets.html', template_vars, context_instance=RequestContext(request))
