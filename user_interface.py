# File name: Aligner.py
# Authors: Kylian de Rooij, Robert van Timmeren, Remi Thüss
# Description: A user interface for a movie script and subtitle aligner

import sys
import argparse
import csv

import subtitles
import scripts
import aligner


def get_arguments():
    '''
    Ensures the file arguments are provided correctly and retrieves the files.
    '''
    parser = argparse.ArgumentParser(prog="Aligner",
                                     description="This program aligns "
                                     "a movie script and its subtitles.",
                                     usage="Provide a .txt and a .srt "
                                     "file to align the two.")
    parser.add_argument("-script", "--Script file", required=True,
                        type=str, metavar="",
                        help="Provide a .txt file that "
                        "contains a movie script.")
    parser.add_argument("-sub", "--Subtitle file", required=True,
                        type=str, metavar="",
                        help="Provide a .srt file that contains "
                        "the subtitles to the movie.")
    args = parser.parse_args()
    argv = vars(args)
    return argv


def ask_choice():
    '''
    Asks the user what they wish to use the aligner for.
    '''
    choice = int(input("Possible choices on what to do:\n"
                       "1. Create a .csv file with the timestamps "
                       "of the subtitles in the script.\n"
                       "2. Create a .csv file with the character "
                       "names in the subtitles.\n"
                       "3. Create a .csv file with the labeled "
                       "script.\n"
                       "4. Provide an overal match of the alignment "
                       "between script and subtitles.\n"
                       "5. Find lexical differences between "
                       "the script and subtitles.\n\n"
                       "Please provide the number of your choice:\n"))
    if choice not in range(1, 6):
        print("Please only provide a number between 1 and 5.")
        exit(-1)
    return choice


def create_clean_script(script_list):
    '''
    Helper function that returns a cleaned up version of the script list.
    '''
    return aligner.clean_script_dialogue(script_list)


def create_clean_script_norm(cleaned_script):
    '''
    Helper function that removes the indexes from the cleaned up script list.
    '''
    cleaned_script_norm = []
    for item in cleaned_script:
        cleaned_script_norm.append(item[0])
    return cleaned_script_norm


def execute_choice(choice, subtitle_list, script_list):
    '''
    Executes the functions of the aligner that were chosen by the user.
    '''
    cleaned_script = create_clean_script(script_list)
    cleaned_script_norm = create_clean_script_norm(cleaned_script)
    aligned_data = aligner.select_dialogue(subtitle_list, cleaned_script_norm)

    if choice == 1:
        with open('output/timestamped_script.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL, delimiter='\n')
            writer.writerow(aligner.align_timestamp(cleaned_script,
                                                    aligned_data,
                                                    script_list,
                                                    subtitle_list))
    elif choice == 2:
        with open('output/character_dialogue.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL, delimiter='\n')
            writer.writerow(aligner.character_dialogue(subtitle_list,
                                                       script_list,
                                                       cleaned_script_norm,
                                                       aligned_data))
    elif choice == 3:
        with open('output/labeled_script.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL, delimiter='\n')
            writer.writerow(script_list)
    elif choice == 4:
        matched_dialogue = aligner.select_dialogue(subtitle_list,
                                                   cleaned_script_norm)
        for element in matched_dialogue:
            print('Score:', round(element[0], 3),
                  '\nScript:', element[2],
                  '\nSubtitle:', element[1], '\n')
    elif choice == 5:
        sub_count, script_count = aligner.find_differences(subtitle_list,
                                                           cleaned_script_norm)
        print("\nSubtitles:")
        for key, value in sub_count.items():
            print("|{0:^10} | {1:^10}|".format(key, value))
        print("\nScript:")
        for key, value in script_count.items():
            print("|{0:^10} | {1:^10}|".format(key, value))


def main(argv):
    argv = get_arguments()
    subtitle_list = subtitles.main(argv['Subtitle file'])
    script_list = scripts.main(argv['Script file'])
    choice = ask_choice()
    execute_choice(choice, subtitle_list, script_list)


if __name__ == "__main__":
    main(sys.argv)
