---
layout: project
category: draft
title: Video Boleba
description: installation
url: video-boleba/
date: 2012-11-10T01:14:56
cover: /images/covers/video-boleba-300x90.jpg
github: https://github.com/thiagohersan/videoBolebaArduino
collab: https://www.youtube.com/user/CelinaPortella
---
In October of 2012 I helped Brazilian performance and video artist Celina Portella with her latest video installation, Video Boleba.

![](bolebaBoyStill.jpg)

Video Boleba is an electro-mechanical video installation that blurs the boundary between representation and reality. It consists of a 2-hour video of kids shooting marbles out of the corner of the screen, and a machine that shoots real marbles from behind the television.

<div class="video-wrapper">
    <iframe width="640" height="360" src="http://www.youtube.com/embed/7qkE40LC90s" frameborder="0" allowfullscreen=""></iframe>
</div>

The marble-shooting mechanism was developed by **Steger Produção De Efeitos Especiais**, a special effects production company in São Paulo. I was responsible for synchronizing the video with the marble shooting machine.

This could've been done in a variety of ways: from a fully-automated approach of visually detecting the marble movements in the video, to a fully-manual approach of using a time-table specifying when the marbles should be shot.

In order to keep the synchronizing mechanism simple, save on equipment, and at the same time have the system work with different videos without having to re-compile any code or modify any text files, I decided to use the audio channel from the video to trigger the machine.

During editing, an inaudible 20kHz signal is inserted in the audio track of the video a few hundred milliseconds before the marble is to come out of the frame. This signal is then detected by an Arduino that sends the signal to a relay that fires the marble machine.

![](bolebaSchematic.jpg)

This way, after the system is calibrated and working, the video can be changed without having to change anything in the machine or the Arduino. No text files have to be updated and no code has to be re-compiled.

Using a whole Arduino to basically do what a [monostable 555 timer](http://en.wikipedia.org/wiki/555_timer_IC#Monostable) does, seems a little exaggerated, but since the project was developed by 3 different people, in 3 different cities, this was the safest and easiest way to have an adjustable trigger/synchronizer circuit whose signals could easily be adjusted/delayed in the millisecond range.

![](bolebaCircuitStill.jpg)

This was good because both the delay and the on-time for the trigger signal had to be adjusted in the code during final testing and calibration.
