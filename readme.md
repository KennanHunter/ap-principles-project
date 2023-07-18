# My ap computer science principles project

Final score 4/5, honestly kinda upset I didn't get a five, but hey whatever.

Not sure exactly what I got on the exam, but practice exams put me near perfect.

## Written responses

### Describes the overall purpose of the program.

Passwords are inherently insecure. The greatest way to mitigate their security risk is by following the best practice of using computer programs to automatically generate your password for you. This program handles the generation of secure passwords, according to the parameters determined by the user.

### Describes what functionality of the program is demonstrated in the video.

The video details the process of a user specifying different lengths and character types that the password will be generated from. The user also demonstrates the failure modes of the program, intentionally entering invalid inputs to view how it handles the messiness of the real world.

### Describes the input and output of the program demonstrated in the video.

The user controls two inputs, the characters it's generated from and the length of the password. The first input prompts the user with "Your Selection: ", where the user can enter any combination of "letters", "numbers", and "symbols". We take much care in sanitizing user input, we strip any insignificant whitespace, match everything case-insensitive, and alert the user when unknown options are entered. We also validate that the length is a valid integer, meaning decimals and text stop the program.

### Identifies the name of the list being used in this response.

Our list is named password, representing its use as a list of characters that the password is formed from.

### Describes what the data contained in the list represent in your program.

The data represent the characters in the password. These characters are appended to the end of the list from a random set that is determined by the user's inputs.

### Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list.

The password list manages complexity by allowing us to dynamically add characters. This dynamic nature gives us a lot of control, we can determine exactly what characters we want to be factored into our random calculation, as well as exactly how long we want our password to be. If we didn't use a list, we would have to manually repeat logic to add characters to our password.

### Describes in general what the identified procedure does and how it contributes to the overall functionality of the program.

The generate_password function handles returning a string with a length given by a parameter. Each character in the said password is determined by a list that is passed into the function. This contributes to the overall functionality by generating the data away from where we prompt the user, abstracting out the generation process.

### Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it.

My algorithm is pretty simple. We create an empty list at the very beginning. We then create a loop, iterating the number of times that the user asked for in the beginning. On each iteration, we create a list of possible characters. This possible character list operates by starting empty, then being populated with the values found in other constant lists. We choose which constant lists to add based on the user's selection at the beginning. We then choose a random character from this list and add it to the password list. Finally, we take the password list and join the characters together.

### Describes two calls to the procedure identified in written response 3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute.

#### First call

The first call of our program the user inputs "letters numbers" for the prompt "Your Selection". The program then splits this into a list, while 
