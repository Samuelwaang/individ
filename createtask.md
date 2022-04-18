{% include navigation.html %}

# Create Task Write Up 

### [Code File](https://github.com/Samuelwaang/individ/blob/main/createTask.html)
### [Video](https://drive.google.com/file/d/1tiF2pJ7x9IrBg6WgglHJp4vaWA5ZlWTw/view?usp=sharing)

## 3a. 
i. The program is a quiz/game where a random fruit is given to the user to answer questions about.

ii. In the video a start buton is pressed, causing the name of the fruit, picture of the fruit, and a question box to appear. The questions were answered in the question box, with some being incorrect and others being correct. The questions that had incorrect answers had their text be changed to red, while the questions that had correct answers had their text be changed to green. After the submit button was pressed, the answers for the incorrectly answered questions and the score were shown at the bottom. Then, the refresh button was clicked to start the game again and a new fruit was shown.

iii. The input of the program are the answers and the outputs are the score, indication of incorrect answers, and correct answers.

## 3b.
i. 
```
var answerArray = Array.from(Array(4), () => new Array(4));
                answerArray[0][0] = 'yellow';
                answerArray[0][1] = 'yellow';
                answerArray[0][2] = 'red';
                answerArray[0][3] = 'red';
                answerArray[1][0] = 'yes';
                answerArray[1][1] = 'no';
                answerArray[1][2] = 'yes';
                answerArray[1][3] = 'yes';
                answerArray[2][0] = 'year';
                answerArray[2][1] = 'year';
                answerArray[2][2] = 'winter';
                answerArray[2][3] = 'summer';
                answerArray[3][0] = 'sour';
                answerArray[3][1] = 'sweet';
                answerArray[3][2] = 'tart';
                answerArray[3][3] = 'sweet';
```
ii. 
```
for (let i = 0; i < 4; i++)
                    {
                        if ( answer[i] == answerArray[i][cf] && (score < 4)  )
                        {
                            score++;
                            isAnswerCorrect[i] = 1;
                        }
                        if (isAnswerCorrect[i] === 1)
                        {
                            document.getElementById(idArray[i]).style.color = "#08ab10";
                        }
                        else if (isAnswerCorrect[i] === 0)
                        {
                            document.getElementById(idArray[i]).style.color = "#e5150f";
                        }
                        document.getElementById("fScore").innerHTML = "Score: "+ score + "/4";
                    }
```
iii. The list is named answerArray.

iv. The data in the list represents the correct answers for all the questions. Each answer corresponds to a certain question and fruit.

v. This list is required to check if the inputted answers by the user are correct or incorrect, which is the most important part of this program. A list like this allows randomization of the fruit type and allows it, based on the question, to correspond to the answer. If this wasn't done, then a bunch of if else statements would've had to been used for each fruit and question variation. So, for example, if a fruit was chosen such as "banana", then for banana and question 1, with an if else statement, it would be checked if the inputted answer is the same as the answer for banana and question 1. If not, it would be marked as incorrect. This would then have to be done with every fruit and question combination.

## 3c
i.
```
function collect(isAnswerCorrect, score) {
                    answer = new Array(4);
                    answer[0] = document.getElementById("col").value;
                    answer[1] = document.getElementById("fru").value;
                    answer[2] = document.getElementById("sea").value;
                    answer[3] = document.getElementById("tas").value;

                    isAnswerCorrect = new Array(4).fill(0);
                    idArray = new Array(4);
                    idArray[0]= 'colchange1';
                    idArray[1]= 'colchange2';
                    idArray[2]= 'colchange3';
                    idArray[3]= 'colchange4';
                    score = 0;

                    for (let i = 0; i < 4; i++)
                    {
                        if ( answer[i] == answerArray[i][cf] && (score < 4)  )
                        {
                            score++;
                            isAnswerCorrect[i] = 1;
                        }
                        if (isAnswerCorrect[i] === 1)
                        {
                            document.getElementById(idArray[i]).style.color = "#08ab10";
                        }
                        else if (isAnswerCorrect[i] === 0)
                        {
                            document.getElementById(idArray[i]).style.color = "#e5150f";
                        }
                        document.getElementById("fScore").innerHTML = "Score: "+ score + "/4";
                    }
                    let rightAnswer = ' ';
                    for (let i = 0; i < 4; i++)
                    {
                        if (isAnswerCorrect[i] === 0)
                        {
                            questionNum = i + 1;
                            rightAnswer =  rightAnswer.concat("Question " + questionNum + ": " + answerArray[i][cf] + ",  ");
                        }
                    }
                    document.getElementById("incAnswer").innerHTML = "The correct answers are: \n" + rightAnswer;
                }
```
ii.
```
<input type="submit" value="submit" class="submit" onclick="collect()">
```
iii. This function "collect" is determining the output of the quiz based on the inputted answers of the user. This changes incorrectly answered questions to red text and correctly answered question to green text. This also adds up the score of the user. It also displays the correct answers for questions answered incorrectly. So, this is the part that shows the user if they were correct or incorrect in doing the quiz and how well they did on it.

iv. Another 3 arrays are made. Two (answer and isAnswerCorrect) are used to compare the user inputted answer and actual correct answer to check answers and calculate the score of the user. This is done with if else statements in a for loop. The 4 loop iterates 4 times, each time increasing the question number by 1, so it can check each question's answer. Each time the user is correct, one score is added and that question is changed to be set to a 1 instead of 0 through an array. Then, an if else statement is used (depending on if that question is set 1 or 0) to indicate if a question was answered correctly or incorrectly through a color change. The score will also then be displayed. Then, through another for loop that checks each question, an if statement is used to check if the question is still to 0. If it is, then the correct answer for those specific questions will be displayed.

## 3d.
i. In the first call, the answer would be marked as 1 if correct.
In the second call, the answer would stay marked as 0 for incorrect.

ii. In the first call, the user inputted answer will be checked if it is equal to the actual answer stored in the list for that question. If it is, then it won't test if the answer isn't equal to the actual answer stored in the list for that question.
In the second call, it tests if the answer isn't equal to the actual answer stored in the list for that question. 

iii. The first call with its question marked as 1 indicating correctness causes the text for a correct answer to be changed to green. It also indicates a right answer, increasing the score of the user by 1. The second call wit its questions remaining marked as 0 indicating incorrectness causes the text for an incorrect answer to be changed to red. This will not change the score at all.
