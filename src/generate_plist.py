from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree

def load_env():
    env_vars = {}
    with open('.env', 'r') as file:
        for line in file.readlines():
            key, value = line.strip().split('=')
            env_vars[key] = value
    return env_vars

def generate_plist(env_vars):
    plist = Element('plist', version="1.0")
    plist_dict = SubElement(plist, 'dict')
    
    # Label
    SubElement(plist_dict, 'key').text = "Label"
    SubElement(plist_dict, 'string').text = env_vars['PLIST_NAME']
    
    # Program Arguments
    SubElement(plist_dict, 'key').text = "ProgramArguments"
    args_array = SubElement(plist_dict, 'array')
    SubElement(args_array, 'string').text = "/usr/local/bin/python3"
    SubElement(args_array, 'string').text = env_vars["SCRIPT_PATH"]
    
    # Start Interval
    SubElement(plist_dict, 'key').text = "StartInterval"
    SubElement(plist_dict, 'integer').text = env_vars['UPDATE_INTERVAL'] # Seconds
    
    # Output Paths
    SubElement(plist_dict, 'key').text = "StandardOutPath"
    SubElement(plist_dict, 'string').text = env_vars["LOG_PATH"]
    
    SubElement(plist_dict, 'key').text = "StandardErrorPath"
    SubElement(plist_dict, 'string').text = env_vars["ERROR_PATH"]
    
    tree = ElementTree(plist)
    tree.write(f'{env_vars["PLIST_NAME"]}.plist', encoding='UTF-8', xml_declaration=True)

if __name__ == '__main__':
    env_vars = load_env()
    generate_plist(env_vars)
