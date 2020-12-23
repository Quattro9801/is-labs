# Tasks

## Lab 1: Prolog introduction

What do you need to do:
- find and configure any Prolog [implementation](https://en.wikipedia.org/wiki/Comparison_of_Prolog_implementations)
- develop a knowledge base:
  - populate it with some facts
  - add as many rules as possible for extracting additional knowleges out of raw facts
  
Example:

```
male(tom).
female(angela).
female(lisa).
parent(tom, angela).
parent(lisa, angela).

% define mother(X, Y), mother(X)
% define father(X, Y), father(X)
% define son, brother, sister, daughter and other relationship
```

Example 2:

```
hobby(drawing).
hobby(sketching).
related_hobbies(drawing,sketching).
person(john).
likes(john, drawing).

% define common_interest(Person1, Person2)
% define suggested_hobbies(Person)
% define unpopular_hobbies(Hobby)
% define the_most_popular_hobby(Hobby)
```

Example 3:

```
book("Title", 120). % 120 - number of pages
written_by(john, "Title").

% define small_book(Book), huge_book(Book)
% define the_biggest_book(Book)
% define author_of_small_books(Author)
```

## Lab 2: Multi-agent systems

The idea of this task is to try and implement a tiny-tiny simple multiy-agent system,
just to get an idea of it and encounter typical problems in that area.

What do you need to do:
- select some existing MAS framework, suggested ones are:
  - [JADE](https://jade.tilab.com/) for JAVA folks
  - [pade](https://github.com/grei-ufc/pade) for python folks
- get yourself familiar with the framework
- code some simple MAS:
  - you need at least 2 agents that communicate about something
  - it is not enough to just send a message from one to another, there should be
    series of replies
    
Example:

One agent tries to sell something, another one tries to buy that. Both agents have some
conditions, i.e. seller wants to get maximum profit and won't sell if price is below
some MIN_SELL_PRICE; buyer wants to buy at minimum possible price and won't buy if price
is above some MAX_BUY_PRICE. So, those agents communicate with each other trying to either
agree on the price or conclude that the deal can't be performed.

Example 2:

You have several agents that need to from a group. In order to do that agents have to select
a leader within a group. So, they communicate with each other to somehow select a leader.

Example 3:

You have several agents and bunch of tasks for them. Each task require particular skill from an
agent and each agent has a unique skill. So, agents need to re-distribute tasks across them so
all tasks can be completed.

## Lab 3: Image recognition (classic algorithms)

The task is to build a simple app, which can detect and/or recognize some objects on an image
or in a video.

Requirements:
- you should use one of the methods I've shown you at the lecture: Haar cascades or
  [KNN](https://www.unite.ai/what-is-k-nearest-neighbors/) (or both)
- programming language is not really important (C++, python)
- you can choose any framework you want (like OpenCV, sklearn)

Example 1:

Find an [existing trained Haar cascade](https://github.com/opencv/opencv/tree/master/data/haarcascades)
and use it to detect some objects on an image or in a video.
Play around various configuration options you can specify to see how they affect result and what
do they mean.
Try to gather some performance data, i.e. how fast (or slow) is using Haar cascades to detect something
on images of different sizes or using different configuration options.
As a bonus, you can [try to train your own cascade](https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/)
and use it.

Example 2:

Use KNN to automatically classify some images

Example 3:

Use KNN to recognize objects on an image: for example you can try to [recognize handwriting](https://aigeekprogrammer.com/k-nearest-neighbors-handwriting-recognition/)
(letters or symbols) or try to recognize [persons on photos](https://medium.com/analytics-vidhya/face-recognition-using-knn-open-cv-9376e7517c9f).

Example 4:

Combine Haar cascades and KNN, i.e. at first you will need to detect whether object is even present
on the image and only then try and recognize it.

## Lab 4: Neural Networks

The task is to try and experiment with neural networks, i.e. to build a simple app, which for example,
recognizes handwriting or draws images procedurally.

Requirements:
- your task should be achieved using neural networks
- besides achiving the main taks (recognition, classification, generation, etc.) you need to perform some
  experiments like measure performance of your solution, measure its accuracy, try and see how it works
  if input is corrupted or doesn't contain what you are looking for, try various configurations of neural
  networks and/or training parameters to see which one is better for your task, etc.
- you can choose any framework you would like to use:
  [PyTorch](https://pytorch.org/), [Tensorflow](https://www.tensorflow.org/), [Keras](https://keras.io/), etc.
- programming language doesn't matter as well: use what is easier for you (python, C++)

It is not necessary to train you own neural networks, because it might be expensive in terms of machine resources and time,
so if you find some pre-trained networks, you can use them. However, you still need to try to perform various experiments
even on pre-trained network: for example you can measure its accuracy on your own dataset.

Example 1:

Build a simple classifier (is it cat or a dog on the image?) or recognizer (recognize handwriting) app.
An example: [handwritten digits recognition](https://towardsdatascience.com/handwritten-digit-mnist-pytorch-977b5338e627),
[generating cats faces](https://towardsdatascience.com/getting-started-with-gans-using-pytorch-78e7c22a14a5) or
[generating people faces](https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html)

Example 2:

Build an app which transforms images by applying some artistic style on them: [artistic style transfer](https://github.com/pytorch/examples/tree/master/fast_neural_style)

Example 3:

[Superresolution](https://github.com/pytorch/examples/tree/master/super_resolution), i.e. upscaling of an image with minimal possible loss of quality and details.

Example 4:

Compare various model architectures for recognition/classification tasks: [example](https://github.com/pytorch/examples/tree/master/imagenet)