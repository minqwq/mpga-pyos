import time,datetime,calendar #时间日期库
import pwinput #密码隐藏库
import os,sys #系统底层库
# import psutil as ps
# 由于 psutil 在实际运行的时候有一些问题，所以暂时禁用
import random #随机库
import base64 #加解密库
from colorama import init, Fore, Back, Style #彩色文字库
import json #解析和保存json配置文件

class Init: #初始化
    def __init__(self):
        init(autoreset=True)
        self.clsn = 0
        self.error = 0
        self.pkg = "8 (sys)"
        self.tips = ["You can find the default password in the passwd file.", "Maybe the coverter is useless :)", "'root' is the default user.", "Is this file system real?", "Columns make the calculator work."]      
        with open('config.json','r',encoding='utf-8') as f: #读取配置
            self.cfg=json.load(f)
            self.names=self.cfg["accounts"].keys()
            initing=self.cfg["system"]
            self.ver = self.cfg["version"]

        with open('config.json','w',encoding='utf-8') as f: #写入配置
            if initing == "":
                while self.clsn != 1:
                    print("Which is your host system?\n[1]Windows   [2]Other")
                    print(
                        Fore.RED + "Note: The wrong option will cause errors in PyOS."
                    )
                    self.cls = input("Input: ")
                    if self.cls in ("1","2"):
                        self.cfg["system"]=self.cls
                        f.write(json.dumps(self.cfg,indent=4,ensure_ascii=False))
                        self.clsn = 1
                    else:
                        print(f"{Fore.RED}Invalid value! Please retry")
            else:
                self.cls = str(initing)
        time.sleep(0.5)
        self.clear()
        for i in range(1, 101):
            print("\r", end="")
            print(f"Starting: {i}%: ", "=" * (i // 8), end="", flush=True)
            # sys.stdout.flush()
            time.sleep(0.005)
        self.clear()
        self.printlist = [
            Style.DIM + "\nPY OS (R) Core Open Source System " + self.ver,
            Fore.BLUE
            + "  __  __ ___  ___   _   \n |  \\/  | _ \\/ __| /_\\  \n | |\\/| |  _/ (_ |/ _ \\ \n |_|  |_|_|  \\___/_/ \\_\\\n                        ",
            Fore.YELLOW + "Make PyOS Great Again!\n",
            "Tip: " + random.choice(self.tips),
            Fore.MAGENTA
            + "\nContributors: MeltIce, Yukari2024, EricDing618\nVisit this project in github: github.com/Meltide/mpga-pyos",
            Fore.CYAN
            + "\nAlso try PyOS's improved version by minqwq and bibimingming!\n",
        ]
        for i in self.printlist:
            print(i)
            time.sleep(0.1)
        self.count = 0
        self.file = "~"

    def clear(self):
        if self.cls == "1":
            i = os.system("cls")
        elif self.cls == "2":
            i = os.system("clear")


class PyOS(Init):
    def __init__(self):
        super().__init__()
        times = datetime.datetime.now()
        while self.count < 3:
            user = input("localhost login: ")
            if user=="create": #可新建账户
                newname=input('Name: ')
                newpwd=pwinput.pwinput()
                if newname in self.names:
                    print(f"{Fore.YELLOW}WARNING: The name was created!")
                self.cfg["accounts"][newname]=base64.b64encode(newpwd.encode("utf-8")).decode("utf-8")
                with open("config.json","w",encoding="utf-8") as f:
                    json.dump(self.cfg,f,ensure_ascii=False,indent=4)
                print(f'{Fore.GREEN}Created successfully.')
            elif user in self.names:
                while self.count < 3:
                    stpasswd = base64.b64decode(self.cfg["accounts"][user].strip()).decode("utf-8")
                    passwd = pwinput.pwinput()
                    if passwd == stpasswd:
                        print(
                            "Last login: "
                            + Fore.CYAN
                            + times.strftime("%y/%m/%d %H:%M:%S")
                        )
                        time.sleep(0.75)
                        print("")
                        while self.count < 3:
                            zshp9k_tm = datetime.datetime.now()
                            zshp9k_pre = zshp9k_tm.strftime(" %m/%d %H:%M:%S ")
                            zshp9k = zshp9k_pre
                            if self.error == 1:
                                cmd = input(
                                    Back.RED
                                    + Fore.WHITE
                                    + " ✘ "
                                    + errcode
                                    + " "
                                    + Back.WHITE
                                    + Fore.BLACK
                                    + zshp9k
                                    + Back.YELLOW
                                    + " root@localhost "
                                    + Back.BLUE
                                    + Fore.WHITE
                                    + " "
                                    + self.file
                                    + " "
                                    + Back.RESET
                                    + "> "
                                )
                            else:
                                cmd = input(
                                    Back.WHITE
                                    + Fore.BLACK
                                    + zshp9k
                                    + Back.YELLOW
                                    + " root@localhost "
                                    + Back.BLUE
                                    + Fore.WHITE
                                    + " "
                                    + self.file
                                    + " "
                                    + Back.RESET
                                    + "> "
                                )

                            self.error = 0
                            match cmd:
                                case "ls": #列出当前目录下的文件和子目录
                                    if self.file == "~":
                                        print("Downloads  Documents  Music  Pictures")
                                    elif self.file == "/":
                                        print("home")
                                case "cd" | "cd ~":
                                    self.file = "~"
                                case "cd ..":
                                    self.file = "/"
                                case "cd /":
                                    self.file = "/"
                                case "cd home":
                                    self.file = "~"
                                case "version":
                                    print(
                                        "PY OS (R) Core Open Source System " + self.ver
                                    )
                                case "time":
                                    other_StyleTime = times.strftime(
                                        "%Y-%m-%d %H:%M:%S"
                                    )
                                    print(other_StyleTime)
                                case "passwd":
                                    npassword = input("Input new password: ")
                                    with open("pwd", "r+") as pswd:
                                        bs64 = str(
                                            base64.b64encode(npassword.encode("utf-8"))
                                        )
                                        pswd.truncate()
                                        pswd.write(bs64.strip("b'"))
                                    print(
                                        "The password takes effect after the restart."
                                    )
                                case "calendar":
                                    today = datetime.datetime.today()
                                    yy = str(today.year)  # int(input("Year: "))
                                    mm = str(today.month)  # int(input("Month: "))
                                    dd = str(today.day)
                                    print(
                                        Fore.BLUE + "Now: " + yy + "-" + mm + "-" + dd
                                    )
                                    c1 = 0
                                    c2 = 0
                                    while c1 == 0:
                                        y = input("Year: ")
                                        if y.isdigit() == True:
                                            c1 = 1
                                        else:
                                            print("Invalid value! Please retype.")
                                    while c2 == 0:
                                        m = input("Month: ")
                                        if m.isdigit() == True:
                                            if int(m) > 0 and int(m) <= 12:
                                                c2 = 1
                                            else:
                                                print("Invalid value! Please retype.")
                                        else:
                                            print("Invalid value! Please retype.")
                                    print(calendar.month(int(y), int(m)))
                                case "help":
                                    print(Fore.BLUE + "=====[System]=====")
                                    print("ls          View the path")
                                    print("version     Show the system's version")
                                    print("clear       Clean the screen")
                                    print("passwd      Change your password")
                                    print(
                                        "neofetch    List all hardware and system version"
                                    )
                                    print(Fore.BLUE + "=====[Tools]=====")
                                    print("time        Show the time and date")
                                    print("calendar    Show a calendar")
                                    print("calc        A simple calculator")
                                    print("asciier     Converts characters to ASCII")
                                    print(Fore.BLUE + "=====[Games]=====")
                                    print("numgame     Number guessing game")
                                    print(Fore.BLUE + "=====[Power]=====")
                                    print("exit        Log out")
                                    print("shutdown    Shutdown the system")
                                case "asciier":
                                    ascount = 0
                                    while ascount == 0:
                                        print(Fore.BLUE + "ASCII Dic")
                                        print(
                                            "Choose the mode\n(1) Chr to ASCII\n(2) ASCII to Chr"
                                        )
                                        print(Style.DIM + "Press 'exit' to exit.")
                                        asciic = input("> ")
                                        if asciic == "1":
                                            while ascount == 0:
                                                print(
                                                    "Enter the character you want to convert to ASCII"
                                                )
                                                print(
                                                    Style.DIM + "Press 'exit' to exit."
                                                )
                                                ascii = input("> ")
                                                length = len(ascii)
                                                if ascii == "exit":
                                                    break
                                                elif ascii == "":
                                                    space = 0
                                                else:
                                                    if length == 1:
                                                        print(
                                                            "Result: "
                                                            + Fore.BLUE
                                                            + str(ord(ascii))
                                                        )
                                                    else:
                                                        print(
                                                            Fore.RED
                                                            + "Only a single character is supported."
                                                        )
                                        elif asciic == "2":
                                            while ascount == 0:
                                                print(
                                                    "Enter the ASCII code you want to convert to character"
                                                )
                                                print(
                                                    Style.DIM + "Press 'exit' to exit."
                                                )
                                                aschx = input("> ")
                                                if aschx == "exit":
                                                    #break
                                                    continue
                                                elif aschx == "":
                                                    space = 0
                                                else:
                                                    try:
                                                        print(
                                                            "Result: "
                                                            + Fore.BLUE
                                                            + chr(int(aschx))
                                                        )
                                                    except:
                                                        print(
                                                            Fore.RED + "Invalid value."
                                                        )
                                        elif asciic == "exit":
                                            break
                                        elif asciic == "":
                                            space = 0
                                        else:
                                            print(Fore.RED + "Unknown command.")
                                case "numgame":
                                    randnum = random.randint(100, 1000)
                                    running = 0
                                    runnin = 0
                                    print(Fore.BLUE + "NUMBER GUESSING GAME")
                                    print("Numerical Range: 100-1000")
                                    print("Difficulty: Normal")
                                    print("The answer is an integer.\n")
                                    while running == 0:
                                        print("Press 'start' to start, 'exit' to exit.")
                                        numcmd = input("> ")
                                        if numcmd == "start":
                                            print(Fore.BLUE + "GAME START")
                                            while runnin == 0:
                                                guess = int(
                                                    input(
                                                        "Enter the number of guesses: "
                                                    )
                                                )
                                                if guess == randnum:
                                                    print(Fore.GREEN + "YOU WIN!")
                                                    runnin = 1
                                                elif guess < randnum:
                                                    print(Fore.RED + "Less.")
                                                else:
                                                    print(Fore.RED + "Large.")
                                        if numcmd == "exit":
                                            break
                                        if numcmd == "":
                                            space = 0
                                        else:
                                            print(Fore.RED+"Unknown value.")
                                case "exit":
                                    self.clear()
                                    sys.exit(0)
                                    # break
                                case "calc":
                                    s1 = 0
                                    while s1 == 0:
                                        try:
                                            formula = input(
                                                "Enter the formula to be calculated (Type 'exit' to exit):\n> "
                                            )
                                            if formula == "exit":
                                                s1 = 1
                                            elif not all(char in '0123456789+-*/' for char in formula): #防止恶意运行Python其他代码
                                                print(Fore.RED+'Input error.')
                                            else:
                                                print(f"Result: {Fore.BLUE}{str(eval(formula))}")
                                        except Exception as e:
                                            print(Fore.RED+"Input error.")
                                case "neofetch":
                                    print(
                                        Fore.BLUE
                                        + "  __  __ ____   ____    _    \n |  \\/  |  _ \\ / ___|  / \\   \n | |\\/| | |_) | |  _  / _ \\  \n | |  | |  __/| |_| |/ ___ \\ \n |_|  |_|_|    \\____/_/   \\_\\\n                             "
                                    )
                                    print(
                                        Fore.BLUE
                                        + "root"
                                        + Fore.RESET
                                        + "@"
                                        + Fore.BLUE
                                        + "localhost"
                                    )
                                    print("-----------------")
                                    time.sleep(0.05)
                                    print(
                                        Fore.BLUE
                                        + "OS"
                                        + Fore.RESET
                                        + ": MPGA PyOS V"
                                        + self.ver
                                        + " aarch64"
                                    )
                                    if self.cls == "1":
                                        host = "Windows CMD"
                                    elif self.cls == "2":
                                        host = "UNIX Shell"
                                    else:
                                        host = "Unknown"
                                    time.sleep(0.05)
                                    print(Fore.BLUE + "Host" + Fore.RESET + ": " + host)
                                    print(
                                        Fore.BLUE
                                        + "Kernel"
                                        + Fore.RESET
                                        + ": PTCORE-V20241013-aarch64"
                                    )
                                    time.sleep(0.05)
                                    print(
                                        Fore.BLUE
                                        + "Uptime"
                                        + Fore.RESET
                                        + ": 9d, 4h, 19m, 27s"
                                    )
                                    time.sleep(0.05)
                                    print(
                                        Fore.BLUE
                                        + "Packages"
                                        + Fore.RESET
                                        + ": "
                                        + self.pkg
                                    )
                                    print(
                                        Fore.BLUE
                                        + "Shell"
                                        + Fore.RESET
                                        + ": pysh 1.0.0"
                                    )
                                    time.sleep(0.05)
                                    # print(Fore.BLUE + "CPU" + Fore.RESET + ": ("+ps.cpu_count(logical=False)+") @ "+ps.cpu_freq()/1000+"Ghz")
                                    # 由于 psutil 在实际运行的时候有一些问题，所以暂时禁用
                                    print(
                                        Fore.BLUE
                                        + "CPU"
                                        + Fore.RESET
                                        + ": (8) @ 2.035Ghz"
                                    )
                                    time.sleep(0.05)
                                    print(
                                        Fore.BLUE
                                        + "Memory"
                                        + Fore.RESET
                                        + ": "
                                        + str(random.randint(1024, 15364))
                                        + "MiB"
                                        + "/15364MiB"
                                    )
                                    time.sleep(0.05)
                                    print("")
                                    print(
                                        Back.BLACK
                                        + "    "
                                        + Back.RED
                                        + "    "
                                        + Back.GREEN
                                        + "    "
                                        + Back.YELLOW
                                        + "    "
                                        + Back.BLUE
                                        + "    "
                                        + Back.MAGENTA
                                        + "    "
                                        + Back.CYAN
                                        + "    "
                                        + Back.WHITE
                                        + "    "
                                    )
                                    print("")
                                case "":
                                    space = 0
                                case "clear":
                                    self.clear()
                                case "shutdown":
                                    print(Fore.BLUE + "Shutting down")
                                    for i in range(5):
                                        print(".", end="")
                                        time.sleep(0.5)
                                    self.clear()
                                    sys.exit(0)
                                case _:
                                    print("Unknown command.")
                                    self.error = 1
                                    errcode = str(random.randint(100, 999))
                    elif passwd == "":
                        print(
                            Style.DIM
                            + "Tip: You can find the default password in the passwd file."
                        )
                    else:
                        print("Error password! Please retry")
                        print(f"{Style.DIM}Tip: You can find the default password in the passwd file.")
            
            else:
                print("Invalid user! Please retry")
                print(Style.DIM + "Tip: 'Root' is the default user.")


if __name__ == "__main__":
    PyOS()
