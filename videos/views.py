from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render
import os
import fnmatch

# Create your views here.

def display_video(request, vid="flowerAndPig_music"):
        if vid is None:
            return HttpResponse("No Video")

        #Finding the name of video file with extension, use this if you have different extension of the videos
        video_name = ""
        for fname in os.listdir(settings.MEDIA_ROOT + "/videos/"):
            #if fnmatch.fnmatch(fname, vid + ".*"): # using pattern to find the video file with given id and any extension
            if fnmatch.fnmatch(fname, vid + ".mp4"): # only mp4 extension
                video_name = fname
                break

        #getting full url -
        video_url = settings.MEDIA_URL + "videos/" + video_name

        return render(request, "video_template.html", {"url":video_url})


def display_video_quiz(request, vid="quiz"):
    if vid is None:
        return HttpResponse("No Video")

    # Finding the name of video file with extension, use this if you have different extension of the videos
    video_name = ""
    for fname in os.listdir(settings.MEDIA_ROOT + "/videos/"):
        # if fnmatch.fnmatch(fname, vid + ".*"): # using pattern to find the video file with given id and any extension
        if fnmatch.fnmatch(fname, vid + ".mp4"):  # only mp4 extension
            video_name = fname
            break

    # getting full url -
    video_url = settings.MEDIA_URL + "videos/" + video_name

    return render(request, "video_template.html", {"url": video_url})