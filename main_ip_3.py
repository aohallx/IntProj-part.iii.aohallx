# ___Aidan O'Halloran___
#  4.28.2023
# This is a custom album designer.
# With all cited information derived from tunebat.com, bigtimemusicians.com and
# lloydworldofaudio.wordpress.com/2016/06/17/genre-analysis-shoegaze
# ..................................................................


def first_welcome():
    """
    Program prints welcome.
    """
    print("   Welcome! ")


def exit_forever():
    """
    If not entering 'Ok', the program prints 'The end'.
    """
    restart_maybe = input("This is the end of the story. "
                          "To try again, type in 'Ok'. ")
    # input function asking if user wants to restart.
    if restart_maybe == "Ok":
        print("Sweet!!")
        first_functions()
    else:
        print("Quitting this section. Here is the next.")


def wanna_exit_first_time_asking():
    """
    Function basically asking user if they want to exit this program.
    """
    wanna_quit = input("Do you want to exit this function? ")
    if (wanna_quit == "Yes") or (wanna_quit == "yes") or \
            (wanna_quit == "YES"):
        exit_forever()
    elif (wanna_quit == "no") or (wanna_quit == "No"):
        print("Ok. Let's try again.")
        asked_amount_of_songs()
    else:
        print("This is not yes or no. ")
        wanna_exit_first_time_asking()


def asked_amount_of_songs():
    """
    Asks for amount of songs in album and checks if it is an integer.
    If not, (last line of this function) calls for the want to exit function
    (basically is a quit program function).
    """
    tries = 1
    condition = False
    while not condition:
        try:
            song_amount = int(input("This is a custom album maker. "
                                    "Enter the amount of songs in your "
                                    "album: "))
            condition = True
            print("\n  ", song_amount, "Songs.\n")
            # This ^^ line of code asks user to enter # of songs in album

            estimate_album_duration(song_amount)
        # ^ Calling estimate_album_duration with the $ of songs given by user

        except ValueError:
            print("Error. This must be a whole number. ")
            #   ^ This is all fine and well until it hits 3 times that the user
            #                                       experiences this question.
            #               Then?  Below solves that issue of frustration

            tries += 1
            if tries == 4:
                condition = True
                print("Sorry for the frustration. ")
                wanna_exit_first_time_asking()


# ^ calls for function that asks if user
#                      wants to quit after 3 tries


def asked_bpm_for_songs(filler_total_album, genre):
    """
    checks if the asked bpm is an integer.
    if not, except prints and re-asks the question.
    """
    input2 = False
    while not input2:
        try:
            custom_input_question = int(input(
                "\nOkay. These are given bpms, so how many beats per "
                "minute do you want your songs to be? "))
            input2 = True
            state_album_description(filler_total_album, genre,
                                    custom_input_question, )
        except ValueError:
            print("Error. This must be a whole number. ")


def estimate_album_duration(song_amount):
    """
    estimates the duration and then asks for amount of songs,
    gives album in minutes, seconds and also the average BPM
    (Beats per minute)
    """
    genre = input("Pick a music genre! ")
    print("Ah. ", genre,
          end=".""\nShoegaze is " + "very, " * 2 + "new genre. It is "
                                                   "one of my favorite genres"
                                                   ".")
    print(
        "\nDid you know: In the early 2000s, guitarists that played "
        "music of this "
        "'gazey' sounding genre would have many effects coming "
        "from their guitar.")
    print(
        "\nThey would often be seen as looking down to change "
        "effects on their pedals.")
    print("\nThus, the genre called 'Shoegaze' had originated.")
    # ^^^^^^^^ Just asking for a genre.

    print("\n  ", song_amount, "Songs.\n")
    print("Estimated album duration in seconds: ",
          song_amount * 255)
    # In seconds. 255 is the avg I found on one of the sites listed.

    duration = song_amount * 255 / 60
    # ^ In minutes (float for now ^ )

    print("Estimated album duration in minutes: ", duration,
          "minutes long", sep=" ")
    print("\n- Press anything to continue.")

    # Next line of code adds a filler song, which basically is an extra song.
    # 'filler' adds duration + 1 song times 255/60
    filler_total_album = song_amount * 255 / 60 + 255 / 60
    round_filler = filler_total_album // 1
    round_filler_sec = filler_total_album - round_filler ** 1
    round_filler_0 = filler_total_album % filler_total_album
    print(
        "\nWe are going to add another song as an end filler. "
        "New album duration: ",
        filler_total_album, ", or ", round_filler, "minutes with ",
        round_filler_sec - round_filler_0, "of a minute long.", sep=" ")
    print("Wow! This is a pretty short album.")
    print("\nLet's estimate more of what this album will sound like. ")
    # Now we are going to calculate the bpm of each song.

    print(
        "Lloydworldofaudio.com states, after studying the Shoegaze genre, "
        "''played... set to a slow tempo of 93 Bpm. "
        "Slow tempo was a common thing and a big part of the genre.''")
    print("\n- (Press Enter)")
    bpm_total_estimate = 93 * filler_total_album
    # ^ 93bpm times the album's minutes = # of beats

    print(
        "\nThe total amount of beats on this album will be around",
        int(bpm_total_estimate // 1), "beats long. ")
    print("- ... So...")
    print("Say you want your songs to have an average of 120 or 140 beats "
          "per minute(bpm).")
    bpm_alt_120_not_rounded = (120 * filler_total_album)
    bpm_alt_140_not_rounded = (140 * filler_total_album)
    bpm_alt_120 = int(bpm_alt_120_not_rounded // 1)
    bpm_alt_140 = int(bpm_alt_140_not_rounded // 1)
    # ^^^ Rounded the bpm to integer place. Put int in for I can calculate
    # strings

    print("\nFor an average of 120 bpm, the album will be",
          bpm_alt_120, "beats long. ")
    print("For an average of 140 bpm, the album will be",
          bpm_alt_140, "beats long. ")
    print("\n- (Press Enter)")
    # ---------------END OF THIS FUNCTION-------------------
    asked_bpm_for_songs(filler_total_album, genre)
    # ---------------CALLS FOR ASK BPM FUNCTION-------------
    # ---------------    (with parameters)     -------------


def state_album_description(custom_input_question, genre, filler_total_album):
    """
    prints album description and rounds album duration in seconds.
    """
    custom_input_unrounded = \
        int(custom_input_question) * int(filler_total_album)
    custom_input = int(custom_input_unrounded // 1)
    print(
        "\nHere we are. Your album with a custom input of",
        custom_input_question,
        "bpm generates the album an estimated", custom_input,
        "beats in total. ")
    print("Press enter to continue! ")
    print("Thus.. with a genre of", genre, "your album is unique")
    print(custom_input, "beats per minute is uniquely yours.")
    what_instrument = input("What instrument would you play in this genre? ")
    print(what_instrument, "is an interesting instrument.")
    print("Have you played this instrument before? ")
    print("\nAh, I see.")
    print("Thanks for tuning in!")
    print("Press enter to continue! ")
    # ---------------END OF THIS FUNCTION-------------------
    # ---------------    NOW GOES TO NEXT    ---------------


def first_functions():
    """
    Calls for the first_welcome function and then the asked_amount_of_songs
    function. I did this because in order for some functions to be connected,
    my calls are inside their function like in the last code of the
    what_filter_function_full function, where it recalls the same function.
    """
    first_welcome()
    asked_amount_of_songs()


first_functions()

# ___Aidan O'Halloran___
#  4.28.2023
# Integration Project part III (I-continued):
# An already made playlist of songs to be filtered by
# chord progression number, year, artist, key, bpm
# ...................................................................
# With all cited information derived from tunebat.com, bigtimemusicians.com,
# lloydworldofaudio.wordpress.com/2016/06/17/genre-analysis-shoegaze,
#                                        and open.spotify.com/search.


list_of_all_songs = "Modern Color - Pale" \
                    "\nModern Color - Skipping stones\nMac Miller - Uber\n" \
                    "Kanye West - Flashing Lights" \
                    "\nMobb Deep  - Shook Ones Pt. II" \
                    "\nBedroom    - In My Head\n" \
                    "Surf Curse - Forever Dumb" \
                    "\nKanye West & Jay Z - Primetime"


def what_filter_function_full():
    """
        what_filter_function_full is the function calling for asking a question
        for what filter the user wants.
    This asks user what they want to filter by.
    if it is not the word 'year' or 'genre' in any series of capitalization,
    (.lower makes them under case), then it recalls this function again.
    """
    filter_by_what_answer = input("What do you want to filter by?\n\n   "
                                  "Filter by:\n Year - "
                                  "'year'\n Music Genre - "
                                  "'genre'\n\nEnter here: ")
    filter_by_what_undercased = filter_by_what_answer.lower()
    # ^^^^ makes answer under case letters as a string
    if filter_by_what_undercased == "year":
        send_to_year_or_genre_function(filter_by_what_undercased)
    elif filter_by_what_undercased == "genre":
        send_to_year_or_genre_function(filter_by_what_undercased)
        # if under cased answer == year or genre, sends to function
    else:
        print("Sorry, this is not a filter.\n")
        what_filter_function_full()


# ^^ This is not the FIRST function asked. it is the function that follows
#                                                if user wants to continue


# (BELOW) Song Functions. (Calling for song info below):


def shook_ones():
    """
    Gives song and bom for Shook Ones (Pt. II). Then sends to
    maybe_continue_to_ask_what_filter_by
    """
    shook_ones_artist = "Mobb Deep"
    shook_ones_bpm = 94
    print("Here is all the information about this song. It is written by",
          shook_ones_artist, "and is", shook_ones_bpm, "bpm.\n")
    maybe_continue_to_ask_what_filter_by()


def uber():
    """
    Gives song and bom for Uber. Then sends to
    maybe_continue_to_ask_what_filter_by
    """
    uber_artist = "Mac Miller"
    uber_bpm = 170
    print("Here is all the information about this song. It is written by",
          uber_artist, "and is", uber_bpm, "bpm.\n")
    maybe_continue_to_ask_what_filter_by()


def flashing_lights():
    """
    Gives song and bom for Flashing lights. Then sends to
    maybe_continue_to_ask_what_filter_by
    """
    flashing_lights_artist = "Kanye West"
    flashing_lights_bpm = 90
    print("Here is all the information about this song. It is written by",
          flashing_lights_artist, "and is", flashing_lights_bpm, "bpm.\n")
    maybe_continue_to_ask_what_filter_by()


def in_my_head():
    """
    Gives song and bom for In My Head. Then sends to
    maybe_continue_to_ask_what_filter_by
    """
    in_my_head_artist = "Bedroom"
    in_my_head_bpm = 151
    print("Here is all the information about this song. It is written by",
          in_my_head_artist, "and is", in_my_head_bpm, "bpm.\n")
    maybe_continue_to_ask_what_filter_by()


def forever_dumb():
    """
    Gives song and bom for Forever Dumb. Then sends to
    maybe_continue_to_ask_what_filter_by
    """
    forever_dumb_artist = "Surf Curse"
    forever_dumb_bpm = 171
    print("Here is all the information about this song. It is written by",
          forever_dumb_artist, "and is", forever_dumb_bpm, "bpm.\n")
    maybe_continue_to_ask_what_filter_by()


def primetime():
    """
    Gives song and bom for Primetime. Then sends to
    maybe_continue_to_ask_what_filter_by
    """
    primetime_artist = "Jay Z and Kanye West"
    primetime_bpm = 85
    print("Here is all the information about this song. It is written by",
          primetime_artist, "and is", primetime_bpm, "bpm.\n")
    maybe_continue_to_ask_what_filter_by()


def pale():
    """
    Gives song and bom for Pale. Then sends to
    maybe_continue_to_ask_what_filter_by
    """
    pale_artist = "Modern Color"
    pale_bpm = 77
    print("Here is all the information about this song. It is written by",
          pale_artist, "and is", pale_bpm, "bpm.\n")
    maybe_continue_to_ask_what_filter_by()


def skipping_stones():
    """
    Gives song and bom for Skipping Stones. Then sends to
    maybe_continue_to_ask_what_filter_by
    """
    skipping_stones_artist = "Modern Color"
    skipping_stones_bpm = 138
    print("Here is all the information about this song. It is written by",
          skipping_stones_artist, "and is", skipping_stones_bpm, "bpm.\n")
    maybe_continue_to_ask_what_filter_by()


# ^^^ no matter which song is chosen, function
#               maybe_continue_to_ask_what_filter_by is then called for.
# function below asks what year, then if its in range the original question
# for what to filter by follows with its function

def send_to_year_or_genre_function(filter_by_what_undercased):
    """
    Here, program asks user if they want to filter the songs by year or genre.
    Also, if is a year in range, it checks if it is range before sending to the
    filter_by_year function.
    """
    input3 = False
    if filter_by_what_undercased == "year":
        while not input3:
            try:
                favorite_year_answer = int(input("What year was your favorite?"
                                                 "\n*Note: The latest year "
                                                 "possible is 2023 and "
                                                 "first is 0000* : "))
                input3 = True
                if favorite_year_answer in range(0, 2023):
                    filter_by_year(favorite_year_answer)
                elif favorite_year_answer not in range(0, 2023):
                    print("Sorry, this is not after year 0 and before 2023.")
                    send_to_year_or_genre_function(filter_by_what_undercased)
                    return
            except ValueError:
                print("Error. This must be a whole number. ")
    if filter_by_what_undercased == "genre":
        asked_genre_uppercase = input("What genre would you like to filter by?"
                                      " \nGenres: \nShoegaze, Rap, Hip Hop "
                                      "and Indie\nGenre : ")
        asked_genre = asked_genre_uppercase.lower()
        filter_by_genre(asked_genre)


# if year inputted, move to function below (year info):


def filter_by_year(favorite_year_answer):
    """
    Filters the songs by year.
    Gives info in this function for the songs and asks if user
    wants to have them recent to earliest, or the opposite
    """
    print("\n", favorite_year_answer, ", a magnificent year...")
    chronological_year_answer = input("Do you want this list"
                                      " from most recent to oldest? : ")
    chronological_year_answer_made_undercased = \
        chronological_year_answer.lower()
    while True:
        if chronological_year_answer_made_undercased == "yes":
            print("\n2020: Modern Color - Pale"
                  "\n2017: Bedroom - In My Head"
                  "\n2016: Modern Color - Skipping Stones"
                  "\n2015: Surf Curse - Forever Dumb"
                  "\n2014: Mac Miller - Uber"
                  "\n2011: Jay Z and Kanye West - Primetime"
                  "\n1995: Mobb Deep - Shook Ones Pt. II")
            ready_to_ask_how_old()
            break
        if chronological_year_answer_made_undercased == "no":
            print(
                "\n1995: Mobb Deep - Shook Ones Pt. II"
                "\n2011: Jay Z and Kanye West - Primetime"
                "\n2014: Mac Miller - Uber"
                "\n2015: Surf Curse - Forever Dumb"
                "\n2016: Modern Color - Skipping Stones"
                "\n2017: Bedroom - In My Head"
                "\n2020: Modern Color - Pale")
            ready_to_ask_how_old()
        else:
            print("Not an answer. Enter another.. ")
            filter_by_year(favorite_year_answer)
        break


# if genre inputted, move to next definition about genres:

def filter_by_genre(asked_genre):
    """
    decides what to do with what genre the user inputted
    (in asked_genre)
    """
    while asked_genre != "shoegaze" and asked_genre != "indie" \
            and asked_genre != "rap" and asked_genre != "hip hop":
        asked_genre = input("Sorry, this is not a genre listed.\nWhat genre? ")
    if asked_genre == "shoegaze":
        shoegaze_genre_function()
    elif asked_genre == "indie":
        indie_genre_function()
    elif asked_genre == "rap":
        rap_genre_function()
    elif asked_genre == "hip hop":
        hip_hop_genre_function()


# down functions are functions including songs by genre. then goes to
# ready_to_ask_how_old which is another bridge type of function to continue.

def hip_hop_genre_function():
    """
    Displays songs in the genre of hip hop
    """
    print("Kanye West - Flashing Lights\nMac Miller - Uber")
    ready_to_ask_how_old()


def shoegaze_genre_function():
    """
    Displays songs in the genre of shoegaze
    """
    print("Modern Color- Pale\nModern Color - Skipping Stones")
    ready_to_ask_how_old()


def rap_genre_function():
    """
    Displays songs in the genre of rap
    """
    print("\nMobb Deep - Shook Ones Pt. II\nKanye West & Jay Z: Primetime\n")
    ready_to_ask_how_old()


def indie_genre_function():
    """
    Displays songs in the genre of indie rock
    """
    print("\nBedroom - In My Head\nSurf Curse - Forever Dumb\n")
    ready_to_ask_how_old()


# first question asked below

def exit_forever2():
    """
    Final segment, if user wants to stay.
    """
    restart_maybe = input("This is the end of the story. "
                          "To try again, type in 'Ok'. ")
    # input function asking if user wants to restart.
    if restart_maybe == "Ok":
        print("Sweet!!")
        first_question()
    else:
        print("The end.")


def wanna_exit_second_time_asking():
    """
    2nd time asking if user wants to exit
    """
    wanna_quit = input("Do you want to exit this function? ")
    if (wanna_quit == "Yes") or (wanna_quit == "yes") or \
            (wanna_quit == "YES"):
        exit_forever2()
    elif (wanna_quit == "no") or (wanna_quit == "No"):
        print("Ok. Let's try again.")
        first_question()
        """
        Above means if user wants to try again, it restarts first_question
        """
    else:
        print("This is not yes or no. ")
        wanna_exit_second_time_asking()


def first_question():
    """
    1st question of whole 2nd part of this program.
    Here we start.
    """
    want_to_start = input("\nDo you want to start? (yes or no): ")
    tries = 1
    condition2 = "True"
    while want_to_start != "yes" and want_to_start != "no" and \
            want_to_start != "Yes" and want_to_start != "No" \
            and condition2 == "True":
        if tries == 3:
            condition2 = "False"
            print("That is not an appropriate answer. \n ")
            print("Sorry for the frustration. ")
            # ^ breaks the loop of starting while condition2 == "True".
            # This forgets that function and moves on
            #                           to wanna_exit_second_time_asking
            wanna_exit_second_time_asking()
        if tries < 3:
            print("Sorry, that is not an appropriate answer. \n ")
            want_to_start = input("\nDo you want to start? (yes or no): ")
        tries += 1
    if want_to_start == "Yes" or want_to_start == "yes" or \
            want_to_start == "no" or want_to_start == "No":
        first_question_was_yes_or_no(want_to_start)


def first_question_was_yes_or_no(want_to_start):
    """
    function based off input from 1st
    then decides what to do with answer
    """
    while want_to_start == "yes" or want_to_start == "Yes":
        condition3 = "True"
        song_info_question_upper_case = input(
            "What song would you like to know about?\n"
            "modern color - pale"
            "\nmodern color - skipping stones\nmac "
            "miller - uber\n"
            "kanye west - flashing lights"
            "\nmobb Deep  - shook ones pt. II"
            "\nbedroom    - in my head\n"
            "surf curse - Forever Dumb"
            "\nkanye west & jay z - primetime"
            "\n: ")
        song_info_question = song_info_question_upper_case.lower()
        while song_info_question != "pale" and \
                song_info_question != "skipping stones" \
                and song_info_question != "uber" \
                and song_info_question != "flashing lights" \
                and song_info_question != "shook ones pt ii" \
                and song_info_question != "in my head" \
                and song_info_question != "forever dumb" \
                and song_info_question != "primetime" \
                and condition3 == "True":
            song_info_question = input(
                "Sorry, that is not a song listed.\n"
                "\nWhat song would you like to know about?\n"
                "modern color - pale"
                "\nmodern color - skipping stones\nmac "
                "miller - uber\n"
                "kanye west - flashing lights"
                "\nmobb Deep  - shook ones pt. II"
                "\nbedroom    - in my head\n"
                "surf curse - Forever Dumb"
                "\nkanye west & jay z - primetime"
                "\n: ")
        if song_info_question == "pale" and condition3 == "True":
            pale()
        elif song_info_question == "skipping stones" and condition3 == "True":
            skipping_stones()
        elif song_info_question == "primetime" and condition3 == "True":
            primetime()
        elif song_info_question == "forever dumb" and wcondition3 == "True":
            forever_dumb()
        elif song_info_question == "in my head" and condition3 == "True":
            in_my_head()
        elif song_info_question == "shook ones pt ii" and condition3 == "True":
            shook_ones()
        elif song_info_question == "flashing lights" and condition3 == "True":
            flashing_lights()
        elif song_info_question == "uber" and condition3 == "True":
            uber()
        else:
            print("What a song!\n")
        return
    while want_to_start == "no" or want_to_start == "No":
        print("Okay then. \n")
        what_filter_function_full()
        break


# bridge function below, then what_filter_function_full asks for
# the user to filter by a genre or year


def maybe_continue_to_ask_what_filter_by():
    """
    Asks user if they want to continue.
    Then, if yes or any answer, proceeds to next function
    which asks what filter to filter by.
    """
    want_to_continue_uppercase = input("\nDo you want to continue? "
                                       "(yes or no): ")
    want_to_continue = want_to_continue_uppercase.lower()
    while want_to_continue != "yes" and want_to_continue != "no":
        print("Sorry, that is not an appropriate answer. \n ")
        want_to_continue = input("\nDo you want to continue? (yes or no): ")
    if want_to_continue == "yes":
        what_filter_function_full()
    elif want_to_continue == "no":
        print("\nHere is the other segment! \n")
        what_filter_function_full()
    return


def ready_to_ask_how_old():
    """
    Function asks user if ready, and then goes to function
    which asks user how old
    """
    ready_for_ask_how_old_value = input("Are you ready "
                                        "for the final segment? (yes or no)"
                                        " ? ")
    if ready_for_ask_how_old_value == "yes":
        ask_how_old.info()
    if ready_for_ask_how_old_value != "yes":
        print("We are going to go anyway.\n")
        ask_how_old_info()


# last set of questions below. all combinations of inputs eventually leads to
# def ask_how_old_info(), first(), and ready_to_ask_how_old_info .


def ask_how_old_info():
    """
    Gives info on age gaps.
    Also a heads up on what is expected next.
    """
    year = 1996
    while year in range(1996, 2013):
        print("If you are born in ", year, ":", sep="")
        year += 1
    print("\nYou are a part of 'Gen Z!\n")
    random_num = 1
    while random_num in range(1, 5):
        star = "*"
        star *= 24
        print(star)
        break
    year = 1995
    while year in range(1980, 1996):
        print("If you are born in ", year, ":", sep="")
        year -= 1
    print("\nYou are a Millennial!\n")
    random_num = 50
    if random_num in range(1, 2001):
        random_num /= 2
        print("*" * 24)
    ask_how_old()


def ask_how_old():
    """
    Asks user how old they are and tells them what
    generation they're in.
    """
    input4 = False
    while not input4:
        try:
            age = int(input("How old are you now? "))
            input4 = True
            if age in range(1, 120):
                print("Wow.", age, "years old.")
            if 1 < age < 26:
                # ( in 2023)
                print("Gen Z. You were alive for 7/8 of these songs.")
            if 26 < age < 43:
                print("Millennial. Yoy were only alive for Mobb Deep - "
                      "Shook Ones Pt. II !")
            if age < 0 or age > 130:
                print("Sorry, out of range. Enter a real age.")
                ask_how_old()
        except ValueError:
            print("Error. This must be a whole number. ")


first_question()
