# Fitness First

Fitness First is a website/application designed to help users reach their fitness goals without the hassle or costs of gym memberships. 
The site focus on using minimal equipment whilst keeping the workouts quick and effective. We also offer meal plans to further help users reach their goal.

## UX

Please head over to the UX folder to find my marvelapp mock ups and my User stories that I used in the planning process.

<a href="{% url 'user_stories' %}">


## Features

#### Feature 1 - Subscription
The Subscription feature is one set cost of $6.99 per week, this allows users full access to the site. This opens up more workouts and more meals to the customer.

#### Feature 2 - Free trial 
Without subscribing any user can log on and access 1 days worth of any programme for free. For E.G. 3 meals, a snack and a workout is accessible to anyone who opens the site. 
The reason for this is I wanted to give any user a taste of what might be coming should they choose to subscribe so they know if its for them or not.

#### Feature 3 - Variety
Offering a variety of programmes opens up the target audience to everyone. No matter the goal of the user this site offers something for them. I didnt want to make a site that
was specificallty for bodybuilding or any one thing particularly. As a business plan I think it is a positive move to target a wider audience.

### Features to implement

#### More detail
If i had more time to work on this project I would deepen the product detail. More workouts, more meals. For E.G. Offering a 6 week programme, 12 week programme all at different costs.
I would also offer a yearly subscription which the customer could pay weekly/monthly/yearly depending on their choice. 

#### Videos on the page 
The workout videos that are currently external links to youtube. I would like to have those embedded into the code so a user can view them without being redirect to another tab.

#### Store 
I would also like to add a store to the site. This would allow users to purchase all the equipment necessary for the workouts (pull-up bars, kettleballs, skipping ropes etc..).
In addition to that there would be some workout apparel available - tanktops, t-shirts, shorts, joggers, yoga pants, water bottles etc..


#### Images
I would also have preferred to have used some images for the meals. Maybe even video instructions on prepping and cooking. But an image of the final product would add a nice effect to 
the page. 

In addition to all of these. The videos used for workouts are not at all what I would want to use. I would prefer to create them all myself or one specific trainer to keep things consistent.
I simply used 3 youtube videos as examples to the function of the site.

# Technologies Used

- Stripe to initalise payment methods.
- Bootstrap for navbar and layout designs.
- Google fonts to specify the font chosen.
- Django framework to simplify the building process.
- Python.
- Javascript.

# Testing

Throughout this project I encountered several bugs and issues. Firstly I struggled linking my templates to eachother through the navbar. This was a difficult problem as I couldnt understand why it wasn't 
working despite going through the course material, slack and tutor support all unsucessfully! Eventually I realised I was missing a folder. For example I had programmes/templates/build_muscle.html and that
wasnt working, what I had to do was make the path programmes/templates/programmes/build_muscle.html and then everything ran smoothly. 

Furthermore I am struggling to get the card element from stripe to show on my project. I have revisited the course material and checked over my views/urls/html/js code for it and still cannot see the issue. 
I found out the issue was the same as the one above, I had to create another folder called subscriptions within the static folder and then everything worked perfectly. 

As a user I want to be able to view workouts and meals as examples before signing up so I had to ensure that there were some available to all user and not just subscribed users. 

As a user I want to be able to navigate and view the site easily and quickly identify the specifc programme to my personal goals. To do this I had to make the site simple, clear and effective. Something I continously 
tested myself and feel succeeded in the resulting project.

I also ran the code through several validators https://validator.w3.org/nu/?doc=https%3A%2F%2Fpink-yak-0xgs5a6b.ws-us03.gitpod.io%2F showed 6 warnings.
http://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fpink-yak-0xgs5a6b.ws-us03.gitpod.io%2F%23%2Fworkspace%2Ffitness-first&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en showed 0 errors.

I had some issues with deployment also. I couldnt login to heroku through the terminal but had to input "heroku login -i" instead of "heroku login". 
Furthermore deployment is still failing and I am unsure why. I am getting a Bad Request(400) but cannot think why at this time. 
I resolved this issue through the help of tutor support. The aws region name was labelled incorrectly.

Finally I couldnt get the payment intent working. I spent my last day working on it and was unsuccessful in solving the issue. I am not sure what the issue is but unfortuneatley I ran out of time and had to submit an 
incomplete project.

# Deployment

To deploy this project I used Heroku. For this project I deployed my app through Heroku. These are the steps I followed: 
1. Sign in to Heroku. 
2. Add a new app named "fitness-first" 
3. Under deployment method select "connect to github". 
4. Link the specifc github repo to the heroku app. 
5. Go to settings and then reveal config vars. 
6. I added the following. 
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - DATABASE_URL
    - DISABLE_COLLECTSTATIC
    - SECRET_KEY
    - STRIPE_PUBLIC_KEY
    - STRIPE_SECRET_KEY
    - STRIPE_WH_SECRET
    - USE_AWS
7. Scroll down to domain. 
8. You will see this message. Your app can be found at https://fitness-first1.herokuapp.com/

To run this file locally: 
1. Follow this link to the github repository https://github.com/phillrutherford/fitness-first 
2. Select code. 
3. Copy the url for the repository. 
4. In your chosen development environment open the terminal. 
5. Type git clone and then paste the url from step 3.

# Credits

- The image is from google images.
- The colour is from bootstrap
- Stripe is used for the payment intent
- Navbar is used from bootstrap
- Font is from Google Fonts.

The project idea comes from an app called Centr. An app I use for my personal workouts and meals.

### Acknowledgement
Inspiration for the project comes from an app called Centr. An app I use for my personal workouts and meals. 
Also given the recent time with COVID alot of the world has been on lockdown so coming up with creative home workout routines has been a challenge for many people.
With the help of my mentor Jonathon on the coding side of the project I was able to come up the end product as you see it.
Alot of the coding format was inspired by the course material, the way I learned it was the easiest and most effective way to produce the final product.