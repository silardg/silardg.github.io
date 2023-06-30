import json
path_data_projects = 'projects.json'

template_images = """
<div class="col-lg-4 mb-4 mb-lg-0 text-center">
    <a href="%%link%%" target="_blank">
        <picture>
            <source srcset="./pics/%%webp_path%%" type="image/webp">
            <img
                src="./pics/%%png_path%%"
                class="shadow-1-strong  mb-4 img-fluid"
                alt="%%project%%"
            />
        </picture>
    </a>
</div>
"""

index_replace_projects = "%%Projects%%"
replace_link = "%%link%%"
replace_webp = "%%webp_path%%"
replace_png = "%%png_path%%"
replace_project = "%%project%%"

json_title = 'title'

with open(path_data_projects, "r") as file_data:
    data = json.load(file_data)

pics_index = 0
pics_current_index = 1

output_projects = ""

for project_name, project_data in data.items():
    # on the beginning and on every third index, add a row
    if pics_index == 0 or pics_index % 3 == 0:
        output_projects += "<div class=\"row\">"

    current_template = template_images

    # project_name
    print("Creating " + project_name)
    project_link = "projects/" + project_name + ".html"
    project_png = project_data["thumbnail"][0]
    project_webp = project_data["thumbnail"][1]
    project_title = project_data["title"]

    print(project_link)
    print(project_png)
    print(project_webp)
    print(project_title)

    # replace here
    current_template = current_template.replace(replace_link, project_link)
    current_template = current_template.replace(replace_webp, project_webp)
    current_template = current_template.replace(replace_png, project_png)
    current_template = current_template.replace(replace_project, project_title)

    # add it to the output pics
    output_projects += current_template

    # on the end of everything, add an end div
    if pics_current_index % 3 == 0:
        print("Adding end of row")
        output_projects += "</div>"

    pics_index = pics_index + 1

    if pics_current_index == 3:
        pics_current_index = 1
    else:
        pics_current_index = pics_current_index + 1

with open("../index_template", 'r') as index_file:
    index_data = index_file.read()

    index_data = index_data.replace(index_replace_projects, output_projects)

    with open("../index.html", 'w') as f:
            f.write(index_data)    
