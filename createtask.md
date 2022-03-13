{% include navigation.html %}

# Description
The create task that we made was a country guessing game that allowed 5 tries, with each incorrect try being followed by a hint. If after the 5 attempts the user still hasn't gotten the answer, they lose. If the user gets it correct, they win and can restart the game with a new country.

### Features:
* text bar to input guesses
* a text box above the guess bar that provides hints
* guess button to submit the guess
* clear button to remove the text in the guess bar
* new button to start a new game with a new country
* 4 hints given:
1. The first letter of the country
2. The last letter of the country
3. The number of letters of the country name
4. The continent the country is in
* When correct, a popup will tell the user how many tries it took. When incorrect after 5 tries, a popup will tell the user the correct answer.

The user can see how good they are at guessing countries or just play this country guesser game when bored.
# Possible Other Ideas
We can show a picture taken inside of the country as an initial hint. We can also make something that allows the user to choose the type of hint they want to receive. Something else that we could make is a timer for each question so the user can see how fast they're doing questions. We can also make a leaderboard for each country with a database.

# Video
Samuel: https://drive.google.com/file/d/1ZMjqZrGbqcSZz2sArd5uVDlmk1HByVBJ/view?usp=sharing

# Final Code/Commits
[file](https://github.com/tonyhieu/csp-anthonys-harem/blob/main/create_task/templates/countryguesser.html)

Commits: [css, fixing buttons](https://github.com/tonyhieu/csp-anthonys-harem/commit/f70a00221964231ef5eafd11b6b45d4d8cec4eb3), [allow user to see how many guesses they took](https://github.com/tonyhieu/csp-anthonys-harem/commit/08e16d31c52b19c7b54f4670423ce9502ca8312f), [continent hint](https://github.com/tonyhieu/csp-anthonys-harem/commit/8f4b98b951a7b89e27096d79d268e60eb3d61baf)

# Questions
3a. 
i. The program is a country guesser game where the user inputs guesses to find what the random country is. This can be a fun game that users use to see how well they can guess countries or something users can play when bored.

ii. In my video, for the first country, different guesses were inputted into the guess box, and a new hint was provided for each incorrect guess. When the answer was correctly guessed, a popup told me that I had correctly guessed the country and that it took me 5 tries. For the second country, I guessed the incorrect answer 5 times and a popup told me that I had not gotten the right answer and told me the right answer was actually Brunei.

iii. The user's input in this program is the country they guess. The output, if the user is incorrect, is a newly generated hint. If the user is correct, the output is a popup telling the user that they were correct and that it took however many tries. If the user is incorrect 5 times, the output is that the user is incorrect and the actual answer. 

3b.
i. `var country = new Array(177);`

    `country[0] = "AFGHANISTAN";`
    `country[1] = "ALBANIA";`
    `country[2] = "ALGERIA";`
    `country[3] = "AMERICA";`
    `country[4] = "ANDORRA";`
    `country[5] = "ANGOLA";`
    `country[6] = "ARGENTINA";`
    `country[7] = "ARMENIA";`
    `country[8] = "AUStrALIA";`
    `country[9] = "AUStrIA";`
    `country[10] = "AZERBAIJAN";`
    `country[11] = "BAHAMAS";`
    `country[12] = "BAHRAIN";`
    `country[13] = "BANGLADESH";`
    `country[14] = "BARBADOS";`
    `country[15] = "BELARUS";`
    `country[16] = "BELGIUM";`
    `country[17] = "BELIZE";`
    `country[18] = "BENIN";`
    `country[19] = "BHUTAN";`
    `country[20] = "BOLIVIA";`
    `country[21] = "BOSNIA HERZEGOVINA";`
    `country[22] = "BOTSWANA";`
    `country[23] = "BRAZIL";`
    `country[24] = "BRUNEI";`
    `country[25] = "BULGARIA";`
    `country[26] = "BURKINA";`
    `country[27] = "BURUNDI";`
    `country[28] = "CAMBODIA";`
    `country[29] = "CAMEROON";`
    `country[30] = "CANADA";`
    `country[31] = "CAPE VERDE ISLANDS";`
    `country[32] = "CHAD";`
    `country[33] = "CHILE";`
    `country[34] = "CHINA";`
    `country[35] = "COLOMBIA";`
    `country[36] = "COMOROS";`
    `country[37] = "CONGO";`
    `country[38] = "COSTA RICA";`
    `country[39] = "CROATIA";`
    `country[40] = "CUBA";`
    `country[41] = "CYPRUS";`
    `country[42] = "CZECH REPUBLIC";`
    `country[43] = "DENMARK";`
    `country[44] = "DJIBOUTI";`
    `country[45] = "DOMINICAN REPUBLIC";`
    `country[46] = "ECUADOR";`
    `country[47] = "EGYPT";`
    `country[48] = "EL SALVADOR";`
    `country[49] = "ERItrEA";`
    `country[50] = "ESTONIA";`
    `country[51] = "ETHIOPIA";`
    `country[52] = "FIJI";`
    `country[53] = "FINLAND";`
    `country[54] = "FRANCE";`
    `country[55] = "GABON";`
    `country[56] = "GAMBIA";`
    `country[57] = "GEORGIA";`
    `country[58] = "GERMANY";`
    `country[59] = "GHANA";`
    `country[60] = "GREECE";`
    `country[61] ="GRENADA";`
    `country[62] = "GUATEMALA";`
    `country[63] = "GUINEA";`
    `country[64] = "HAITI";`
    `country[65] = "HOLLAND";`
    `country[66] = "HONDURAS";`
    `country[67] = "HONG KONG";`
    `country[68] = "HUNGARY";`
    `country[69] = "ICELAND";`
    `country[70] = "INDIA";`
    `country[71] = "INDONESIA";`
    `country[72] = "IRAN";`
    `country[73] = "IRAQ";`
    `country[74] = "ISRAEL";`
    `country[75] = "ITALY";`
    `country[76] = "JAMAICA";`
    `country[77] = "JAPAN";`
    `country[78] = "JORDAN";`
    `country[79] = "KAZAKHSTAN";`
    `country[80] = "KENYA";`
    `country[81] = "KYRGYZSTAN";`
    `country[82] = "KIRIBATI";`
    `country[83] = "KOREA";`
    `country[84] = "KUWAIT";`
    `country[85] = "LAOS";`
    `country[86] = "LATVIA";`
    `country[87] = "LEBANON";`
    `country[88] = "LESOTHO";`
    `country[89] = "LIBERIA";`
    `country[90] = "LIBYA";`
    `country[91] = "LIECHTENSTEIN";`
    `country[92] = "LITHUANIA";`
    `country[93] = "LUXEMBOURG";`
    `country[94] = "MADAGASCAR";`
    `country[95] = "MALAWI";`
    `country[96] = "MALAYSIA";`
    `country[97] = "MALDIVES";`
    `country[98] = "MALI";`
    `country[99] = "MALTA";`
    `country[100] = "MAURITANIA";`
    `country[101] = "MAURITIUS";`
    `country[102] = "MEXICO";`
    `country[103] = "MOLDOVA";`
    `country[104] = "MONACO";`
    `country[105] = "MONGOLIA";`
    `country[106] = "MONTENEGRO";`
    `country[107] = "MOROCCO";`
    `country[108] = "MOZAMBIQUE";`
    `country[109] = "MYANMAR";`
    `country[110] = "NAMIBIA";`
    `country[111] = "NAURU";`
    `country[112] = "NEPAL";`
    `country[113] = "NETHERLANDS";`
    `country[114] = "NEW ZEALAND";`
    `country[115] = "NICARAGUA";`
    `country[116] = "NIGERIA";`
    `country[117] = "NORWAY";`
    `country[118] = "OMAN";`
    `country[119] = "PAKISTAN";`
    `country[120] = "PANAMA";`
    `country[121] = "PAPUA NEW GUINEA";`
    `country[122] = "PARAGUAY";`
    `country[123] = "PERU";`
    `country[124] = "PHILIPPINES";`
    `country[125] = "POLAND";`
    `country[126] = "PORTUGAL";`
    `country[127] = "QATAR";`
    `country[128] = "ROMANIA";`
    `country[129] = "RUSSIA";`
    `country[130] = "RWANDA";`
    `country[131] = "SAN MARINO";`
    `country[132] = "SAUDI ARABIA";`
    `country[133] = "SENEGAL";`
    `country[134] = "SEYCHELLES";`
    `country[135] = "SIERRA LEONE";`
    `country[136] = "SINGAPORE";`
    `country[137] = "SLOVAKIA";`
    `country[138] = "SLOVENIA";`
    `country[139] = "SOLOMON ISLANDS";`
    `country[140] = "SOMALIA";`
    `country[141] = "SOUTH AFRICA";`
    `country[142] = "SPAIN";`
    `country[143] = "SRI LANKA";`
    `country[144] = "SUDAN";`
    `country[145] = "SURINAME";`
    `country[146] = "SWAZILAND";`
    `country[147] = "SWEDEN";`
    `country[148] = "SWITZERLAND";`
    `country[149] = "SYRIA";`
    `country[150] = "TAIWAN";`
    `country[151] = "TAJIKISTAN";`
    `country[152] = "TANZANIA";`
    `country[153] = "THAILAND";`
    `country[154] = "TOGO";`
    `country[155] = "TONGA";`
    `country[156] = "TRINIDAD AND TOBAGO";`
    `country[157] = "TUNISIA";`
    `country[158] = "TURKEY";`
    `country[159] = "TURKMENISTAN";`
    `country[160] = "TUVALU";`
    `country[161] = "UGANDA";`
    `country[162] = "UKRAINE";`
    `country[163] = "UNITED ARAB EMIRATES";`
    `country[164] = "URUGUAY";`
    `country[165] = "UZBEKISTAN";`
    `country[166] = "VANUATU";`
    `country[167] = "VATICAN CITY";`
    `country[168] = "VENEZUELA";`
    `country[169] = "VIETNAM";`
    `country[170] = "WEST INDIES";`
    `country[171] = "WESTERN SAMOA";`
    `country[172] = "YEMEN";`
    `country[173] = "YUGOSLAVIA";`
    `country[174] = "ZAIRE";`
    `country[175] = "ZAMBIA";`
    `country[176] = "ZIMBABWE";`
ii.  `function guessit()`
    `{`
        `var guess = document.form1.guess1.value;`
        `tries++;`
        `window.status = "tries : " + tries + " ";`
        `switch(tries)`
        `{`
            `case 1:`
                `document.form1.hint.value = "First Hint : The country name starts with " + temp.charAt(0);`
                `break;`

            `case 2:`
                `document.form1.hint.value = "Second Hint : The country name ends with " + temp.charAt(temp.length - 1);`
                `break;`

            `case 3:`
                `document.form1.hint.value = "Third Hint : The country name has " + temp.length + " characters";`
                `break;`

            `case 4:`
                `document.form1.hint.value = "Last Hint : The country is in " + temp2;`
                `break;`

            `default:`
                `document.form1.hint.value = "No hints are available";`
        `}`
        `if(guess.toUpperCase() == temp)`
        `{`
            `if(window.confirm("Absolutely Right! Yes the country was " + temp + ". This took " + tries + " tries.\nDo you want to play again?"))`
                `window.location.reload();`
        `}`
        `else`
        `{`
            `if(tries == 5)`
            `{`
                `if(window.confirm("Sorry ! You've used up your 5 tries. The country was  " + temp + "\nDo you want to play again?"))`
                `{`
                    `window.location.reload();`
                    `document.form1.hint.value = "Enter your guess below and click on Guess!";`
                `}`
            `}`
        `}`
    `}`

iii) The name of this list is country.

iv) The data in the list is the different names of the countries in the world, which are represented by country[number].

v) The program requires this list for the names of the countries that are being guessed by the user. Without this, there wouldn't be any countries in the game and the user would be guessing for nothing. The country[number] is used to represent the country names, which allows easy randomizing of countries and to select a country for the hints.

3c.
i)    ` var sr = Math.floor(Math.random() * 177);`
    `var temp = country[sr];`
    `var temp2 = continent[sr];`
    `var tries = 0;`

    `function guessit()`
    `{`
        `var guess = document.form1.guess1.value;`
        `tries++;`
        `window.status = "tries : " + tries + " ";`
        `switch(tries)`
        `{`
            `case 1:`
                `document.form1.hint.value = "First Hint : The country name starts with " + temp.charAt(0);`
                `break;`

            `case 2:`
                `document.form1.hint.value = "Second Hint : The country name ends with " + temp.charAt(temp.length - 1);`
                `break;`

            `case 3:`
                `document.form1.hint.value = "Third Hint : The country name has " + temp.length + " characters";`
                `break;`

            `case 4:`
                `document.form1.hint.value = "Last Hint : The country is in " + temp2;`
                `break;`

            `default:`
                `document.form1.hint.value = "No hints are available";`
        `}`
        `if(guess.toUpperCase() == temp)`
        `{`
            `if(window.confirm("Absolutely Right! Yes the country was " + temp + ". This took " + tries + " tries.\nDo you want to play again?"))`
                `window.location.reload();`
        `}`
        `else`
        `{`
            `if(tries == 5)`
            `{`
                `if(window.confirm("Sorry ! You've used up your 5 tries. The country was  " + temp + "\nDo you want to play again?"))`
                `{`
                    `window.location.reload();`
                    `document.form1.hint.value = "Enter your guess below and click on Guess!";`
                `}`
            `}`
        `}`
    `}`

ii)             ` <input type=button  class=td2 value=Guess! onClick=guessit()`
                   `title="Click here to get a hint or check your guess.">`

iii) This procedure from when the user clicks the new game button or goes to our page, a country is taken and stored as temp, which will be used as the correct answer. Then the user will have 5 tries to try and guess this random country, with a hint following each incorrect guess, which can be seen with each "case". If the answer is correct, a popup will show the user that they were correct and tell them how many guesses it took. If after 5 attempts, the answer is still not gotten by the user, then a popup will tell the user that they were incorrect and tell them the real answer.

iv)  This procedure will randomly take a country from our array and store it as temp. The user will then have to guess what temp is within 5 guesses. After each guess, a hint is provided. The first hint is one that tells the user the first letter of the country, the second hint tells the user the last letter of the country, the third hint tells the user the number of letters in the country name, and the last hint tells the user what continent the country is in. If the answer is guessed correctly, then a popup shows up that tells the user how many attempts it took. When still incorrect after 5 tries, a popup tells the user that they were incorrect and will also tell them the correct answer. The popups for both scenarios will allow the user to restart the game. 

3d.

i) 
First Call: Calls to the procedure new game so that the user can start a new game if they want, which will get a new country as the correct country, saving it as temp and start the game all over again. This can happen when the user clicks the new game button or when the user first loads into the page.

Second Call: When the user enters a guess, the procedure guessit is called, which will either give a hint for an incorrect answer, a popup telling the user they were correct for a correct answer, or a popup telling the user that they were incorrect for 5 incorrect guesses.
ii)
First Call: If the user clicked the new game button on the page or the new game button in the popup, which will decide to start a new game or not.

Second Call: If the guess is correct, incorrect, and the number of attempts the user has taken, will determine if a hint is given, or the type of popup shown to the user.
iii)
First Call: If the user clicked ok for new game in the popup, the page will reload and a new country will be saved as temp for the user to guess. If the clicks cancel in the popup, no page reload will happen and no new country will be saved as temp. The user will then go back to the page.

Second Call: If the user inputs the correct guess, a popup indicating that the user is correct will show, telling them that they were correct and telling them the number of attempts it took them. It will also give the user an option to play again. If the guess is incorrect and hasn't reached 5 incorrect guesses yet, then the user will be given another hint. If the number of attempts has reached 5 and the user still hasn't correctly guessed the country, a popup will tell the user that they were incorrect, while telling them the correct answer and that they can play again.
