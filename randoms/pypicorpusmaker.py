def write_html(sections):
    if not sections:
        return

    with open("pythonlibraries.html", "w+") as out_file:
        out_file.write("<html>\n")
        out_file.write("\t<head>\n")
        out_file.write("\t\t<title>Python Libraries</title>\n")
        out_file.write("\t</head>\n")
        out_file.write("\t<body>\n")
        for head, text in sections:
            out_file.write("\t\t<div>\n")
            out_file.write("\t\t\t<h2>")
            out_file.write(head)
            out_file.write("</h2>\n")
            out_file.write("\t\t\t"+text.replace("=", "").replace("-", ""))
            out_file.write("\n\t\t</div>\n")
        out_file.write("\t</body>\n")
        out_file.write("</html>")

if __name__ == "__main__":
    sections = list()
    with open("asdf.txt") as infile:
        title = None
        content = None
        for i, line in enumerate(infile):
            if i % 3 == 0:
                title = line
            elif i % 3 == 1:
                content = line
            else:
                sections.append((title, content))
    write_html(sections)
