import os

MAILS_DIR = "MAILS/"
# CPN_DIR = MAILS_DIR+"/CPN/"
# SUG_DIR = MAILS_DIR+"/SUG/"


def check_dirs(dir):
    if not os.path.exists(MAILS_DIR):
        os.mkdir(MAILS_DIR)

    if not os.path.exists((MAILS_DIR + str(dir))):
        os.mkdir((MAILS_DIR + str(dir)))

def save_mail(dir, msg, subject, name):
    check_exist_number = 1
    while os.path.exists(f"{(MAILS_DIR + str(dir))}/{name}{check_dirs}"):
        check_exist_number += 1
    with open(f"{(MAILS_DIR + str(dir))}/{name}.{check_exist_number}.em", "w") as em_file:
        em_file.write(f"Name:{name}\nSubject:{subject}\n\nMessage:\n{msg}\n")
    em_file.close()
    check_exist_number = 1
