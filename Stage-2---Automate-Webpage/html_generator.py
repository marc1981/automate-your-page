

print("                                Welcome to this HTML builder!")
print("*********************************************************************************************")
print("Type in the information requested to make formatted HTML code. Hit enter after each question.")
print("*********************************************************************************************")
print()

html_project_title = input("What is the name of your HTML project? ")
stage_number_string = input("How many Course Stages does your notes cover (e.g. 1, 2, 3...)? ")
stage_number = int(stage_number_string)

if stage_number != 0:
    s = 1
    st = []
    lt = []
    lc = []
    html_total = ['', ['', '']]
    while stage_number > 0:
        try:
            s = str(s)
            stage_title = input(("What is the title for Stage") + ' ' + s + ("? "))
            
            get_lesson_number = input(("How many lessons does Stage ") + ' ' +  s  + ' ' + ("contain? Please use integers only. "))
                
            lesson_number = int(get_lesson_number)
            if lesson_number == 0:
                print("You do not have any lessons. What are you trying to pull?")
            elif lesson_number != 0:
                n = 1
                while lesson_number > 0:
                    n = str(n)
                    lesson_title = input(("What is the title for Lesson") + ' ' + n + ("? "))
                    lesson_contents = input(("What is the topic of Lesson") + ' ' + n + ("? "))
                    
                    lt.append(lesson_title)
                    
                    lc.append(lesson_contents)
                    html_total.append([stage_title, [lesson_title, lesson_contents]])
                    lesson_number = lesson_number - 1
                    n = int(n)
                    n = n + 1
        except ValueError:
                print("That's not a number. This is a number: 7")
                    
        
        st.append(stage_title)                
        stage_number = stage_number - 1
        s = int(s)
        s = s + 1
else:
    print("You do not have any stages, therefore you have no business here.")
html_total = html_total[2:]


print("_____________________________________________________")    
print("************** Here is your HTML code! **************")
print("_____________________________________________________")   
print("""
        <!DOCTYPE HTML>
            <HTML>
                <head>
                    <title>"""+html_project_title+"""</title>
                    <link rel="stylesheet" href="marc-styles.css">
                </head>
                <body>
                    <div class="project-title">  
                     """+html_project_title+"""
                    </div>""")

for piece in html_total:
    stage_title_alone = piece[0]
    
    lesson_title_alone = piece[1][0]
    lesson_contents_alone = piece[1][1]
    lesson_title_alone = str(lesson_title_alone)
    lesson_contents_alone = str(lesson_contents_alone)
    print("""
                    <div class="stage-title">
                     """ + stage_title_alone + """
                    </div>"""
                    """
                        <div class="lesson_title">
                         """ + lesson_title_alone + """
                        </div>"""
                        """
                            <div class="lesson_content">
                             """ + lesson_contents_alone + """
                            </div>"""
                   )

            
#closing lines            
print("""
                </body>
            </HTML>""")

