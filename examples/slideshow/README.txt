This is a generalised Wiki-like Slideshow application.

The slide names and headings go in public/slides.txt - the file must
be of the format
    name: heading
    name1: heading1

The name is taken as the name of the file containing the slide content.
name can contain spaces - they will be replaced with underscores.
The name will also be lowercased, and ".txt" is automatically appended.
For example, "What is it" is converted to "what_is_it.txt".

Rules for formatting of slide content are as follows:

    1) Spaces are stripped off the front of all content
    2) Large headings begin with '= ' and end with ' =' for example:
           = Introduction =
       is converted to
           <h1 class='slide_heading1'> Introduction </h1>
    3) Medium headings begin with '== ' and end with ' ==' for example:
           == Introduction ==
       is converted to
           <h2 class='slide_heading2'> Introduction </h2>
    4) Unordered Lists begin with '* ' for example:
           * Hello
           * Goodbye
       is converted to
           <ul>
           <li /> Hello
           <li /> Goodbye
           </ul>
    5) Secondary unordered lists begin with '** '
    6) Blank lines result in a blank line
    7) Text on its own is wrapped in a paragraph block
    8) Code begins with {{ and ends with }} - place these on their own lines
           {{
             hello
           }}
       is converted to
           <pre>
             hello
           </pre>

