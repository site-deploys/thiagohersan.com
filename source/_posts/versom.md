---
layout: project
category: draft
title: VerSom
description: performance software
url: versom/
date: 2012-08-17T21:56:16
cover: /images/covers/versom-300x90.jpg
---
During the months of august and september of 2012, I worked with the residents Ciça Lucchesi and Juliana Perdigão on their project *VerSom* while they were in residency at Marginalia+Lab.

*VerSom* is a loosely defined performance and experimentation environment. It is an opportunity for Ciça, Juliana and other collaborators to explore the relationship between images and sounds.

Part of my contribution to the project was a real-time system for triggering simple animations based on the vowels being sung by Juliana.

The animation system was created in Processing based on initial sketches done by Ciça in Modul8. It consists of a few different reactive scenes and a simple control panel to enable/disable different scenes and to vary different parameters.

The control-panel/GUI:

![](/images/projects/versom/UI.png)

And some of the scenes. This one created ‘O’ shapes whose size varied in accordance to the volume of the voice detected by the microphone:

![](/images/projects/versom/O2.png)

This one released running streams of vowels in different directions:

![](/images/projects/versom/AE.png)

This one used a [physics engine](http://www.jbox2d.org/) to simulate realistic arcing trajectories for small words made up of vowels:

![](/images/projects/versom/I.png)

More than one scene can be enabled at any given time, with different vowels, determined by the control panel:

![](/images/projects/versom/AEOU.png)

The vowel-detection system was developed in Max/MSP using [Linear Predictive Coding](http://en.wikipedia.org/wiki/Linear_predictive_coding) analysis and filtering.

The Processing code for the [scenes](https://github.com/thiagohersan/VersomVogaisProcessing) and the [control panel](https://github.com/thiagohersan/VersomControleProcessing) are on github.
