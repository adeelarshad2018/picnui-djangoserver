"""picnui_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from server.controller.manage_routines import *
from server.views import testing

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^RecoredVideo/', RecordedVideoEvent),
    url(r'^KinectLiveStream/', KinectLiveStreamEvent),
    url(r'^CameraLiveStream/', CameraLiveStreamEvent),
    url(r'^CameraStaticImage/', CameraStaticImageEvent),
    url(r'^KinectStaticImage/',KinectStaticImageEvent),
    url(r'^StaticImage/', StaticImageEvent),
    url(r'^SaveRoutine/', SaveRoutineEvent),
    url(r'^GetRoutines/', GetRoutinesEvent),
    url(r'^DeleteRoutine/', DeleteRoutineEvent),
    url(r'^UpdateRoutine/', UpdateRoutineEvent),
    url(r'^SaveRobotProfile/', SaveRobotProfileEvent),
    url(r'^GetRobotProfiles/', GetRobotProfilesEvent),
    url(r'^DeleteRobotProfile/', DeleteRobotProfileEvent),
    url(r'^UpdateRobotProfile/', UpdateRobotProfileEvent),
    url(r'^GetRobotProfileWithRoutine/', GetRobotProfilesWithRoutineEvent),
    url(r'^TriggerWebotsSim/', TriggerWebotsSimEvent),
    url(r'^TriggerURSim/', TriggerURSimEvent),
    url(r'^testing/', testing),


]



