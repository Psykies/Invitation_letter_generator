# Invitation Letter Generator

This Python script generates personalized invitation letters for a birthday party by replacing a placeholder with the names of invited guests.

## Description

The script reads a sample invitation letter from a file named `starting_letter.txt` located in the `Input/Letters` directory. The sample letter contains a placeholder `[name]` which will be replaced with the names of the invited guests.

The names of the invited guests are stored in a file named `invited_names.txt` located in the `Input/Names` directory. Each name is read from the file, processed to remove newline characters, and stored in a list.

For each invited guest, the script creates a personalized invitation letter by replacing the placeholder `[name]` with the actual name and saves the letter in the `Output/ReadyToSend` directory with the filename format `letter_to_[name].txt`.

## Usage

1. Make sure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the repository directory.
4. Place the sample invitation letter in the `Input/Letters` directory.
5. Place the list of invited guests in the `Input/Names` directory.


7. The personalized invitation letters will be generated and saved in the `Output/ReadyToSend` directory.

## Resources

- [Python `readlines()` Method](https://www.w3schools.com/python/ref_file_readlines.asp)
- [Python `replace()` Method](https://www.w3schools.com/python/ref_string_replace.asp)
- [Python `strip()` Method](https://www.w3schools.com/python/ref_string_strip.asp)
