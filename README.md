# Aligner for movie scripts and subtitles

<h2>About</h2>
aligner.py is a program that aligns the moviescript with the subtitles by using regex and string comparison. The program first divides each subtitle and each part of the script. It then assigns an appropriate tag to the script lines: metadata (M), character (C), dialogue (D), scene boundary (S) and scene description (N). Then it takes the dialogue from the script and removes its tag again, so that it is ready to be compared. After the preprocessing is done, the program takes the dialogue from both the subtitles and the script and aligns them using string comparison.
For a more detailed explanation about the code, you can look at the comments in the programs (aligner.py, subtitles.py and scripts.py).
<br/>
<br/>
<b>Disclaimer:</b> This program can be run on any subtitle and script of a movie however movies where the script and subtitle differ greatly will offer a lower amount of correct matches. This has two main causes:
<li>If an entire scene isn't present in either the script or subtitles the program can't find correct matches. It constantly tries to align the scripts and subtitle by assuming a high match score means a match (and therefore a moment that the script and subtitles align). If it can't find correct matches for a long time the allignment of the two files can get out of sync and affect the accuracy.</li>
<li>If two items in the script and subtitles are reversed and the first in the subtitle offers a great match, the second line will not be found. This issue has a lesser effect, but is still noticible. This occurs because the program throws away al earlier looped over items if a good match occured. If it then needs to match with something that occured before that it won't be able to.</li>

<h2>Preparing to run the program</h2>
Prior to running the program, a few things have to be prepared. First, two files have to be prepared: a SubRip Subtitle file (.srt) containing the subtitles and a standard text file (.txt) containing the script. After this, it is useful to put the files in the same directory, as this will make it easier to call the program.
In order to run the program, you also need a few libraries installed. How to install these is described in the first step of how to run the program. If this doesn't work, you can type the following lines into your terminal:
<ul>
<li>pip3 install jellyfish</li>
<li>pip3 install nltk</li>
<li>pip3 install fuzzy-match</li>
<li>pip3 install fuzzywuzzy</li>
<li>pip3 install python-Levenshtein</li>
</ul>
You also need to install a part of nltk through Python, which you can do by using the interactive Python shell. Type 'python3' into your terminal. When the interactive shell has opened, type the following:
<ul>
  <li>import nltk</li>
  <li>nltk.download('averaged_perceptron_tagger')</li>
</ul>

<h2>How to run the program</h2>
<ol>
<li>Run the requirements file by typing 'pip3 install -r requirements.txt' into your terminal</li>
<li>Have a script file (.srt) and subtitle file (.txt) prepared in the main directory or move a script and corresponding subtitle file from the scripts_subtitles directory</li>
<li>Run the program in the terminal by typing: python3 user_interface.py -script [SCRIPT_FILE].txt -sub [SUBTITLE_FILE].srt</li>
<li>Replace the square brackets and text within the square brackets with the desired name of the script and subtitle</li>
<li>Follow the instructions provided by the program and put in the number of the desired output and press Enter</li>
<li>The file with the output can be found in a .csv file in the output folder</li>
</ol>

<h2>Notable results</h2>

To illustrate the performance of the program the first 100 matches of 4 movies were annotated by hand to check if the program found the right match.
The results were:

- Mission impossible: 32 correct, 68 incorrect
- The assignment: 63 correct, 37 incorrect
- Birthday girl: 31 correct, 69 incorrect
- Chinatown: 89 correct, 11 incorrect

Total: 215 correct, 185 incorrect
Accuracy based on results above: 53.75%

If you'd like to reproduce these results follow these steps:
<ol>
<li>Run the program with the steps provided in "How to run the program"</li>
<li>For the script and subtitle file use the files provided in the scripts_subtitles folder (the scripts and subtitles for the 4 movies above can be found here)</li>
<li>Pick option 4</li>
<li>The output can be found in a .csv file in the output folder</li>
<li>Compare as you wish! These raw results will be exactly the same as the ones we used for the annotation as well as the raw results below</li>
</ol>

Raw results: https://docs.google.com/spreadsheets/d/1vUpw906vSVXqh4vc2DsbTovbaMD9jZwdd3C7rRKSZC8/edit#gid=0

<h2>Other important information</h2>

It is important to note that that the program will not work on all scripts as the regex required to make this work is different for many scripts.
The regex implemented in this program allows for 2 different types of scripts which'll allow for handling the most common types of scripts to be handled.
We tested this on 16 different scripts out of which the programm will work on 12 of them. 

The 12 scripts the program works on:
1. Mission impossible
2. The assignment
3. Birthday girl
4. Chinatown
5. Mystery Men
6. Intolerable cruelty
7. Crash+(1996)
8. The Cooler
9. Confidence
10. Cold Mountain
11. Autumn in New York
12. 84 Charlie Mopic

The 4 scripts the program didn't work on:
1. 8mm
2. The Fifth Element
3. Carnivore
4. The Cable Guy

A summary of the differences between the scripts listed above can be found here: https://docs.google.com/document/d/1rBSFIQtOgTlFwx307YCkwJkS6_ezAEBf5Gh1HtDDLkk/edit?ts=60742cab

<h2>Research question</h2>

<b>Subtitles contain less nouns than their respective scripts</b>

To answer the hypothesis the scripts and subtitles for 10 different movies were POS-tagged. In total subtitles contained 495610 words and the subtitles contained 615655 words.
The subtitles contained 19147 nouns and the scripts contained 24968 nouns, which means that 3.86% of the subtitles were nouns and 4.06% of the scripts were nouns. It therefore seems that subtitles contain less nouns than the scripts.
The earlier described hypothesis can therefore be accepted.

Raw data: https://docs.google.com/spreadsheets/d/150YQtX-zg8Dtcm1p6E7EqZWD-_9SMR_BxGRO5A01eA4/edit?usp=sharing 