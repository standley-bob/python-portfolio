"""Edit this file to make the site yours."""

NAME = "Standley David"
HANDLE = "standley-bob"
ROLE = "Python software developer"
LOCATION = "Building from home"
EMAIL = "stunningstanley@gmail.com"

TAGLINE = "I write Python that does real work — tools, APIs, and small products I actually use."

INTRO = (
    "I am a coding enthusiast who likes turning messy problems into clean Python. "
    "This page is my live bench: projects I have built, the stack I reach for, "
    "and the next thing I am shipping."
)

ABOUT = [
    "I treat software as craft. A script should be readable six months later. An API should fail loudly and recover quietly. A UI should get out of the way.",
    "Most of my time is in Python: CLIs, Flask services, automation, and data plumbing. I like small, finished things more than infinite backlogs.",
    "This site itself is a Flask app — templates, a JSON-backed project catalog, and a contact inbox — so the portfolio is also a working piece of software.",
]

SKILLS = [
    {"group": "Language", "items": ["Python 3", "typing", "pytest", "packaging"]},
    {"group": "Web", "items": ["Flask", "Jinja", "REST APIs", "HTML / CSS"]},
    {"group": "Tooling", "items": ["Git", "CLI design", "automation", "JSON / files"]},
    {"group": "Mindset", "items": ["readable code", "small ships", "tests first when it counts"]},
]

SOCIALS = [
    {"label": "GitHub", "icon": "github", "href": "https://github.com/standley-bob"},
    {"label": "LinkedIn", "icon": "linkedin", "href": "https://www.linkedin.com/in/standley-david-/"},
]

HERO_SNIPPETS = [
    """from coffee import one_more

def build(idea: str) -> Software:
    while idea.count("bug") > idea.count("test"):
        one_more()
    return Software(shipped=True)  # it ran once. ship it.""",
    """from meetings import this_could_have_been_an_email

def standup(status: str) -> None:
    if "blocked" in status:
        status = "synergizing"
    print(status)  # nobody heard it anyway""",
    """try:
    sleep(8 * 60 * 60)
except Production:
    print("I am a teapot. Also awake.")
finally:
    coffee += 1""",
    """def estimate(hours: int) -> str:
    return f"{hours * 3} hours, plus a snack, plus denial"

# PM heard: "two hours\"""",
    """if production.fine:
    don't.touch()
else:
    git.commit("-m", "hotfix")
    git.commit("-m", "hotfix for the hotfix")""",
    """from stackoverflow import paste

def intern_to_senior():
    paste()
    return "LGTM"  # I did not read it""",
    """import this
del this  # I needed the namespace for bugs

while True:
    print("I'll start after this snack")""",
    """def friday() -> Release:
    tests = run_tests()
    return Release(shipped=True)  # tests were a suggestion""",
    """user.clicked("Submit")
for _ in range(4):
    user.clicked("Submit")
# we debounce in production. this is local.""",
    """from imposter import syndrome

def code_review(me: Human) -> str:
    if syndrome:
        return "looks good, I guess I got lucky"
    return "looks good, I guess I got lucky\"""",
    """inbox = Downloads()
inbox.sort()  # lol no
organizer.apply(inbox)
# the desktop is still a crime scene""",
    """def ai_help(prompt: str) -> str:
    return prompt.replace("please", "please work")

raise ItWorksOnMyMachineError("shipped")""",
]
# Drop your own mark over static/img/logo.svg when you have it.
