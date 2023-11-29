file = open("html_quotes.txt", "r")
lines = []
for line in file.readlines():
    if '<p class="outdent">HOLMES: </p><p>' in line:
        lines.append(line.replace('<p class="outdent">HOLMES: </p><p>', '').replace('</p>', '').replace('<span style="text-decoration: underline">', '').replace('</span>', '').replace('<br />', '').replace('=','\''))

write = open("parsed_quotes.txt", "w")    
write.writelines(lines)