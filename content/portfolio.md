title: Personal Site (tristian.us)
date: 2014-08-01
author: Tristian Azuara
slug:personal-site
category: system-implementation
tags: personal-site,planning
summary: The design process of my personal site.
thumbnail: http://i.imgur.com/sZmkn4i.png

Like every professional in the software and engineering industry I needed a way to convey
my knowledge, experience and skills to future clients; in other words to create a personal brand. 
Thats how the planning and development of this site began.

## Constraints, Goals and oportunities

One cannot just decide that you need a personal site and get started with the development. As with every project it has to be 
planned; to a certain degree (not to every detail).

I had simple goals for this site:

 * It had to reflect my skills, knowledge and experience.
 * It had to function as a publishing platform.
 * It had to provide a way to engage prospects.
 * It had to have a clean, simple and maintaineble design (visually and logically).

The above goals are quite common, simple and a bit vague. Thats why every project (and system) 
needs to adhere to *constraints* that allow to narrow down the paths on how to reach
the stablished goals. Constraints can be of any type; technical, technological or resourced based are few of 
the most common types.

The constraints for this project were:

 * It had to be a *static* generated site.
 * It had to use free hosting platforms.
 * It had to strive for web responsiveness.
 * It had to rely on FOSS components.
 * It had to be easy to maintain.

The constraints pretty much limit the _solution space_, my constraints were mostly technical and technology 
focused because a personal site is an on-going project in which time is not rigourously controlled.

In my opinion every project that is undertaken should offer oportunities of growth and self-improvement; be it
by learning new skills, trying new technologies or adopting different methodologies.

## Design

Design not only refers to the visual design but also on how the solution will be aproached.

The second goal "reflect my skills, knwoledge and experience" obviously requires an about page (about me)
where I list my areas of expertise and how I've developed my self profesionally and technically. 
I had an objective for my about page; It had to use charts to represent my knowledge.

The third goal defines it as a _publishing_ platform; that involves having content produced peridically.
Content would be related to the work and services that I offer.

The fourth goal is to engage prospects. My solution to that offer a newsletter/mailing list where 
visitors can subscribe and receive updates with content that add value to their business or that are
relevant to their fields. Also a comments section for each publication.

The fifth goal says that it has to be maintainable, be simple and clean. This particular goal 
requires use of creativity and is polished across all stages of the project, it was not decided
completely at the start of the project.

## Implementation

So, now that I've defined in terms of the user experience how the site will work it is time to determine
the tools and technology to implement it.

With the creation of a personal site, I wanted to explore using a static site genertor, also I wanted it 
to be python based. That left me with only two options (that I know of):

 * [Hyde][1]
 * [Pelican][2]

At first I tried using Hyde, but it seems like the project development has not been that active and I had 
a few issues while testing it. Then I tried pelican and I was convinced, it seemed to fit my work flow better
and I like the way it has been architected.

For showing my skills I wanted to use a chart, after fiddling with the idea of creating a charting library specific for showing skills
I found [chart.js][3] which is an absolutly wonderfull charting library.

I then started looking on how to create themes for Pelican something that is well documented on the [Pelican docs][4]

The articles are created using markdown, reStructured text or even html if a more *intricate* and *detailed* article is needed.

To showcase projects that I've worked on I'll create articles and categorize them with the `project` category, those articles 
will not appear on the index page.

## Conclusion

Creating a personal site is like every project, it has to be planned, it has to be contrained and it 
has to offer oportunities of personal and professional growth.

It is an ongoing project but I believe I've set the guidelines and took advantage of the oportunities it presented.


[1]:https://hyde.github.io/
[2]:http://blog.getpelican.com/
[3]:http://www.chartjs.org/
[4]:http://pelican.readthedocs.org/en/latest/themes.html
