# programming-for-the-web

This is the Year 1 module Programming for the Web coursework.

Task 1
Created a diabetes.py module.
The provided Python module, "diabetes.py," defines a function called generate_summary_for_web. This function takes a diabetes-related CSV file, an HTML title, and an HTML filename as input parameters. 
It produces an HTML file with a table displaying the count of attribute values (excluding 'Age' and 'Gender') for both Positive and Negative classes. 
Optionally, it includes a bar chart illustrating the distribution of Positive and Negative cases based on Gender. The module utilizes pandas for data manipulation and matplotlib for creating visualizations. 
The generated HTML file serves as a summary report for diabetes-related data analysis.


Task 2
Modified the JavaScript functions in the lights_off.html file.
The provided HTML file, "lights_off.html," contains JavaScript functions to create a grid of buttons. Upon opening the file in a browser, the central button at position (2,2) is toggled. Three JavaScript functions are implemented:
toggle(i, j): This function switches the state of the button at position (i, j) between the white "O" state (on) and the black "X" state (off).
press(i, j): This function toggles the state of the button pressed at position (i, j) and the states of the buttons above, below, left, and right of the pressed button. It also calls the checkAllOff() function to verify if all buttons are in the off state.
checkAllOff(): This function tests whether all buttons are in the off state (black). If they are, it displays a congratulatory message ("Congratulations! All lights out!") at the HTML element with id="end." This function also removes the message if, following a subsequent press, one or more buttons return to the "on" state.
resetGrid(): This function resets the grid to its initial state and removes the congratulatory message. It is called when the Reset button is clicked.
The puzzle can be solved by clicking the buttons as indicated in the grid. The congratulatory message is displayed when all buttons are turned off. Clicking the Reset button resets the grid and removes the message.





