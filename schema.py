import random
import sys
import zipfile
import json
from TemplateCreate import GenerateTemplate

SCREENS = {}
PROJECTS = {}
EXTENSIONS = {}


def Generate(screenName, author):
    template = GenerateTemplate(PROJECTS[screenName], EXTENSIONS)
    template['author'] = author
    template['keys'] = ["id"]
    path = f"semalar/{random.randint(45, 500)}_{template['name']}-{screenName}.json"
    open(path, "w+").write(json.dumps(template, indent=4))
    return path

def Convert(file, author):
    with zipfile.ZipFile(file, "r") as z:
        global SCREENS
        global PROJECTS
        global EXTENSIONS
        # Get the screen names.
        SCREENS = {name.split("/")[-1].replace(".scm", ""): name for name in z.namelist() if
                   name.startswith("src/") and name.endswith(".scm")}
        # Get the extension names and their class names by reading their components.json files.
        # Save the extension name and type in the dictionary.
        for extension in [name for name in z.namelist() if
                          name.startswith("assets/external_comps/") and name.endswith("/components.json")]:
            componentDetails = json.loads(z.open(extension, "r").read())[0]
            EXTENSIONS[componentDetails["name"]] = componentDetails["type"]
        # Read the screens' SCM files.
        # Then, save the results in the dictionary.
        for screenName, screenPath in SCREENS.items():
            f = z.open(screenPath, "r").readlines()[2].decode(sys.stdout.encoding)
            PROJECTS[screenName] = json.loads(f)
        return Generate(list(SCREENS.keys())[0], author)

