
<div align="center"><h1>Project 100 - a.k.a. tem ps5?</h1>


It has been hard to get a PS5 since launch, especially in Brazil, so I made a scraper that searches through the most popular retailers online and checks the availability (and price) of a product, in this case, the PS5.

Since I'm always trying to improve my coding skills and try out new things, I over engineered this scraper to oblivion, using things I wouldn't normally use on a scraper, like classes, Interfaces, attachable modules and even tests (jk, I use tests at work, I swear). You can check it out [here](https://temps5.herokuapp.com/) (it might take a while to load because heroku turns it off)
</div>

### my idea
okay, so I'll try and explain what it does and what it should do just so you don't look at the code and be like "wtf this kid on about". my idea was a 24/7 scraper running at intervals (once every 10 minutes?) that would scrape the product page and get availability/price. and then you could enter the website and it would tell you if its available and where (yes, there are a lot of sites that do that, I know). if it wasn't available at the time, you could leave your email and the app would message you as soon as it was.

### how I did it
so, for starters, I created an abstract class that structures how a scraper should be, what properties and methods it should have. then, I created a scraper manager, that can add scrapers as modules to itself, and this manager would call the functions on the modules, so you don't have to call functions on every scraper every time you want to scrape stuff. 

then, I made a webserver using FastAPI so I could serve the page where it tells you if its available or not. I couldn't figure out how to run the scraping as a background job so I just call the function each time the page is requested. Yeah, I know, it adds load time and I'll work on it ASAP.
