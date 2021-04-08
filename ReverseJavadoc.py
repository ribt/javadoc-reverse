#!/usr/bin/env python3

from bs4 import BeautifulSoup
import argparse
import re
import os.path
import requests

def clear(txt):
    return re.sub("\n|  *|\xa0|\u200b", " ", txt).replace("extends Object", "").replace("  ", " ").replace(" (", "(")

def getSoup(location):
    if location.startswith("http"):
        return BeautifulSoup(requests.get(location).content, "html.parser")
    else:
        return BeautifulSoup(open(location).read(), "html.parser")

def getClassCode(path):
    soup = getSoup(path)
    code = clear(soup.find("pre").text) + " {\n"

    for section in soup.findAll("section"):
        if section.h3.text == "Field Detail":
            for field in section.ul.findAll("ul", class_=re.compile("blockList(Last)?")):
                code += args.indent_with+ clear(field.pre.text) + ";\n"

        if section.h3.text == "Constructor Detail":
            for field in section.ul.findAll("ul", class_=re.compile("blockList(Last)?")):
                code += "\n" + args.indent_with+ clear(field.pre.text) + " {\n"
                code += args.indent_with*2 + "// TO DO\n"
                code += args.indent_with+ "}\n"

        if section.h3.text == "Method Detail":
            for field in section.ul.findAll("ul", class_=re.compile("blockList(Last)?")):
                description = field.text.split(field.pre.text)[-1].strip().replace("\n", "\n"+args.indent_with)
                if description:
                    code += "\n"+args.indent_with+"/*"
                    code += "\n"+args.indent_with+description
                    code += "\n"+args.indent_with+"*/\n"
                code += args.indent_with+ clear(field.pre.text) + " {\n"
                code += args.indent_with*2 + "// TO DO\n"
                code += args.indent_with+ "}\n"

    return code + "}\n"

def getClassLocations(path):
    rep = []
    soup = getSoup(path)
    for i in soup.findAll("a"):
        rep.append(os.path.split(path)[0]+"/"+i["href"])
    return rep
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create Java files from Javadoc.")
    parser.add_argument("-i", "--indent-with", metavar="chars", help="choose the indentation chars", default="\t")
    parser.add_argument("javadoc", help="location of the Javadoc (a file path or an URL)")
    parser.add_argument("out_dir", help="location of the directory to store Java files")
    args = parser.parse_args()

    for location in getClassLocations(args.javadoc+"allclasses.html"):
        with open(args.out_dir+os.path.split(location)[1].split(".")[0]+".java", "w") as f:
            f.write(getClassCode(location))
