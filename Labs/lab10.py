#Lab10 Nazli Zamanian Gustavsson Regex


#10.2 Introductory experiments
import re
txt = "Hanoror bought 5 portions of orange soil for 13.50 EUR."
re.findall("or", txt)

#10.2.1 Dot means joker
#dot in regex matches all characters. except linebreak.

txt = "Hanoror bought 5 portions of orange soil for 13.50 EUR."
re.findall(".", txt)


txt = "Hanoror bought 5 portions of orange soil for 13.50 EUR."
re.findall("or.", txt) #searches for all strings that start with or and continue charater.
# findall find only non-overlapping strings.

re.findall("..\.",txt) #gives us a real . 

#10.2.3 Other special characters
re.findall(r"\w",txt) #w as in word, matches all words. 
re.findall(r"\W",txt)#!= as w, w as not word. 

re.findall(r"\d",txt) #digit
re.findall(r"\D",txt)# opposite gives word. 

re.findall(r"\s",txt) #spaces 



#Task 1 // Task 2??
def is_valid_email(email):
    
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use re.match() to check if the email matches the pattern
    match = re.match(email_pattern, email)
    
    if match:
        print(f"The email address '{email}' is valid.")

is_valid_email('r.nohre@jth.hj.se')
is_valid_email('bjox@se') #not valid
is_valid_email('adam@example.com')
is_valid_email('jox@jox@jox.com."') #not valid

#Task 3 Simpsons Tv tabla 
import re

html_code = """
<tr class="svtTablaPast svtOpacity-60 svtXDisplayNone tv6" >
    <td class="svtTablaTime">
        10.30
    </td>
    <td class="svtJsTablaShowInfo">
        <h4 class="svtLink-hover svtTablaHeading">
            Simpsons
        </h4>
        <div class="svtJsStopPropagation">
            <div class="svtTablaTitleInfo svtHide-Js">
                <div class="svtTablaContent-Description">
                    <p class="svtXMargin-Bottom-10px">
                        Amerikansk animerad komediserie från 2002-03. Säsong 14. Del 14 av 23. Familjen bestämmer sig för att flytta när de upptäcker att deras hus ligger rätt under den nya flygbanan. Simpsons bor i Springfield. Mamma Marge är den som håller familjen samman, bakar kakor och fixar sitt höga, blå hår två gånger per dag. Pappa Homer gillar att dricka öl och titta på tv. Sonen Bart tycker om att åka skateboard och att reta sin syster Lisa. Lisa är väluppfostrad, intelligent och en moralens väktare.
                    </p>
                </div>
            </div>
        </div>
    </td>
</tr>
<tr class="svtTablaPast svtOpacity-60 svtXDisplayNone tv6" >
    <td class="svtTablaTime">
        11.00
    </td>
    <td class="svtJsTablaShowInfo">
        <h4 class="svtLink-hover svtTablaHeading">
            Simpsons
        </h4>
        <div class="svtJsStopPropagation">
            <div class="svtTablaTitleInfo svtHide-Js">
                <div class="svtTablaContent-Description">
                    <p class="svtXMargin-Bottom-10px">
                        Amerikansk animerad komediserie från 2002-03. Säsong 14. Del 15 av 23. Homer blir besviken när Marge motstår hans manliga charm på alla hjärtans dag. Simpsons bor i Springfield. Mamma Marge är den som håller familjen samman, bakar kakor och fixar sitt höga, blå hår två gånger per dag. Pappa Homer gillar att dricka öl och titta på tv. Sonen Bart tycker om att åka skateboard och att reta sin syster Lisa. Lisa är väluppfostrad, intelligent och en moralens väktare.
                    </p>
                </div>
            </div>
        </div>
    </td>
</tr>
<td class="svtTablaTime">14.30 </td>
    <td class="svtJsTablaShowInfo">
    <h4 class="svtLink-hover svtTablaHeading">
    Simpsons
    </h4>
<div class="svtJsStopPropagation">
<div class="svtTablaTitleInfo svtHide-Js">
<div class="svtTablaContent-Description">
<p class="svtXMargin-Bottom-10px">
Amerikansk animerad komediserie från 2007. Säsong 19. Del 8 av 20. Bob återvänder och sätter en djävulsk plan i verket för att försöka döda Bart. Regi: Neil Affleck och Bob Anderson. Simpsons bor i Springfield. Mamma Marge är den som håller familjen samman, bakar kakor och fixar sitt höga, blå hår två gånger per dag. Pappa Homer gillar att dricka öl och titta på tv. Sonen Bart tycker om att åka skateboard och att reta sin syster Lisa. Lisa är väluppfostrad, intelligent och en moralens väktare.
</p>
</div>
</div>
</div>
</td>
</tr>
<tr class="svtTablaPast svtOpacity-60 tv6" >
<td class="svtTablaTime">
15.00
</td>
<td class="svtJsTablaShowInfo">
<h4 class="svtLink-hover svtTablaHeading">
Simpsons
</h4>
<div class="svtJsStopPropagation">
<div class="svtTablaTitleInfo svtHide-Js">
<div class="svtTablaContent-Description">
<p class="svtXMargin-Bottom-10px">
Amerikansk animerad komediserie från 2007. Säsong 19. Del 9 av 20. En morgon när Homer vaknar befinner han sig utomhus och är täckt av snö. När han kommer hem är hela familjen borta. Regi: Neil Affleck och Bob Anderson. Simpsons bor i Springfield. Mamma Marge är den som håller familjen samman, bakar kakor och fixar sitt höga, blå hår två gånger per dag. Pappa Homer gillar att dricka öl och titta på tv. Sonen Bart tycker om att åka skateboard och att reta sin syster Lisa. Lisa är väluppfostrad, intelligent och en moralens väktare.
</p>
</div>
</div>
</div>
</td>
</tr>
"""

regex_pattern = r'<td class="svtTablaTime">\s*(.*?)\s*<\/td>\s*(?:<td.*?>\s*<h4.*?>\s*.*?\s*<\/h4>\s*<div.*?>\s*<div.*?>\s*<div.*?>\s*<p.*?>\s*(.*?)\s*<\/p>\s*<\/div>\s*<\/div>\s*<\/div>\s*<\/td>)?'


matches = re.finditer(regex_pattern, html_code, re.DOTALL) #iterator to match our regex with the html code. 

for match in matches:
    time = match.group(1)
    handling = match.group(2)

    # Extract season and episode information
    season_match = re.search(r'Säsong (\d+)', handling)
    episode_match = re.search(r'Del (\d+)', handling)

    season = season_match.group(1) if season_match else "N/A"
    episode = episode_match.group(1) if episode_match else "N/A"

    print("Time:", time.strip())
    print(f"Säsong: {season}")
    print(f"Avsnitt: {episode}")
    print("Handling:", handling.strip())
    print("\n---\n")