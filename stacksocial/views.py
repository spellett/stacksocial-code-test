import plugins.twitter as twitter

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    template_vars = {}
    return render_to_response('index.html', template_vars, context_instance=RequestContext(request))

def term_tweets(request):
    template_vars = {}

    search_results = twitter.get_tweets_by_term('venice')
  
    template_vars['tweets'] = search_results.get('statuses')

    return render_to_response('termTweets.html', template_vars, context_instance=RequestContext(request))

def user_tweets(request, handle, **kwargs):
    template_vars = {}

    template_vars['handle'] = handle

    template_vars['tweets'] = twitter.get_tweets_by_user(handle)

    return render_to_response('userTweets.html', template_vars, context_instance=RequestContext(request))
