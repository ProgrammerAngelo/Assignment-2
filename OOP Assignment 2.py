from pyfiglet import Figlet
style = Figlet(font="chunky")
design = Figlet(font="bulbhead")
style_name = Figlet(font="straight")
style_job = Figlet(font="straight")

name = input("\033[1;31m" + style_name.renderText("Enter a name: "))
print("\033[0m")
print("\033[1;7m Your name is: \033[0m")
print("\033[1;93m" + style.renderText(name))
print("\033[0m")

job = input("\033[1;34m" + style_job.renderText("Enter a Job: "))
print("\033[0m")
print("\033[1;42m Your Job is: \033[0m")
print("\033[1;33m" + design.renderText(job))
print("\033[0m")