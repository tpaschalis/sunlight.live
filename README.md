# sunlight.live

TODO : Remove dev cruft from requirements.txt   
only 3 or 4 lines should actually be there, everything else is remnants from development tests

Feel free to raise Issues, create Pull Requests, or send comments! The [advice.md](https://github.com/tpaschalis/sunlight.live/blob/master/advice.md) file contains, well, advice and feedback I've gathered from other people, that I'm thinking of implementing.




## What's this?

I recently wanted to make a pixel worldmap, and dusted my undergrad astronomy books to create this illustration. The base inspiration was the pixel worldmap that exists on many Android phones "Clock" application.

sunlight.live shows the Sun's <a href="https://en.wikipedia.org/wiki/Terminator_(solar)">terminator</a>, the line which divides "day" and "night" on earth.

Mote detailed information about the development can be found on <a href="https://tpaschalis.github.io/show-hn-sunlight-live/">this blog post</a>. The project has been submitted on [Reddit](https://www.reddit.com/r/dataisbeautiful/comments/baytxa/a_liveupdating_visual_map_of_sunlight_on_earth_oc/) and [HackerNews](https://news.ycombinator.com/item?id=20284870), reaching the front-page.
 
All suggestions, insights, and astronomy-related tidbits are welcome!

## Deployment

The website runs on a $5 DigitalOcean droplet, with a near-default Apache and Let'sEncrypt, as this was all an excuse to find astronomy, not an exercise in DevOps.

The image is updated every 10 minutes using cron, Python3, a single line of <a href="http://www.numpy.org/">NumPy</a> plus some celestial mechanics formulas, and should have an accuracy of ±1 degree. 

The goal was to create a minimal, fast and aesthetically pleasing result. I'm not much of a designer, but I'm pretty happy with the first version of this site, and its small-ish size.

All plotting happens using Matplotlib. Most Matplotlib code and tutorials can be *very* confusing, but I think the source can serve as a guide to readable and maintainable plotting.

The world data is obtained from the wonderful [Natural Earth](https://www.naturalearthdata.com/) datasets, and handled using [GeoPandas](http://geopandas.org)

## Roadmap
Once I have some time, I want to :
                    
- Learn more about the accuracy of astronomical formulas
- Offer some more astronomical data through this page and an API
- Provide some more illustrations about the solar system

