#opening a file in read mode where a sample letter is located
#it has invitation to a birthday party where there is text for invitation and a place holder [name]
with open("./Input/Letters/starting_letter.txt") as sampleletter:
    example_letter = sampleletter.read()
    print(example_letter)

#extract individal name from the text file and save it as a list
# for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as invities:
    invited_person = []
    for name in invities:
        invited_person.append(name.replace("\n", ""))
    print(invited_person)

# Replace the [name] placeholder with the actual name.
# create a txt file of invitation for the guests and save it to a folder

for name in invited_person:
    with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode="w") as send_letter:
        replace_letter = example_letter.replace("[name]", name)
        send_letter.write(replace_letter)

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
