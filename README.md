# Athena_Hack_2021
EasyCycle - a hassle-free recycling app for the Athena 2021 Hackathon

## How to use:
1) Install packages in terminal: pip install requirements.txt
2) To launch the website:
    In your terminal, run python3 app.py
    either 
        click on the link displayed in the terminal
        or type localhost:5000 in your browser to access the website 
   

## Model Training
1) open the Hackathon_Final.ipynb in Colab / Jupyter notebooks
2) run all the cells in order to load packages, data, and train an ML model using the TrashNet dataset
Papers we were inspired by: https://www.sciencedirect.com/science/article/pii/S0921344920304493


## Inspiration
Recycling is an essential part of the circular economy - it ensures we can repurpose materials to create new products instead of letting the materials go to waste. However, still not enough products get recycled. 
**Why don't people recycle**
Commonly reported frustrations with recycling are:
- "It's a hassle, I can't be bothered"
- "I don't know what to recycle where" 
- "It doesn't actually help"

In addition, there's a disconnect between products builds to promote recycling and their audience. Existing recycling website and apps are often convoluted, have bad interfaces, and don't give potential users a reason to use the app other than an abstract idea of "I'll recycle because I have to".

To address these concerns we've built a website powered by state of the art AI models that makes recycling transparent, easy and fun!

## What it does
EasyCycle is a website (with dreams of becoming a mobile app), that gives you an incentive to recycle and clear up confusion about recycling. It's three simple steps:
- you take a picture of your rubbish. Our state of the art machine learning models then determine what the product is and if you can recycle it.
- you dispose of your rubbish in the way that the website suggests
- you log that you've recycled correctly! Well done! As a reward, you get points to spend on discounts at sustainable brands.

You can even participate in team challenges with your social group or neighbourhood to earn your goal amount of recycle points for even bigger rewards! And the app introduces you to sustainable brands so if you have an item that can't be recycled you get introduced to a sustainable alternative.

###  Website Navigation:

1) Homepage: displays the key pillars of our product
    - know your recyclables
    - join our community
    - make the switch (to sustainable goods)
    
2) Recyclable checker:
   - powered by AI, this computer vision tool recognises your trash
   - browse for an image and click upload
   - you will be redirected to the results page where you can find out what to do with your trash
    
3) Community:
   - log your recyclables
   - join a team and complete challenges
   - earn EasyCycle reward points
    
4) Rewards:
    - follow the links to the sites of our sustainable partners
    - unlock discounts by recycling more!
    

## How we built it
The AI model was built in pytorch.
The website is html, javascript and css with a flask backend.

## Challenges we ran into
Not enough data, not enough time! AI models take a lot of time to train properly so although we have a model that works, its accuracy could be better. There also aren't many open-source rubbish datasets on the internet, so if we had more data the classification would be better as well.

## Accomplishments that we're proud of
We all love the website which is stylish and modern, unlike some of the websites we came across in our market research. In addition, the AI model has a real opportunity to make recycling easier as it does away with typing in your waste product and makes the app easy to use. 

## What we learned
We split the team in a front-end and back-end pair. The front-end pair got to learn a lot about web development, using the Bootstrap package, and creating webpages that look good on any device. The back-end pair learned how to create and AI model from scratch under time pressure and got more pytorch knowledge.
And of course we all learned about the circular economy!

## What's next for EasyCycle
There are a few features which we haven't managed to implement yet. 
These are:
- location services, that load the recycling data for your specific location. This is invaluable for trips to other countries with a different recycling infrastructure. It could even be more fine-grained, as London boroughs also all have different recycling guidelines. Location services help determine exactly what's appropriate for your location
- nearby recycling centre finder. For when you have a couch (or a car, or three tons of crude oil) to recycle and you need to find the nearest place for recycling
- alternative products for non-recyclables. If your product isn't recyclable, your might want to switch to a more sustainable alternative. Ideally, the app would suggest certified partner companies that produce a similar version of the same product
