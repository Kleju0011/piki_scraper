<h1>Pikio Article Extractor</h2>
<h3>Needments</h3>
<ul>
    <li>Ubuntu or Windows OS</li>
    <li>Python 3</li>
    <li>Pip</li>
    <li>Virtualenv or other similar tool</li>
</ul>
<h3>Setup</h3>
<p>You can find all needed software within 'requirements.txt' file, You can use it to create your own isolated  environment via Virtualenv or other tool </p>
<h3>CLI Manual</h3>
<p>You can use article scraper via command:<br
><i>python main.py -url 'url_of_piki_article'</url_of_piki_article> </i>
 <br> The url argument is obligatory!
 <br>You can use also as well:
 <ul>
    <li>-j: will return output in json format.</li>
    <li>-f: will save output to txt or to json file if you choose a proper option.</li>
    <li>-t: will return the title of article with output.</li>
    <li>-d: will return the date of the article with output.</li>
    <li>-p: will download picture from the article.</li>
 </ul>
 </p>