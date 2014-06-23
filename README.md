dcogs-voter
===========

It's a simple application for having awesome vote of top records of all time. It does the counting and uses discogs for source.

THIS IS A PROTOTYPE HACKED IN TWO HOURS

usage
==========

Collect data from discogs as urls and save it in file (new line separated, refer to votes.data in source tree). Run prototype-vote-counter.py with votesfile as an argument.

<pre>
you@computer:~/vinylcount$ python prototype-vote-counter.py 
Hello, I'm DISCOGS based prototype of best records ever vote counter
I lack of unit testing and proper structure. I don't do any caching.
I'm made of pythons


USAGE:
python  prototype-vote-counter.py  votesfile
</pre>

sample run
===========
<pre>
you@computer:~/vinylcount$ python prototype-vote-counter.py votes.data 
Hello, I'm DISCOGS based prototype of best records ever vote counter
I lack of unit testing and proper structure. I don't do any caching.
I'm made of pythons

Reading votes from votes.data
Here we go

Handling:	http://www.discogs.com/Black-Sabbath-Black-Sabbath-Vol-4/release/4011127
 API-URL:	http://api.discogs.com/release/4011127
 NORMALIZED:	http://api.discogs.com/masters/4894

Handling:	http://www.discogs.com/Black-Sabbath-Born-Again/master/6100
 API-URL:	http://api.discogs.com/master/6100
 NORMALIZED:	http://api.discogs.com/masters/6100

Handling:	http://www.discogs.com/Black-Sabbath-Black-Sabbath-Vol-4/release/4493832
 API-URL:	http://api.discogs.com/release/4493832
 NORMALIZED:	http://api.discogs.com/masters/4894

Handling:	http://www.discogs.com/Black-Sabbath-Reunion/release/1437822
 API-URL:	http://api.discogs.com/release/1437822
 NORMALIZED:	http://api.discogs.com/masters/37622

Handling:	http://www.discogs.com/Infest-Infest/release/2193903
 API-URL:	http://api.discogs.com/release/2193903
 NORMALIZED:	http://api.discogs.com/masters/185923

Handling:	http://www.discogs.com/Pirkka-Pekka-Petelius-Muistan-Sua-Elaine/release/2866532
 API-URL:	http://api.discogs.com/release/2866532
 NORMALIZED:	http://api.discogs.com/release/2866532

Handling:	http://www.discogs.com/Pirkka-Pekka-Petelius-Pimpparauta/release/2183069
 API-URL:	http://api.discogs.com/release/2183069
 NORMALIZED:	http://api.discogs.com/release/2183069

Handling:	http://www.discogs.com/Pirkka-Pekka-Petelius-Muistan-Sua-Elaine/release/2866532
 API-URL:	http://api.discogs.com/release/2866532
 NORMALIZED:	http://api.discogs.com/release/2866532

Handling:	http://www.discogs.com/Pirkka-Pekka-Petelius-Muistan-Sua-Elaine/release/2866532
 API-URL:	http://api.discogs.com/release/2866532
 NORMALIZED:	http://api.discogs.com/release/2866532

Handling:	http://www.discogs.com/Rorschach-2-Neanderthal-Rorschach-Neanderthal/release/1366793
 API-URL:	http://api.discogs.com/release/1366793
 NORMALIZED:	http://api.discogs.com/release/1366793

Handling:	http://www.discogs.com/Jope-Ruonansuu-Piinapenkki/release/1849843
 API-URL:	http://api.discogs.com/release/1849843
 NORMALIZED:	http://api.discogs.com/release/1849843

Handling:	http://www.discogs.com/Jope-Ruonansuu-Presidentiksi/master/398825
 API-URL:	http://api.discogs.com/master/398825
 NORMALIZED:	http://api.discogs.com/masters/398825

Handling:	http://www.discogs.com/Jope-Ruonansuu-Presidentiksi/release/1849744
 API-URL:	http://api.discogs.com/release/1849744
 NORMALIZED:	http://api.discogs.com/masters/398825

Handling:	http://www.discogs.com/Jope-Ruonansuu-Presidentiksi/release/3327908
 API-URL:	http://api.discogs.com/release/3327908
 NORMALIZED:	http://api.discogs.com/masters/398825

Handling:	http://www.discogs.com/Jope-Ruonansuu-Presidentiksi/release/3327908
 API-URL:	http://api.discogs.com/release/3327908
 NORMALIZED:	http://api.discogs.com/masters/398825

Handling:	http://www.discogs.com/Screamin-Jay-Hawkins-Lawdy-Miss-Clawdy/release/4513687
 API-URL:	http://api.discogs.com/release/4513687
 NORMALIZED:	http://api.discogs.com/release/4513687

Handling:	http://www.discogs.com/Screaming-Jay-Hawkins-I-Put-A-Spell-On-You/release/3822005
 API-URL:	http://api.discogs.com/release/3822005
 NORMALIZED:	http://api.discogs.com/masters/465138

Handling:	http://www.discogs.com/Rezillos-Cant-Stand-The-Rezillos/release/468420
 API-URL:	http://api.discogs.com/release/468420
 NORMALIZED:	http://api.discogs.com/masters/174547

Handling:	http://www.discogs.com/Rezillos-Cant-Stand-The-Rezillos/release/5127809
 API-URL:	http://api.discogs.com/release/5127809
 NORMALIZED:	http://api.discogs.com/masters/174547

Handling:	http://www.discogs.com/Rezillos-Cant-Stand-The-Rezillos/release/4058638
 API-URL:	http://api.discogs.com/release/4058638
 NORMALIZED:	http://api.discogs.com/masters/174547

Handling:	http://www.discogs.com/Rezillos-Cant-Stand-The-Rezillos/release/3734972
 API-URL:	http://api.discogs.com/release/3734972
 NORMALIZED:	http://api.discogs.com/masters/174547

http://api.discogs.com/release/2183069 	 VOTES:  1 	Pirkka-Pekka Petelius : Pimpparauta
http://api.discogs.com/masters/185923 	 VOTES:  1 	Infest : Infest
http://api.discogs.com/masters/4894 	 VOTES:  2 	Black Sabbath : Black Sabbath Vol 4
http://api.discogs.com/masters/398825 	 VOTES:  4 	Jope Ruonansuu : Presidentiksi
http://api.discogs.com/masters/6100 	 VOTES:  1 	Black Sabbath : Born Again
http://api.discogs.com/masters/465138 	 VOTES:  1 	Screamin' Jay Hawkins : I Put A Spell On You
http://api.discogs.com/release/2866532 	 VOTES:  3 	Pirkka-Pekka Petelius : Muistan Sua Elaine
http://api.discogs.com/release/1849843 	 VOTES:  1 	Jope Ruonansuu : Piinapenkki
http://api.discogs.com/masters/37622 	 VOTES:  1 	Black Sabbath : Reunion
http://api.discogs.com/release/4513687 	 VOTES:  1 	Screamin' Jay Hawkins : Lawdy Miss Clawdy
http://api.discogs.com/masters/174547 	 VOTES:  4 	Rezillos : Can't Stand The Rezillos
http://api.discogs.com/release/1366793 	 VOTES:  1 	Rorschach (2) : Rorschach / Neanderthal
</pre>
