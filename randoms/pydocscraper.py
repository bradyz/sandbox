import os


def get_sections(filename):
    sections = list()
    content = None
    content_key = None

    in_name = os.path.join(os.path.dirname(__file__), "library/"+filename)

    with open(in_name) as in_file:
        for line in in_file:
            if line.strip() and line.strip()[-1] == ")" and line[0] != " ":
                if content_key and content.strip():
                    sections.append((content_key, content.strip()))
                content = ""
                content_key = line.strip()
            elif content_key and line.strip():
                content += line.strip() + " "

    return sections


def write_html(sections, filename):
    if not sections:
        return

    filename = filename.replace(".txt", "")

    out_name = os.path.join(os.path.dirname(__file__), "library/" +
                            filename + ".html")

    with open(out_name, "w+") as out_file:
        out_file.write("<html>\n")
        out_file.write("\t<head>\n")
        out_file.write("\t\t<title>"+str(out_name)+"</title>\n")
        out_file.write("\t</head>\n")
        out_file.write("\t<body>\n")
        for head, text in sections:
            out_file.write("\t\t<div>\n")
            out_file.write("\t\t\t<h2>")
            out_file.write(head)
            out_file.write("</h2>\n")
            out_file.write("\t\t\t"+text)
            out_file.write("\n\t\t</div>\n")
        out_file.write("\t</body>\n")
        out_file.write("</html>")

if __name__ == "__main__":
    file_names = [name for name in os.listdir("library/") if ".txt" in name]
    for name in file_names:
        write_html(get_sections(name), name)
