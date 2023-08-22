from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

def generate_plist():
    plist = Element('plist', version="1.0")
    plist_dict = SubElement(plist, 'dict')
    
    # Label
    SubElement(plist_dict, 'key').text = "Label"
    SubElement(plist_dict, 'string').text = os.getenv('PLIST_PATH')
    
    # Program Arguments
    SubElement(plist_dict, 'key').text = "ProgramArguments"
    args_array = SubElement(plist_dict, 'array')
    SubElement(args_array, 'string').text = "/usr/local/bin/python3"
    SubElement(args_array, 'string').text = os.getenv("SCRIPT_PATH")
    
    # Start Interval
    SubElement(plist_dict, 'key').text = "StartInterval"
    SubElement(plist_dict, 'integer').text = os.getenv('UPDATE_INTERVAL') # Seconds
    
    # Output Paths
    SubElement(plist_dict, 'key').text = "StandardOutPath"
    SubElement(plist_dict, 'string').text = os.getenv("LOG_PATH")
    
    SubElement(plist_dict, 'key').text = "StandardErrorPath"
    SubElement(plist_dict, 'string').text = os.getenv("ERROR_PATH")
    
    tree = ElementTree(plist)
    tree.write(f'{os.getenv("PLIST_PATH")}.plist', encoding='UTF-8', xml_declaration=True)

if __name__ == '__main__':
    #env_vars = load_env()
    generate_plist()
