# Copyright (c) Phil Charlesworth 2010
# See issue 481

def create_xml_doc(text):
    parser = get_main_frame().getDOMParser()
    parser.async = False
    parser.loadXML(text)
    return parser
