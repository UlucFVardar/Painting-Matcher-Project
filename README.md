# Where are you at MEF Universty ? 


>The main idea of the project to find your location at MEF Universty. Basicly the paintings around you is the key of the finding your location. The picture given by the user program makes some processes to find best macth through Database images then program shows specific location of you on the floor plan.

# Painting Matcher Project
This is a project developed by @Uluç Furkan Vardar and @ilkay Tevfik Devran for Computer Vision lecture (COMP 482). The aim of the project to compare the implemantations in below show test results.
  > SIFT implemantation for regocnation of paintings.
  >CNN (Convolutional Neural Network)implemantation for regocnation of paintings.

# How Does Program Do This?
 > Our SIFT implemantation steps in below:
 ![alt text](https://raw.githubusercontent.com/ilkayDevran/Painting-Search/master/github_readMe_images/DiagramOfSIFT.png)

>Our CNN implemantation steps in below:
 ![alt text](https://34tzkp3af7ck1k675g1stf6n-wpengine.netdna-ssl.com/wp-content/uploads/2016/11/typical_cnn_architecture.png)
 


### Topic Research
If you want to learn more about these topics you can go for it:
* [Keras information](https://elitedatascience.com/keras-tutorial-deep-learning-in-python) - You can find needed information from this website.
* [Keras Script resource](https://gist.github.com/fchollet/0830affa1f7f19fd47b06d4cf89ed44d) - You can find how to use keras in python from here like us :)
* [TensorFlow](http://developercoding.com/tensorflow/#About-TensorFlow)- TensorFlow is an open source software library which helps us to build neural networks, more info go to link.
* [SIFT information] (A. Rosebrock, Practical Python and OpenCV : Case Studies, 3rd ed. pyimagesearch, 2016, pp. 86-105.)

After you view, lets continue

### Installation

>Firstly you need python2.7 for to run *SIFT* implementation.
,also you need python3 to use *CNN* implementation.
>For production environments...
[Install python versions to your computer](https://www.python.org/downloads/)

| Required Libraries  | installation |
| ------ | ------ |
| numpy |  pip install numpy |
| cv2 |  pip install opencv-python |
| tensorflow |  pip3 install tensorflow |
| keras |  pip3 install keras |
| graphviz |  pip install graphviz |
| pydot |  pip install pydot |


# Usage
>Usage of *SIFT* on terminal
```sh
$  python PaintingFecherWSift.py -p 'PATH OF THE INPUT IMAGE'
```
ex:
```sh
$  python PaintingFecherWSift.py -p queries/query1.png
```
 A typical output of the program:
![alt text](https://raw.githubusercontent.com/ilkayDevran/Painting-Search/master/github_readMe_images/outPutOfSIFT.png)

>Usage of *CNN* on terminal
 ```sh
$  python3 Keras_test.py
```
 
 >Sample Output of the CNN implemantation:
 ![alt text](https://raw.githubusercontent.com/ilkayDevran/Painting-Search/master/github_readMe_images/CNNTerminal.png)


 
# Mobile Text Recognizer As An Additional Project

> The Main idea of the project is to regocnize the text in real time using a mobil app.
=======
> The Main idea of the project is to recognize the text in real time using a mobil app.

for this app we use google.android.textRecognizer component.

>An android project is developed  for this reason and we can recognize text on time view.
There are sample of examples:
![alt text](https://raw.githubusercontent.com/ilkayDevran/Painting-Search/master/github_readMe_images/android%20App.png)
Our app can recognize text easly if it is computer printed.
Hand writing have some problem as shown in the image.

### Then app project improves to Sudoku Solver App 
> Our aim was to make a sudoku solver in real time.

* To do this, an API works on AWS was writen.

```sh
SUDOKU SOLVER API:
API="https://20mmb62l09.execute-api.us-east-2.amazonaws.com/prob/sudokusolver"
#this sudokuMap string is genereted from the mobil app
sudokuMap=  "530070000"+   
            "600195000"+
            "098000060"+
            "800060003"+
            "400803001"+
            "700020006"+
            "060000280"+
            "000419005"+
            "000080079"
API_result=requests.get(API+"?sudoku="+sudokuMap)
print "solution is" + API_result.text
```
>Now we have the API to solve the Sudoku

### The problem is app can not focus to the Sudoku Map clearly.
>![alt text](https://raw.githubusercontent.com/ilkayDevran/Painting-Search/master/github_readMe_images/sudoku-ex.png)
First problem is empty slots. we put zeros to empty placeses even this we cant focus the hole matrix of the sudoku map 
> !!After solving this problem app can real solve sudokus.!!

# TO DO 
* Focusing of the empty places problem, we can find a solution and app will be finished.
* Our concole apps are works but we want to move all system to AWS. Thanks to the cloud system, our service is planned to be supported on all platforms.
