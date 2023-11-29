file = open("html_quotes.txt", "r")
write = open("parsed_quotes_context.txt", "w")   
lines = []
fileLines = list(file.readlines())
for i in range(2, len(fileLines)):
    if '<p class="outdent">HOLMES: </p><p>' in fileLines[i] and '<p class="outdent">' in fileLines[i-2] and '<p class="outdent">SOUND: </p><p>' not in fileLines[i-2]:
        contextQuote = fileLines[i-2][fileLines[i-2].index('</p><p>')+7:]
        contextQuote = contextQuote.replace('</p>', '').replace('<span style="text-decoration: underline">', '').replace('</span>', '').replace('<br />', '').replace('=','\'')
        sherlockQuote = fileLines[i].replace('<p class="outdent">HOLMES: </p><p>', '').replace('</p>', '').replace('<span style="text-decoration: underline">', '').replace('</span>', '').replace('<br />', '').replace('=','\'')
        write.write(contextQuote)
        write.write(sherlockQuote)
        write.write("===\n")
