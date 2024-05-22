import json
with open('bookreview.json','r+') as in_file:
    review = json.load(in_file)
#greeting and set up
print("Hello, and Welcome to Your Book Reviewer.")
yn_ybr = input("Would you like to review a book? Yes/No: ")
##varible and while loop set up
i = 0
while i == 0:
    
    if yn_ybr == "Yes":
        #enter book title
        user_book_title = input("What is the Book's Name?: ")
        
        #enter author
        user_book_author_s = input("Book's Author(s)?: ")

        #enter rating
        user_book_rating = input("How many out of stars out of 5?: ")

        #enter genre
        user_genre = input("What genre(s)?: ")

        #enter likes
        user_likes = input("What did you like?: ")

        #enter dislikes
        user_dislikes = input("What did you dislike?: ")

        #enter final thoughts
        user_final_thoughts = input("Any final thoughts?: ")

        def write_json(new_data, filename='bookreview.json'):
            #Reads the json file
            with open(filename,'r+') as file:
                #dictionary w/ previous data
                file_data = json.load(file)
                #ads new_data and file_data together
                file_data["My Book Reviews"].append(new_data)
                file.seek(0)
                json.dump(file_data, file, indent = 4)
        y = {"Title": user_book_title ,
        "Author(s)": user_book_author_s ,
        "Star Rating" : user_book_rating ,
        "Genre(s)" : user_genre ,
        "Likes" : user_likes ,
        "Dislikes" : user_dislikes ,
        "Final Thoughts" : user_final_thoughts }
        print(y)
        write_json(y)
        user_continue = input("Continue? Yes or No: ")
        options = ["Yes", "No"]
        if user_continue == "Yes":
            i = 0
            continue
        elif user_continue == "No":
            i = i + 1
            break
    elif yn_ybr == "No":
        print("K. Byeee! :)")
        i = i + 1
        exit
    else:
        #i did this for the lolz
        print("????")
        i = i + 1
        exit
br_search = input("Would you like to search previous reviews? Yes/No: ")
if br_search == "Yes":
     entry = input("What Book's Review Are You Looking For?(Answer With the Book's Exact Title as You Prevously Typed It.): ")
     for i in range(100):
         if review['My Book Reviews'][i]['Title'] == entry:
             ##Below is a test print that was used to check that it would print properly
             ## print(review['My Book Reviews'][i])
             ##Prints The Selected Book Review "Prettily" lol 
             print("Title: " + review['My Book Reviews'][i]['Title'])
             print("Author(s): " + review['My Book Reviews'][i]['Author(s)'])
             print("Star Rating: " + review['My Book Reviews'][i]['Star Rating'])
             print("Genre(s): " + review['My Book Reviews'][i]['Genre(s)'])
             print("Likes: " + review['My Book Reviews'][i]['Likes'])
             print("Dislikes: " + review['My Book Reviews'][i]['Dislikes'])
             print("Final Thoughts: " + review['My Book Reviews'][i]['Final Thoughts'])
elif yn_ybr == "No":
     print("K. Byeee! :)")
     exit
else:
     #i did this for the lolz
     print("????")
     exit
