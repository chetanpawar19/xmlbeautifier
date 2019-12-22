import re

def xml_beautify(given_xml_str):
    s = given_xml_str
    l = s.split("\n")
    tab_count = 0
    final_s=""

    for line in l:
        if re.findall(r"<\?.*>",line)!=[]:
            final_s=final_s+tab_count*"   "+line+"\n"
        elif re.findall(r"<.*>",line)!=[] and re.findall("</\w+>",line)==[] and re.findall(r"<\?.*>",line)==[]:
            final_s=final_s+tab_count*"   "+line+"\n"
            tab_count = tab_count + 1
        elif re.findall("<\w+>",line)!=[] and re.findall("</\w+>",line)!=[]:
            final_s=final_s+tab_count*"   "+line+"\n"
        elif re.findall("<\w+>",line)==[] and re.findall("</\w+>",line)!=[]:
            tab_count = tab_count - 1
            final_s=final_s+tab_count*"   "+line+"\n"
        else:
            pass

    return final_s
