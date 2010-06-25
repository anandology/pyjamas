def esc(txt):
    return txt

def urlmap(txt):
    idx = txt.find("http://")
    if idx == -1:
        return esc(txt)
    for i in range(idx, len(txt)):
        c = txt[i]
        if c == ' ' or c == '\n' or c == '\t':
            i -= 1
            break

    i += 1

    beg = txt[:idx]
    if i == len(txt):
        url = txt[idx:]
        end = ''
    else:
        url = txt[idx:i]
        end = txt[i:]
    txt = esc(beg) + "<a href='%s'>" % url
    txt += "%s</a>" % esc(url) + urlmap(end)
    return txt
 
def ts(txt):
    l = txt.split('\n')
    r = []
    for line in l:
        r.append(urlmap(line))
    return '<br />'.join(r)

def markdown(text):
    result = ''
    ul_stack1 = 0
    ul_stack2 = 0
    doing_code = 0
    txt = ''
    text += '\n'
    for line in text.split("\n"):
        if doing_code:
            if line == "}}":
                doing_code = 0
                line = "</pre>"
                txt += line
                self.vp.add(HTML(txt))
                txt = ''
                continue
            if line:
                txt += line
            txt += "\n"
            continue
            
        line = line.strip()
        ul_line = False
        ul_line2 = False
        add = False
        if not line:
            line = "&nbsp;"
        elif line[:2] == "{{":
            doing_code = 1
            if len(line) > 2:
                line = "<pre class='slide_code'>%s" % line[2:]
            else:
                line = "<pre class='slide_code'>"
        elif line[:2] == '= ' and line[-2:] == ' =':
            line = "<h1 class='slide_heading1'>%s</h1>" % line[2:-2]
        elif line[:3] == '== ' and line[-3:] == ' ==':
            line = "<h2 class='slide_heading2>%s</h2>" % line[3:-3]
        elif line[:2] == '* ':
            if not ul_stack1:
                txt += "<ul class='slide_list1'>\n"
            line = "<li class='slide_listitem1'/>%s\n" % ts(line[2:])
            ul_stack1 = True
            ul_line = True
        elif line[:3] == '** ':
            if not ul_stack2:
                txt += "<ul class='slide_list2'>\n"
            line = "<li class='slide_listitem2'/>%s\n" % ts(line[2:])
            ul_stack2 = True
            ul_line2 = True
            ul_line = True
        else:
            if not doing_code:
                line = "<p class='slide_para'>%s</p>" % line
        if ul_stack2 and not ul_line2:
            ul_stack2 = False
            txt += "</ul>\n"
        if ul_stack1 and not ul_line:
            ul_stack1 = False
            txt += "</ul>\n"
        if not ul_stack2 and not ul_stack1 and not doing_code:
            add = True
        txt += line
        if add:
            result += txt
            txt = ''
    return result

