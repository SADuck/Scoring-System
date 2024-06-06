import PySimpleGUI as sg

# Initialize variables
round_number = 1
total1 = 0
total2 = 0
table_data = []


# Define the layout
layout = [
    [sg.Text("Player 1", font=("calibri", 15)), sg.Input(key='player1', size=(15,1)), sg.Text("Points:"), sg.Text("", key='total1', size=(5,1))],
    [sg.Text("Player 2", font=("calibri", 15)), sg.Input(key='player2', size=(15,1)), sg.Text("Points:"), sg.Text("", key='total2', size=(5,1))],
    [sg.Text("Round", font=("calibri", 12)), sg.Input(key='round', size=(5,1), disabled=True), sg.Text("of 5", font=("calibri", 12))],
    [sg.Text("Enter Score for Player 1:", font=("calibri", 12)), sg.Input(key='score1', size=(5,1))],
    [sg.Text("Enter Score for Player 2:", font=("calibri", 12)), sg.Input(key='score2', size=(5,1))],
    [sg.Button("Calculate Scores", button_color=("white", "green")), sg.Button("Reset", button_color=("white", "black")), sg.Button("Exit", button_color=("white", "red"))],
    [sg.Text("", key='winner', font=("calibri", 15))],
    [sg.Table(values=table_data, headings=["Round", "Player 1", "Player 2", "Player 1 Score", "Player 2 Score", "Winner"], key='table', col_widths=[10, 10, 10, 10, 10, 10], auto_size_columns=False, num_rows=5, enable_events=True, enable_click_events=True)]
]

# Create the window
window = sg.Window("Tournament Scoring System", layout, size=(500, 300), element_justification='c')

# Function to update the table
def update_table(round_number, player1, score1, player2, score2, winner):
    global table_data
    table_data.append([round_number, player1, player2, score1, score2, winner])
    window['table'].update(table_data)

# Event loop
while True:
    event, values = window.read()

    # Exit event
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    # Calculate scores event
    elif event == "Calculate Scores":
        try:
            score1 = (float(values['score1'])/100)
            score2 = (float(values['score2'])/100)

            total1 += score1
            total2 += score2

            window['total1'].update(total1)
            window['total2'].update(total2)

            # Determine the winner
            if total1 > total2:
                winner = values['player1']
            elif total1 < total2:
                winner = values['player2']
            else:
                winner = "Both players"

            # Update the winner text
            window['winner'].update(f"The winner is {winner} with a score of {max(total1, total2)} points.")

            # Update the table
            update_table(round_number, values['player1'], score1, values['player2'], score2, winner)

            # Move to the next round
            round_number += 1
            window['round'].update(round_number)

            # Reset the score inputs
            window['score1'].update("")
            window['score2'].update("")

            # Check if all rounds have been played
            if round_number > 5:
                sg.popup("All rounds have been played. Please rerun the program play again.")
                window['table'].set_col_props(0, disabled=True)
                window['table'].set_col_props(1, disabled=True)
                window['table'].set_col_props(2, disabled=True)

        except ValueError:
            sg.popup("Please enter valid numbers for the scores.")

    # Reset event
    elif event == "Reset":
        window['player1'].update("")
        window['player2'].update("")
        window['score1'].update("")
        window['score2'].update("")
        window['total1'].update("")
        window['total2'].update("")
        window['winner'].update("")
        round_number = 1
        total1 = 0
        total2 = 0
        table_data = []
        window['round'].update(round_number)
        window['table'].set_col_props(0, disabled=False)
        window['table'].set_col_props(1, disabled=False)
        window['table'].set_col_props(2, disabled=False)
        window['table'].update(values=table_data)

# Close the window
window.close()