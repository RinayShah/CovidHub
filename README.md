# CovidHub
## IBM Intern Hackathon 2020
### Group Members: Roman Rezinkin, Rachit Sharma, Rinay Shah, Abhishek Chatterjee, Alan Tran

# Table of Contents
* [Introduction](https://github.ibm.com/Roman-Rezinkin/CovidHub#introduction)
* [Technologies](https://github.ibm.com/Roman-Rezinkin/CovidHub#technologies)
* [Requirements](https://github.ibm.com/Roman-Rezinkin/CovidHub#requirements)
* [Status](https://github.ibm.com/Roman-Rezinkin/CovidHub#status)
* [Acknowledgements](https://github.ibm.com/Roman-Rezinkin/CovidHub#acknowledgements)

## Introduction
The COVID-19 epidemic has led to isolation measures being implemented by governments all around the world in order to contain this virus. Chief among these measures, is a quarantine; which involves physically isolating yourself in your home, away from the outside world. However, a quaratine is only effective as long as the home is COVID free. What if you accept delivery of a package that potentially has COVID-19 residue on its packaging? Or you order takeout and the container potentially transfers COVID-19 to your dining table? Any of these potentially drastic situations could result in exposure to the virus, leading to possibly being infected with it. As IBMers, we thought about this problem and came up with CovidHub. CovidHub is a web dashboard, designed to be the one stop solution for all your COVID-19 concerns. It features an interactive ChatBot, which uses the power of the IBM Cloud and Watson AI in order to answer your queries. Need to know the latest local news about COVID-19? No problem. Confused about how to disinfect a surface around your home? Our object recogniser model, which is seamlessly integrated into our chatbot can identify surfaces from an image and provide you with important information, such as how long the virus will last on the surface as well as tips on disinfecting the surface. CovidHub is the fastest way to get the information you need, in order to keep you and your loved ones safe during this crisis.

## Technologies
The web dashboard uses a mix of HTML, CSS, JavaScript and the Bootstrap framework. The chatbot runs on the IBM Cloud and uses Watson Assistant and Watson Discovery. The object detection model is written in Python, and uses the Watson Visual Recogniser API and the IBM Cloud. The model communicates with the web dashboard using Flask. The dashboard, along with the object detection code is hosted on IBM Cloud Foundry.

## Requirements
A web browser is all that is needed to experience the dashboard :)

To start a webserver session, run `$ npm install` and then `$ npm start`

You can also directly access our dashboard at this [link](http://think-fyre-covid-hub.us-east.mybluemix.net)

## Status
As of 16th July 2020, the project is still active. We are open to ideas on how to expand the offerings of the CovidHub dashboard.

## Acknowledgements
We used the [Watson Recognition API](https://www.ibm.com/cloud/watson-visual-recognition) in order to create the object recognition model. Furthermore, we used [Watson Assistant](https://www.ibm.com/cloud/watson-assistant/) and [Watson Discovery](https://www.ibm.com/watson/services/discovery-news/) in order to create the chatbot and embed it within our website.
