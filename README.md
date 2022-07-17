##💡 Inspiration💡
Have you ever been in a situation where your friend clicked a picture of their outfit and thought ‘I want that 👀'  and immediately saved that image in your phone for inspiration? We had that problem statement in mind when we created this app. We believe that self expression is healthy and utilizing clothes to convey who you are and what you stand for is amazing. We want this app to be a tool that helps you explore *you*. 

References:
https://repeller.com/self-expression-clothing/
https://lifestylebyps.com/blogs/lifestyle/fashion-as-self-expression

## ⚙️ What it does ⚙️
- Any images you like can be saved by giving it to the Whatsapp bot. Whether it's your friend's photo from a Whatsapp group chat or elsewhere. The bot saves your image, and you can optionally write notes about the image or not, and it will be stored in your personal WhatsThatStyle gallery. You can view your gallery on the web app, and tap on any image to get similar images and their details like where to buy them and their price.
- You can plan your outfits via the notes feature of the web app, where you can upload images that you want to wear and easily access these notes that include a description that you can edit any time. 

## 🏗️ How we built it 🏗️
In a span of 48 hours, we used **Python and Flask** for the backend and **React.js** for the frontend. The designs were initially put together using **Figma**, were then changed during frontend's testing. For our database, we used **CockroachDB** , the **Google Vision API** and **Coil**.

We also did full justice to all the amazing technology that MLH and their sponsors provided us with this weekend. We used CockroachDB, Coil, Twilio and GitHub. 

## 🟣 CockroachDB 🟣
We used CockroachDB to create, delete, edit and update our resources that was populated by the Google Cloud Vision API and connected to the WhatsApp and Twilio API.

## 🔴 Twilio 🔴
We used ngrok to connect Twilio to our flask app. We used a flask POST request that the Twilio whatsapp bot calls whenever the user sends a text, and is processed by flask.

## ⚫ Coil ⚫
We used Coil's Web Monetization capabilities to provide an exclusive feature to users who have the coil extension. Monetized users can access cards in the Gallery which can provide fashion inspiration


## 🐙 Github

Our team forked, made pull requests and also created multiple branches. We did this because our program has three main components: the website, the WhatsApp bot, and the database. We created a separate branch for each of them. 

## 🚩 Challenges we ran into
- Most of us already started on a few ideas, before later getting scrapped for new ones. The moment we settled on one idea together, was when we realized the deadline was nearly closing in.
- Some of the challenges for us were either having almost _no_ challenges to start with. The team struggled to stick with a solid idea, but eventually came to it.
 - It was our first time working with GitHub pull requests and had to overcome hurdles of merge conflicts.
- One of our challenges was that this was Lu’s first hackathon so we had to get her up to speed and help her acclimate to what we were doing. 
- There were no links associated with the Cloud Vision Product set, so we had to manually load them from Google Lens and into CockroachDB. 


## 🥇 Accomplishments that we're proud of
- Being able to use Google cloud Vision to utilize their Image Detection Model
- We’re happy to have solidified our understanding of ML and Web Development principles with this project and are super happy with what we learned. 
- We’re proud of being able to work together as a team in a very friendly way considering that most of us had only met in the last 48 hours. It really is the friends you make along the way :)


## 📚 What we learned
- We learnt core principles in ML by studying the Google Vision API 
- We learnt how to collaborate more effectively using Github and LiveShare from Visual Studio
- This was a big challenge as we wanted to learn something new from this hackathon while also creating a full application, so we really tried to hone our weaknesses and are happy with what we made. 

## ⏳ What's next for Stylist?
- We want to add secure authentication if we have time. The privacy of this app is really important, as you do not want others to see your personal-saved photos. We might implement this system using Twilio Verify API or DeSo authentication.
