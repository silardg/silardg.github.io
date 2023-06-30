import json
path_template_html = "../projects/template"
path_template_images = "../projects/template_images"
path_data_projects = 'projects.json'

json_title = 'title'
json_desc = 'description'
json_pics = 'pictures'
json_medium_link = 'medium'
json_git_link = 'git'

replace_title = "%%Title%%"
replace_description = "%%Description%%"
replace_pictures = "%%Pictures%%"
replace_width = "%%width%%"
replace_high_res = "%%highres_path%%"
replace_webp = "%%webp_path%%"
replace_png = "%%png_path%%"
replace_git = "%%git%%"
replace_medium = "%%medium%%"

with open(path_data_projects, "r") as file_data:
    data = json.load(file_data)

for project_name, project_data in data.items():

    file_name = project_name + ".html"
    print("Creating " + file_name)
    project_title = project_data[json_title]
    project_desc = project_data[json_desc]
    project_pics = project_data[json_pics]
    project_medium = project_data[json_medium_link]
    project_git = project_data[json_git_link]
    
    pic_number = len(project_pics)
    
    output_width = pic_number
    output_description = ""
    output_pics = ""

    with open(path_template_html, 'r') as file:
        data = file.read()

        # set the title
        data = data.replace(replace_title, project_title)
        
        # set the description
        for singl_description in project_desc:
            output_description += singl_description
            #output_description += "\n<br><br>"
        data = data.replace(replace_description, output_description)

        if pic_number != 0:
            # set the pictures
            if pic_number > 3:
                print("Too many pics, have to divide")
                pic_number = 4
            else:
                pic_number = int(12/pic_number)

            template_images = ""

            # read out the template
            with open(path_template_images, 'r') as pic_file:
                template_images = pic_file.read()

            pics_index = 0
            pics_current_index = 1

            # go through the json data
            for pics_data in project_pics:

                # on the beginning and on every third index, add a row
                if pics_index == 0 or pics_index % 3 == 0:
                    output_pics += "<div class=\"row\">"

                # set the temporary text from the template
                pic_section = template_images

                # get the data from the json
                pic_high_res = pics_data[0]
                pic_png = pics_data[1]
                pic_webp = pics_data[2]
                pic_desc = pics_data[3]

                #print(pic_number)
                print(pic_high_res)

                # replace it within the text
                pic_section = pic_section.replace(replace_width, str(pic_number))
                pic_section = pic_section.replace(replace_high_res, pic_high_res)
                pic_section = pic_section.replace(replace_webp, pic_webp)
                pic_section = pic_section.replace(replace_png, pic_png)
                pic_section = pic_section.replace(replace_description, pic_desc)

                # add it to the output pics
                output_pics += pic_section

                # on the end of everything, add an end div
                if pics_current_index % 3 == 0:
                    print("Adding end of row")
                    output_pics += "</div>"

                pics_index = pics_index + 1

                if pics_current_index == 3:
                    pics_current_index = 1
                else:
                    pics_current_index = pics_current_index + 1
                
            
            # add the pictures
            data = data.replace(replace_pictures, output_pics)
        else:
            data = data.replace(replace_pictures, "")
            
        # git
        if len(project_git) != 0:
            data = data.replace(replace_git, "You can find this project on <i class=\"bi bi-github\"></i> <a href=" + project_git + " target=\"_blank\">GitHub</a>!<br>")
        else:
            data = data.replace(replace_git, "")

        # medium
        if len(project_medium) != 0:
            data = data.replace(replace_medium, "There is an additional blog post about this project on <i class=\"bi bi-medium\"></i> <a href=" + project_medium + " target=\"_blank\">Medium</a>!")
        else:
            data = data.replace(replace_medium, "")

        # write to the file
        with open("../projects/" + file_name, 'w') as f:
            f.write(data)    