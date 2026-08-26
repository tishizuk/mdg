# **Linux Pocket Guide** 

# **Daniel J. Barrett** 

Beijing • Cambridge • Farnham • Köln • Sebastopol • Tokyo

# **Special Upgrade Offer** 

If you purchased this ebook directly from <u>oreilly.com, you have the</u> following benefits:

- DRM-free ebooks — use your ebooks across devices without restrictions or limitations 

- Multiple formats — use on your laptop, tablet, or phone Lifetime access, with free updates 

- Dropbox syncing — your files, anywhere 

If you purchased this ebook from another retailer, you can upgrade your ebook to take advantage of all these benefits for just $4.99. <u>Click here</u> to access your ebook upgrade.

_Please note that upgrade offers are not available from sample content._

# **Chapter 1. Linux Pocket Guide** 

Welcome to Linux! If you’re a new user, this book can serve as a quick introduction, as well as a guide to common and practical commands. If you have Linux experience, feel free to skip the introductory material.

## **What’s in This Book?** 

This book is a short guide, _not a comprehensive reference_ . We cover important, useful aspects of Linux so you can work productively. We do not, however, present every single command and every last option (our apologies if your favorite was omitted), nor delve into detail about operating system internals. Short, sweet, and essential, that’s our motto. We focus on _commands_ , those pesky little words you type on a command line to tell a Linux system what to do. Here’s an example command that counts lines of text in a file, _myfile_ :

```
wc -l myfile
```

We’ll cover the most important Linux commands for the average user, such as `ls` (list files), `grep` (search for text in a file), `amarok` (play audio files), and `df` (measure free disk space). We touch only briefly on graphical windowing environments like GNOME and KDE, each of which could fill a Pocket Guide by itself.

We’ve organized the material by function to provide a concise learning path. For example, to help you view the contents of a file, we introduce all file-viewing commands together: `cat` for short text files, `less` for longer ones, `od` for binary files, `acroread` for PDF files, and so on. Then we explain each command in turn, briefly presenting its common uses and options.

We assume you have an account on a Linux system and know how to log in with your username and password. If not, speak with your system administrator, or if the system is your own, use the account created when you installed Linux.

#### **What’s Linux?** 

Linux is a popular, open source operating system that competes with Microsoft Windows and the Apple Macintosh. There are two ways to work with a Linux system:

- A graphical user interface with windows, icons, and mouse control. A command-line interface, called the _shell_ , for typing and running commands like the preceding `wc` . 

Windows and Mac OS computers can be operated by command line as well (Windows with its `cmd` and PowerShell command tools, and OS X with its Terminal application), but most of their users can survive without typing commands. On Linux, however, the shell is critical. If you use Linux without the shell, you are missing out.

#### **What’s a Distro?** 

Linux is extremely configurable and includes thousands of programs. As a result, different varieties of Linux have arisen to serve different needs and tastes. They all share certain core components but may look different and include different programs and files. Each variety is called a _distro_ (short for “distribution”). Popular distros include Ubuntu Linux, Red Hat Enterprise Linux, Slackware, Mint, and more. This book covers core material that should apply to every distro.

#### **What’s a Command?** 

A Linux command typically consists of a _program name_ followed by _options_ and _arguments_ , typed within a shell, like this:

```
$ wc -l myfile
```

The program name ( `wc` , the “word count” program) refers to a program somewhere on disk that the shell will locate and run. Options, which usually begin with a dash, affect the behavior of the program. In the preceding command, the `-l` option tells `wc` to count lines rather than words. The argument `myfile` specifies the file that `wc` should read and process. The leading dollar sign ( `$` ) is a _prompt_ from the shell, indicating that it is waiting for your command.

Commands can have multiple options and arguments. Options may be given individually:

```
$ wc -l -w myfile           Two individual options
```

or combined behind a single dash:

```
$ wc -lw myfile             Same as -l -w
```

though some programs are quirky and do not recognize combined options. Multiple arguments are also OK:

Options are not standardized. The same option letter (say, `-l` ) may have different meanings to different programs: in `wc -l` it means “lines of text,” but in `ls -l` it means “longer output.” In the other direction, two programs might use different options to mean the same thing, such as `-q` for “run quietly” versus `-s` for “run silently.”

Likewise, arguments are not standardized, unfortunately. They usually represent filenames for input or output, but they can be other things too, like directory names or regular expressions.

Commands can be more complex and interesting than a single program with options:

- Commands can run more than one program at a time, either in sequence (one program after another) or in a “pipeline” with the output of one command becoming the input of the next. Linux experts use pipelines all the time. 

- The Linux command-line user interface — the _shell_ — has a programming language built in. So instead of a command saying “run this program,” it might say, “if today is Tuesday, run this program; otherwise, run another command six times for each file whose name ends in _.txt_ .” 

#### **Reading This Book** 

We’ll describe many Linux commands in this book. Each description begins with a standard heading about the command; <u>Figure 1-1</u> shows one for the `ls` (list files) command. This heading demonstrates the general usage in a simple format:

```
ls [options] [files]
```

which means you’d type “ls” followed, if you choose, by options and then filenames. You wouldn’t type the square brackets “[” and “]”: they just indicate their contents are optional; and words in italics mean you have to fill in your own specific values, like names of actual files. If you see a vertical bar between options or arguments, perhaps grouped by parentheses:

```
(file | directory)
```

This indicates choice: you may supply either a filename or directory name as an argument.

The special heading also includes six properties of the command printed in black (supported) or gray (unsupported):

_Figure 1-1. Standard command heading_

_stdin_

The command reads from standard input, i.e., your keyboard, by default. See <u>Input and Output.</u>

_stdout_

The command writes to standard output, i.e., your screen, by default. See <u>Input and Output.</u>

###### - _file_ 

When given a dash (-) argument in place of an input filename, the command reads from standard input; and likewise, if the dash is supplied as an output filename, the command writes to standard output. For example, the following `wc` command line reads the files _file1_ and _file2_ , then standard input, then _file3_ :

```
$ wc file1 file2 - file3
```

###### -- _opt_ 

If you supply the command-line option “--” it means “end of options”: anything appearing later on the command line is not an option. This is sometimes necessary to operate on a file whose name begins with a dash, which otherwise would be (mistakenly) treated as an option. For example, if you have a file named _-foo_ , the command `wc -foo` will fail because `- foo` will be treated as an (invalid) option. `wc -- -foo` works. If a command does not support “--”, you can prepend the current directory path “./” to the filename so the dash is no longer the first character:

```
$ wc ./-foo
```

-- _help_

The option `--help` makes the command print a help message explaining proper usage, then exit.

###### -- _version_ 

The option `--version` makes the command print its version information and exit.

###### **Shell prompts** 

Some commands in this book can be run successfully only by the _superuser_ , a special user with permission to do anything on the system. In this case, we use a hash mark (#) as the shell prompt:

```
# superuser command goes here
```

Otherwise, we will use the dollar sign prompt, indicating an ordinary user:

```
$ ordinary command goes here
```

###### **Keystrokes** 

Throughout the book, we use certain symbols to indicate keystrokes. Like many other Linux documents, we use the ^ symbol to mean “press and hold the Control (Ctrl) key,” so for example, `^D` (pronounced “control D”) means “press and hold the Control key and type D.” We also write ESC to mean “press the Escape key.” Keys like Enter and the space bar should be selfexplanatory.

###### **Your friend, the echo command** 

In many of our examples, we’ll print information to the screen with the `echo` command, which we’ll formally describe in <u>Screen Output.</u> `echo` is one of the simplest commands: it merely prints its arguments on standard output, once those arguments have been processed by the shell.

> `$ echo My dog has fleas My dog has fleas $ echo My name is $USER` _`Shell variable USER`_ `My name is smith` 

## **Getting Help** 

If you need more information than this book provides, there are several things you can do.

_Run the_ _`man` command_

The `man` command displays an online manual page, or _manpage_ , for a given program. For example, to learn about listing files with `ls` , run:

```
$ man ls
```

To search for manpages by keyword for a particular topic, use the `-k` option followed by the keyword:

```
$ man -k database
```

_Run the_ _`info` command_

The `info` command is an extended, hypertext help system covering many Linux programs.

```
$ info ls
```

While `info` is running, some useful keystrokes are:

- To get help, type `h` To quit, type `q` 

- To page forward and backward, use the space bar and Backspace keys 

- To jump between hyperlinks, press TAB To follow a hyperlink, press Enter 

If `info` has no documentation on a given program, it displays the program’s manpage. For a listing of available documentation, type `info` by itself. To learn how to navigate the info system, type `info info` . _Use the_ _`--help` option (if any)_

Many Linux commands respond to the option `--help` by printing a short help message. Try:

```
$ ls --help
```

If the output is longer than the screen, pipe it into the `less` program to display it in pages (press `q` to quit):

```
$ ls --help | less
```

###### _Examine the directory /usr/share/doc_ 

This directory contains supporting documents for many programs, usually organized by program name and version. For example, files for the text editor emacs, version 23, are likely found (depending on distro) in _/usr/share/doc/emacs23_ .

###### _GNOME and KDE Help_ 

For help with GNOME or KDE, visit <u>http://www.gnome.org</u> or <u>http://www.kde.org.</u>

###### _Distro-specific websites_ 

Most Linux distros have an official site that includes documentation, discussion forums for questions and answers, and other resources. Simply enter the distro name (e.g., “Ubuntu”) into any popular search engine to find its web site. You can also visit the web site for this book: <u>http://shop.oreilly.com/product/0636920023029.do.</u>

###### _Linux help sites_ 

Many web sites answer Linux questions, such as <u>http://www.linuxquestions.org, http://unix.stackexchange.com, http://www.linuxhelp.net, and http://www.linuxforums.org.</u>

###### _Web search_ 

To decipher a specific Linux error message, enter the message into a web search engine, word for word, and you will likely find helpful results.

## **Linux: A First View** 

Linux has four major parts:

_The kernel_

The low-level operating system, handling files, disks, networking, and other necessities we take for granted. Most users rarely notice the kernel.

_Supplied programs_

Thousands of programs for file manipulation, text editing, mathematics, web browsing, audio, video, computer programming, typesetting, encryption, DVD burning...you name it.

###### _The shell_ 

A user interface for typing commands, executing them, and displaying the results. Linux has various shells: the Bourne shell, Korn shell, C shell, and others. This book focuses on bash, the Bourne-Again Shell, which is often the default for user accounts. However, all these shells have similar basic functions.

###### _X_ 

A graphical system that provides windows, menus, icons, mouse support, and other familiar GUI elements. More complex graphical environments are built on X; the most popular are KDE and GNOME. We’ll discuss a few programs that open X windows to run.

This book focuses on the second and third parts: supplied programs and the shell.

#### **The Graphical Desktop** 

When you log into a Linux system, you’re likely to be greeted by a graphical desktop<sup>[</sup> <u>1</u><sup>]</sup> like <u>Figure 1-2, which contains:</u>

- A main menu or taskbar. Depending on your distro and system settings, this might be at the top, bottom, or side of the screen. 

- Desktop icons representing the computer, a folder representing your home directory for personal files, a trash can, and more. 

- Icons to run applications, such as the Firefox web browser and the Thunderbird email program. 

- Controls for opening and closing windows and running multiple desktops at once. 

- A clock and other small, informational icons. 

_Figure 1-2. Graphical desktops (CentOS Linux with GNOME, Ubuntu with KDE). Desktops can look wildly different, depending on your distro and system settings._

Linux systems have several graphical interfaces, the most common being GNOME and KDE. Identify yours by clicking your system’s equivalent of a main menu or start menu and looking for the words GNOME, KDE, Kubuntu (KDE on Ubuntu Linux), or similar.

[1<sup>]</sup> Unless you’re logging in remotely over the network, in which case you’ll see just a command prompt, waiting for you to type a command.

#### **Running a Shell** 

The icons and menus in GNOME and KDE are, for some users, the primary way to work with Linux. This is fine for simple tasks like reading email and browsing the Web. Nevertheless, the true power of Linux lies beneath this graphical interface, in the shell.

To get the most out of Linux, take the time to become proficient with the shell. (That’s what this book is all about.) It might initially be more difficult than icons and menus, but once you’re used to it, the shell is quite easy to use and _very_ powerful.

To run a shell within GNOME, KDE, or any other graphical interface for Linux, you need to open a _shell window_ : a window with a shell running in it. <u>Figure 1-2</u> shows two shell windows with “$” shell prompts, awaiting your commands. Look through your system menus for an application to do this. Typical menu items are `Terminal` , `xterm` , `gnome-terminal` , `konsole` , and `uxterm` .

Don’t confuse the window program (like `konsole` ) with the shell running inside it. The window is just a container — possibly with fancy features of its own — but the shell is what prompts you for commands and runs them. If you’re not running a graphical interface — say, you’re logging in remotely over the network, or directly over an attached terminal — a shell will run immediately when you log in. No shell window is required. This was just a quick introduction. We’ll discuss more details in <u>The Shell,</u> and cover more powerful constructs in <u>Programming with Shell Scripts.</u>

#### **Input and Output** 

Most Linux commands accept input and produce output. Input can come from files or from _standard input_ , which is usually your keyboard. Likewise, output is written to files or to _standard output_ , which is usually your shell window or screen. Error messages are treated specially and displayed on _standard error_ , which also is usually your screen but kept separate from standard output.<sup>[</sup> <u>2</u><sup>]</sup> Later we’ll see how to _redirect_ standard input, output, and error to and from files or pipes. But let’s get our vocabulary straight. When we say a command “reads,” we mean from standard input unless we say otherwise. And when a command “writes” or “prints,” we mean on standard output, unless we’re talking about computer printers.

[2<sup>]</sup> For example, you can capture standard output in a file and still have standard error messages appear on screen.

#### **Users and Superusers** 

Linux is a multiuser operating system: multiple people can use a single Linux computer at the same time. On a given computer, each user is identified by a unique _username_ , like “smith” or “funkyguy,” and owns a (reasonably) private part of the system for doing work. There is also a special user named _root_ — the _superuser_ — who has the privileges to do anything at all on the system. Ordinary users are restricted: though they can run most programs, in general they can modify only the files they own. The superuser, on the other hand, can create, modify, or delete any file and run any program.

To become the superuser, you needn’t log out and log back in; just run the `su` command (see <u>Becoming the Superuser) and provide the superuser</u> password:

```
$ su -l
Password: *******
#
```

The superuser prompt ( `#` ) indicates that you’re ready to run superuser commands. Alternatively, run the `sudo` command (if your system is configured to use it), which executes a single command as the superuser, then returns control to the original user:

```
$ sudo ls /private/secrets           View a protected directory
Password: *******
secretfile1    secretfile2           It worked!
$
```

## **The Filesystem** 

To make use of any Linux system, you need to be comfortable with Linux files and _directories_ (a.k.a. folders). In a “windows and icons” system, the files and directories are obvious on screen. With a command-line system like the Linux shell, the same files and directories are still present but are not constantly visible, so at times you must remember which directory you are “in” and how it relates to other directories. You’ll use shell commands like `cd` and `pwd` to “move” between directories and keep track of where you are.

Let’s cover some terminology. As we’ve said, Linux files are collected into directories. The directories form a hierarchy, or _tree_ , as in <u>Figure 1-3: one</u> directory may contain other directories, called _subdirectories_ , which may themselves contain other files and subdirectories, and so on, into infinity. The topmost directory is called the _root directory_ and is denoted by a slash (/).<sup>[</sup> <u>3</u><sup>]</sup>

_Figure 1-3. A Linux filesystem (partial). The root folder is at the top. The “dan” folder’s full path is /home/dan._ We refer to files and directories using a “names and slashes” syntax called a _path_ . For instance, this path:

```
/one/two/three/four
```

refers to the root directory /, which contains a directory called _one_ , which contains a directory _two_ , which contains a directory _three_ , which contains a final file or directory, _four_ . If a path begins with the root directory, it’s called an _absolute_ path, and if not, it’s a _relative_ path. More on this in a moment.

Whenever you are running a shell, that shell is working “in” some directory (in an abstract sense). More technically, your shell has a _current working directory_ , and when you run commands in that shell, they operate relative (there’s that word again) to the directory. More specifically, if you refer to a relative file path in that shell, it is relative to your current working directory. For example, if your shell is “in” the directory _/one/two/three_ , and you run a command that refers to a file _myfile_ , then the file is really _/one/two/three/myfile_ . Likewise, a relative path _a/b/c_ would imply the true path _/one/two/three/a/b/c_ .

Two special directories are denoted . (a single period) and .. (two periods in a row). The former means your current directory, and the latter means your _parent_ directory, one level above. So if your current directory is _/one/two/three_ , then . refers to this directory and .. refers to _/one/two_ . You “move” your shell from one directory to another using the `cd` command:

```
$ cd /one/two/three
```

More technically, this command changes your shell’s current working directory to be _/one/two/three_ . This is an absolute change (since the directory begins with “/”); of course you can make relative moves as well:

```
$ cd d               Enter subdirectoryd
```

```
$ cd ../mydir        Go up to my parent, then into directorymydir
```

File and directory names may contain most characters you expect: capital and lowercase letters,<sup>[</sup> <u>4</u><sup>]</sup> numbers, periods, dashes, underscores, and most symbols (but not “/”, which is reserved for separating directories). For practical use, however, avoid spaces, asterisks, parentheses, and other characters that have special meaning to the shell. Otherwise, you’ll need to quote or escape these characters all the time. (See <u>Quoting.)</u>

[3<sup>]</sup> In Linux, _all_ files and directories descend from the root. This is unlike Windows or DOS, in which different devices are accessed by drive letters.

[4<sup>]</sup> Linux filenames are case-sensitive, so capital and lowercase letters are not equivalent.

#### **Home Directories** 

Users’ personal files are often found in _/home_ (for ordinary users) or _/root_ (for the superuser). Your home directory is typically _/home/_ _`your-username`_ : _/home/smith_ , _/home/jones_ , etc. There are several ways to locate or refer to your home directory.

```
cd
```

With no arguments, the `cd` command returns you (i.e., sets the shell’s working directory) to your home directory.

_`HOME` variable_

The environment variable `HOME` (see <u>Shell variables) contains the name</u> of your home directory.

```
$ echo $HOME     Theechocommand prints its arguments
/home/smith
```

When used in place of a directory, a lone tilde is expanded by the shell to the name of your home directory.

```
$ echo  ̃
/home/smith
```

When followed by a username (as in _~fred_ ), the shell expands this string to be the user’s home directory:

```
$ cd  ̃fred
```

```
$ pwd            The “print working directory” command
/home/fred
```

#### **System Directories** 

A typical Linux system has tens of thousands of system directories. These directories contain operating system files, applications, documentation, and just about everything _except_ personal user files (which typically live in _/home_ ).

Unless you’re a system administrator, you’ll rarely visit most system directories — but with a little knowledge you can understand or guess their purposes. Their names often contain three parts, which we’ll call the scope, category, and application. (These are not standard terms, but they’ll help you understand things.) For example, the directory _/usr/local/share/emacs_ , which contains local data for the emacs text editor, has scope _/usr/local_ (locally installed system files), category _share_ (program-specific data and documentation), and application _emacs_ (a text editor), shown in <u>Figure 1-4.</u> We’ll explain these three parts, slightly out of order.

_Figure 1-4. Directory scope, category, and application_

###### **Directory path part 1: category** 

A _category_ tells you the types of files found in a directory. For example, if the category is _bin_ , you can be reasonably assured that the directory contains programs. Common categories are:

###### **Categories for programs** 

|_bin_|Programs (usually binary files)|
|---|---|
|_sbin_|Programs (usually binary files) intended to be run by the superuser|
|_lib_|Libraries of code used by programs|
|_libexec_|Programs invoked by other programs, not usually by users; think “library of<br>executable programs”|

###### **Categories for documentation** 

|_doc_<br>Documentation|
|---|

|_info_|Documentation files for emacs’s built-in help system|
|---|---|
|_man_|Documentation files (manual pages) displayed by the`man`program; the files are often<br>compressed, or sprinkled with typesetting commands for`man`to interpret|
|_share_|Program-specific files, such as examples and installation instructions|
|**Categorie**|**s for configuration**|
|_etc_|Configuration files for the system (and other miscellaneous stuff)|
|_init.d_|Configuration files for booting Linux|
|_rc.d_|Configuration files for booting Linux; also_rc1.d_,_rc2.d_, ...|
|**Categorie**|**s for programming**|
|_include_|Header files for programming|
|_src_|Source code for programs|
|**Categorie**|**s for web files**|
|_cgi-bin_|Scripts/programs that run on web pages|
|_html_|Web pages|
|_public_ht_<br>_ml_|Web pages, typically in users’ home directories|
|_www_|Web pages|
|**Categorie**|**s for display**|
|_fonts_|Fonts (surprise!)|
|_X11_|X window system files|
|**Categorie**|**s for hardware**|
|_dev_|Device files for interfacing with disks and other hardware|
|_media_|Mount points: directories that provide access to disks|
|_mnt_|Mount points: directories that provide access to disks|
|_misc_|Mount points: directories that provide access to disks|

###### **Categories for runtime files** 

|_var_|Files specific to this computer, created and updated as the computer runs|
|---|---|
|_lock_|Lock files, created by programs to say, “I am running”; the existence of a lock file may|

||prevent another program, or another instance of the same program, from running or<br>performing an action|
|---|---|
|_log_|Log files that track important system events, containing error, warning, and<br>informational messages|
|_mail_|Mailboxes for incoming mail|
|_run_|PID files, which contain the IDs of running processes; these files are often consulted to<br>track or kill particular processes|
|_spool_|Files queued or in transit, such as outgoing email, print jobs, and scheduled jobs|
|_tmp_|Temporary storage for programs and/or people to use|
|_proc_|Operating system state: see<br>Operating System Directories|

###### **Directory path part 2: scope** 

The _scope_ of a directory path describes, at a high level, the purpose of an entire directory hierarchy. Some common ones are:

|_/_|System files supplied with Linux (pronounced “root”)|
|---|---|
|_/usr_|More system files supplied with Linux (pronounced “user”)|
|_/usr/gam_<br>_es_|Games (surprise!)|
|_/usr/loca_<br>_l_|System files developed “locally,” either for your organization or your individual<br>computer|
|_/usr/X11_<br>_R6_|Files pertaining to the X window system|

So for a category like _lib_ (libraries), your Linux system might have directories _/lib, /usr/lib, /usr/local/lib, /usr/games/lib_ , and _/usr/X11R6/lib_ . There isn’t a clear distinction between _/_ and _/usr_ in practice, but there is a sense that _/_ is “lower-level” and closer to the operating system. So _/bin_ contains fundamental programs like `ls` and `cat` , _/usr/bin_ contains a wide variety of applications supplied with your Linux distribution, and _/usr/local/bin_ contains programs your system administrator chose to install. These are not hard-and-fast rules but typical cases.

###### **Directory path part 3: application** 

The application part of a directory path, if present, is usually the name of a program. After the scope and category (say, _/usr/local/doc_ ), a program may

have its own subdirectory (say, _/usr/local/doc/myprogram_ ) containing files it needs.

#### **Operating System Directories** 

Some directories support the Linux kernel, the lowest-level part of the Linux operating system.

_/boot_

Files for booting the system. This is where the kernel lives, typically named _/boot/vmlinuz_ .

_/lost+found_

Damaged files that were rescued by a disk recovery tool.

_/proc_

Describes currently running processes; for advanced users. The files in _/proc_ provide views into the running kernel and have special properties. They always appear to be zero sized, read-only, and dated now:

```
$ ls -l /proc/version
```

```
-r--r--r--   1 root   root    0 Oct  3 22:55 /proc/version
```

However, their contents magically contain information about the Linux kernel:

```
$ cat /proc/version
Linux version 2.6.32-71.el6.i686 ...
```

Files in _/proc_ are used mostly by programs, but feel free to explore them. Here are some examples:

|_/proc/ioports_|A list of your computer’s input/output hardware.|
|---|---|
|_/proc/version_|The operating system version. The`uname`command prints the same information.|
|_/proc/uptime_|System uptime, i.e., seconds elapsed since the system was last booted. Run the<br>`uptime`command for a more human-readable result.|
|_/proc/_**_nnn_**|Where_`nnn`_is a positive integer, information about the Linux process with process<br>ID_`nnn`_.|
|_/proc/self_|Information about the current process you’re running; a symbolic link to a_/proc/__`nnn`_<br>file, automatically updated. Try`ls -l /proc/self`several times in a row: you’ll see<br>_/proc/self_changing where it points.|

#### **File Protections** 

A Linux system may have many users with login accounts. To maintain privacy and security, most users can access only _some_ files on the system, not all. This access control is embodied in two questions:

_Who has permission?_

   - Every file and directory has an _owner_ who has permission to do anything with it. Typically the user who created a file is its owner, but relationships can be more complex. 

   - Additionally, a predefined _group_ of users may have permission to access a file. Groups are defined by the system administrator and are covered in <u>Group Management.</u> 

   - Finally, a file or directory can be opened to _all users_ with login accounts on the system. You’ll also see this set of users called _the world_ or simply _other_ . 

- _What kind of permission is granted?_ 

   - File owners, groups, and the world may each have permission to _read_ , _write_ (modify), and _execute_ (run) particular files. Permissions also extend to directories, which users may read (access files within the directory), write (create and delete files within the directory), and execute (enter the directory with `cd` ). 

To see the ownership and permissions of a file, run:

```
$ ls -l myfile
-rw-r--r-- 1 smith smith   7384 Jan 04 22:40 myfile
```

To see the ownership and permissions of a directory, run:

```
$ ls -ld dirname
drwxr-x--- 3 smith smith   4096 Jan 08 15:02 dirname
```

In the output, the file permissions are the 10 leftmost characters, a string of `r` (read), `w` (write), `x` (execute), other letters, and dashes. For example:

```
-rwxr-x---
```

Here’s what these letters and symbols mean.

Positi on Meaning

|Positi<br>on|Meaning|
|---|---|
|1|File type:`-`= file,`d`= directory,`l`= symbolic link,`p`= named pipe,`c`= character device,`b`<br>= block device|
|2–4|Read, write, and execute permissions for the file’s owner|
|5–7|Read, write, and execute permissions for the file’s group|
|8–10|Read, write, and execute permissions for all other users|

So our example `-rwxr-x---` means a file that can be read, written, and executed by the owner, read and executed by the group, and not accessed at all by the rest of the world. We describe `ls` in more detail in <u>Basic File Operations. To change the owner, group ownership, or permissions of a file,</u> use the `chown` , `chgrp` , and `chmod` commands, respectively, as described in <u>File Properties.</u>

## **The Shell** 

In order to run commands on a Linux system, you’ll need somewhere to type them. That “somewhere” is called the _shell_ , which is Linux’s command-line user interface: you type a command and press Enter, and the shell runs whatever program (or programs) you’ve requested. (See <u>Running a Shell</u> to learn how to open a shell window.)

For example, to see who’s logged in, you could execute this command in a shell:

```
$ who
silver       :0    Sep 23 20:44
byrnes    pts/0    Sep 15 13:51
barrett   pts/1    Sep 22 21:15
silver    pts/2    Sep 22 21:18
```

(The dollar sign is the shell prompt, which means the shell is ready to run a command.) A single command can also invoke several programs at the same time, and even connect programs together so they interact. Here’s a command that redirects the output of the `who` program to become the input of the `wc` program, which counts lines of text in a file; the result is the number of lines in the output of `who` :

```
$ who | wc -l
4
```

telling you how many users are logged in.<sup>[</sup> <u>5</u><sup>]</sup> The vertical bar, called a _pipe_ , makes the connection between `who` and `wc` .

A shell is actually a program itself, and Linux has several. We focus on bash (the Bourne-Again Shell), located in _/bin/bash_ , which is usually the default in Linux distros.

[5<sup>]</sup> Actually, how many interactive shells those users are running. If a user has two shells running, like the user silver in our example, he’ll have two lines of output from `who` .

#### **The Shell Versus Programs** 

When you run a command, it might invoke a Linux program (like `who` ), or instead it might be a _built-in command_ , a feature of the shell itself. You can tell the difference with the `type` command:

```
$ type who
who is /usr/bin/who
$ type cd
cd is a shell builtin
```

It is helpful to know what the shell provides versus what Linux does. The next few sections describe features of the shell.

#### **Selected Features of the bash Shell** 

A shell does much more than simply run commands. It also has powerful features to make this task easier: wildcards for matching filenames, a “command history” to recall previous commands quickly, pipes for making the output of one command become the input of another, variables for storing values for use by the shell, and more. Take the time to learn these features, and you will become faster and more productive with Linux. Let’s skim the surface and introduce you to these useful tools. (For full documentation, run `info bash` .)

###### **Wildcards** 

Wildcards are a shorthand for sets of files with similar names. For example, `a*` means all files whose names begin with lowercase “a”. Wildcards are “expanded” by the shell into the actual set of filenames they match. So if you type:

```
$ ls a*
```

the shell first expands `a*` into the filenames that begin with “a” in your current directory, as if you had typed:

```
$ ls aardvark adamantium apple
```

`ls` never knows you used a wildcard: it sees only the final list of filenames after the shell expands the wildcard. Importantly, this means _every_ Linux command, regardless of its origin, works with wildcards and other shell features.

Wildcards never match two characters: a leading period, and the directory slash ( `/` ). These must be given literally, as in `.pro*` to match _.profile_ , or `/etc/*conf` to match all filenames ending in _conf_ in the _/etc_ directory.

###### **DOT FILES** 

Filenames with a leading period, called _dot files_ , are special in Linux. When you name a file beginning with a period, it will not be displayed by some programs:

`ls` will omit the file from directory listings, unless you provide the `-a` option Shell wildcards do not match a leading period

Effectively, dot files are hidden unless you explicitly ask to see them. As a result, sometimes they are called “hidden files.”

|Wildca<br>rd|Meaning|
|---|---|
|*|Zero or more consecutive characters|
|?|Any single character|
|[_`set`_]|Any single character in the given_`set`_, most commonly a sequence of characters, like<br>`[aeiouAEIOU]`for all vowels, or a range with a dash, like`[A-Z]`for all capital letters|
|[^_`set`_]|Any single character_not_in the given_`set`_(as in the earlier example)|
|[!_`set`_]|Same as`^`|

When using character sets, if you want to include a literal dash in the set, put it first or last. To include a literal closing square bracket in the set, put it first. To include a `^` or `!` symbol literally, don’t put it first.

###### **Brace expansion** 

Similar to wildcards, expressions with curly braces also expand to become multiple arguments to a command. The comma-separated expression:

```
{X,YY,ZZZ}
```

expands first to X, then YY, and finally ZZZ within a command line, like this:

```
$ echo sand{X,YY,ZZZ}wich
sandXwich sandYYwich sandZZZwich
```

Braces work with any strings, unlike wildcards, which are limited to filenames. The preceding example works regardless of which files are in the current directory.

###### **Shell variables** 

You can define variables and their values by assigning them:

```
$ MYVAR=3
```

To refer to a value, simply place a dollar sign in front of the variable name:

```
$ echo $MYVAR
3
```

Some variables are standard and commonly defined by your shell upon login.

|Variab<br>le|Meaning|
|---|---|
|`DISPLAY`|The name of your X window display|
|`HOME`|Your home directory, such as_/home/smith_|
|`LOGNAME`|Your login name, such as`smith`|
|`MAIL`|Your incoming mailbox, such as_/var/spool/mail/smith_|
|`OLDPWD`|Your shell’s previous directory, prior to the last`cd`<br>command|
|`PATH`|Your shell search path: directories separated by colons|
|`PWD`|Your shell’s current directory|
|`SHELL`|The path to your shell, e.g.,_/bin/bash_|
|`TERM`|The type of your terminal, e.g., xterm or vt100|
|`USER`|Your login name|

To see a shell’s variables, run:

```
$ printenv
```

The scope of the variable (i.e., which programs know about it) is, by default, the shell in which it’s defined. To make a variable and its value available to other programs your shell invokes (i.e., subshells), use the `export` command:

```
$ export MYVAR
```

or the shorthand:

```
$ export MYVAR=3
```

Your variable is now called an _environment variable_ , since it’s available to other programs in your shell’s “environment.” So in the preceding example, the exported variable `MYVAR` is available to all programs run by that same shell (including shell scripts: see <u>Variables).</u>

To make a variable value available to a specific program just once, prepend _`variable=value`_ to the command line:

```
$ printenv HOME
/home/smith
$ HOME=/home/sally printenv HOME
/home/sally
$ printenv HOME
/home/smith                  The original value is unaffected
```

###### **Search path** 

Programs are scattered all over the Linux filesystem, in directories like _/bin_ and _/usr/bin_ . When you run a program via a shell command, how does the shell find it? The critical variable `PATH` tells the shell where to look. When you type any command:

```
$ who
```

the shell has to find the `who` program by searching through Linux directories. The shell consults the value of `PATH` , which is a sequence of directories separated by colons:

```
$ echo $PATH
```

```
/usr/local/bin:/bin:/usr/bin:/home/smith/bin
```

and looks for the `who` command in each of these directories. If it finds `who` (say, _/usr/bin/who_ ), it runs the command. Otherwise, it reports:

```
bash: who: command not found
```

To add directories to your shell’s search path temporarily, modify its `PATH` variable. For example, to append _/usr/sbin_ to your shell’s search path:

```
$ PATH=$PATH:/usr/sbin
$ echo $PATH
/usr/local/bin:/bin:/usr/bin:/home/smith/bin:/usr/sbin
```

This change affects only the current shell. To make it permanent, modify the `PATH` variable in your startup file _~/.bash_profile_ , as explained in <u>Tailoring Shell Behavior. Then log out and log back in.</u>

###### **Aliases** 

The built-in command `alias` defines a convenient shorthand for a longer command, to save typing. For example:

```
$ alias ll='ls -l'
```

defines a new command `ll` that runs `ls -l` :

```
$ ll
total 436
-rw-r--r--    1 smith     3584 Oct 11 14:59 file1
-rwxr-xr-x    1 smith       72 Aug  6 23:04 file2
...
```

Define aliases in your _~/.bashrc_ file (see <u>Tailoring Shell Behavior) to be</u> available whenever you log in.<sup>[</sup> <u>6</u><sup>]</sup> To list all your aliases, type `alias` . If aliases don’t seem powerful enough for you (since they have no parameters or branching), see <u>Programming with Shell Scripts, run</u> `info bash` , and read up on “shell functions.”

###### **Input/output redirection** 

The shell can redirect standard input, standard output, and standard error to and from files. In other words, any command that reads from standard input can have its input come from a file instead with the shell’s < operator:

```
$ mycommand < infile
```

Likewise, any command that writes to standard output can write to a file instead:

```
$ mycommand > outfile                Create/overwrite outfile
```

```
$ mycommand >> outfile               Append to outfile
```

A command that writes to standard error can have its output redirected to a file as well, while standard output still goes to the screen:

```
$ mycommand 2> errorfile
```

To redirect both standard output and standard error to files:

```
$ mycommand > outfile 2> errorfile   Separate files
```

```
$ mycommand >& outfile               Single file
```

###### **Pipes** 

You can redirect the standard output of one command to be the standard input of another, using the shell’s pipe (|) operator. For example:

```
$ who | sort
```

sends the output of `who` into the `sort` program, printing an alphabetically sorted list of logged-in users. Multiple pipes work too. Here we sort the output of `who` again, extract the first column of information (using `awk` ), and display the results one page at a time (using `less` ):

```
$ who | sort | awk '{print $1}' | less
```

###### **Combining commands** 

To invoke several commands in sequence on a single command line, separate them with semicolons:

```
$ command1 ; command2 ; command3
```

To run a sequence of commands as before, but stop execution if any of them fails, separate them with `&&` (“and”) symbols:

```
$ command1 && command2 && command3
```

To run a sequence of commands, stopping execution as soon as one succeeds, separate them with `||` (“or”) symbols:

```
$ command1 || command2 || command3
```

###### **Quoting** 

Normally, the shell treats whitespace simply as separating the words on the command line. If you want a word to _contain_ whitespace (e.g., a filename with a space in it), surround it with single or double quotes to make the shell treat it as a unit. Single quotes treat their contents literally, while double quotes let shell constructs be evaluated, such as variables:

> `$ echo 'The variable HOME has value $HOME' The variable HOME has value $HOME $ echo "The variable HOME has value $HOME" The variable HOME has value /home/smith` 

Backquotes (“backticks”) cause their contents to be evaluated as a shell command. The contents are then replaced by the standard output of the command:

```
$ whoami           Program that prints your username
smith
```

```
$ echo My name is `whoami`
My name is smith
```

###### **Escaping** 

If a character has special meaning to the shell but you want it used literally (e.g., `*` as a literal asterisk rather than a wildcard), precede the character with the backward slash “\” character. This is called _escaping_ the special character:

```
$ echo a*                   As a wildcard, matching “a” filenames
aardvark  agnostic  apple
$ echo a\*                  As a literal asterisk
a*
$ echo "I live in $HOME"    Dollar sign means a variable value
I live in /home/smith
$ echo "I live in \$HOME"   A literal dollar sign
I live in $HOME
```

You can also escape control characters (tabs, newlines, ^D, and so forth) to have them used literally on the command line, if you precede them with `^V` . This is particularly useful for tab ( `^I` ) characters, which the shell would otherwise use for filename completion (see <u>Filename completion).</u>

```
$ echo "There is a tab between here^V^I and here"
There is a tab between here        and here
```

###### **Command-line editing** 

Bash lets you edit the command line you’re working on, using keystrokes inspired by the text editors emacs and vi (see <u>File Creation and Editing). To</u> enable command-line editing with emacs keys, run this command (and place it in your _~/.bash_profile_ to make it permanent):

```
$ set -o emacs
```

For vi keys:

```
$ set -o vi
```

|emacs keystroke|vi keystroke (after<br>ESC)|Meaning|
|---|---|---|
|^P or up arrow|k|Go to previous command|
|^N or down<br>arrow|j|Go to next command|

|emacs keystroke|vi keystroke (after<br>ESC)|Meaning|
|---|---|---|
|^F or right<br>arrow|l|Go forward one character|
|^B or left arrow|h|Go backward one<br>character|
|^A|0|Go to beginning of line|
|^E|$|Go to end of line|
|^D|x|Delete next character|
|^U|^U|Erase entire line|

###### **Command history** 

You can recall previous commands you’ve run — that is, the shell’s _history_ — and re-execute them. Some useful history-related commands are listed below.

|Comma<br>nd|Meaning|
|---|---|
|`history`|Print your history|
|`history` _`N`_|Print the most recent_`N`_commands in your history|
|`history -`<br>`c`|Clear (delete) your history|
|`!!`|Re-run previous command|
|`!`_`N`_|Re-run command number_`N`_in your history|
|`!-`_`N`_|Re-run the command you typed_`N`_commands ago|
|`!$`|Represents the last parameter from the previous command; great for checking that files<br>are present before removing them:|
||`$ ls a*`<br>`acorn.txt   affidavit`<br>`$ rm !$`|

|Comma|||
|---|---|---|
|nd|Meaning||
|`!*`|Represents|all parameters from the previous command:|
||`$ ls a`|`b c`|
||`a   b`|`c`|
||`$ wc !*`||
||`103`|`252   2904 a`|
||`12`|`25    384 b`|
||`25473`|`65510 988215 c`|
||`25588`|`65787 991503 total`|

###### **Filename completion** 

Press the TAB key while you are in the middle of typing a filename, and the shell will automatically complete (finish typing) the filename for you. If several filenames match what you’ve typed so far, the shell will beep, indicating the match is ambiguous. Immediately press TAB again and the shell will present the alternatives. Try this:

- `$ cd /usr/bin` 

```
$ ls un<TAB><TAB>
```

The shell will display all files in _/usr/bin_ that begin with _un_ , such as _uniq_ , _units_ , and _unzip_ . Type a few more characters to disambiguate your choice and press TAB again.

[6<sup>]</sup> Some setups use a separate file, _~/.bash_aliases_ , for this purpose.

#### **Shell Job Control** 

|jobs|List your jobs.|
|---|---|
|`&`|Run a job in the background.|
|`^Z`|Suspend the current (foreground) job.|
|`suspen`<br>`d`|Suspend a shell.|
|`fg`|Unsuspend a job: bring it into the<br>foreground.|
|`bg`|Make a suspended job run in the<br>background.|

All Linux shells have _job control_ : the ability to run programs in the background (multitasking behind the scenes) and foreground (running as the active process at your shell prompt). A _job_ is simply the shell’s unit of work. When you run a command interactively, your current shell tracks it as a job. When the command completes, the associated job disappears. Jobs are at a higher level than Linux processes; the Linux operating system knows nothing about them. They are merely constructs of the shell. Some important vocabulary about job control is:

###### _Foreground job_ 

Running in a shell, occupying the shell prompt so you cannot run another command

###### _Background job_ 

Running in a shell, but not occupying the shell prompt, so you can run another command in the same shell

###### _Suspend_ 

To stop a foreground job temporarily

###### _Resume_ 

To cause a suspended job to start running again

#### **Name** 

jobs

The built-in command `jobs` lists the jobs running in your current shell.

```
$ jobs
```

- `[1]-  Running                 emacs myfile &` 

```
[2]+  Stopped                 su
```

The integer on the left is the job number, and the plus sign identifies the default job affected by the `fg` (foreground) and `bg` (background) commands.

#### **Name** 

&

Placed at the end of a command line, the ampersand causes the given command to run as a background job.

- `$ emacs myfile &` 

```
[2] 28090
```

The shell’s response includes the job number (2) and the process ID of the command (28090).

#### **Name** 

^Z

Typing `^Z` in a shell, while a job is running in the foreground, will suspend that job. It simply stops running, but its state is remembered.

```
$ mybigprogram
```

```
^Z
[1]+  Stopped                 mybigprogram
$
```

Now you’re ready to type `bg` to put the command into the background, or `fg` to resume it in the foreground.

#### **Name** 

###### suspend 

The built-in command `suspend` will suspend the current shell if possible, as if you’d typed `^Z` to the shell itself. For instance, if you’ve run the `su` command and want to return to your original shell:

```
$ whoami
smith
$ su -l
Password: *******
# whoami
root
# suspend
[1]+  Stopped                 su
$ whoami
smith
```

#### **Name** 

bg

#### **Synopsis** 

```
bg [%jobnumber]
```

The built-in command `bg` sends a suspended job to run in the background. With no arguments, `bg` operates on the most recently suspended job. To specify a particular job (shown by the `jobs` command), supply the job number preceded by a percent sign:

```
$ bg %2
```

Some types of interactive jobs cannot remain in the background — for instance, if they are waiting for input. If you try, the shell will suspend the job and display:

```
[2]+  Stopped            command line here
```

You can now resume the job (with `fg` ) and continue.

#### **Name** 

fg

#### **Synopsis** 

```
fg [%jobnumber]
```

The built-in command `fg` brings a suspended or backgrounded job into the foreground. With no arguments, it selects a job, usually the most recently suspended or backgrounded one. To specify a particular job (as shown by the `jobs` command), supply the job number preceded by a percent sign:

```
$ fg %2
```

#### **Killing a Command in Progress** 

If you’ve launched a command from the shell running in the foreground, and want to kill it immediately, type `^C` . The shell recognizes `^C` as meaning, “terminate the current foreground command right now.” So if you are displaying a very long file (say, with the `cat` command) and want to stop, type `^C` :

```
$ cat bigfile
This is a very long file with many lines. Blah blah blah
blah blah blah blahblahblah ^C
$
```

To kill a program running in the background, you can bring it into the foreground with `fg` and then type `^C` , or alternatively, use the `kill` command (see <u>Controlling Processes).</u>

Typing `^C` is not a friendly way to end a program. If the program has its own way to exit, use that when possible: see the sidebar for details.

###### **SURVIVING A KILL** 

Killing a foreground program with `^C` may leave your shell in an odd or unresponsive state, perhaps not displaying the keystrokes you type. This happens because the killed program had no opportunity to clean up after itself. If this happens to you:

1. Press `^J` to get a shell prompt. This produces the same character as the Enter key (a newline) but will work even if Enter does not. 

2. Type the shell command `reset` (even if the letters don’t appear while you type) and press `^J` again to run this command. This should bring your shell back to normal. 

`^C` works only with shells. It will likely have no effect if typed in a window that is not a shell window. Additionally, some programs are written to “catch” the `^C` and ignore it: an example is the text editor emacs.

#### **Terminating a Shell** 

To terminate a shell, either run the `exit` command or type ^D.<sup>[</sup> <u>7</u><sup>]</sup>

```
$ exit
```

[7<sup>]</sup> Control-D sends an “end of file” signal to any program reading from standard input. In this case, the program is the shell itself, which terminates.

#### **Tailoring Shell Behavior** 

To configure all your shells to work in a particular way, edit the files _.bash_profile_ and _.bashrc_ in your home directory. These files execute each time you log in ( _~/.bash_profile_ ) or open a shell ( _~/.bashrc_ ). They can set variables and aliases, run programs, print your horoscope, or whatever you like.

These two files are examples of _shell scripts_ : executable files that contain shell commands. We’ll cover this feature in more detail in <u>Programming with Shell Scripts.</u>

This concludes our basic overview of Linux and the shell. Now we turn to Linux commands, listing and describing the most useful commands for working with files, processes, users, networking, multimedia, and more.

## **Basic File Operations** 

<!-- Start of picture text --> ls List files in a directory.<br>cp Copy a file.<br>mv Rename (“move”) a file.<br>rm Delete (“remove”) a file.<br>ln Create links (alternative names) to a<br>file.<br><!-- End of picture text -->

One of the first things you’ll need to do on a Linux system is manipulate files: copying, renaming, deleting, and so forth.

#### **Name** 

ls — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
ls [options] [files]
```

The `ls` command (pronounced as it is spelled, _ell ess_ ) lists attributes of files and directories. You can list files in the current directory:

```
$ ls
```

in given directories:

```
$ ls dir1 dir2 dir3
```

or individually:

```
$ ls file1 file2 file3
```

The most important options are `-a` , `-l` , and `-d` . By default, `ls` hides files whose names begin with a dot, as explained in the sidebar <u>Dot Files. The</u> `-a` option displays all files.

```
$ ls
myfile1   myfile2
$ ls -a
.hidden_file   myfile1   myfile2
```

The `-l` option produces a long listing:

```
-rw-r--r--    1 smith users       149 Oct 28  2011 my.data
```

that includes, from left to right: the file’s permissions (-rw-r--r--), owner (smith), group (users), size (149 bytes), last modification date (Oct 28 2011) and name. See <u>File Protections</u> for more information on permissions.

The `-d` option lists information about a directory itself, rather than descending into the directory to list its files.

```
$ ls -ld my.dir
drwxr-xr-x    1 smith users      4096 Oct 29  2011 my.dir
```

#### **Useful options** 

> `-a`<sup>List all files, including those whose names begin with a dot.</sup> 

> `-l`<sup>Long listing, including file attributes. Add the</sup><sup>`-h`option (human-readable) to print file sizes in</sup> kilobytes, megabytes, and gigabytes, instead of bytes. 

> `-F`<sup>Decorate certain filenames with meaningful symbols, indicating their types. Appends “/” to</sup> directories, “*” to executables, “@” to symbolic links, “|” to named pipes, and “=” to sockets. These are just visual indicators for you, not part of the filenames! 

> `-i`<sup>Prepend the inode numbers of the files.</sup> 

> `-s`<sup>Prepend the size of the file in blocks, useful for sorting files by their size:</sup> `$ ls -s | sort -n` 

> `-R`<sup>If listing a directory, list its contents recursively.</sup> 

> `-d`<sup>If listing a directory, do not list its contents, just the directory itself.</sup> 

#### **Name** 

cp — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
cp [options] files (file | directory)
```

The `cp` command normally copies a file:

```
$ cp file file2
```

or copies multiple files into a directory:

```
$ cp file1 file2 file3 file4 destination_directory
```

Using the `-a` option, you can also recursively copy directories.

#### **Useful options** 

> `-p`<sup>Copy not only the file contents, but also the file’s permissions, timestamps and, if you have</sup> sufficient permission to do so, its owner and group. (Normally the copies will be owned by you, timestamped now, with permissions set by applying your umask to the original permissions.) 

> `-a`<sup>Copy a directory hierarchy recursively, preserving all file attributes and links.</sup> 

> `-r`<sup>Copy a directory hierarchy recursively. This option does not preserve the files’ attributes such as</sup> permissions and timestamps. It does preserve symbolic links. 

> `-i`<sup>Interactive mode. Ask before overwriting destination files.</sup> 

> `-f`<sup>Force the copy. If a destination file exists, overwrite it unconditionally.</sup> 

#### **Name** 

mv — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
mv [options] source target
```

The `mv` (move) command can rename a file:

```
$ mv file1 file2
```

or move files and directories into a destination directory:

```
$ mv file1 file2 dir3 dir4 destination_directory
```

#### **Useful options** 

> `-i`<sup>Interactive mode. Ask before overwriting destination files.</sup> 

> `-f`<sup>Force the move. If a destination file exists, overwrite it</sup> unconditionally. 

#### **Name** 

rm — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
rm [options] files | directories
```

The `rm` (remove) command can delete files:

```
$ rm file1 file2 file3
```

or recursively delete directories:

```
$ rm -r dir1 dir2
```

#### **Useful options** 

> `-i`<sup>Interactive mode. Ask before deleting each file.</sup> 

> `-f`<sup>Force the deletion, ignoring any errors or warnings.</sup> 

> `-r`<sup>Recursively remove a directory and its contents. Use with caution, especially if combined with</sup> the `-f` option, as it can wipe out all your files. 

#### **Name** 

ln — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
ln [options] source target
```

A _link_ is a reference to another file, created by the `ln` command. Intuitively, links give the same file multiple names, allowing it to live in two (or more) locations at once.

There are two kinds of links. A _symbolic link_ (also called a _symlink_ or _soft link_ ) refers to another file by its path, much like a Windows “shortcut” or a Macintosh “alias.” To create a symbolic link, use the `-s` option:

```
$ ln -s myfile mysoftlink
```

If you delete the original file, the now-dangling link will be invalid, pointing to a nonexistent file path. A _hard link_ , on the other hand, is simply a _second name_ for a physical file on disk (in tech talk, it points to the same _inode_ ). If you delete the original file, the link still works. <u>Figure 1-5</u> illustrates the difference. To create a hard link, type:

- `$ ln myfile myhardlink` 

_Figure 1-5. Hard link versus symbolic link_

Symbolic links can point to files on other disk partitions, since they are just references to file paths; hard links cannot, since an inode on one disk has no meaning on another. Symbolic links can also point to directories, whereas hard links cannot...unless you are the superuser and use the `-d` option.

#### **Useful options** 

> `-s`<sup>Make a symbolic link. The default is a hard link.</sup> 

> `-i`<sup>Interactive mode. Ask before overwriting destination files.</sup> 

> `-f`<sup>Force the link. If a destination file exists, overwrite it</sup> unconditionally. 

> `-d`<sup>Create a hard link to a directory (superusers only).</sup> 

It’s easy to find out where a symbolic link points with either of these commands:

- `$ readlink` _`linkname`_ 

- `$ ls -l` _`linkname`_ 

## **Directory Operations** 

|`cd`|Change your current directory.|
|---|---|
|`pwd`|Print the name of your current directory, i.e., “where you are now” in the<br>filesystem.|
|`basena`<br>`me`|Print the final part of a file path.|
|`dirnam`<br>`e`|Print a file path without its final part.|
|`mkdir`|Create (make) a directory.|
|`rmdir`|Delete (remove) an empty directory.|
|`rm -r`|Delete a nonempty directory and its contents.|

We discussed the directory structure of Linux in <u>The Filesystem. Now we’ll</u> cover commands that create, modify, delete, and manipulate directories within that structure.

#### **Name** 

cd — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
cd [directory]
```

The `cd` (change directory) command sets your current working directory:

```
$ cd /usr/games
```

With no directory supplied, `cd` defaults to your home directory:

```
$ cd
```

#### **Name** 

pwd — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
pwd
```

The `pwd` command prints the absolute path of your current working directory:

```
$ pwd
```

```
/users/smith/mydir
```

#### **Name** 

basename — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
basename path [suffix]
```

The `basename` command prints the final component in a file path:

```
$ basename /users/smith/finances/money.txt
money.txt
```

If you provide an optional suffix, it gets stripped from the result:

```
$ basename /users/smith/finances/money.txt .txt
```

```
money
```

#### **Name** 

dirname — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
dirname path
```

The `dirname` command prints a file path with its final component removed:

```
$ dirname /users/smith/mydir
```

```
/users/smith
```

`dirname` does not change your current working directory. It simply manipulates a string, just like `basename` does.

#### **Name** 

mkdir — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
mkdir [options] directories
```

###### `mkdir` creates one or more directories: 

```
$ mkdir directory1 directory2 directory3
```

#### **Useful options** 

- `-p` Given a directory path (not just a simple directory name), create any necessary parent directories automatically: `mkdir -p /one/two/three` creates _/one_ and _/one/two_ if they don’t already exist, then _/one/two/three_ . 

- `-m` Create the directory with the given permissions: _`mo de`_ `$ mkdir -m 0755 mydir` 

By default, your shell’s umask controls the permissions. See the `chmod` command in <u>File Properties, and File Protections.</u>

#### **Name** 

rmdir — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
rmdir [options] directories
```

The `rmdir` (remove directory) command deletes one or more empty directories you name:

```
$ rmdir /tmp/junk
```

#### **Useful options** 

> `-p`<sup>If you supply a directory path (not just a simple directory name), delete not only the given</sup> directory, but the specified parent directories automatically, all of which must be empty. So `rmdir - p /one/two/three` will delete not only _/one/two/three_ , but also _/one/two_ and _/one_ . 

To delete a nonempty directory and its contents, use (carefully) `rm -r` _`directory`_ . Use `rm -ri` to delete interactively, or `rm -rf` to annihilate without any error messages or confirmation.

## **File Viewing** 

|`cat`|View files in their entirety.|
|---|---|
|`less`|View text files one page at a time.|
|`head`|View the first lines of a text file.|
|`tail`|View the last lines of a text file.|
|`nl`|View text files with their lines numbered.|
|`string`<br>`s`|Display text that’s embedded in a binary<br>file.|
|`od`|View data in octal (or other formats).|
|`xxd`|View data in hexadecimal.|
|`acrore`<br>`ad`|View PDF files.|
|`gv`|View PostScript or PDF files.|
|`xdvi`|View TeX DVI files.|

In Linux, you’ll encounter various types of files to view: plain text, PostScript, binary data, and more. Here we’ll explain how to view them. Note that commands for viewing graphics files are covered in <u>Graphics and Screensavers, and video files in Video.</u>

#### **Name** 

cat — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
cat [options] [files]
```

The simplest viewer is `cat` , which just prints its files to standard output, concatenating them (hence the name). Large files will likely scroll off screen, so consider using `less` if you plan to read the output. That being said, `cat` is particularly useful for sending a set of files into a shell pipeline:

```
$ cat * | wc
```

`cat` can also manipulate its output in small ways, optionally displaying nonprinting characters, prepending line numbers (though `nl` is more powerful for this purpose), and eliminating whitespace.

#### **Useful options** 

|`-`<br>`T`|<sup>Print tabs as ^I.</sup>|
|---|---|
|`-`<br>`E`|<sup>Print newlines as $.</sup>|
|`-`<br>`v`|<sup>Print other nonprinting characters in a human-readable</sup><br>format.|
|`-`<br>`n`|<sup>Prepend line numbers to every line.</sup>|
|`-`<br>`b`|<sup>Prepend line numbers to nonblank lines.</sup>|
|`-`<br>`s`|<sup>Squeeze each sequence of blank lines into a single blank</sup><br>line.|

#### **Name** 

less — stdin  stdout<sup>[</sup> <u>8</u><sup>]</sup> - file  -- opt  --help  --version

#### **Synopsis** 

```
less [options] [files]
```

Use `less` to view text one “page” at a time (i.e., one window or screenful at a time). It’s great for text files, or as the final command in a shell pipeline with lengthy output.

```
$ command1 | command2 | command3 | command4 | less
```

While running `less` , type `h` for a help message describing all its features. Here are some useful keystrokes for paging through files.

|Keystrok<br>e|Meaning|
|---|---|
|`h, H`|View a help page.|
|Space<br>bar,`f`,`^V`,<br>`^F`|Move forward one screenful.|
|Enter|Move forward one line.|
|`b`,`^B`,<br>ESC-v|Move backward one screenful.|
|`/`|Enter search mode. Follow it with a regular expression and press Enter, and`less`will<br>look for the first line matching it.|
|`?`|Same as /, but it searches backward in the file.|
|`n`|Repeat your most recent search forward.|
|N|Repeat your most recent search backward.|
|v|Edit the current file with your default text editor (the value of environment variable<br>`VISUAL`, or if not defined,`EDITOR`, or if not defined,`vi`).|
|<|Jump to beginning of file.|
|>|Jump to end of file.|

|Keystrok<br>e|Meaning|
|---|---|
|:n|Jump to next file.|
|:p|Jump to previous file.|

`less` has a mind-boggling number of features; we’re presenting only the most common. (For instance, `less` will display the contents of a compressed Zip file: try `less myfile.zip` .) The manpage is recommended reading.

#### **Useful options** 

> `-c`<sup>Clear the screen before displaying the next page. This avoids scrolling and may be more</sup> comfortable on the eyes. 

> `-m`<sup>Print a more verbose prompt, displaying the percentage of the file displayed so far.</sup> 

> `-N`<sup>Display line numbers.</sup> 

> `-r`<sup>Display control characters literally; normally</sup><sup>`less`converts them to a human-readable format.</sup> 

> `-s`<sup>Squeeze multiple, adjacent blank lines into a single blank line.</sup> 

> `-S`<sup>Truncate long lines to the width of the screen, instead of wrapping.</sup> 

[8<sup>]</sup> Although technically `less` can be plugged into the middle of a pipeline, or its output redirected to a file, there isn’t much point to doing this.

#### **Name** 

head — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
head [options] [files]
```

The `head` command prints the first 10 lines of a file: great for previewing the contents.

- `$ head myfile` 

```
$ head * | less            Preview all files in the current directory
```

It’s also good for previewing the first few lines of output from a pipeline:

```
$ grep 'E' very-big-file | head
```

#### **Useful options** 

- Print the first _`N`_ lines instead of 10. 

- _`N`_ 

- Print the first _`N`_ lines instead of 10. 

- `n` _`N`_ 

`-` Print the first _`N`_ bytes of the file. `c` _`N`_

> `-q`<sup>Quiet mode: when processing more than one file, don’t print a banner above each file. Normally,</sup> `head` prints a banner containing the filename. 

#### **Name** 

tail — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
tail [options] [files]
```

The `tail` command prints the last 10 lines of a file, and does other tricks as well.

```
$ tail myfile
```

The ultra-useful `-f` option causes `tail` to watch a file actively while another program is writing to it, displaying new lines as they are written to the file. This is invaluable for watching log files in active use:

```
$ tail -f /var/log/messages
```

#### **Useful options** 

|_`-`_<br>_`N`_ <sup>Print the last</sup><sup>_`N`_ lines of the file instead of 10.</sup>|
|---|
|`-`<br>`n`<br>_`N`_<br>Print the last_`N`_lines of the file instead of 10.|
|`-`<br>`n`<br>`+`<br>_`N`_<br>Print all lines except the first_`N`_.|
|`-`<br>`c`<br>_`N`_<br>Print the last_`N`_bytes of the file.|
|`-`<br>`f` <sup>Keep the file open, and whenever lines are appended to the file, print them. This is extremely</sup><br>useful. Add the`--retry`option if the file doesn’t exist yet, but you want to wait for it to exist.|
|`-`<br>`q` <sup>Quiet mode: when processing more than one file, don’t print a banner above each file. Normally</sup><br>`tail`prints a banner containing the filename.|

#### **Name** 

nl — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
nl [options] [files]
```

`nl` copies its files to standard output, prepending line numbers.

- `$ nl myfile` 

- `1  Once upon a time, there was` 

- `2  a little operating system named` 

- `3  Linux, which everybody loved.` 

It’s more flexible than `cat` with its `-n` and `-b` options, providing an almost bizarre amount of control over the numbering. `nl` can be used in two ways: on ordinary text files, and on specially marked-up text files with predefined headers and footers.

#### **Useful options** 

|`-b`<br>`[a|t|n|`<br>`p` _`R`_ `]`|Prepend numbers to all lines (`a`), nonblank lines (`t`), no lines (`n`), or only lines that contain<br>regular expression_`R`_. (Default=`a`)|
|---|---|
|`-v` _`N`_|Begin numbering with integer_`N`_. (Default=1)|
|`-i` _`N`_|Increment the number by_`N`_for each line, so for example, you could use odd numbers only<br>(`-i2`) or even numbers only (`-v2 -i2`). (Default=1)|
|`-n`<br>`[ln|rn|`<br>`rz]`|Format numbers as left-justified (`ln`), right-justified (`rn`), or right-justified with leading<br>zeroes (`rz`). (Default=`ln`)|
|`-w` _`N`_|Force the width of the number to be_`N`_columns. (Default=6)|
|`-s` _`S`_|Insert string_`S`_between the line number and the text. (Default=`TAB`)|

Additionally, `nl` has the wacky ability to divide text files into virtual pages, each with a header, body, and footer with different numbering schemes. For this to work, however, you must insert `nl` -specific delimiter strings into the file, such as `\:\:\:` (start of header), `\:\:` (start of body), and `\:` (start of footer). Each must appear on a line by itself. Then you can use additional

options (see the manpage) to affect line numbering in the headers and footers of your decorated file.

#### **Name** 

strings — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
strings [options] [files]
```

Binary files, such as executable programs and object files, usually contain some readable text. The `strings` program extracts that text and displays it on standard output. You can discover version information, authors’ names, and other useful tidbits with `strings` .

```
$ strings /usr/bin/who
David MacKenzie
Copyright %s %d Free Software Foundation, Inc.
Report %s bugs to %s
```

Combine `strings` and `grep` to make your exploring more efficient. Here we look for email addresses:

```
$ strings /usr/bin/who | grep '@'
bug-coreutils@gnu.org
```

#### **Useful options** 

`-n` Display only strings with length greater than _`length`_ (the default is _`length`_ 4).

#### **Name** 

od — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
od [options] [files]
```

When you want to view a binary file, consider `od` (Octal Dump) for the job. It copies one or more files to standard output, displaying their data in ASCII, octal, decimal, hexadecimal, or floating point, in various sizes (byte, short, long). For example, this command:

```
$ od -w8 /usr/bin/who
0000000 042577 043114 000401 000001
0000010 000000 000000 000000 000000
0000020 000002 000003 000001 000000
...
```

displays the bytes in binary file _/usr/bin/who_ in octal, eight bytes per line. The column on the left contains the file offset of each row, again in octal. If your binary file also contains text, consider the `-tc` option, which displays character data. For example, binary executables like `who` contain the string “ELF” at the beginning:

```
$ od -tc -w8 /usr/bin/who | head -3
0000000 177   E   L   F 001 001 001  \0
0000010  \0  \0  \0  \0  \0  \0  \0  \0
0000020 002  \0 003  \0 001  \0  \0  \0
```

#### **Useful options** 

- `-N` _`B`_ Display only the first _`B`_ bytes of each file, specified in decimal, hexadecimal (by prepending 0x or 0X), 512-byte blocks (by appending `b` ), kilobytes (by appending `k` ), or megabytes (by appending `m` ). (Default displays the entire file.) 

`-j` _`B`_ Begin the output at byte _`B`_ +1 of each file; acceptable formats are the same as for the `-N` option. (Default=0)

- `-w [` _`B`_ `]` Display _`B`_ bytes per line; acceptable formats are the same as in the `-N` option. Using `-w` by itself is equivalent to `-w32` . (Default=16) 

- `-s [` _`B`_ `]` Group each row of bytes into sequences of _`B`_ bytes, separated by whitespace; acceptable 

||formats are the same as in the`-N`option. Using`-s`by itself is equivalent to`-s3`.<br>(Default=2)|
|---|---|
|`-A`<br>`(d|o|x|`<br>`n)`|Display file offsets in the leftmost column, in decimal (`d`), octal (`o`), hexadecimal (`h`), or<br>not at all (`n`). (Default=`o`)|
|`-t`<br>`(a|c)`<br>`[z]`|Display output in a character format, with nonalphanumeric characters printed as escape<br>sequences (`c`) or by name (`a`). For`z`, see below.|
|`-t`<br>`(d|o|u|`<br>`x)`<br>`[SIZE[z`<br>`]]`|Display output in an integer format, including octal (`o`), signed decimal (`d`), unsigned<br>decimal (`u`), hexadecimal (`x`). (For binary output, use`xxd`instead.)_`SIZE`_represents the<br>number of bytes per integer; it can be a positive integer or any of the values C, S, I, or L,<br>which stand for the size of a char, short, int, or long datatype, respectively. For`z`, see<br>below.|
|`-t`<br>`f[SIZE[`<br>`z]]`|Display output in floating point._`SIZE`_represents the number of bytes per integer; it can be<br>a positive integer or any of the values F, D, or L, which stand for the size of a float,<br>double, or long double datatype, respectively. For`z`, see below. If`-t`is omitted, the<br>default is`-to2`.|

Appending `z` to the `-t` option prints a new column on the right-hand side of the output, displaying the printable characters on each line, much like the default output of `xxd` .

#### **Name** 

xxd — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
xxd [options] [files]
```

Similar to `od` , `xxd` produces a hexadecimal or binary dump of a file in several different formats. It can also do the reverse, converting from its hex dump format back into the original data. For example, here’s a hex dump of binary file _/usr/bin/who_ :

```
$ xxd /usr/bin/who
0000000: 7f45 4c46 0101 0100 0000 ... 0000 .ELF............
0000010: 0200 0300 0100 0000 a08c ... 0000 ............4...
0000020: 6824 0000 0000 0000 3400 ... 2800 h$......4. ...(.
0000030: 1900 1800 0600 0000 3400 ... 0408 ........4...4...
...
```

The left column indicates the file offset of the row, the next eight columns contain the data, and the final column displays the printable characters in the row, if any.

By default, `xxd` outputs three columns: file offsets, the data in hex, and the data as text (printable characters only).

#### **Useful options** 

- Display only the first _`N`_ bytes. (Default displays the entire file,) 

- `l` _`N`_ 

- Skip the first _`N`_ bytes of the file. 

- `s` _`N`_ 

- Begin _`N`_ bytes from the end of the file. (There is also a _`+N`_ syntax for more advanced skipping 

- `s` through standard input; see the manpage.) `-` _`N`_ 

- Display _`N`_ bytes per row. (Default=16) 

- `c` 

_`N`_ `-` Group each row of bytes into sequences of _`N`_ bytes, separated by whitespace, like `od -s` . `g` (Default=2) _`N`_ `-b`<sup>Display the output in binary instead of hexadecimal.</sup> `-u`<sup>Display the output in uppercase hexadecimal instead of lowercase.</sup> `-p`<sup>Display the output as a plain hexdump, 60 contiguous bytes per line.</sup> `-r`<sup>The reverse operation: convert from an</sup><sup>`xxd`hex dump back into the original file format. Works</sup> with the default hexdump format and, if you add the `-p` option, the plain hexdump format. If you’re bored, try either of these commands to convert and unconvert a file in a pipeline, reproducing the original file on standard output: `$ xxd myfile | xxd -r $ xxd -p myfile | xxd -r -p`

> `-i`<sup>Display the output as a C programming language data structure. When reading from a file, it</sup> produces an array of unsigned chars containing the data, and an unsigned int containing the array length. When reading from standard input, it produces only a comma-separated list of hex bytes. 

#### **Name** 

acroread — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
acroread [options] file.pdf
```

`acroread` is the official PDF reader from Adobe. It’s easy to use and similar to Adobe Reader on Windows. You can also view PDF files with `xpdf` <u>(http://www.foolabs.com/xpdf/) and</u> `gv` .

#### **Name** 

gv — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
gv [options] file
```

GhostView displays an Adobe PostScript or PDF file in an X window. You can invoke it as `gv` or `ghostview` . Its basic operation is simple: click the desired page number to jump to that page, and so forth. A few minutes of playing around and you’ll have the hang of it.

#### **Useful options** 

|`-page` _`P`_|Begin on page_P_. (Default=1)|
|---|---|
|`-`<br>`monochro`<br>`me`|Display in black and white.|
|`-`<br>`grayscal`<br>`e`|Display in grayscale.|
|`-color`|Display in color.|
|`-`<br>`portrait`|Choose portrait orientation.|
|`-`<br>`landscap`<br>`e`|Choose landscape orientation.|
|`-`<br>`seascape`|Choose upside-down landscape orientation.|
|`-`<br>`upsidedo`<br>`wn`|Choose upside-down portrait orientation.|
|`-scale` _`N`_|Zoom in or out. The integer_`N`_may be positive (make the image larger) or negative<br>(smaller).|
|`-watch`|Automatically reload the PostScript file when it changes.|
|`-nowatch`|Do not automatically reload the PostScript file when it changes.|

#### **Name** 

xdvi — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
xdvi [options] file
```

The document processing system TeX produces binary output files in a format called DVI, with suffix _.dvi_ . The viewer `xdvi` displays a DVI file in an X window. While displaying a file, `xdvi` has a column of buttons down the right-hand side with obvious uses, such as Next to move to the next page. (You can hide the buttons by invoking `xdvi` with the `-expert` option.) You can also navigate the file by keystroke.

|Keystroke|Meaning|
|---|---|
|`q`|Quit.|
|`n`|Jump to next page. (Alternatively, press Space bar, Enter, or Pagedown.) Precede it<br>with a number_`N`_to jump by_`N`_pages.|
|`p`|Jump to previous page. (Alternatively, press Backspace, Delete, or Pageup.) Precede<br>it with a number_`N`_to jump by_`N`_pages.|
|`<`|Jump to first page.|
|`>`|Jump to last page.|
|`^L`|Redisplay the page.|
|`R`|Reread the DVI file, say, after you’ve modified it.|
|Any<br>mouse<br>button|Magnify a rectangular region under the mouse cursor.|

`xdvi` has dozens of command-line options for tailoring its colors, geometry, zoom, and overall behavior.

If you prefer, convert a DVI file to PostScript via the `dvips` command and then use GhostView ( `gv` ) to display it:

> `$ dvips -o myfile.ps myfile.dvi` 

> `$ gv myfile.ps` 

## **File Creation and Editing** 

|Comma<br>nd|Meaning|
|---|---|
|`emacs`|Text editor from Free Software Foundation.|
|`vim`|Text editor, extension of Unix`vi`.|
|`soffice`|Office suite for editing Microsoft Word, Excel, and PowerPoint<br>documents.|
|`abiword`|Edit Microsoft Word documents.|
|`gnumeric`|Edit Excel spreadsheets.|

To get far with Linux, you must become proficient with one of its text editors. The two major ones are emacs from the Free Software Foundation, and vim, a successor to the Unix editor vi. Teaching these editors fully is beyond the scope of this book, but both have online tutorials, and we list common operations in <u>Table 1-1. To edit a file, run either:</u>

- `$ emacs myfile` 

- `$ vim myfile` 

If _myfile_ doesn’t exist, it is created automatically.

In case you share files with Microsoft Windows systems, we will also cover Linux programs that edit Microsoft Word, Excel, and PowerPoint documents.

#### **Creating a File Quickly** 

You can quickly create an empty file (for later editing) using the `touch` command:

```
$ touch newfile
```

or the `echo -n` command (see <u>File Properties):</u><sup>[</sup> <u>9</u><sup>]</sup>

```
$ echo -n > newfile2
```

or write data into a new file by redirecting the output of a program (see <u>Input/output redirection):</u>

- `$ echo anything at all > newfile` 

[9<sup>]</sup> The `-n` option prevents a newline character from being written to the file, making it truly empty.

#### **Your Default Editor** 

Various Linux programs will run an editor when necessary, and by default the editor is vim. For example, your email program may invoke an editor to compose a new message, and `less` invokes an editor if you type “v”. But what if you don’t want vim to be your default editor? Set the environment variables `VISUAL` and `EDITOR` to your choice, for example:

- `$ EDITOR=emacs` 

- `$ VISUAL=emacs` 

```
$ export EDITOR VISUAL                Optional
```

Both variables are necessary because different programs check one variable or the other. Set `EDITOR` and `VISUAL` in your _~/.bash_profile_ startup file if you want your choices made permanent. Any program can be made your default editor as long as it accepts a filename as an argument.

Regardless of how you set these variables, all system administrators should know at least basic vim and emacs commands in case a system tool suddenly runs an editor on a critical file.

#### **Name** 

emacs — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
emacs [options] [files]
```

emacs is an extremely powerful editing environment with more commands than you could possibly imagine, plus a complete programming language to define your own editing features. To invoke emacs in a new X window, run:

```
$ emacs
```

To run in a existing shell window:

```
$ emacs -nw
```

Now to invoke the built-in emacs tutorial, type `^h t` . Most emacs keystroke commands involve the control key (like `^F` ) or the _meta_ key, which is usually the Escape key or the Alt key. emacs’s own documentation notates the meta key as `M-` (as in `M-F` to mean “hold the meta key and type F”), so we will too. For basic keystrokes, see <u>Table 1-1.</u>

#### **Name** 

vim — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
vim [options] [files]
```

vim is an enhanced version of the old standard Unix editor vi. To invoke the editor in a new X window, run:

```
$ gvim
```

To run in a existing shell window:

```
$ vim
```

To run the vim tutorial, run:

```
$ vimtutor
```

vim is a mode-based editor. It operates in two modes, _insert_ and _normal_ . Insert mode is for entering text in the usual manner, while normal mode is for running commands like “delete a line” or copy/paste. For basic keystrokes in normal mode, see <u>Table 1-1.</u>

_Table 1-1. Basic keystrokes in emacs and vim_

|Task|emacs|vim|
|---|---|---|
|Type text|Just type|Type`i`, then<br>any text, and<br>finally`ESC`|
|Save and quit|`^x^s`then`^x^c`|`:wq`|
|Quit without saving|`^x^c`<br>Respond “no”<br>when asked to<br>save buffers|`:q!`|
|Save|`^x^s`|`:w`|

|Task|emacs|vim|
|---|---|---|
|Save As|`^x^w`|`:w` _`filename`_|
|Undo|`^/ or ^x u`|`u`|
|Suspend editor (not in X)|`^z`|`^z`|
|Switch to edit mode|(_N/A_)|`ESC`|
|Switch to command mode|`M-x`|:|
|Abort command in progress|`^g`|`ESC`|
|Move forward|`^f`or right arrow|`l`or right arrow|
|Move backward|`^b`or left arrow|`h`or left arrow|
|Move up|`^p`or up arrow|`k`or up arrow|
|Move down|`^n`or down arrow|`j`or down<br>arrow|
|Move to next word|`M-f`|`w`|
|Move to previous word|`M-b`|`b`|
|Move to beginning of line|`^a`|`0`|
|Move to end of line|`^e`|`$`|
|Move down one screen|`^v`|`^f`|
|Move up one screen|`M-v`|`^b`|
|Move to beginning of buffer|`M-<`|`gg`|
|Move to end of buffer|`M->`|`G`|
|Delete next character|^d|`x`|
|Delete previous character|`BACKSPACE`|`X`|
|Delete next word|`M-d`|`de`|
|Delete previous word|`M-BACKSPACE`|`db`|
|Delete current line|`^a^k`|`dd`|
|Delete to end of line|`^k`|`d$`|

|Task|emacs|vim|
|---|---|---|
|Define region (type this keystroke to mark the beginning of<br>the region, then move the cursor to the end of the desired<br>region)|`^`Space bar|`v`|
|Cut region|`^w`|`d`|
|Copy region|`M-w`|`y`|
|Paste region|`^y`|`p`|
|Get help|`^h`|`:help`|
|View the manual|`^h i`|`:help`|

#### **Name** 

soffice — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
soffice [files]
```

OpenOffice.org<sup>[</sup> <u>10</u><sup>]</sup> is a comprehensive, integrated office software suite that can edit Microsoft Word, Excel, and PowerPoint files. Simply run:

```
$ soffice
```

and you’re ready to work. The same program edits all three types of files. [11<sup>]</sup> It is a large program that requires plenty of memory and disk space. OpenOffice.org can also handle drawings ( `oodraw` command), databases ( `oobase` ), and mathematical formulas ( `oomath` ). <u>OpenOffice.org</u> has more information, or you can use the `soffice` Help menu.

Some distros supply a different package, LibreOffice, a spin-off of OpenOffice.org with the same commands. See <u>http://www.libreoffice.org/</u> for details.

[10<sup>]</sup> The “.org” is part of the software package’s name.

[11<sup>]</sup> Under the hood, `soffice` comprises the separate programs Writer ( `oowriter` command) for word processing, Calc ( `oocalc` ) for spreadsheets, and Impress ( `ooimpress` ) for presentations, which you can run directly if desired.

#### **Name** 

abiword — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
abiword [options] [files]
```

`abiword` is another program for editing Microsoft Word documents. It is smaller and quicker than `soffice` , though not as powerful, and perfectly suitable for many editing tasks.

```
$ abiword myfile.doc
```

If you specify files on the command line, they must exist: `abiword` won’t create them for you.

#### **Name** 

gnumeric — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
gnumeric [options] [files]
```

`gnumeric` is a spreadsheet program that can edit Microsoft Excel documents. It is quite powerful and fast, and if you’ve used Excel before, `gnumeric` will feel familiar.

- `$ gnumeric myfile.xls` 

If you specify files on the command line, they must exist: `gnumeric` won’t create them for you.

## **File Properties** 

|`stat`|Display attributes of files and directories.|
|---|---|
|`wc`|Count bytes, words, lines in a file.|
|`du`|Measure disk usage of files and directories.|
|`file`|Identify (guess) the type of a file.|
|`touc`<br>`h`|Change timestamps of files and directories.|
|`chow`<br>`n`|Change owner of files and directories.|
|`chgr`<br>`p`|Change group ownership of files and directories.|
|`chmo`<br>`d`|Change protection mode of files and directories.|
|`umas`<br>`k`|Set a default mode for new files and directories.|
|`chat`<br>`tr`|Change extended attributes of files and<br>directories.|
|`lsat`<br>`tr`|List extended attributes of files and directories.|

When examining a Linux file, keep in mind that the contents are only half the story. Every file and directory also has attributes that describe its owner, size, access permissions, and other information. The `ls -l` command (see <u>Basic File Operations) displays some of these attributes, but other</u> commands provide additional information.

#### **Name** 

stat — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
stat [options] files
```

The `stat` command lists important attributes of files (by default) or filesystems ( `-f` option). File information looks like:

```
$ stat myfile
  File: "myfile"
  Size: 1264       Blocks: 8         Regular File
Access: (0644/-rw-r--r--) Uid: (600/lisa) Gid: (620/users)
Device: 30a        Inode: 99492      Links: 1
Access: Fri Aug 29 00:16:12 2003
Modify: Wed Jul 23 23:09:41 2003
Change: Wed Jul 23 23:11:48 2003
```

and includes the filename, size in bytes (1264), size in blocks (8), file type (Regular File), permissions in octal (0644), permissions in the format of “ls -l” (-rw-r--r--), owner’s user ID (600), owner’s name (lisa), owner’s group ID (620), owner’s group name (users), device type (30a), inode number (99492), number of hard links (1), and timestamps of the file’s most recent access, modification, and status change. Filesystem information looks like:

```
$ stat -f myfile
  File: "myfile"
    ID: bffff358 ffffffff Namelen: 255     Type: EXT2
Blocks: Total: 2016068    Free: 876122     Available:
773709     Size: 4096
Inodes: Total: 1026144    Free: 912372
```

and includes the filename ( _myfile_ ), filesystem ID (bffff358 ffffffff), maximum length of a filename for that filesystem (255 bytes), filesystem type (EXT2), the counts of total, free, and available blocks in the filesystem (2016068, 876122, and 773709, respectively), block size for the filesystem (4096), and the counts of total and free inodes (1026144 and 912372, respectively).

The `-t` option presents the same data but on a single line, without headings. This is handy for processing by shell scripts or other programs:

```
$ stat -t myfile
myfile 1264 8 81a4 500 500 30a 99492 1 44 1e 1062130572
  1059016181 1059016308
$ stat -tf myfile
myfile bffff358 ffffffff 255 ef53 2016068 875984 773571
  4096 1026144 912372
```

#### **Useful options** 

> `-L`<sup>Follow symbolic links and report on the file they point to.</sup> 

> `-f`<sup>Report on the filesystem containing the file, not the file</sup> itself. 

> `-t`<sup>Terse mode: print information on a single line.</sup> 

#### **Name** 

wc — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
wc [options] [files]
```

The `wc` (word count) program prints a count of bytes, words, and lines in (presumably) a text file.

```
$ wc myfile
   24      62     428 myfile
```

This file has 24 lines, 62 whitespace-delimited words, and 428 bytes.

#### **Useful options** 

|`-`<br>`l`|<sup>Print the line count only.</sup>|
|---|---|
|`-`<br>`w`|<sup>Print the word count only.</sup>|
|`-`<br>`c`|<sup>Print the byte count only.</sup>|
|`-`<br>`L`|<sup>Locate the longest line in each file and print its length in</sup><br>bytes.|

#### **Name** 

du — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
du [options] [files| directories]
```

The `du` (disk usage) command measures the disk space occupied by files or directories. By default, it measures the current directory and all its subdirectories, printing totals in blocks for each, with a grand total at the bottom.

```
$ du
8    ./Notes
36   ./Mail
340  ./Files/mine
40   ./Files/bob
416  ./Files
216  ./PC
2404 .
```

It can also measure the size of files:

```
$ du myfile myfile2
4    myfile
16   myfile2
```

#### **Useful options** 

> `-b`<sup>Measure usage in bytes.</sup> 

> `-k`<sup>Measure usage in kilobytes.</sup> 

> `-m`<sup>Measure usage in megabytes.</sup> 

`-` Display sizes in blocks that you define, where 1 block = _`N`_ bytes. (Default = 1024) `B` _`N`_

> `-h` Print in human-readable units. For example, if two directories are of size 1 gigabyte or 25 `-` kilobytes, respectively, `du -h` prints 1G and 25K. The `-h` option uses powers of 1024, whereas `-H` 

> `H` uses powers of 1000. 

- Print a total in the last line. This is the default behavior when measuring a directory, but for 

> `c` measuring individual files, provide `-c` if you want a total. 

> `-L`<sup>Follow symbolic links and measure the files they point to.</sup> 

> `-s`<sup>Print only the total size.</sup> 

#### **Name** 

file — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
file [options] files
```

The `file` command reports the type of a file:

```
$ file /etc/hosts /usr/bin/who letter.doc
/etc/hosts:    ASCII text
/usr/bin/who:  ELF 32-bit LSB executable, Intel 80386 ...
letter.doc:    Microsoft Office Document
```

Unlike some other operating systems, Linux does not keep track of file types, so the output is an educated guess based on the file content and other factors.

#### **Useful options** 

|`-b`|Omit filenames (left column of output).|
|---|---|
|`-i`|Print MIME types for the file, such as “text/plain” or “audio/mpeg”, instead of the usual<br>output.|
|`-f`<br>_`name_fi`_<br>_`le`_|Read filenames, one per line, from the given_`name_file`_, and report their types. Afterward,<br>process filenames on the command line as usual.|
|`-L`|Follow symbolic links, reporting the type of the destination file instead of the link.|
|`-z`|If a file is compressed (see<br>File Compression and Packaging), examine the uncompressed<br>contents to decide the file type, instead of reporting “compressed data.”|

#### **Name** 

touch — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
touch [options] files
```

The `touch` command changes two timestamps associated with a file: its modification time (when the file’s data was last changed) and its access time (when the file was last read). To set both timestamps to right now, run:

```
$ touch myfile
```

You can set these timestamps to arbitrary values, e.g.:

```
$ touch -d "November 18 1975" myfile
```

If a given file doesn’t exist, `touch` creates it, a handy way to create empty files.

#### **Useful options** 

|`-a`|Change the access time only.|
|---|---|
|`-m`|Change the modification time only.|
|`-c`|If the file doesn’t exist, don’t create it (normally,`touch`creates it).|
|`-d`<br>_`timesta`_<br>_`mp`_|Set the file’s timestamp(s). A tremendous number of timestamp formats are acceptable,<br>from “12/28/2001 3pm” to “28-May” (the current year is assumed, and a time of<br>midnight) to “next tuesday 13:59” to “0” (midnight today). Experiment and check your<br>work with`stat`. Full documentation is available from`info touch`.|
|`-t`<br>_`timesta`_<br>_`mp`_|A less intelligent way to set the file’s_`timestamp`_, using the format [[_`CC`_]_`YY`_]_`MMDDhhmm`_[._`ss`_],<br>where_`CC`_is the two-digit century,_`YY`_is the two-digit year,_`MM`_is the 2-digit month,_`DD`_is the<br>two-digit day,_`hh`_is the two-digit hour,_`mm`_is the two-digit minute, and_`ss`_is the two-digit<br>second. For example,`-t 20030812150047`represents August 12, 2003, at 15:00:47.|

#### **Name** 

chown — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
chown [options] user_spec files
```

The `chown` (change owner) command sets the ownership of files and directories. To make user `smith` the owner of several files and a directory, run:

```
# chown smith myfile myfile2 mydir
```

The _`user_spec`_ parameter may be any of these possibilities:

- A username (or numeric user ID), to set the owner: `chown smith myfile` 

- A username (or numeric user ID), optionally followed by a colon and a group name (or numeric group ID), to set the owner and group: `chown smith:users myfile` 

- A username (or numeric user ID) followed by a colon, to set the owner _and_ to set the group to the invoking user’s login group: `chown smith: myfile` 

- A group name (or numeric group ID) preceded by a colon, to set the group only: `chown :users myfile` 

- `--reference=` _`file`_ to set the same owner and group as another given file 

#### **Useful options** 

|`--`<br>`dereference`|Follow symbolic links and operate on the files they point to.|
|---|---|
|`-R`|Recursively change the ownership within a directory<br>hierarchy.|

#### **Name** 

chgrp — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
chgrp [options] group_spec files
```

The `chgrp` (change group) command sets the group ownership of files and directories.

- `$ chgrp smith myfile myfile2 mydir` 

The _`group_spec`_ parameter may be any of these possibilities:

- A group name or numeric group ID 

- `--reference=` _`file`_ , to set the same group ownership as another given file 

See <u>Group Management</u> for more information on groups.

#### **Useful options** 

|`--`<br>`dereference`|Follow symbolic links and operate on the files they point to.|
|---|---|
|`-R`|Recursively change the ownership within a directory<br>hierarchy.|

#### **Name** 

chmod — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
chmod [options] permissions files
```

The `chmod` (change mode) command protects files and directories from unauthorized users on the same system, by setting access permissions. Typical permissions are read, write, and execute, and they may be limited to the file owner, the file’s group owner, and/or other users. The permissions argument can take three different forms:

- `--reference=` _`file`_ , to set the same permissions as another given file. An octal number, up to four digits long, that specifies the file’s _absolute_ permissions in bits, as in <u>Figure 1-6. The leftmost digit is special</u> (described later) and the second, third, and fourth represent the file’s owner, the file’s group, and all users. 

- One or more strings specifying _absolute or relative_ permissions (i.e., relative to the file’s existing permissions). For example, `a+r` makes a file readable by all users. 

_Figure 1-6. File permission bits explained_

In the third form, each string consists of three parts: an optional _scope_ , a _command_ , and _permissions_ .

_Scope (optional)_

`u` for user, `g` for group, `o` for other users not in the group, `a` for all users. The default is `a` .

_Command_

`+` to add permissions; `−` to remove permissions; or `=` to set absolute permissions, ignoring existing ones.

###### _Permissions_ 

`r` for read, `w` for write/modify, `x` for execute (for directories, this is permission to `cd` into the directory), `X` for conditional execute (explained later), `u` to duplicate the user permissions, `g` to duplicate the group permissions, `o` to duplicate the “other users” permissions, `s` for setuid or setgid, and `t` for the sticky bit.

For example, `ug+rw` would add read and write permission for the user and the group, `a-x` (or just `-x` ) would remove execute permission for everyone, and `u=r` would first remove all existing permissions and then make the file readable only by its owner. You can combine these strings by separating them with commas, such as `ug+rw,a-x` .

Conditional execute permission ( `X` ) means the same as `x` , except that it succeeds only if the file is already executable, or if the file is a directory. Otherwise, it has no effect.

Setuid and setgid apply to executable files (programs and scripts). Suppose we have an executable file _F_ owned by user “smith” and the group “friends”. If file _F_ has setuid (set user ID) enabled, then anyone who runs _F_ will “become” user smith, with all her rights and privileges, for the duration of the program. Likewise, if _F_ has setgid (set group ID) enabled, anyone who executes _F_ becomes a member of the friends group for the duration of the program. As you might imagine, setuid and setgid can impact system security, so don’t use them unless you _really_ know what you’re doing. One misplaced `chmod +s` can leave your whole system vulnerable to attack.

The sticky bit, most commonly used for _/tmp_ directories, controls removal of files in that directory. Normally, if you have write permission in a directory, you can delete or move files within it, even if you don’t have this

access to the files themselves. Inside a directory with the sticky bit set, you need write permission on a file in order to delete or move it.

#### **Useful options** 

> `-R`<sup>Recursively change the ownership within a directory</sup> hierarchy. 

#### **Name** 

umask — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
umask [options] [mask]
```

The `umask` command sets or displays your default mode for creating files and directories: whether they are readable, writable, and/or executable by yourself, your group, and the world.

```
$ umask
0002
$ umask -S
u=rwx,g=rwx,o=rx
```

Let’s start with some technical talk and follow with common-sense advice. A umask is a binary (base two) value, though it is commonly presented in octal (base eight). It defines your default protection mode by combining with the octal value 0666 for files and 0777 for directories, using the binary operation `NOT AND` . For example, the umask 0002 yields a default file mode of 0664:

```
0666 NOT AND 0002
= 000110110110 NOT AND 000000000010
= 000110110110 AND 111111111101
= 000110110100
= 0664
```

Similarly for directories, `0002 NOT AND 0777` yields a default mode of 0775. If that explanation seems from outer space, here are some simple recipes. Use mask 0022 to give yourself full privileges, and all others read/execute privileges only:

```
$ umask 0022
```

```
$ touch newfile && mkdir dir
$ ls -ld newfile dir
-rw-r--r--    1 smith smith        0 Nov 11 12:25 newfile
drwxr-xr-x    2 smith smith     4096 Nov 11 12:25 dir
```

Use mask 0002 to give yourself and your default group full privileges, and read/execute to others:

```
$ umask 0002
$ touch newfile && mkdir dir
$ ls -ld newfile dir
-rw-rw-r--    1 smith smith        0 Nov 11 12:26 newfile
drwxrwxr-x    2 smith smith     4096 Nov 11 12:26 dir
```

Use mask 0077 to give yourself full privileges with nothing for anyone else:

```
$ umask 0077
$ touch newfile && mkdir dir
$ ls -ld newfile dir
-rw-------    1 smith smith        0 Nov 11 12:27 newfile
drwx------    2 smith smith     4096 Nov 11 12:27 dir
```

#### **Name** 

chattr — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
chattr [options] [+ − =]attributes [files]
```

If you grew up with other Unix systems, you might be surprised that Linux files can have additional attributes beyond their access permissions. If a file is on an “ext” filesystem (ext2, ext3, etc.), you can set these extended attributes with the `chattr` (change attribute) command and list them with `lsattr` .

As with `chmod` , attributes may be added (+) or removed (-) relatively, or set absolutely (=). For example, to keep a file compressed and nondumpable, run:

###### `$ chattr +cd myfile` 

|Attribu<br>te|Meaning|
|---|---|
|`a`|Append-only: appends are permitted to this file, but it cannot otherwise be edited. Root<br>only.|
|`A`|Accesses not timestamped: accesses to this file don’t update its access timestamp (atime).|
|`c`|Compressed: data is transparently compressed on writes and uncompressed on reads.|
|`d`|Don’t dump: tell the`dump`program to ignore this file when making backups (see<br>Backups<br>and Remote Storage).|
|`i`|Immutable: file cannot be changed or deleted (root only).|
|`j`|Journaled data (ext3 filesystems only).|
|`s`|Secure deletion: if deleted, this file’s data is overwritten with zeroes.|
|`S`|Synchronous update: changes are written to disk immediately, as if you had typed`sync`<br>after saving (see<br>Disks and Filesystems).|
|`u`|Undeletable: file cannot be deleted.|

There are a few other attributes too, some of them obscure or experimental. See the manpage for details.

#### **Useful options** 

> `-R`<sup>Recursively process</sup> directories. 

#### **Name** 

lsattr — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
lsattr [options] [files]
```

If you set extended attributes with `chattr` , you can view them with `lsattr` (list attributes). The output uses the same letters as `chattr` ; for example, this file is immutable and undeletable:

```
$ lsattr myfile
```

```
-u--i--- myfile
```

With no files specified, `lsattr` prints the attributes of all files in the current directory.

#### **Useful options** 

<!-- Start of picture text --> -R Recursively process directories.<br>-a List all files, including those whose names begin with a dot.<br>-d If listing a directory, do not list its contents, just the directory<br>itself.<br><!-- End of picture text -->

## **File Location** 

|`find`|Locate files in a directory hierarchy.|
|---|---|
|`xargs`|Process a list of located files (and much more).|
|`locat`<br>`e`|Create an index of files, and search the index for<br>string.|
|`which`|Locate executables in your search path (command).|
|`type`|Locate executables in your search path (bash built-in).|
|`where`<br>`is`|Locate executables, documentation, and source files.|

Linux systems can contain hundreds of thousands of files easily. How can you find a particular file when you need to? The first step is to organize your files logically into directories in some thoughtful manner, but there are several other ways to find files, depending on what you’re looking for.

For finding any file, `find` is a brute-force program that slogs file-by-file through a directory hierarchy to locate a target. `locate` is much faster, searching through a prebuilt index that you generate as needed. (Some distros generate the index nightly by default.)

For finding programs, the `which` and `type` commands check all directories in your shell search path. `type` is built into the bash shell (and therefore available only when you’re running bash), while `which` is a program (normally _/usr/bin/which_ ); `type` is faster and can detect shell aliases.<sup>[</sup> <u>12</u><sup>]</sup> In contrast, `whereis` examines a known set of directories, rather than your search path.

[12<sup>]</sup> The `tcsh` shell performs some trickery to make `which` detect aliases.

#### **Name** 

find — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
find [directories] [expression]
```

The `find` command searches one or more directories (and their subdirectories recursively) for files matching certain criteria. It is very powerful, with over 50 options and, unfortunately, a rather unusual syntax. Here are some simple examples that search the entire filesystem from the root directory:

Find a particular file named _myfile_ :

```
$ find / -type f -name myfile -print
```

Print all directory names:

```
$ find / -type d -print
```

Print filenames ending in “.txt” (notice how the wildcard is escaped so the shell ignores it):

```
$ find / -type f -name \*.txt -print
```

#### **Useful options** 

`-name` The name ( `-name` ), pathname ( `-path` ), or symbolic link target ( `-lname` ) of the desired file _`pattern`_ must match this shell pattern, which may include shell wildcards *, ?, and []. (You must `-path` escape the wildcards, however, so they are ignored by the shell and passed literally to _`pattern`_ `find` .) Paths are relative to the directory tree being searched. `-lname` _`pattern`_ `-iname` The `-iname` , `-ipath` and `-ilname` options are the same as `-name` , `-path` , and `-lname` , respectively, _`pattern`_ but are case-insensitive. `-ipath` _`pattern`_

|`-ilname`<br>_`pattern`_||
|---|---|
|`-regex`<br>_`regexp`_|The path (relative to the directory tree being searched) must match the given regular<br>expression.|
|`-type`_`t`_|Locate only files of type_`t`_. This includes plain files (`f`), directories (`d`), symbolic links (`l`),<br>block devices (`b`), character devices (`c`), named pipes (`p`), and sockets (`s`).|
|`-atime` _`N`_<br>`-ctime` _`N`_<br>`-mtime` _`N`_|File was last accessed (`-atime`), last modified (`-mtime`), or had a status change (`-ctime`)<br>exactly_`N`_*24 hours ago. Use +_`N`_for “greater than_`N`_,” or -_`N`_for “less than_`N`_.”|
|`-amin` _`N`_<br>`-cmin` _`N`_<br>`-mmin` _`N`_|File was last accessed (`-amin`), last modified (`-mmin`), or had a status change (`-cmin`) exactly_`N`_<br>minutes ago. Use +_`N`_for “greater than_`N`_,”or -_`N`_for “less than_`N`_.”|
|`-anewer`<br>_`other_f`_<br>_`ile`_<br>`-cnewer`<br>_`other_f`_<br>_`ile`_<br>`-newer`<br>_`other_f`_<br>_`ile`_|File was accessed (`-anewer`), modified (`-newer`), or had a status change (`-cnewer`) more<br>recently than_`other_file`_has.|
|`-`<br>`maxdept`<br>`h` _`N`_|Consider files at least (`-mindepth`) or at most (`-maxdepth`)_`N`_levels deep in the directory tree<br>being searched.|
|`-`<br>`mindept`<br>`h` _`N`_||
|`-follow`|Dereference symbolic links.|
|`-depth`|Proceed using depth-first search: completely search a directory’s contents (recursively)<br>before operating on the directory itself.|
|`-xdev`|Limit the search to a single filesystem, i.e., don’t cross device boundaries.|
|`-size` _`N`_<br>`[bckw]`|Consider files of size_`N`_, which can be given in blocks (`b`), one-byte characters (`c`),<br>kilobytes (`k`), or two-byte words (`w`). Use +_`N`_for “greater than_`N`_,” or -_`N`_for “less than_`N`_.”|
|`-empty`|File has zero size, and is a regular file or directory.|
|`-user`<br>_`name`_|File is owned by the given user.|
|`-group`|File is owned by the given group.|

```
name
```

`-perm` File has permissions equal to mode. Use `-` _`mode`_ to check that _all_ of the given bits are set, _`mode`_ or + _`mode`_ to check that _any_ of the given bits are set.

You can group and negate parts of the expression with the following operators:

```
expression1-aexpression2
```

And. (This is the default if two expressions appear side by side, so the “- a” is optional.)

```
expression1-oexpression2
```

Or.

```
!expression
```

```
-notexpression
```

Negate the expression.

```
(expression)
```

Precedence markers, just like in algebra class. Evaluate what’s in parentheses first. You may need to escape these from the shell with “\”.

```
expression1,expression2
```

Same as the comma operator in the C programming language. Evaluate both expressions and return the value of the second one.

Once you’ve specified the search criteria, you can tell `find` to perform these actions on files that match the criteria.

#### **Useful options** 

|`-`<br>`prin`<br>`t`|Simply print the path to the file, relative to the search directory.|
|---|---|
|`-`<br>`prin`<br>`tf`<br>_`stri`_<br>_`ng`_|Print the given string, which may have substitutions applied to it in the manner of the C<br>library function,`printf( )`. See the manpage for the full list of outputs.|
|`-`<br>`prin`<br>`t0`|Like`-print`, but instead of separating each line of output with a newline character, use a null<br>(ASCII 0) character. Use when piping the output of`find`to another program, and your list of<br>filenames may contain space characters. Of course, the receiving program must be capable of<br>reading and parsing these null-separated lines — for example,`xargs −0`.|

|`-`<br>`exec`<br>_`cmd`_<br>`;`|Invoke the given shell command,_`cmd`_. Make sure to escape any shell metacharacters,<br>including the required, final semicolon, so they are not immediately evaluated on the<br>command line. Also, the symbol “{}” (make sure to quote or escape it) represents the path to<br>the file found.|
|---|---|
|`-ok`<br>_`cmd`_<br>`;`|Same as`-exec`, but also prompts the user before invoking each command.|
|`-ls`|Perform the command`ls -dils`on the file.|

#### **Name** 

xargs — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
xargs [options] [command]
```

`xargs` is one of the oddest yet most powerful commands available to the shell. It reads lines of text from standard input, turns them into commands, and executes them. This might not sound exciting, but `xargs` has some unique uses, particularly for processing a list of files you’ve located. Suppose you made a file named _important_ that lists important files, one per line:

```
$ cat important
/home/jsmith/mail/love-letters
/usr/local/lib/critical_stuff
/etc/passwd
...
```

With `xargs` , you can process each of these files easily with other Linux commands. For instance, the following command runs the `ls -l` command on all the listed files:

```
$ cat important | xargs ls -l
```

Similarly, you can view the files with `less` :

```
$ cat important | xargs less
```

and even delete them with `rm` :

```
$ cat important | xargs rm -f
```

Each of these pipelines reads the list of files from _important_ and produces and runs new Linux commands based on the list. The power begins when the input list doesn’t come from a file, but from another command writing to standard output. In particular, the `find` command, which prints a list of files on standard output, makes a great partner for `xargs` . For example, to search your current directory hierarchy for files containing the word “myxomatosis”:

```
$ find . -print | xargs grep -l myxomatosis
```

This power comes with one warning: if any of the files located by `find` contains whitespace in its name, this will confuse `grep` . If one file is named (say) _my stuff_ , then the `grep` command constructed is:

```
$ grep -l myxomatosis my stuff
```

which tells `grep` to process _two_ files named _my_ and _stuff_ . Oops! Now imagine if the program had been `rm` instead of `grep` . You’d be telling `rm` to delete the wrong files! To avoid this problem, always use `find -print0` instead of `-print` , which separates lines with ASCII null characters instead of newline characters, combined with `xargs -0` , which expects ASCII nulls:

```
$ find . -print0 | xargs -0 grep -l myxomatosis
```

We have barely scratched the surface of the `xargs` command, so please experiment! (With harmless commands like `grep` and `ls` at first!)

#### **Useful options** 

`-` Feed _`k`_ lines of input to the command being executed. A common scenario is to use `-n1` , `n` guaranteeing that each execution will process only one line of input. Otherwise, `xargs` may pass _`k`_ multiple lines of input to a single command.

> `-0`<sup>Set the end-of-line character for input to be ASCII zero rather than whitespace, and treat all</sup> characters literally. Use this when the input is coming from `find -print0` . 

###### **XARGS VERSUS BACKQUOTES** 

If you remember <u>Quoting, you might realize that some</u> `xargs` tricks can be accomplished with backquotes:

```
$ cat file_list | xargs rm -f   with xargs
```

```
$ rm -f `cat file_list`         with backquotes
```

While both commands do similar things, backquotes can fail if the command line gets so long, after the quoted part is expanded, that it exceeds the maximum length of a shell command line. `xargs` does not have this limitation, so it’s safer and more suitable for large or risky operations.

#### **Name** 

locate — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
locate [options]
```

The `locate` command, with its partner `updatedb` , creates an index (database) of file locations that is quickly searchable.<sup>[</sup> <u>13</u><sup>]</sup> If you plan to locate many files over time in a directory hierarchy that doesn’t change much, `locate` is a good choice. For locating a single file or performing more complex processing of found files, use `find` .

Some distros automatically index the entire filesystem on a regular basis (e.g., once a day), so you can simply run `locate` and it will work. But if you ever need to create an index yourself of a directory and all its subdirectories (say, storing it in _/tmp/myindex_ ), run:

```
$ updatedb -l0 -U directory -o /tmp/myindex
```

(Note that `-l0` is a lowercase `L` followed by a zero, not the number 10.) Then to search for a string in the index:

```
$ locate -d /tmp/myindex string
```

`locate` has an interesting, optional security feature. You can create an index that, when searched, will display only files that the user is permitted to see. So if the superuser created an index of a protected directory, a nonsuperuser could search it but not see the protected files. This is done by omitting the `-l0` option to `updatedb` and running it as root:

```
# updatedb -U directory -o /tmp/myindex
```

#### **Indexing options for updatedb** 

|`-u`<br>Create index|from the root directory downward.|
|---|---|
|`-U` _`directory`_<br>Create index|from_`directory`_downward.|

<!-- Start of picture text --> -l (0|1) Turn security off (0) or on (1). The default is 1.<br>-e Exclude one or more directories from the index. Separate their paths by<br>directories commas.<br>-o outfile Write the index to file  outfile .<br><!-- End of picture text -->

#### **Search options for locate** 

|`-d`<br>_`index`_|Indicate which index to use (in our example,<br>_/tmp/myindex_).|
|---|---|
|`-i`|Case-insensitive search.|
|`-r`|Search for files matching the given regular expression.|
|_`regexp`_||

[13<sup>]</sup> Our `locate` command comes from a package called “mlocate.” Some systems have an older package called “slocate” with slightly different usage. If you have slocate, simply type `slocate` instead of `updatedb` in our examples.

#### **Name** 

which — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
which file
```

The `which` command locates an executable file in your shell’s search path. If you’ve been invoking a program by typing its name:

```
$ who
```

the `which` command tells you where this command is located:

```
$ which who
/usr/bin/who
```

You can even find the `which` program itself:

```
$ which which
```

```
/usr/bin/which
```

If several programs in your search path have the same name (for example, _/usr/bin/who_ and _/usr/local/bin/who_ ), `which` reports only the first.

#### **Name** 

type — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
type [options] commands
```

The `type` command, like `which` , locates an executable file in your shell’s search path:

```
$ type grep who
grep is /bin/grep
who is /usr/bin/who
```

However, `type` is built into the bash shell, whereas `which` is a program on disk:

```
$ type which type rm if
which is /usr/bin/which
type is a shell builtin
rm is aliased to `/bin/rm -i'
if is a shell keyword
```

As a built-in command, `type` is faster than `which` ; however, it’s available only if you’re running bash.

#### **Name** 

whereis — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
whereis [options] files
```

The `whereis` command attempts to locate the given files by searching a hardcoded list of directories. It can find executables, documentation, and source code. `whereis` is somewhat quirky because its list of directories might not include the ones you need.

#### **Useful options** 

> `-b` List only executables ( `-b` ), manpages ( `-m` ), or source code files ( `-s` ). `-m -s -B` Search for executables ( `-B` ), manpages ( `-M` ), or source code files ( `-S` ) only in the given _`dirs.`_ directories. You must follow the directory list with the `-f` option before listing the files you _`..`_ `-f` seek. `-M` _`dirs. ..`_ `-f -S` _`dirs. ..`_ `-f` 

## **File Text Manipulation** 

|`gre`<br>`p`|Find lines in a file that match a regular expression.|
|---|---|
|`cut`|Extract columns from a file.|
|`pas`<br>`te`|Append columns.|
|`tr`|Translate characters into other characters.|
|`sor`<br>`t`|Sort lines of text by various criteria.|
|`uni`<br>`q`|Locate identical lines in a file.|
|`tee`|Copy a file_and_print it on standard output,<br>simultaneously.|

Perhaps Linux’s greatest strength is text manipulation: massaging a text file (or standard input) into a desired form by applying transformations, often in a pipeline. Any program that reads standard input and writes standard output falls into this category, but here we’ll present some of the most important tools.

#### **Name** 

grep — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
grep [options] pattern [files]
```

The `grep` command is one of the most consistently useful and powerful in the Linux arsenal. Its premise is simple: given one or more files, print all lines in those files that match a particular regular expression pattern. For example, if a file contains these lines:

```
The quick brown fox jumped over the lazy dogs!
My very eager mother just served us nine pancakes.
Film at eleven.
```

and we search for all lines containing “pancake”, we get:

```
$ grep pancake myfile
My very eager mother just served us nine pancakes.
```

Now we use a regular expression to match lines ending in an exclamation point:

```
$ grep '\!$' myfile
The quick brown fox jumped over the lazy dogs!
```

`grep` can use two different types of regular expressions, which it calls _basic_ and _extended_ . They are equally powerful, just different, and you may prefer one over the other based on your experience with other `grep` implementations. The basic syntax is in <u>Table 1-2.</u>

#### **Useful options** 

|`-v`|Print only lines that_do not_match the regular expression.|
|---|---|
|`-l`|Print only the_names_of files that contain matching lines, not the lines themselves.|
|`-L`|Print only the names of files that_do not_contain matching lines.|
|`-c`|Print only a count of matching lines.|

|`-n`|In front of each line of matching output, print its original line number.|
|---|---|
|`-b`|In front of each line of matching output, print the byte offset of the line in the input<br>file.|
|`-i`|Case-insensitive match.|
|`-w`|Match only complete words (i.e., words that match the entire regular expression).|
|`-x`|Match only complete lines (i.e., lines that match the entire regular expression).<br>Overrides`-w`.|
|`-A` _`N`_|After each matching line, print the next_`N`_lines from its file.|
|`-B` _`N`_|Before each matching line, print the previous_`N`_lines from its file.|
|`-C` _`N`_|Same as -A_`N`_-B_`N`_: print_`N`_lines (from the original file) above_and_below each matching<br>line.|
|`--`<br>`color=alway`<br>`s`|Highlight the matched text in color, for better readability.|
|`-r`|Recursively search all files in a directory and its subdirectories.|
|`-E`|Use extended regular expressions. See`egrep`.|
|`-F`|Use lists of fixed strings instead of regular expressions. See`fgrep`.|

#### **Name** 

egrep — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
egrep [options] pattern [files]
```

The `egrep` command is just like `grep` , but uses a different (“extended”) language for regular expressions. It’s the same as `grep -E` .

_Table 1-2. Regular expressions for grep and egrep_

|Reg<br>expr|ular<br>ession||
|---|---|---|
|Pla<br>in|Extend<br>ed|Meaning|
|`.`||Any single character.|
|`[...`|`]`|Match any single character in this list.|
|`[^..`|`.]`|Match any single character NOT in this list.|
|`(...`|`)`|Grouping.|
|`\|`|`|`|Or.|
|`^`||Beginning of a line.|
|`$`||End of a line.|
|`\<`||Beginning of a word.|
|`\>`||End of a word.|
|`[:al`|`num:]`|Any alphanumeric character.|
|`[:al`|`pha:]`|Any alphabetic character.|
|`[:cn`|`trl:]`|Any control character.|
|`[:di`|`git:]`|Any digit.|
|`[:gr`|`aph:]`|Any graphic character.|

|Reg<br>exp|ular<br>ression||
|---|---|---|
|Pla<br>in|Extend<br>ed|Meaning|
|`[:lo`|`wer:]`|Any lowercase letter.|
|`[:pr`|`int:]`|Any printable character.|
|`[:pu`|`nct:]`|Any punctuation mark.|
|`[:sp`|`ace:]`|Any whitespace character.|
|`[:up`|`per:]`|Any uppercase letter.|
|`[:xd`|`igit:]`|Any hexadecimal digit.|
|`*`||Zero or more repetitions of a regular expression.|
|`\+`|`+`|One or more repetitions of a regular expression.|
|`\?`|`?`|Zero or one occurrence of a regular expression.|
|`\{`_`n`_<br>`\}`|`{`_`n`_ `}`|Exactly_`n`_repetitions of a regular expression.|
|`\{`<br>_`n`_<br>`,\}`|`{`_`n`_ `,}`|_`n`_or more repetitions of a regular expression.|
|`\{`<br>_`n`_ `,`<br>_`m`_<br>`\}`|`{` _`n`_ `,` _`m`_ `}`|Between_`n`_and_`m`_(inclusive) repetitions of a regular expression,_`n`_ `<` _`m`_.|
|`\`_`c`_||The character_`c`_literally, even if_`c`_is a special regular expression character. For<br>example, use \* to match an asterisk or \\ to match a backslash. Alternatively, put<br>the literal character inside square brackets, like [*] or [\].|

###### **GREP AND END-OF-LINE CHARACTERS** 

When you match the end of a line ( `$` ) with `grep` , text files created on Microsoft Windows or Macintosh OS X systems may produce odd results. The reason is that each operating system has a different standard for ending a line. On Linux, each line in a text file ends with a newline character (ASCII 10). On Windows, text lines end with two characters: a carriage return (ASCII 13) followed by a newline character. And on Macintosh, a text file might end its lines with newlines or carriage returns alone. If `grep` isn’t matching the ends of lines properly, check for non-Linux end-of-line characters with `cat -v` , which displays carriage returns as `^M` :

```
$ cat -v dosfile
Uh-oh! This file seems to end its lines with^M
carriage returns before the newlines.^M
```

To remove the carriage returns, use the `tr -d` command:

```
$ tr -d '\r' < dosfile > newfile
$ cat -v newfile
Uh-oh! This file seems to end its lines with
carriage returns before the newlines.
```

#### **Name** 

fgrep — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
fgrep [options] [fixed_strings] [files]
```

The `fgrep` command is just like `grep` , but instead of accepting a regular expression, it accepts a list of fixed strings, separated by newlines. It’s the same as `grep -F` . For example, if you have a dictionary file full of strings, one per line:

```
$ cat my_dictionary_file
aardvark
aback
abandon
...
```

you can conveniently search for those strings in a set of input files:

```
$ fgrep -f my_dictionary_file inputfile1 inputfile2
```

Normally, you’ll use the lowercase `-f` option to make `fgrep` read the fixed strings from a file. You can also read the fixed strings on the command line using quoting, but it’s a bit trickier. To search for the strings one, two, and three in a file, you’d type:

```
$ fgrep 'one            Note we are typing newline characters
two
three' myfile
```

`fgrep` is convenient when searching for nonalphanumeric characters like * and { because they are taken literally, not as regular expression characters.

#### **Name** 

cut — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
cut -(b|c|f)range [options] [files]
```

The `cut` command extracts columns of text from files. A “column” is defined by character offsets (e.g., the nineteenth character of each line):

```
$ cut -c19 myfile
```

or by byte offsets (which are often the same as characters, unless you have multibyte characters in your language):

```
$ cut -b19 myfile
```

or by delimited fields (e.g., the fifth field in each line of a comma-delimited file):

```
$ cut -f5 -d, myfile
```

You aren’t limited to printing a single column: you can provide a range ( `316` ), a comma-separated sequence ( `3,4,5,6,8,16` ), or both ( `3,4,8-16` ). For ranges, if you omit the first number ( `-16` ), a 1 is assumed ( `1-16` ); if you omit the last number ( `5-` ), the end of line is used.

#### **Useful options** 

|`-d` _`C`_|Use character_`C`_as the_input_delimiter character between fields for the`-f`option. By<br>default it’s a tab character.|
|---|---|
|`--output-`<br>`delimiter=`_`C`_|Use character_`C`_as the_output_delimiter character between fields for`-f`. By default<br>it’s a tab character.|
|`-s`|Suppress (don’t print) lines that don’t contain the delimiter character.|

#### **Name** 

paste — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
paste [options] [files]
```

The `paste` command is the opposite of `cut` : it treats several files as vertical columns and combines them on standard output:

```
$ cat letters
A
B
C
$ cat numbers
1
2
3
4
5
$ paste numbers letters
1  A
2  B
3  C
4
5
$ paste letters numbers
A  1
B  2
C  3
   4
   5
```

#### **Useful options** 

|`-d`<br>_`delimit`_<br>_`ers`_|Use the given_`delimiters`_characters between columns; the default is a tab character.<br>Provide a single character (`-d:`) to be used always, or a list of characters (`-dxyz`) to be<br>applied in sequence on each line (the first delimiter is x, then y, then z, then x, then y, ...).|
|---|---|
|`-s`|Transpose the rows and columns of output:|
||`$ paste -s letters numbers`<br>`A   B   C`<br>`1   2   3   4   5`|

#### **Name** 

tr — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
tr [options] charset1 [charset2]
```

The `tr` command performs some simple, useful translations of one set of characters into another. For example, to capitalize everything in a file:

```
$ cat myfile
This is a very wonderful file.
$ cat myfile | tr 'a-z' 'A-Z'
THIS IS A VERY WONDERFUL FILE.
```

or to change all vowels into asterisks:

```
$ cat myfile | tr aeiouAEIOU '*'
Th*s *s * v*ry w*nd*rf*l f*l*.
```

or to delete all vowels:

```
$ cat myfile | tr -d aeiouAEIOU
Ths s  vry wndrfl fl.
```

As a very practical example, delete all carriage returns from a DOS text file so it’s more compatible with Linux text utilities like `grep` :

```
$ tr -d '\r' < dosfile > newfile
```

`tr` translates the first character in _`charset1`_ into the first character in _`charset2`_ , the second into the second, the third into the third, etc. If the length of _`charset1`_ is _`N`_ , only the first _`N`_ characters in _`charset2`_ are used. (If _`charset1`_ is longer than _`charset2`_ , see the `-t` option.)

Character sets can have the following forms.

|Form|Meaning|
|---|---|
|`ABCD`|The sequence of characters A, B, C, D.|
|`A-B`|The range of characters from A to B.|
|`[x*y]`|y repetitions of the character x.|

Form Meaning

`[:` _`class`_ The same character classes ( `[:alnum:]` , `[:digit:]` , etc.) accepted by `:] grep` .

`tr` also understands the escape characters “\a” ( `^G` = ring bell), “\b” ( `^H` = backspace), “\f” ( `^L` = formfeed), “\n” ( `^J` = newline), “\r” ( `^M` = return), “\t” ( `^I` = tab), and “\v” ( `^K` = vertical tab) accepted by `printf` (see <u>Screen Output), as well as the notation \</u> _`nnn`_ to mean the character with octal value _`nnn`_ .

`tr` is great for quick and simple translations, but for more powerful jobs consider `sed` , `awk` , or `perl` .

#### **Useful options** 

> `-d`<sup>Delete the characters in</sup><sup>_`charset1`_from the input.</sup> 

> `-s`<sup>Eliminate adjacent duplicates (found in</sup><sup>_`charset1`_) from the input. For example,</sup><sup>`tr -s aeiouAEIOU`</sup> would squeeze adjacent, duplicate vowels to be single vowels (reeeeeeally would become really). 

> `-c`<sup>Operate on all characters</sup><sup>_not_found in</sup><sup>_`charset1`_.</sup> 

> `-t`<sup>If</sup><sup>_`charset1`_is longer than</sup><sup>_`charset2`_, make them the same length by truncating</sup><sup>_`charset1`_. If</sup><sup>`-t`is not</sup> present, the last character of _`charset2`_ is (invisibly) repeated until _`charset2`_ is the same length as _`charset1`_ . 

#### **Name** 

sort — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
sort [options] [files]
```

The `sort` command prints lines of text in alphabetical order, or sorted by some other rule you specify. All provided files are concatenated, and the result is sorted and printed.

```
$ cat myfile
def
xyz
abc
$ sort myfile
abc
def
xyz
```

#### **Useful options** 

> `-f` Case-insensitive sorting. 

> `-n` Sort numerically (i.e., 9 comes before 10) instead of alphabetically (10 comes before 9 because it begins with a “1”). 

- `-g` Another numerical sorting method with a different algorithm that, among other things, recognizes scientific notation (7.4e3 means “7.4 times ten to the third power,” or 7400). Run `info sort` for full technical details. 

> `-u` Unique sort: ignore duplicate lines. (If used with `-c` for checking sorted files, fail if any consecutive lines are identical.) 

> `-c` Don’t sort, just check if the input is already sorted. If it is, print nothing; otherwise, print an error message. 

> `-b` Ignore leading whitespace in lines. 

> `-r` Reverse the output: sort from greatest to least. 

- Use _`X`_ as the field delimiter for the `-k` option. 

- `t` _`X`_ 

`-` Choose sorting keys. (Combine with `-t` to choose a separator character between keys.) `k` _`k e y`_

A sorting key is a portion of a line that’s considered when sorting, instead of considering the entire line. An example is “the fifth character of each line.” Normally, `sort` would consider these lines to be in sorted order:

```
aaaaz
bbbby
```

but if your sorting key is “the fifth character of each line,” then the lines are reversed because `y` comes before `z` . A more practical example involves this file of names and addresses:

```
$ cat people
George Washington,123 Main Street,New York
Abraham Lincoln,54 First Avenue,San Francisco
John Adams,39 Tremont Street,Boston
```

An ordinary sort would display the “Abraham Lincoln” line first. But if you consider each line as three comma-separated values, you can sort on the second value with:

```
$ sort -k2 -t, people
George Washington,123 Main Street,New York
John Adams,39 Tremont Street,Boston
Abraham Lincoln,54 First Avenue,San Francisco
```

where “123 Main Street” is first alphabetically. Likewise, you can sort on the city (third value) with:

```
$ sort -k3 -t, people
John Adams,39 Tremont Street,Boston
George Washington,123 Main Street,New York
Abraham Lincoln,54 First Avenue,San Francisco
```

and see that Boston comes up first alphabetically. The general syntax `-k` _`F1[.C1][,F2[.C2]]`_ means:

|Ite||Default if not|
|---|---|---|
|m|Meaning|supplied|
|_`F1`_|Starting field|Required|
|_`C1`_|Starting position within field 1|1|

|Ite||Default if not|
|---|---|---|
|m|Meaning|supplied|
|_`F2`_|Ending field|Last field|
|_`C2`_|Starting position within ending<br>field|1|

So `sort -k1.5` sorts based on the first field, beginning at its fifth character; and `sort -k2.8,5` means “from the eighth character of the second field, to the first character of the fifth field.” The `-t` option changes the behavior of `-k` so it considers delimiter characters such as commas rather than spaces. You can repeat the `-k` option to define multiple keys, which will be applied from first to last as found on the command line.

#### **Name** 

uniq — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
uniq [options] [files]
```

The `uniq` command operates on consecutive, duplicate lines of text. For example, if you have a file _myfile_ :

```
$ cat myfile
a
b
b
c
b
```

then `uniq` would detect and process (in whatever way you specify) the two consecutive b’s, but not the third b.

```
$ uniq myfile
a
b
c
b
```

`uniq` is often used after sorting a file:

```
$ sort myfile | uniq
a
b
c
```

In this case, only a single b remains because all three were made adjacent by `sort` , then collapsed to one by `uniq` . Also, you can count duplicate lines instead of eliminating them:

```
$ sort myfile | uniq -c
      1 a
      3 b
      1 c
```

#### **Useful options** 

- `-c`<sup>Count adjacent duplicate lines.</sup> `-i`<sup>Case-insensitive operation.</sup> `-u`<sup>Print unique lines only.</sup> `-d`<sup>Print duplicate lines only.</sup> `-` Ignore the first _`N`_ characters on each line when detecting duplicates. 

- `s` _`N`_ `-` Ignore the first _`N`_ whitespace-separated fields on each line when detecting duplicates. 

- `f` _`N`_ `-` Consider only the first _`N`_ characters on each line when detecting duplicates. If used with `-s` or `-f` , 

- `w sort` will ignore the specified number of characters or fields first, then consider the next _`N N`_ characters. 

#### **Name** 

tee — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
tee [options] files
```

Like the `cat` command, the `tee` command copies standard input to standard output unaltered. Simultaneously, however, it also copies that same standard input to one or more files. `tee` is most often found in the middle of pipelines, writing some intermediate data to a file while also passing it to the next command in the pipeline:

```
$ who | tee original_who | sort
```

In this command line, `tee` writes the output of `who` to the file `original_who` , and then passes along that same output to the rest of the pipeline ( `sort` ), producing sorted output on screen.

#### **Useful options** 

> `-a`<sup>Append instead of overwriting</sup> files. 

> `-i`<sup>Ignore interrupt signals.</sup> 

#### **Name** 

#### **More Powerful Manipulations** 

We’ve just touched the tip of the iceberg for Linux text filtering. Linux has hundreds of filters that produce ever more complex manipulations of the data. But with great power comes a great learning curve, too much for a short book. Here are a few filters to get you started.

###### **awk** 

awk is a pattern-matching language. It matches data by regular expression and then performs actions based on the data. Here are a few simple examples for processing a text file, _myfile_ .

Print the second and fourth word on each line:

```
$ awk '{print $2, $4}' myfile
```

Print all lines that are shorter than 60 characters:

```
$ awk 'length < 60 {print}' myfile
```

###### **sed** 

Like awk, sed is a pattern-matching engine that can perform manipulations on lines of text. Its syntax is closely related to that of vim and the line editor ed. Here are some trivial examples.

Print the file with all occurrences of the string “red” changed to “hat”:

```
$ sed 's/red/hat/g' myfile
```

Print the file with the first 10 lines removed:

```
$ sed '1,10d' myfile
```

**m4**

m4 is a macro-processing language and command. It locates keywords within a file and substitutes values for them. For example, given this file:

```
$ cat myfile
My name is NAME and I am AGE years old
ifelse(QUOTE,yes,No matter where you go... there you are)
```

see what m4 does with substitutions for `NAME` , `AGE` , and `QUOTE` :

```
$ m4 -DNAME=Sandy myfile
My name is Sandy and I am AGE years old
```

```
$ m4 -DNAME=Sandy -DAGE=25 myfile
My name is Sandy and I am 25 years old
```

```
$ m4 -DNAME=Sandy -DAGE=25 -DQUOTE=yes myfile
My name is Sandy and I am 25 years old
No matter where you go... there you are
```

###### **Perl, PHP, Python** 

Perl, PHP, and Python are full-fledged scripting languages powerful enough to build complete, robust applications. See <u>Beyond Shell Scripting</u> for references.

## **File Compression and Packaging** 

|`tar`|Package multiple files into a single file.|
|---|---|
|`gzip`|Compress files with GNU Zip.|
|`gunzip`|Uncompress GNU Zip files.|
|`bzip2`|Compress files in BZip format.|
|`bunzip2`|Uncompress BZip files.|
|`bzcat`|Compress/uncompress BZip files via standard input/output.|
|`compress`|Compress files with traditional Unix compression.|
|`uncompress`|Uncompress files with traditional Unix compression.|
|`zcat`|Compress/uncompress file via standard input/output (gzip or<br>compress).|
|`zip`|Compress files in Windows Zip format.|
|`unzip`|Uncompress Windows Zip files.|
|`metamail`|Extract MIME data to files.|

Linux can compress files into a variety of formats and uncompress them. The most popular formats are GNU Zip ( `gzip` ), whose compressed files are named with the _.gz_ suffix, and BZip, which uses the _.bz2_ suffix. Other common formats include Zip files from Windows systems ( _.zip_ suffix) and occasionally, classic Unix compression ( _.Z_ suffix).

A related technology involves converting binary files into textual formats, so they can (say) be transmitted within an email message. Nowadays this is done automatically with attachments and MIME tools, but we’ll cover the `metamail` program, which can do this from the command line.

If you come across a format we don’t cover, such as Macintosh sit files, Arc, Zoo, rar, and others, learn more at <u>http://en.wikipedia.org/wiki/List_of_archive_formats.</u>

#### **Name** 

tar — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
tar [options] [files]
```

The `tar` program was originally for backing up files onto a tape drive (its name is short for “tape archive”). Although tape has lost its popularity, `tar` is still the most common file-packaging format for Linux. It can pack multiple files and directories into a single file for transport, optionally compressed.

```
$ tar -czvf myarchive.tar.gz mydir      Create
$ tar -tzvf myarchive.tar.gz            List contents
$ tar -xzvf myarchive.tar.gz            Extract
```

If you actually have a tape drive, simply specify the drive’s device (such as _/dev/tape_ ) as the destination file:

```
$ tar -cf /dev/tape myfile1 myfile2
```

If you specify files on the command line, only those files are processed:

```
$ tar -xvf myarchive.tar file1 file2 file3
```

Otherwise, the entire archive is processed.

#### **Useful options** 

- `-c` Create an archive. You’ll have to list the input files and directories on the command line. `-r` Append files to an existing archive. 

- `-u` Append new/changed files to an existing archive. 

- `-A` Append one archive to the end of another: e.g., `tar -A -f first.tar second.tar` appends the contents of _second.tar_ to _first.tar_ . Does not work for compressed archives. 

- `-t` List the archive. 

- `-x` Extract files from the archive. 

|`-f`<br>_`fi`_<br>_`le`_|Read the archive from, or write the archive to, the given file. This is usually a tar file on disk<br>(such as_myarchive.tar_) but can also be a tape drive (such as_/dev/tape_).|
|---|---|
|`-d`|Diff (compare) the archive against the filesystem.|
|`-z`|Use`gzip`compression.|
|`-j`|Use`bzip2`compression.|
|`-Z`|Use Unix compression.|
|`-b`<br>_`N`_|Use a block size of_`N`_* 512 bytes.|
|`-v`|Verbose mode: print extra information.|
|`-h`|Follow symbolic links rather than merely copying them.|
|`-p`|When extracting files, restore their original permissions and ownership.|

#### **Name** 

gzip — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
gzip [options] [files]
```

`gzip` and `gunzip` compress and uncompress files in GNU Zip format. Compressed files have the suffix _.gz_ .

#### **Sample commands** 

|`gzip` _`file`_|Compress_`file`_to create_`file.gz`_. Original_`file`_is deleted.|
|---|---|
|`gzip -c` _`file`_|Produce compressed data on standard output.|
|`cat` _`file`_ `| gzip`|Produce compressed data from a pipeline.|
|`gunzip` _`file`_`.gz`|Uncompress_`file.gz`_to create_`file`_. Original_`file.gz`_is<br>deleted.|
|`gunzip -c` _`file`_`.gz`|Uncompress the data on standard output.|
|`cat` _`file`_`.gz |`<br>`gunzip`|Uncompress the data from a pipeline.|
|`zcat` _`file`_`.gz`|Uncompress the data on standard output.|

#### **gzipped tar files: sample commands** 

|`tar -czf` _`myfile`_`.tar.gz`|Pack directory|
|---|---|
|_`dirname`_|_`dirname`_.|
|`tar -tzf` _`myfile`_`.tar.gz`|List contents.|
|`tar -xzf` _`myfile`_`.tar.gz`|Unpack.|

Add the `-v` option to `tar` to print filenames as they are processed.

#### **Name** 

bzip2 — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
bzip2 [options] [files]
```

`bzip2` and `bunzip2` compress and uncompress files in Burrows-Wheeler format. Compressed files have the suffix _.bz2_ .

#### **Sample commands** 

|`bzip2` _`file`_|Compress_`file`_to create_`file.bz2`_. Original_`file`_is deleted.|
|---|---|
|`bzip2 -c` _`file`_|Produce compressed data on standard output.|
|`cat` _`file`_ `| bzip2`|Produce compressed data on standard output.|
|`bunzip2` _`file`_`.bz2`|Uncompress_`file.bz2`_to create_`file`_. Original_`file.bz2`_is<br>deleted.|
|`bunzip2 -c` _`file`_`.bz2`|Uncompress the data on standard output.|
|`cat` _`file`_`.bz2 |`<br>`bunzip2`|Uncompress the data on standard output.|
|`bzcat` _`file`_`.bz2`|Uncompress the data on standard output.|

#### **bzipped tar files: sample commands** 

|`tar -cjf` _`myfile`_`.tar.bz2`|Pack.|
|---|---|
|_`dirname`_||
|`tar -tjf`-_`myfile`_`.tar.bz2`|List|
||contents.|
|`tar -xjf` _`myfile`_`.tar.bz2`|Unpack.|

Add the `-v` option to `tar` to print filenames as they are processed.

#### **Name** 

compress — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
compress [options] [files]
```

`compress` and `uncompress` compress and uncompress files in standard Unix compression format (Lempel Ziv). Compressed files have the suffix _.Z_ .

#### **Sample commands** 

|`compress` _`file`_|Compress_`file`_to create_`file.Z`_. Original_`file`_is deleted.|
|---|---|
|`compress -c` _`file`_|Produce compressed data on standard output.|
|`cat` _`file`_ `| compress`|Produce compressed data from a pipeline.|
|`uncompress` _`file`_`.Z`|Uncompress_`file.Z`_to create_`file`_. Original_`file.Z`_is<br>deleted.|
|`uncompress -c` _`file`_`.Z`|Uncompress the data on standard output.|
|`cat` _`file`_`.Z |`<br>`uncompress`|Uncompress the data from a pipeline.|
|`zcat` _`file`_`.Z`|Uncompress the data on standard output.|

#### **Compressed tar files: sample commands** 

|`tar -cZf` _`myfile`_`.tar.Z`|Pack directory|
|---|---|
|_`dirname`_|_`dirname`_.|
|`tar -tZf` _`myfile`_`.tar.Z`|List contents.|
|`tar -xZf` _`myfile`_`.tar.Z`|Unpack.|

Add the `-v` option to `tar` to print filenames as they are processed.

#### **Name** 

zip — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
zip [options] [files]
```

`zip` and `unzip` compress and uncompress files in Windows Zip format. Compressed files have the suffix _.zip_ . Unlike most other Linux compression commands, `zip` does not delete the original files.

<!-- Start of picture text --> zip myfile .zip file1 file2 file3 Pack.<br>...<br>zip -r myfile .zip dirname Pack<br>recursively.<br>unzip -l myfile .zip List contents.<br>unzip myfile .zip Unpack.<br><!-- End of picture text -->

#### **Name** 

metamail — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
metamail [options] mail_file
```

Modern email programs can send and receive attachments so easily we rarely think about it, but this was not always the case. Programs like `metamail` were created to work with attachments directly on the command line, appending or extracting them to and from mail messages. For example, if you have an email message in a file, _mymessage_ , and it contains a JPEG image as an attachment, `metamail` can extract the image:

```
$ metamail -w mymessage
Content-Description: coolcat.jpg
This message contains 'image/jpeg`-format data.
Please enter the name of a file to which the data should
 be written (Default: coolcat.jpg) > hotdog.jpg
Wrote file hotdog.jpg
```

Here we extracted the attached JPEG file, _coolcat.jpg_ , renaming it as _hotdog.jpg_ . The `-w` option tells `metamail` to write the data to a file; otherwise, `metamail` would attempt to display the attachment with an appropriate program, such as an image viewer:

```
$ metamail mymessage
This message contains 'image/jpeg'-format data.
Do you want to view it using the 'xv' command (y/n) [y] y
---Executing: gthumb
```

## **File Comparison** 

|`diff`|Line-by-line comparison of two files or<br>directories.|
|---|---|
|`comm`|Line-by-line comparison of two sorted files.|
|`cmp`|Byte-by-byte comparison of two files.|
|`md5s`<br>`um`|Compute a checksum of the given files (MD5).|

There are three ways to compare Linux files:

- Line by line ( `diff` , `diff3` , `sdiff` , `comm` ), best suited to text files Byte by byte ( `cmp` ), often used for binary files 

- By comparing checksums ( `md5sum` , `sum` , `cksum` ) 

These programs are all text-based. For a graphical file-comparison tool, try `xxdiff` at <u>http://furius.ca/xxdiff.</u>

#### **Name** 

diff — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
diff [options] file1 file2
```

The `diff` command compares two files line-by-line, or two directories. When comparing text files, `diff` can produce detailed reports of their differences. For binary files, `diff` merely reports whether they differ or not. For all files, if there are no differences, `diff` produces no output. The traditional output format looks like this:

```
Indication of line numbers and the type of change
< Corresponding section of file1, if any
---
> Corresponding section of file2, if any
```

For example, if we start with a file _fileA_ :

```
Hello, this is a wonderful file.
The quick brown fox jumped over
the lazy dogs.
Goodbye for now.
```

Suppose we delete the first line, change “brown” to “blue” on the second line, and add a final line, creating a file _fileB_ :

```
The quick blue fox jumped over
the lazy dogs.
Goodbye for now.
Linux r00lz!
```

Then `diff fileA fileB` produces this output:

```
1,2c1                            fileA lines 1-2 became fileB line 1
< Hello, this is a wonderful file. Lines 1-2 of fileA
< The quick brown fox jumped over
---                                diff separator
> The quick blue fox jumped over   Line 1 of fileB
4a4                                Line 4 was added in fileB
> Linux r00lz!                     The added line
```

The leading symbols < and > are arrows indicating _fileA_ and _fileB_ , respectively. This output format is the default: many others are available,

some of which can be fed directly to other tools. Try them out to see what they look like.

|Opti<br>on|Output format|
|---|---|
|`-n`|RCS version control format, as produced by`rcsdiff`(`man rcsdiff`).|
|`-c`|Context diff format, as used by the`patch`command (`man patch`).|
|`-D`<br>_`macro`_|C preprocessor format, using`#ifdef` _`macro`_`... #else ... #endif`.|
|`-u`|Unified format, which merges the files and prepends “-” for deletion and “+” for<br>addition.|
|`-y`|Side-by-side format; use`-W`to adjust the width of the output.|
|`-e`|Create an`ed`script that would change_fileA_into_fileB_if run.|
|`-q`|Don’t report changes, just say whether the files differ.|

`diff` can also compare directories:

```
$ diff dir1 dir2
```

which compares any same-named files in those directories, and lists all files that appear in one directory but not the other. To compare entire directory hierarchies recursively, use the `-r` option:

```
$ diff -r dir1 dir2
```

which produces a (potentially massive) report of all differences.

#### **Useful options** 

|`-`<br>`b`|<sup>Don’t consider whitespace.</sup>|
|---|---|
|`-`<br>`B`|<sup>Don’t consider blank lines.</sup>|
|`-`<br>`i`|<sup>Ignore case.</sup>|
|`-`<br>`r`|<sup>When comparing directories, recurse into</sup><br>subdirectories.|

`diff` is just one member of a family of programs that operate on file differences. Some others are `diff3` , which compares three files at a time,

and `sdiff` , which merges the differences between two files to create a third file according to your instructions.

#### **Name** 

comm — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
comm [options] file1 file2
```

The `comm` command compares two sorted files and produces three columns of output, separated by tabs:

1. All lines that appear in _file1_ but not in _file2_ . 

2. All lines that appear in _file2_ but not in _file1_ . 

3. All lines that appear in both files. 

For example, if _file1_ and _file2_ contain these lines:

```
file1:                           file2:
apple            baker
baker            charlie
charlie          dark
```

then `comm` produces this three-column output:

```
$ comm file1 file2
apple
                baker
                charlie
        dark
```

#### **Useful options** 

<!-- Start of picture text --> −<br>Suppress column<br>1 1.<br>−2 Suppress column<br>2.<br>−3 Suppress column<br>3.<br><!-- End of picture text -->

#### **Name** 

cmp — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
cmp [options] file1 file2 [offset1 [offset2]]
```

The `cmp` command compares two files. If their contents are the same, `cmp` reports nothing; otherwise, it lists the location of the first difference:

```
$ cmp myfile yourfile
```

```
myfile yourfile differ: char 494, line 17
```

By default, `cmp` does not tell you what the difference is, only where it is. It also is perfectly suitable for comparing binary files, as opposed to `diff` , which operates best on text files.

Normally, `cmp` starts its comparison at the beginning of each file, but it will start elsewhere if you provide offsets:

```
$ cmp myfile yourfile 10 20
```

This begins the comparison at the tenth character of _myfile_ and the twentieth of _yourfile_ .

#### **Useful options** 

> `-l`<sup>Long output: print all differences, byte by byte:</sup> 

```
$ cmp -l myfile yourfile
494 164 172
```

This means at offset 494 (in decimal), _myfile_ has “t” (octal 164) but _yourfile_ has “z” (octal 172).

> `-s`<sup>Silent output: don’t print anything, just exit with an appropriate return code; 0 if the files match, 1</sup> if they don’t. (Or other codes if the comparison fails for some reason.) 

#### **Name** 

md5sum — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
md5sum files | --check file
```

The `md5sum` command works with checksums to verify that files are unchanged. The first form produces the 32-byte checksum of the given files, using the MD5 algorithm:

```
$ md5sum myfile
dd63602df1cceb57966d085524c3980f  myfile
```

while the second form tests whether a checksum matches its file, using `-check` :

```
$ md5sum file1 file2 file3 > mysum
$ cat mysum
90a022707ca5b5fc8f465e7cbb954987  file1
86d19ef79d33c28cf0c9ba882f25cdb8  file2
d0dc53c9941e33a10e7f38ecc0de772f  file3
$ md5sum --check mysum
file1: OK
file2: OK
file3: OK
$ echo "new data" > file2
$ md5sum --check mysum
file1: OK
file2: FAILED
file3: OK
md5sum: WARNING: 1 of 3 computed checksums did NOT match
```

Two different files are highly unlikely to have the same MD5 checksum, so comparing checksums is a reasonably reliable way to detect if two files differ:

```
$ md5sum myfile1 | cut -c1-32 > sum1
$ md5sum myfile2 | cut -c1-32 > sum2
$ diff -q sum1 sum2
Files sum1 and sum2 differ
```

Some other programs similar to `md5sum` are `sum` and `cksum` , which use different algorithms to compute their checksums. `sum` is compatible with

other Unix systems, specifically BSD Unix (the default) or System V Unix ( `-s` option), and `cksum` produces a CRC checksum:

```
$ sum myfile
12410     3
$ sum -s myfile
47909 6 myfile
$ cksum myfile
1204834076 2863 myfile
```

The first integer is a checksum and the second is a block count. But as you can see, these checksums are small numbers and therefore unreliable, since files could have identical checksums by coincidence. `md5sum` is by far the best. See <u>http://www.faqs.org/rfcs/rfc1321.html</u> for the technical details.

## **Printing** 

> `lpr` Print a file. 

> `lpq` View the print queue. 

> `lpr` Remove a print job from the 

> `m` queue. 

Linux has two popular printing systems, called CUPS and LPRng. Both systems use commands with the same names: `lpr` , `lpq` , and `lprm` . However, these commands have different options depending whether you’re using CUPS or LPRng. To be generally helpful, we will present common options that work with both systems.

Installing a printer on Linux used to require editing a cryptic configuration file, such as _/etc/cups/printers.conf_ or _/etc/printcap_ . Nowadays, both GNOME and KDE have printer configuration tools in their system settings that generate these files.

#### **Name** 

lpr — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
lpr [options] [files]
```

The `lpr` (line printer) command sends a file to a printer.

```
$ lpr -P myprinter myfile
```

#### **Useful options** 

|`-P`|Send the file to printer_`printername`_, which you have previously set up.|
|---|---|
|_`printername`_||
|`-#` _`N`_|Print_`N`_copies of the file.|
|`-J` _`name`_|Set the job_`name`_that prints on the cover page (if your system is set up to print cover<br>pages).|

#### **Name** 

lpq — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
lpq [options]
```

The `lpq` (line printer queue) command lists all print jobs waiting to be printed.

#### **Useful options** 

|`-P`|List the queue for printer_`printername`_.|
|---|---|
|_`printername`_||
|`-a`|List the queue for all printers.|
|`-l`|Be verbose: display information in a longer<br>format.|

#### **Name** 

lprm — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
lprm [options] [job_IDs]
```

The `lprm` (line printer remove) command cancels one or more print jobs. Use `lpq` to learn the ID of the desired print jobs (say, 61 and 78), then type:

```
$ lprm -P printername 61 78
```

If you don’t supply any job IDs, your current print job is canceled. (Only the superuser can cancel other users’ jobs.) The `-P` option specifies which print queue contains the job.

## **Spell Checking** 

|`look`|Look up the spelling of a word<br>quickly.|
|---|---|
|`aspel`<br>`l`|Interactive spelling checker.|
|`spell`|Batch spelling checker.|

Linux has several spellcheckers built in. If you’re accustomed to graphical spellcheckers, you might find Linux’s text-based ones fairly primitive, but they can be used in pipelines, which is quite powerful.

#### **Name** 

look — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
look [options] prefix [dictionary_file]
```

The `look` command prints (on standard output) words that begin with a given string _`prefix`_ . The words are located in a dictionary file (default _/usr/share/dict/words)_ . For instance, `look bigg` prints:

```
bigger
biggest
Biggs
```

If you supply your own dictionary file — any text file with alphabetically sorted lines — `look` will print all lines beginning with the given _`prefix`_ .

#### **Useful options** 

> `-f`<sup>Ignore case.</sup> 

- Match the prefix only up to and including the termination character _`X`_ . For instance, `look -t i big` 

- `t` prints all words beginning with “bi”. 

- _`X`_ 

#### **Name** 

aspell — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
aspell [options] file | command
```

`aspell` is a powerful spellchecker with dozens of options. A few useful commands are:

```
aspell -cfile
```

Interactively check, and optionally correct, the spelling of all words in file.

```
aspell -l <file
```

Print a list of the misspelled words in _`file`_ on standard output. `aspell dump master`

Print `aspell` ’s master dictionary on standard output.

```
aspell help
```

Print a concise help message. See <u>http://aspell.net</u> for more information.

#### **Name** 

spell — stdin  stdout  -file  --opt  --help  --version **Synopsis**

```
spell [files]
```

The `spell` command prints all words in the given files that are misspelled, according to its dictionary.

```
$ spell myfile
thier
naturaly
Linuxx
```

## **Disks and Filesystems** 

|`df`|Display available space on mounted<br>filesystems.|
|---|---|
|`moun`<br>`t`|Make a disk partition accessible.|
|`umou`<br>`nt`|Unmount a disk partition (make it<br>inaccessible).|
|`fsck`|Check a disk partition for errors.|
|`sync`|Flush all disk caches to disk.|

Linux systems can have multiple disks or disk partitions. In casual conversation, these are variously called disks, partitions, filesystems, volumes, even directories. We’ll try to be more accurate.

A _disk_ is a hardware device, which may be divided into _partitions_ that act as independent storage devices. Partitions are represented on Linux systems as special files in (usually) the directory _/dev_ . For example, _/dev/sda7_ could be a partition on your hard drive. Some common devices in _/dev_ are:

_hd_ First IDE bus, master device; partitions are _hda1_ , _hda2_ , ... _a hd_ First IDE bus, slave device; partitions are _hdb1_ , _hdb2_ , ... _b hd_ Second IDE bus, master device; partitions are _hdc1_ , _hdc2_ , ... _c hd_ Second IDE bus, slave device; partitions are _hdd1_ , _hdd2_ , ... _d sd_ First block device, such as SCSI, SATA, USB, or Firewire hard drives; partitions are _sda1_ , _a sda2_ , ... _sd_ Second block device; partitions are _sdb1_ , _sdb2_ , ... Likewise for _sdc_ , _sdd_ , ... _b ht_ First IDE tape drive (then _ht1_ , _ht2_ , ...) with auto-rewind _0 nh_ First IDE tape drive (then _nht1_ , _nht2_ , ...) without auto-rewind _t0 st_ First SCSI tape drive (then _st1_ , _st2_ , ...)

|_0_||
|---|---|
|_sc_<br>_d0_|First SCSI CD-ROM drive (then_scd1_,_scd2_, ...)|
|_fd_<br>_0_|First floppy drive (then_fd1_,_fd2_, ...), usually mounted on_/mnt/floppy_|

Before a partition can hold files, it is “formatted” by a program that writes a _filesystem_ on it (see <u>Partitioning and Formatting). A filesystem defines how</u> files are represented; examples are ext3 (a Linux journaling filesystem) and ntfs (Microsoft Windows NT filesystem). Formatting is generally done for you when you install Linux.

Once a filesystem is created, you can make it available for use by _mounting_ it on an empty directory. For example, if you mount a Windows filesystem on a directory _/mnt/win_ , it becomes part of your system’s directory tree, and you can create and edit files like _/mnt/win/myfile_ . Mounting is generally done automatically at boot time. Filesystems can also be unmounted to make them inaccessible via the filesystem, say, for maintenance.

###### **PARTITIONING AND FORMATTING** 

Disk-related operations like partitioning and formatting can be complex on Linux systems. Here are pointers to the programs you may need (start with their manpages).

`parted` , `fdisk` , or `sfdisk`

Partition a hard drive. Any of these programs will do: they simply have different user interfaces.

```
mkfs
```

Format a hard disk, i.e., create a new filesystem.

```
floppy
```

Format a floppy disk.

#### **Name** 

df — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
df [options] [disk devices | files | directories]
```

The `df` (disk free) program shows you the size, used space, and free space on a given disk partition. If you supply a file or directory, `df` describes the disk device on which that file or directory resides. With no arguments, `df` reports on all mounted filesystems.

```
$ df
Filesystem    1k-blocks     Used Available Use% Mounted on
/dev/sda        1011928   225464    735060  24% /
/dev/sda9        521748   249148    246096  51% /var
/dev/sda8       8064272  4088636   3565984  54% /usr
/dev/sda10      8064272  4586576   3068044  60% /home
```

#### **Useful options** 

|`-k`|List sizes in kilobytes (the default).|
|---|---|
|`-m`|List sizes in megabytes.|
|`-B`<br>_`N`_|Display sizes in blocks of_`N`_bytes. (Default = 1024)|
|`-h`<br>`-H`|Print human-readable output, and choose the most appropriate unit for each size. For example,<br>if your two disks have 1 gigabyte and 25 kilobytes free, respectively,`df -h`prints 1G and 25K.<br>The`-h`option uses powers of 1024, whereas`-H`uses powers of 1000.|
|`-l`|Display only local filesystems, not networked filesystems.|
|`-T`|Include the filesystem type (ext3, vfat, etc.) in the output.|
|`-t`<br>_`ty`_<br>_`pe`_|Display only filesystems of the given type.|
|`-x`<br>_`ty`_<br>_`pe`_|Don’t display filesystems of the given type.|

> `-i` Inode mode. Display total, used, and free inodes for each filesystem, instead of disk blocks. 

#### **Name** 

mount — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
mount [options] device | directory
```

The `mount` command makes a partition accessible. Most commonly it handles disk drives (say, _/dev/sda1_ ) and removal media (e.g., USB keys), making them accessible via an existing directory (say, _/mnt/mydir_ ):

```
# mkdir /mnt/mydir
# ls /mnt/mydir                 Notice it’s empty
# mount /dev/sda1 /mnt/mydir
# ls /mnt/mydir
file1      file2      file3     Files on the mounted partition
# df /mnt/mydir
Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/sda1        1011928  285744    674780  30% /mnt/mydir
```

`mount` has tons of options and uses; we will discuss only the most basic. In most common cases, `mount` reads the file _/etc/fstab_ (filesystem table) to learn how to mount a desired disk. For example, if you type mount _/usr_ , the `mount` command looks up “/usr” in _/etc/fstab_ , whose line might look like this:

```
/dev/sda8    /usr    ext3    defaults    1    2
```

Here `mount` learns, among other things, that disk device _/dev/sda8_ should be mounted on _/usr_ as a Linux ext3-formatted filesystem. Now you can mount _/dev/sda8_ on _/usr_ with either of these commands:

```
# mount /dev/sda8     by device
# mount /usr          by directory
```

`mount` is run typically by the superuser, but common devices like USB and CD-ROM drives often can be mounted and unmounted by any user.

```
$ mount /media/cdrom
```

#### **Useful options** 

|`-t`<br>_`typ`_|Specify the type of filesystem, such as`ext3`or`ntfs`.|
|---|---|
|_`e`_||
|`-l`|List all mounted filesystems; works with`-t`too.|
|`-a`|Mount all filesystems listed in_/etc/fstab_. Ignores entries that include the`noauto`option. Works<br>well with`-t`too.|
|`-r`|Mount the filesystem read-only (but see the manpage for some disclaimers).|

#### **Name** 

umount — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
umount [options] [device | directory]
```

`umount` does the opposite of `mount` : it makes a disk partition unavailable via the filesystem. For instance, if you’ve mounted a CD-ROM disc, you can’t eject it until it’s `umount` ed:

```
$ umount /media/cdrom
```

Always unmount a removable medium before ejecting it or you risk damage to its filesystem. To unmount all mounted devices:

```
# umount -a
```

Don’t unmount a filesystem that’s in use; in fact, the `umount` command will refuse to do so for safety reasons.

#### **Name** 

fsck — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
fsck [options] [devices]
```

The `fsck` (filesystem check) command validates a Linux disk partition and, if requested, repairs errors found on it. `fsck` is run automatically when your system boots; however, you can run it manually if you like. In general, unmount a device before checking it, so no other programs are operating on it at the same time:

```
# umount /dev/sda10
# fsck -f /dev/sda10
Pass 1: Checking inodes, blocks, and sizes
Pass 2: Checking directory structure
Pass 3: Checking directory connectivity
Pass 4: Checking reference counts
Pass 5: Checking group summary information
/home: 172/1281696 files (11.6% non-contiguous), ...
```

`fsck` is a frontend for a set of filesystem-checking programs found in _/sbin_ , with names beginning “fsck”. Only certain types of filesystems are supported; you can list them with the command:

```
$ ls /sbin/fsck.* | cut -d. -f2
```

#### **Useful options** 

> `-A`<sup>Check all disks listed in</sup><sup>_/etc/fstab_, in order.</sup> 

> `-N`<sup>Print a description of the checking that would be done, but exit without performing any checking.</sup> 

> `-r`<sup>Fix errors interactively, prompting before each fix.</sup> 

> `-a`<sup>Fix errors automatically (use only if you</sup><sup>_really_know what you’re doing; if not, you can seriously</sup> mess up a filesystem). 

#### **Name** 

sync — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
sync
```

The `sync` command flushes all disk caches to disk. The kernel usually buffers reads, writes, inode changes, and other disk-related activity in memory. `sync` writes the changes to disk. Normally, you don’t need to run this command, but if (say) you’re about to do something risky that might crash your machine, running `sync` immediately beforehand can’t hurt.

## **Backups and Remote Storage** 

|`dump`|Write a disk partition to a backup medium.|
|---|---|
|`restor`<br>`e`|Restore the results of a dump.|
|`cdreco`<br>`rd`|Burn a CD, DVD, or Blu-ray disc.|
|`rsync`|Mirror a set of files onto another device or<br>host.|
|`mt`|Control a tape drive.|

There are various way to back up your precious Linux files:

- Copy them to a backup medium, such as an external hard drive. Burn them onto a writeable CD, DVD, or Blu-ray disc. Mirror them to a remote machine. 

We aren’t presenting every available Linux command for backups. Some users prefer `cpio` , and for low-level disk copies, `dd` is invaluable. See the manpages for these programs if you are interested in them.

#### **Name** 

dump — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
dump [options] partition_or_files
```

The `dump` command writes an entire disk partition, or selected files, to a backup medium such as tape. It supports full and incremental backups, automatically figuring out which files need to be backed up (i.e., which have changed since the last backup). To restore files from the backup medium, use the `restore` command.

To perform a full backup of a given filesystem (say, _/usr_ ) to your backup device (say, _/dev/tape_ ), use the `−0` (zero) and `-u` options:

```
# dump −0 -u -f /dev/tape /usr
```

This is called a _level zero_ dump. The `-u` option writes a note to the file _/etc/dumpdates_ to say that the backup was performed.

Incremental backups may have levels 1 through 9: a level _`i`_ backup stores all new and changed files since the last level _`i-1`_ backup.

```
# dump −1 -u -f /dev/tape /usr
```

Don’t run `dump` on a “live” filesystem actively in use: unmount it first when possible.

#### **Name** 

restore — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
restore [options] [files]
```

The `restore` command reads a backup created by `dump` . It can then restore the files to disk, compare them against those on disk, and other operations. The friendliest way to use `restore` is with the `-i` flag for interactive operation, which lets you browse the dumped contents just like a filesystem, selecting files and directories, and finally restoring them.

```
# restore -i -f /dev/tape
```

`restore` then prompts you for commands like the ones listed below.

|`help`|Print a help message.|
|---|---|
|`quit`|Exit the program without restoring any files.|
|`cd`<br>_`dir`_|Like the shell’s`cd`command, set your current working directory within the dump for<br>working with files.|
|`ls`|Like the Linux`ls`command, view all files in the current working directory within the dump.|
|`pwd`|Like the shell’s`pwd`command, print the name of your current working directory within the<br>dump.|
|`add`|Add files or directories to the “extraction list”: the list of files you’ll want to restore. With<br>no arguments,`add`adds the current directory and all its files.|
|`add`<br>_`file`_|Add the file to the extraction list.|
|`add`<br>_`dir`_|Add the directory_dir_to the extraction list.|
|`delet`<br>`e`|The opposite of`add`: remove files from the extraction list. If run with no arguments,`delete`<br>removes the current directory (and its contents) from the extraction list.|
|`delet`<br>`e`<br>_`file`_|Remove the file from the extraction list.|

|`delet`<br>`e` _`dir`_|Remove the directory_dir_from the extraction list.|
|---|---|
|`extra`<br>`ct`|Restore all the files you added to the extraction list. (Tip: if your backup spans multiple<br>tapes, start with the last tape and work backward.)|

###### `restore` also works in other noninteractive modes: 

|`resto`<br>`re -x`|Restore everything from the backup into an existing filesystem. (`cd`into the root of the<br>desired filesystem first.)|
|---|---|
|`resto`<br>`re -r`|Restore everything from the backup into a freshly formatted disk partition. (`cd`into the root<br>of the desired filesystem first.)|
|`resto`<br>`re -t`|List the contents of the dump.|
|`resto`<br>`re -C`|Compare the dump against the original filesystem.|

#### **Name** 

cdrecord — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
cdrecord [options] tracks
```

The `cdrecord` command burns a writable CD, DVD, or Blu-ray disc. To burn the contents of a Linux directory onto a disc readable on Linux, Windows, and Macintosh systems:<sup>[</sup> <u>14</u><sup>]</sup>

1. Locate your disc writer’s device by running: 

```
$ cdrecord --scanbus
...
0,0,0     0) *
0,1,0     1) *
0,2,0     2) *
0,3,0     3) 'YAMAHA  ' 'CRW6416S  ' '1.0d' CD-ROM
```

The device in this case is 0,3,0.

2. Find out your CD writer’s speed for writing CD-R or CD-RW discs (whichever you’re using). Suppose it is a 6x writer of CD-Rs, so the speed is 6. 

3. Put the files you want to burn into a directory, say, _dir_ . Arrange them exactly as you’d like them on the CD. The directory _dir_ itself will not be copied to CD, just its contents. 

4. Burn the CD: 

```
$ DEVICE="0,3,0"
```

```
$ SPEED=6
```

```
$ mkisofs -R -l dir > mydisk.iso
```

```
$ cdrecord -v dev=${DEVICE} speed=${SPEED} mydisk.iso
```

or if your system is fast enough, you can do this with a single pipeline:

```
$ mkisofs -R -l dir \
```

```
  | cdrecord -v dev=${DEVICE} speed=${SPEED} -
```

`cdrecord` can burn music CDs as well, but you might want to use a friendlier, graphical program like `k3b` instead (see <u>Audio), which is built on</u> top of `cdrecord` .

[14<sup>]</sup> Specifically, an ISO9660 CD with Rock Ridge extensions. `mkisofs` can create other formats for `cdrecord` to burn: see `man mkisofs` .

#### **Name** 

rsync — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
rsync [options] source destination
```

The `rsync` command copies a set of files. It can make an exact copy, including file permissions and other attributes (called _mirroring_ ), or it can just copy the data. It can run over a network or on a single machine. `rsync` has many uses and over 50 options; we’ll present just a few common cases relating to backups.

To mirror the directory _D1_ and its contents into another directory _D2_ on a single machine:

```
$ rsync -a D1 D2
```

In order to mirror directory _D1_ over the network to another host, _server.example.com_ , where you have an account with username smith, secure the connection with SSH to prevent eavesdropping:

```
$ rsync -a -e ssh D1 smith@server.example.com:D2
```

#### **Useful options** 

|`-`<br>`o`|Copy the ownership of the files. (You might need superuser privileges on the remote host.)|
|---|---|
|`-`<br>`g`|Copy the group ownership of the files. (You might need superuser privileges on the remote<br>host.)|
|`-`<br>`p`|Copy the file permissions.|
|`-`<br>`t`|Copy the file timestamps.|
|`-`<br>`r`|Copy directories recursively, i.e., including their contents.|
|`-`<br>`l`|Permit symbolic links to be copied (not the files they point to).|
|`-`<br>`D`|Permit devices to be copied. (Superuser only.)|

|`-`<br>`a`|Mirroring: copy all attributes of the original files. This implies all of the options,`-ogptrlD`.|
|---|---|
|`-`<br>`v`|Verbose mode: print information about what’s happening during the copy. Add`--progress`to<br>display a numeric progress meter while files are copied.|
|`-`<br>`e`<br>`s`<br>`s`<br>`h`|Connect via`ssh`for more security. (Other remote shells are possible, but`ssh`is the most<br>common.)|

#### **Name** 

mt — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
mt [-f device] command
```

The `mt` (magnetic tape) command performs simple operations on a tape drive, such as rewinding, skipping forward and backward, and retensioning. Some common operations are:

|`status`|Show the status of the drive.|
|---|---|
|`rewind`|Rewind the tape.|
|`retensio`<br>`n`|Retension the tape.|
|`erase`|Erase the tape.|
|`offline`|Take the tape drive offline.|
|`eod`|Move forward on the tape to the end of<br>data.|

For example:

```
$ mt -f /dev/tape rewind
```

You can also move through the tape, file by file or record by record, but often you’ll use a tape reading/writing program for that, such as `tar` or `restore` .

## **Viewing Processes** 

|`ps`|List process.|
|---|---|
|`uptime`|View the system load.|
|`w`|List active processes for all users.|
|`top`|Monitor resource-intensive processes<br>interactively.|
|`gnome-system-`<br>`monitor`|Monitor system load and processes graphically.|
|`xload`|Simple, graphical monitor of system load.|
|`free`|Display free memory.|

A _process_ is a unit of work on a Linux system. Each program you run represents one or more processes, and Linux provides commands for viewing and manipulating them. Every process is identified by a numeric _process ID_ , or PID.

Processes are different from jobs (see <u>Shell Job Control): processes are part</u> of the operating system, whereas jobs are higher-level constructs known only to the shell in which they’re running. A running program comprises one or more processes; a job consists of one or more programs executed as a shell command.

#### **Name** 

ps — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
ps [options]
```

The `ps` command displays information about your running processes, and optionally the processes of other users.

```
$ ps
  PID TTY          TIME CMD
 4706 pts/2    00:00:01 bash
15007 pts/2    00:00:00 emacs
16729 pts/2    00:00:00 ps
```

`ps` has at least 80 options; we’ll cover just a few useful combinations. If the options seem arbitrary or inconsistent, it’s because the supplied `ps` command (GNU ps) incorporates the features of several other Unix `ps` commands, attempting to be compatible with all of them.

To view your processes:

```
$ ps -ux
```

all of user smith’s processes:

```
$ ps -U smith
```

all occurrences of a program:

```
$ ps -C program_name
```

processes on terminal _`N`_ :

```
$ ps -tN
```

particular processes 1, 2, and 3505:

```
$ ps -p1,2,3505
```

all processes with command lines truncated to screen width:

```
$ ps -ef
```

all processes with full command lines:

```
$ ps -efww
```

and all processes in a threaded view, which indents child processes below their parents:

```
$ ps -efH
```

Remember, you can extract information more finely from the output of `ps` using `grep` and other filter programs:

```
$ ps -ux | grep myprogram
```

#### **Name** 

uptime — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
uptime
```

The `uptime` command tells you how long the system has been running since the last boot.

```
$ uptime
 10:54pm  up 8 days,  3:44,  3 users,  load average: 0.89,
1.00, 2.15
```

This information is, from left to right: the current time (10:54pm), system uptime (8 days, 3 hours, 44 minutes), number of users logged in (3), and system load average for three time periods: one minute (0.89), five minutes (1.00), and fifteen minutes (2.15). The load average is the average number of processes ready to run in that time interval.

#### **Name** 

w — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
w [username]
```

The `w` command displays the current process running in each shell for all logged-in users:

```
$ w
 10:51pm  up 8 days,  3:42,  8 users,
 load average: 0.00, 0.00, 0.00
USER    TTY   FROM  LOGIN@  IDLE   JCPU   PCPU  WHAT
barrett pts/0 :0    Sat 2pm 27:13m 0.07s  0.07s emacs
jones   pts/1 host1 6Sep03   2:33m 0.74s  0.21s bash
smith   pts/2 host2 6Sep03   0.00s 13.35s 0.04s w
```

The top line is the same one printed by `uptime` . The columns indicate the user’s terminal, originating host or X display (if applicable), login time, idle time, two measures of the CPU time (run `man w` for details), and the current process. Provide a username to see only that user’s information.

For the briefest output, try `w -hfs` .

#### **Useful options** 

<!-- Start of picture text --> -h Don’t print the header line.<br>-f Don’t print the FROM column.<br>-s Don’t print the JCPU and PCPU<br>columns.<br><!-- End of picture text -->

#### **Name** 

top — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
top [options]
```

The `top` command lets you monitor the most active processes, updating the display at regular intervals (say, every second). It is a screen-based program that updates the display in place, interactively.

```
$ top
```

```
94 processes: 81 sleeping, 1 running, 0 zombie, 11 stopped
CPU states: 1.1% user, 0.5% system, 0.0% nice, 4.5% idle
Mem: 523812K av, 502328K used, 21484K free, 0K shrd, ...
Swap:  530104K av,  0K used, 530104K free  115300K cached
```

```
PID   USER PRI NI SIZE SHARE STAT %CPU %MEM TIME COMMAND
26265 smith 10 0  1092  840  R    4.7  0.2  0:00 top
    1 root   0 0   540  472  S    0.0  0.1  0:07 init
    2 root   0 0     0    0  SW   0.0  0.0  0:00 kflushd
```

While `top` is running, you can press keys to change its behavior, such as setting the update speed ( `s` ), hiding idle processes ( `i` ), or killing processes ( `k` ). Type `h` to see a complete list and `q` to quit.

#### **Useful options** 

|`-n`_`N`_|Perform_`N`_updates, then quit.|
|---|---|
|`-d`_`N`_|Update the display every_`N`_seconds.|
|`-p`_`N`_ `-`<br>`p`_`M`_|Display only the processes with PID_`N`_,_`M`_, ..., up to 20 processes.|
|`...`||
|`-c`|Display the command-line arguments of processes.|
|`-b`|Print on standard output noninteractively, without playing screen tricks.`top -b -n1 > outfile`<br>saves a quick snapshot to a file.|

#### **Name** 

gnome-system-monitor — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
gnome-system-monitor
```

`gnome-system-monitor` is a graphical tool that displays the system load of each processor, a list of running processes, and information on memory, filesystems, and more.

#### **Name** 

xload — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
xload
```

`xload` is a very simple monitoring tool that graphs processor load (Y axis) over time (X axis). If your computer has multiple processors or cores, `xload` does not provide separate views, and you’ll probably prefer a more powerful tool like `gnome-system-monitor` .

#### **Useful options** 

|`-update`<br>_`N`_|Update the display every_`N`_seconds (default 10).|
|---|---|
|`-scale` _`N`_|Divide the Y axis into_`N`_sections (default 1).`xload`may add more divisions as the load<br>goes up;_`N`_is the minimum visible at any time.|
|`-hl`<br>_`color`_|Use this_`color`_for the scale divider lines.|
|`-label` _`X`_|Print the text_`X`_above the graph (default = your hostname).|
|`-`<br>`nolabel`|Don’t print any text label above the graph.|
|`-`<br>`jumpscr`<br>`oll` _`N`_|When the graph reaches the right margin, scroll_`N`_pixels to the left and keep drawing<br>(default is half the window width).|

#### **Name** 

free — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
free [options]
```

The `free` command displays memory usage in kilobytes:

```
$ free
          total      used    free shared buffers cached
Mem:     523812    491944   31868      0   67856 199276
-/+ buffers/cache: 224812  299000
Swap:    530104         0  530104
```

The Linux kernel reserves as much memory as possible for caching purposes, so your best estimate of free RAM in the preceding output is in the `buffers/cache` row, `free` column (i.e., 299000K).

#### **Useful options** 

|`-s`<br>_`N`_|Run continuously and update the display every_`N`_<br>seconds.|
|---|---|
|`-b`|Display amounts in bytes.|
|`-m`|Display amounts in megabytes.|
|`-t`|Add a totals row at the bottom.|
|`-o`|Don’t display the “buffers/cache” row.|

## **Controlling Processes** 

|`kill`|Terminate a process (or send it a<br>signal).|
|---|---|
|`nice`|Invoke a program at a particular<br>priority.|
|`renic`<br>`e`|Change a process’s priority as it runs.|

Once processes are started, they can be stopped, restarted, killed, and reprioritized. We discussed some of these operations as handled by the shell in <u>Shell Job Control. Now we cover killing and reprioritizing.</u>

#### **Name** 

kill — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
kill [options] [process_ids]
```

The `kill` command sends a signal to a process. This can terminate a process (the default action), interrupt it, suspend it, crash it, and so on. You must own the process, or be the superuser, to affect it. To terminate process 13243, for example, run:

```
$ kill 13243
```

If this does not work — some programs catch this signal without terminating — add the `-KILL` or (equivalently) `-9` option:

```
$ kill -KILL 13243
```

which is virtually guaranteed to work. However, this is not a clean exit for the program, which may leave resources allocated (or cause other inconsistencies) upon its death.

If you don’t know the PID of a process, run `ps` and examine the output:

```
$ ps -uax | grep emacs
```

or even better, try the `pidof` command, which looks up and prints the PID of a process by its name:

```
$ pidof emacs
8374
```

Now you can kill a process knowing only its program name in a single line, using shell backquotes to execute `pidof` :

```
$ kill `pidof emacs`
```

In addition to the `kill` program in the filesystem (usually _/bin/kill_ ), most shells have built-in `kill` commands, but their syntax and behavior differ. However, they all support the following usage:

```
$ kill -N PID
$ kill -NAME PID
```

where _`N`_ is a signal number, and _`NAME`_ is a signal name without its leading “SIG” (e.g., use `-HUP` to send the `SIGHUP` signal). To see a complete list of signals transmitted by `kill` , run `kill -l` , though its output differs depending on which `kill` you’re running. For descriptions of the signals, run `man 7 signal` .

#### **Name** 

nice — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
nice [-level] command_line
```

When invoking a system-intensive program, you can be nice to the other processes (and users) by lowering its priority. That’s what the `nice` command is for: it sets a _nice level_ (an amount of “niceness”) for a process so it gets less attention from the Linux process scheduler.<sup>[</sup> <u>15</u><sup>]</sup> Here’s an example of setting a big job to run at nice level 7:

```
$ nice −7 sort VeryLargeFile > outfile
```

If you run `nice` without a level, 10 is used. Normal processes (run without `nice` ) run at level zero, which you can see by running `nice` with no arguments:

```
$ nice
0
```

The superuser can also lower the nice level, increasing a process’s priority:

```
# nice --10 myprogram
```

(Yes, that’s “dash negative 10”.) To see the `nice` levels of your jobs, use `ps` and look at the “NI” column:

```
$ ps -o pid,user,args,nice
```

[15<sup>]</sup> This is called “nicing” the process. You’ll hear the term used as a verb: “That process was niced to 12.”

#### **Name** 

renice — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
renice [+-N] [options] PID
```

While the `nice` command can invoke a program at a given nice level, `renice` changes the nice level of an already-running process. Here we increase the `nice` level (decrease the priority) of process 28734 by five:

```
$ renice +5 -p 28734
```

Ordinary users can increase the nice level of their own processes, while the superuser can also decrease it (increasing the priority) and can operate on any process. The valid range is −20 to +20, but avoid high negative numbers or you might interfere with vital system processes.

#### **Useful options** 

|`-p` _`pid`_|Affect the given process ID. You can omit the`-p`and just provide a PID (`renice +5`<br>`28734`).|
|---|---|
|`-u`|Affect all processes owned by the given user.|
|_`username`_||

## **Scheduling Jobs** 

|`sleep`|Wait a set number of seconds, doing<br>nothing.|
|---|---|
|`watch`|Run a program at set intervals.|
|`at`|Schedule a job for a single, future time.|
|`cronta`<br>`b`|Schedule jobs for many future times.|

If you need to launch programs at particular times or at regular intervals, Linux provides several scheduling tools at various degrees of complexity.

#### **Name** 

sleep — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
sleep time_specification
```

The `sleep` command simply waits a set amount of time. The given time specification can be an integer (meaning seconds) or an integer followed by the letter `s` (also seconds), `m` (minutes), `h` (hours), or `d` (days).

```
$ sleep 5m              Do nothing for 5 minutes
```

`sleep` is useful for delaying a command for a set amount of time:

```
$ sleep 10 && echo 'Ten seconds have passed.'
(10 seconds pass)
Ten seconds have passed.
```

#### **Name** 

watch — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
watch [options] command
```

The `watch` program executes a given command at regular intervals; the default is every two seconds. The command is passed to the shell (so be sure to quote or escape any special characters), and the results are displayed in a full-screen mode, so you can observe the output conveniently and see what has changed. For example, `watch -n 60 date` executes the `date` command once a minute, sort of a poor man’s clock. Type `^C` to exit.

#### **Useful options** 

|`-n`|Set the time between executions, in seconds.|
|---|---|
|_`seconds`_||
|`-d`|Highlight differences in the output, to emphasize what has changed from one execution to<br>the next.|

#### **Name** 

at — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
at [options] time_specification
```

The `at` command runs a shell command once at a specified time:

```
$ at 7am next sunday
at> echo Remember to go shopping | mail smith
at> lpr $HOME/shopping-list
at> ^D
<EOT>
job 559 at 2011-09-14 21:30
```

The time specifications understood by `at` are enormously flexible. In general, you can specify:

- A time followed by a date (not a date followed by a time) Only a date (assumes the current clock time) 

- Only a time (assumes the very next occurrence, whether today or tomorrow) 

- A special word like `now` , `midnight` , or `teatime` (16:00) Any of the preceding followed by an offset, like “+ 3 days” 

Dates are acceptable in many forms: `december 25 2012` , `25 december 2012` , `december 25` , `25 december` , `12/25/2012` , `25.12.2012` , `20121225` , `today` , `thursday` , `next thursday` , `next month` , `next year` , and more. Month names can be abbreviated to three letters ( `jan` , `feb` , `mar` , ...). Times are also flexible: `8pm` , `8 pm` , `8:00pm` , `8:00 pm` , `20:00` , and `2000` are equivalent. Offsets are a plus or minus sign followed by whitespace and an amount of time: `+ 3 seconds` , `+ 2 weeks` , `- 1 hour` , and so on.<sup>[</sup> <u>16</u><sup>]</sup> If you don’t specify a part of the date or time, `at` copies the missing information from the system date and time. So “next year” means one year from right now, “thursday” means the upcoming Thursday at the current clock time, “december 25” means the next upcoming December 25, and “4:30pm” means the very next occurrence of 4:30 p.m. in the future.

The command you supply to `at` is not evaluated by the shell until execution time, so wildcards, variables, and other shell constructs are not expanded until then. Also, your current environment (see `printenv` ) is preserved within each job so it executes as if you were logged in. Aliases, however, aren’t available to `at` jobs, so don’t include them.

To list your `at` jobs, use `atq` (“at queue”):

```
$ atq
```

```
559  2011-09-14 07:00 a smith
```

To delete an `at` job, run `atrm` (“at remove”) with the job number:

```
$ atrm 559
```

#### **Useful options** 

|`-f` _`filename`_|Read commands from the given file instead of standard<br>input.|
|---|---|
|`-c`|Print the job commands to standard output.|
|_`job_number`_||

> [16<sup>]</sup> Programmers can read the precise syntax in _/usr/share/doc/at/timespec_ . 

#### **Name** 

crontab — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
crontab [options] [file]
```

The `crontab` command, like `at` , schedules jobs for specific times. However, `crontab` is for recurring jobs, such as “Run this command at midnight on the second Tuesday of each month.” To make this work, you edit and save a file (called your _crontab file_ ), which automatically gets installed in a system directory ( _/var/spool/cron_ ). Once a minute, a Linux process called `cron` wakes up, checks your crontab file, and executes any jobs that are due.

- `$ crontab -e` 

Edit your crontab file in your default editor ( `$EDITOR` )

- `$ crontab -l` 

Print your crontab file on standard output

- `$ crontab -r` 

Delete your crontab file

- `$ crontab myfile` 

Install the file _myfile_ as your crontab file

The superuser can add the option `-u` _`username`_ to work with other users’ crontab files.

Crontab files contain one job per line. (Blank lines and comment lines beginning with “ `#` ” are ignored.) Each line has six fields, separated by whitespace. The first five fields specify the time to run the job, and the last is the job command itself.

_Minutes of the hour_

Integers between 0 and 59. This can be a single number ( `30` ), a sequence of numbers separated by commas ( `0,15,30,45` ), a range ( `20–30` ), a sequence of ranges ( `0-15,50-59` ), or an asterisk to mean “all.” You can also specify “every _`n`_ th time” with the suffix `/` _`n`_ ; for instance, both `*/12` and `0-59/12` mean `0,12,24,36,48` (i.e., every 12 minutes).

_Hours of the day_

###### Same syntax as for minutes. 

###### _Days of the month_ 

Integers between 1 and 31; again, you may use sequences, ranges, sequences of ranges, or an asterisk.

###### _Months of the year_ 

Integers between 1 and 12; again, you may use sequences, ranges, sequences of ranges, or an asterisk. Additionally, you may use threeletter abbreviations ( `jan` , `feb` , `mar` , ...), but not in ranges or sequences.

###### _Days of the week_ 

Integers between 0 (Sunday) and 6 (Saturday); again, you may use sequences, ranges, sequences of ranges, or an asterisk. Additionally, you may use three-letter abbreviations ( `sun` , `mon` , `tue` , ...), but not in ranges or sequences.

###### _Command to execute_ 

Any shell command, which will be executed in your login environment, so you can refer to environment variables like `$HOME` and expect them to work. Use only absolute paths to your commands (e.g., _/usr/bin/who_ instead of `who` ) as a general rule.

Some example time specifications are:

|`*    *`<br>`*`|`*    *`|Every minute|
|---|---|---|
|`45   *`<br>`*`|`*    *`|45 minutes after each hour (1:45, 2:45, etc.)|
|`45   9`<br>`*`|`*    *`|Every day at 9:45 am|
|`45   9`<br>`*`|`8    *`|The eighth day of every month at 9:45 am|
|`45   9`<br>`*`|`8    12`|Every December 8 at 9:45 am|
|`45   9`<br>`*`|`8    dec`|Every December 8 at 9:45 am|
|`45   9`<br>`6`|`*    *`|Every Saturday at 9:45 am|

|`45`<br>`sat`|`9    *    *`|<br>Every Saturday at 9:45 am|
|---|---|---|
|`45`<br>`6`|`9    *    12`|<br>Every Saturday in December, at 9:45 am|
|`45`<br>`6`|`9    8    12`|<br>Every Saturday in December, plus December 8, at 9:45<br>am|

If the command produces any output upon execution, `cron` will email it to you.

## **Logins, Logouts, and Shutdowns** 

We assume you know how to log into your Linux account. To log out using GNOME or KDE, choose Logout from the main menu. To log out from a remote shell, just close the shell (type `exit` or `logout` ).

Never simply turn off the power to a Linux system: it needs a more graceful shutdown. To perform a shutdown from GNOME or KDE, use the main menu. To perform a shutdown from a shell, run the `shutdown` command as the superuser, as follows.

#### **Name** 

shutdown — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
shutdown [options] time [message]
```

The `shutdown` command halts or reboots a Linux system; only the superuser may run it. Here’s a command to halt the system in 10 minutes, broadcasting the message “scheduled maintenance” to all users logged in:

```
# shutdown -h +10 "scheduled maintenance"
```

The _`time`_ may be a number of minutes preceded by a plus sign, like +10; an absolute time in hours and minutes, like 16:25; or the word `now` to mean immediately.

With no options, `shutdown` puts the system into single-user mode, a special maintenance mode in which only one person is logged in (at the system console), and all nonessential services are off. To exit single-user mode, either perform another `shutdown` to halt or reboot, or type `^D` to bring up the system in normal, multiuser mode.

#### **Useful options** 

> `-r`<sup>Reboot the system.</sup> 

> `-h`<sup>Halt the system.</sup> 

> `-k`<sup>Kidding: don’t really perform a shutdown, just broadcast warning messages to all users as if the</sup> system were going down. 

> `-c`<sup>Cancel a shutdown in progress (omit the</sup><sup>_`time`_argument).</sup> 

> `-f`<sup>On reboot, skip the usual filesystem check performed by the</sup><sup>`fsck`program (described in</sup> <u>Disks and Filesystems).</u> 

> `-F`<sup>On reboot, require the usual filesystem check.</sup> 

For technical information about shutdowns, single-user mode, and various system states, see the manpages for `init` and `inittab` .

## **Users and Their Environment** 

|`lognam`<br>`e`|Print your login name.|
|---|---|
|`whoami`|Print your current, effective username.|
|`id`|Print the user ID and group membership of a<br>user.|
|`who`|List logged-in users, long output.|
|`users`|List logged-in users, short output.|
|`finger`|Print information about users.|
|`last`|Determine when someone last logged in.|
|`printe`<br>`nv`|Print your environment.|

Who are you? Only the system knows for sure. This grab-bag of programs tells you all about _users_ : their names, login times, and properties of their environment.

#### **Name** 

logname — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
logname
```

The `logname` command prints your login name. It might seem trivial, but it’s useful in shell scripts.

```
$ logname
smith
```

#### **Name** 

whoami — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
whoami
```

The `whoami` command prints the name of the current, effective user. This may differ from your login name (the output of `logname` ) if you’ve used the `su` command. This example distinguishes `whoami` from `logname` :

```
$ logname
smith
$ whoami
smith
$ su
Password: ********
# logname
smith
# whoami
root
```

#### **Name** 

id — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
id [options] [username]
```

Every user has a unique, numeric _user ID_ , and a default group with a unique, numeric _group ID_ . The `id` command prints these values along with their associated user and group names:

```
$ id
uid=500(smith) gid=500(smith)
groups=500(smith),6(disk),490(src),501(cdwrite)
```

#### **Useful options** 

> `-u`<sup>Print the effective user ID and exit.</sup> 

> `-g`<sup>Print the effective group ID and exit.</sup> 

> `-G`<sup>Print the IDs of all other groups to which the user belongs.</sup> 

> `-n`<sup>Print names (for users and groups) rather than numeric IDs. Must be combined with</sup><sup>`-u`,</sup><sup>`-g`, or</sup><sup>`-G`.</sup> For example, `id -Gn` produces the same output as the `groups` command. 

> `-r`<sup>Print login values instead of effective values. Must be combined with</sup><sup>`-u`,</sup><sup>`-g`, or</sup><sup>`-G`.</sup> 

#### **Name** 

who — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
who [options] [filename]
```

The `who` command lists all logged-in users, one user shell per line:

```
$ who
smith    pts/0    Sep  6 17:09 (:0)
barrett  pts/1    Sep  6 17:10 (10.24.19.240)
jones    pts/2    Sep  8 20:58 (192.168.13.7)
jones    pts/4    Sep  3 05:11 (192.168.13.7)
```

Normally, `who` gets its data from the file _/var/run/utmp_ . The _`filename`_ argument can specify a different data file, such as _/var/log/wtmp_ for past logins or _/var/log/btmp_ for failed logins.<sup>[</sup> <u>17</u><sup>]</sup>

#### **Useful options** 

|`-H`|Print a row of headings as the first line.|
|---|---|
|`--`<br>`look`<br>`up`|For remotely logged-in users, print the hostnames of origin.|
|`-u`|Also print each user’s idle time at his/her terminal.|
|`-T`|Also indicate whether each user’s terminal is writable (see`mesg`in<br>Instant Messaging). A plus<br>sign means yes, a minus sign means no, and a question mark means unknown.|
|`-m`|Display information only about yourself, i.e., the user associated with the current terminal.|
|`-q`|Quick display of usernames only, and a count of users. Much like the`users`command, but it<br>adds a count.|

[17<sup>]</sup> If your system is configured to log this information.

#### **Name** 

users — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
users [filename]
```

The `users` command prints a quick listing of users who have login sessions. If a user is running multiple shells, she appears multiple times.

```
$ users
barrett jones smith smith smith
```

Like the `who` command, `users` reads _/var/log/utmp_ by default but can read from another supplied file instead.

#### **Name** 

finger — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
finger [options] [user[@host]]
```

The `finger` command prints logged-in user information in a short form:

```
$ finger
Login     Name             Tty      Idle  Login Time
smith     Sandy Smith      :0             Sep  6 17:09
barrett   Daniel Barrett   :pts/1     24  Sep  6 17:10
jones     Jill Jones       :pts/2         Sep  8 20:58
```

###### or a long form: 

```
$ finger smith
Login: smith                       Name: Sandy Smith
Directory: /home/smith             Shell: /bin/bash
On since Sat Sep  6 17:09 (EDT) on :0
Last login Mon Sep  8 21:07 (EDT) on pts/6 from localhost
No mail.
Project:
Enhance world peace
Plan:
Mistrust first impulses; they are always right.
```

The _`user`_ argument can be a local username or a remote user in the form _`user@host`_ . Remote hosts will respond to `finger` requests only if they are configured to do so.

#### **Useful options** 

> `-l`<sup>Print in long format.</sup> 

> `-s`<sup>Print in short format.</sup> 

> `-p`<sup>Don’t display the Project and Plan sections, which are ordinarily read from the user’s</sup><sup>_~/.project_</sup> and _~/.plan_ files, respectively. 

#### **Name** 

last — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
last [options] [users] [ttys]
```

The `last` command displays a history of logins, in reverse chronological order.

```
$ last
barrett pts/3  localhost Mon Sep 8 21:07 - 21:08 (00:01)
smith   pts/6  :0        Mon Sep 8 20:25 - 20:56 (00:31)
barrett pts/4  myhost    Sun Sep 7 22:19 still logged in
...
```

You may provide usernames or tty names to limit the output.

#### **Useful options** 

|`-`_`N`_|Print only the latest_`N`_lines of output, where_`N`_is a positive integer.|
|---|---|
|`-i`|Display IP addresses instead of hostnames.|
|`-R`|Don’t display hostnames.|
|`-x`|Also display system shutdowns and changes in system runlevel (e.g., from single-user<br>mode into multiuser mode).|
|`-f`<br>_`filena`_<br>_`me`_|Read from some other data file than_/var/run/wtmp_; see the`who`command for more details.|

#### **Name** 

printenv — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
printenv [environment_variables]
```

The `printenv` command prints all environment variables known to your shell and their values:

```
$ printenv
HOME=/home/smith
MAIL=/var/spool/mail/smith
NAME=Sandy Smith
SHELL=/bin/bash
...
```

or only specified variables:

```
$ printenv HOME SHELL
```

```
/home/smith
```

```
/bin/bash
```

## **User Account Management** 

|`userad`<br>`d`|Create an account.|
|---|---|
|`userde`<br>`l`|Delete an account.|
|`usermo`<br>`d`|Modify an account.|
|`passwd`|Change a password.|
|`chfn`|Change a user’s personal<br>information.|
|`chsh`|Change a user’s shell.|

The installation process for your Linux distro undoubtedly prompted you to create a superuser account (root), and possibly also an ordinary user account (presumably for yourself). But you might want to create other accounts, too.

Creating users is an important job not to be taken lightly. Every account is a potential avenue for an intruder to enter your system, so every user should have a strong, hard-to-guess password.

#### **Name** 

useradd — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
useradd [options] username
```

The `useradd` command lets the superuser create a user account.

```
# useradd smith
```

Its defaults are not very useful (run `useradd -D` to see them), so be sure to supply all desired options. For example:

```
# useradd -d /home/smith -s /bin/bash -g users smith
```

#### **Useful options** 

|`-d` _`dir`_|Set the user’s home directory to be_`dir`_.|
|---|---|
|`-s` _`shell`_|Set the user’s login shell to be_`shell`_.|
|`-u` _`uid`_|Set the user’s ID to be_`uid`_. Unless you know what you’re doing, omit this option<br>and accept the default.|
|`-c` _`string`_|Set the user’s comment field (historically called the GECOS field). This is usually<br>the user’s full name, but it can be any string. The`chfn`command can also set this<br>information.|
|`-g` _`group`_|Set the user’s initial (default) group to_`group`_, which can either be a numeric group<br>ID or a group name, and which must already exist.|
|`-G`<br>_`group1,group2,.`_<br>_`..`_|Make the user a member of the additional, existing groups_`group1`_,_`group2`_, and so on.|
|`-m`|Copy all files from your system skeleton directory,_/etc/skel_, into the newly created<br>home directory. The skeleton directory traditionally contains minimal (skeletal)<br>versions of initialization files, like_~/.bash_profile_, to get new users started. If you<br>prefer to copy from a different directory, add the`-k`option (`-k` _`dirname`_).|

#### **Name** 

userdel — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
userdel [-r] username
```

The `userdel` command deletes an existing user.

```
# userdel smith
```

It does not delete the files in the user’s home directory unless you supply the `-r` option. Think carefully before deleting a user; consider deactivating the account instead (with `usermod -L` ). And make sure you have backups of all the user’s files before deleting them: you might need them again someday.

#### **Name** 

usermod — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
usermod [options] username
```

The `usermod` command modifies the given user’s account in various ways, such as changing a home directory:

```
# usermod -d /home/another smith
```

#### **Useful options** 

|`-d` _`dir`_|Change the user’s home directory to_`dir`_.|
|---|---|
|`-l` _`username`_|Change the user’s login name to_`username`_. Think carefully before doing this, in case<br>anything on your system depends on the original name. And don’t change system<br>accounts (root, daemon, and so on) unless you really know what you’re doing!|
|`-s` _`shell`_|Change the user’s login shell to_`shell`_.|
|`-g` _`group`_|Change the user’s initial (default) group to_`group`_, which can either be a numeric<br>group ID or a group name, and which must already exist.|
|`-G`<br>_`group1,group2,.`_<br>_`..`_|Make the user a member_only_of the additional, existing groups_`group1`_,_`group2`_, and<br>so on. If the user previously belonged to other groups, but you don’t specify them<br>here, the user will no longer belong to them.|
|`-L`|Disable (lock) the account so the user cannot log in.|
|`-U`|Unlock the account after a lock (`-L`) operation.|

#### **Name** 

passwd — stdin  stdout  - file  -- opt  --help  --version

**Synopsis**

```
passwd [options] [username]
```

The `passwd` command changes a login password, yours by default:

```
$ passwd
```

or another user’s password if run by the superuser:

```
# passwd smith
```

`passwd` does have options, most of them related to password expiration. Use them only in the context of a well-thought-out security policy.

#### **Name** 

chfn — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
chfn [options] [username]
```

The `chfn` (change finger) command updates a few pieces of personal information maintained by the system: real name, home telephone, office telephone, and office location, as displayed by the `finger` command. Invoked without a username, `chfn` affects your account; invoked with a username (by root), it affects that user. With no options, `chfn` will prompt you for the desired information.

```
$ chfn
Password: ********
Name [Shawn Smith]: Shawn E. Smith
Office [100 Barton Hall]:
Office Phone [212-555-1212]: 212-555-1234
Home Phone []:
```

#### **Useful options** 

<!-- Start of picture text --> -f name Change the full name to  name .<br>-h phone Change the home phone number to<br>phone .<br>-p phone Change the office phone number to<br>phone .<br>-o Change the office location to  office .<br>office<br><!-- End of picture text -->

#### **Name** 

chsh — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
chsh [options] [username]
```

The `chsh` (change shell) command sets your login shell program. Invoked without a username, `chsh` affects your account; invoked with a username (by root), it affects that user. With no options, `chsh` will prompt you for the desired information.

```
$ chsh
Changing shell for smith.
Password: *******
New shell [/bin/bash]: /bin/tcsh
```

The new shell must be listed in _/etc/shells_ .

#### **Useful options** 

`-s` Specify the new shell. _`shell`_ `-l` List all permissible shells.

## **Becoming the Superuser** 

Normal users, for the most part, can modify only the files they own. One special user, called the _superuser_ or _root_ , has full access to the machine and can do anything on it. To become the superuser, log in as yourself and type:

```
$ su -l
Password: *******
#
```

You will be prompted for the superuser password (which we presume you know, if it’s your computer). Your shell prompt will change to a hash mark ( `#` ) to indicate you are the superuser. When finished executing commands as the superuser, type `^D` or run `exit` to end the superuser shell and become yourself again.

If you provide a username to `su` :

```
$ su -l sophia
Password: ********
```

you can become that user (provided you know her password).

###### **SUDO** 

`su` is the simplest way to obtain superuser privileges. A more complex program, `sudo` , runs one command at a time as the superuser, using _your own_ password, if your system is configured to use it:

```
$ sudo rm protected_file
Password: ********Your own password
```

`sudo` is superior for systems with multiple superusers, as it provides precise control over privileges (in the _/etc/sudoers_ file) and even logs the commands that get run. A full discussion is beyond the scope of this book: see `man sudo` and <u>http://www.gratisoft.us/sudo/</u> for full details.

#### **Name** 

#### **Useful options** 

|`-l`|Run a login shell. You almost always want this option, so root’s proper search path is set.|
|---|---|
|`-m`|Preserve your current environment variables in the new shell.|
|`-c`<br>_`command`_|Run just this_`command`_(as the other user) and exit. If you need to do this a lot, read the`sudo`<br>manpage.|
|`-s`<br>_`shell`_|Run the given shell (e.g.,_/bin/bash_).|

## **Group Management** 

|`groups`|Print the group membership of a<br>user.|
|---|---|
|`groupad`<br>`d`|Create a group.|
|`groupde`<br>`l`|Delete a group.|
|`groupmo`<br>`d`|Modify a group.|

A _group_ is a set of accounts treated as a single entity. If you give permission for a group to take some action (such as modify a file), then all members of that group can take it. For example, you can give full permissions for the group `friends` to read, write, and execute the file _/tmp/sample_ :

```
$ groups
users smith friends
$ chgrp friends /tmp/sample
$ chmod 770 /tmp/sample
$ ls -l /tmp/sample
-rwxrwx---  1 smith friends  2874 Oct 20 22:35 /tmp/sample
```

To add users to a group, edit _/etc/group_ as root.<sup>[</sup> <u>18</u><sup>]</sup> To change the group ownership of a file, recall the `chgrp` commands from <u>File Properties .</u>

[18<sup>]</sup> Different systems may store the group member list in other ways.

#### **Name** 

groups — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
groups [usernames]
```

The `groups` command prints the Linux groups to which you belong, or to which other users belong:

```
$ whoami
smith
$ groups
smith users
$ groups jones root
jones : jones users
root : root bin daemon sys adm disk wheel src
```

#### **Name** 

groupadd — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
groupadd [options] group
```

The `groupadd` command creates a group. In most cases, you should use the `-f` option to prevent duplicate groups from being created:

```
# groupadd -f friends
```

#### **Useful options** 

|`-g`<br>_`gid`_|Specify your own numeric group ID instead of letting`groupadd`choose<br>one.|
|---|---|
|`-f`|If the specified group exists already, complain and exit.|

#### **Name** 

groupdel — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
groupdel group
```

The `groupdel` command deletes an existing group.

```
# groupdel friends
```

Before doing this, it’s a good idea to identify all files that have their group ID set to the given group, so you can deal with them later:

```
# find / -group friends -print
```

because `groupdel` does not change the group ownership of any files. It simply removes the group name from the system’s records. If you list such files, you’ll see a numeric group ID in place of a group name.

#### **Name** 

groupmod — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
groupmod [options] group
```

The `groupmod` command modifies the given group, changing its name or group ID.

```
# groupmod -n newname friends
```

`groupmod` does not affect any files owned by this group: it simply changes the ID or name in the system’s records. Be careful when changing the ID, or these files will have group ownership by a nonexistent group.

#### **Useful options** 

<!-- Start of picture text --> -n Change the group’s name to  name<br>name (safe).<br>-g gid Change the group’s ID to  gid  (risky).<br><!-- End of picture text -->

## **Host Information** 

|`uname`|Print basic system information.|
|---|---|
|`hostname`|Print the system’s hostname.|
|`dnsdomainna`<br>`me`|Same as`hostname -d`.|
|`domainname`|Same as`hostname -y`.|
|`nisdomainna`<br>`me`|Same as`hostname -y`.|
|`ypdomainnam`<br>`e`|Same as`hostname -y`.|
|`ip`|Set and display network interface information.|
|`ifconfig`|Older command to set and display network interface<br>information.|

Every Linux machine (or _host_ ) has a name, a network IP address, and other properties. Here’s how to display this information.

#### **Name** 

uname — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
uname [options]
```

The `uname` command prints fundamental information about your computer:

```
$ uname -a
Linux server.example.com 2.6.32-35-generic-pae #78-Ubuntu
 SMP Tue Oct 11 17:01:12 UTC 2011 i686 GNU/Linux
```

This includes the kernel name (Linux), hostname (server.example.com), kernel release (2.6.32-35-generic-pae), kernel version (#78-Ubuntu SMP Tue Oct 11 17:01:12 UTC 2011), hardware name (i686), processor type (i686), and operating system name (GNU/Linux). Each of these values can be printed individually using options.

#### **Useful options** 

<!-- Start of picture text --> -a All information.<br>-s Only the kernel name (the default).<br>-n Only the hostname, as with the  hostname<br>command.<br>-r Only the kernel release.<br>-v Only the kernel version.<br>-m Only the hardware name.<br>-p Only the processor type.<br>-i Only the hardware platform.<br>-o Only the operating system name.<br><!-- End of picture text -->

#### **Name** 

hostname — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
hostname [options] [name]
```

The `hostname` command prints the name of your computer. Depending on how you have things set up, this might be the fully qualified hostname:

```
$ hostname
myhost.example.com
```

or your short hostname:

```
$ hostname
myhost
```

You can also set your hostname, as root:<sup>[</sup> <u>19</u><sup>]</sup>

```
# hostname orange
```

However, hostnames and nameservers are complicated topics well beyond the scope of this book. Don’t just blindly start setting hostnames!

#### **Useful options** 

|`-i`|Print your host’s IP address.|
|---|---|
|`-a`|Print your host’s alias name.|
|`-s`|Print your host’s short name.|
|`-f`|Print your host’s fully qualified name.|
|`-d`|Print your host’s DNS domain name.|
|`-y`|Print your host’s NIS or YP domain name.|
|`-F`<br>_`hostfile`_|Set your hostname by reading the name from file<br>_`hostfile`_.|

[19<sup>]</sup> This change might not survive a reboot. Some Linux distros require additional steps, such as placing the hostname into a configuration file that is read at boot time. Consult the documentation for your distro.

#### **Name** 

ip — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
ip [options] objectcommand...
```

The `ip` command displays and sets various aspects of your computer’s network interface. This topic is beyond the scope of the book, but we’ll teach you a few tricks.

You can get information about the default network interface (usually called _eth0_ ):

```
$ ip addr show eth0
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 ...
  link/ether 00:50:ba:48:4f:ba brd ff:ff:ff:ff:ff:ff
  inet 192.168.0.21/24 brd 192.168.0.255 scope global eth0
  inet6 fe80::21e:8cff:fe53:41e4/64 scope link
    valid_lft forever preferred_lft forever
```

This includes your MAC address (00:50:ba:48:4f:ba), your IP address (192.168.0.21), and various other information. To view all loaded network interfaces, run:

```
$ ip addr show
```

Some other useful commands for displaying network information include: `ip help`

See usage information for all these commands

```
ip addr
```

Display IP addresses of your network devices

```
ip maddr
```

Display multicast addresses of your network devices

```
ip link
```

Display attributes of your network devices

```
ip route
```

Display your routing table

```
ip monitor
```

Begin monitoring your network devices; type `^C` to stop Each of these commands has various options: add `help` on the end (e.g., `ip link help` ) for usage. Additionally, `ip` can modify your network: configuring your network devices, managing routing tables and rules, creating tunnels, and more. It’s part of a suite of tools called _iproute2_ . You’ll need networking experience to understand this complex command; see the `ip` manpage to get started, or visit <u>http://lartc.org.</u>

#### **Name** 

ifconfig — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
ifconfig [options] interface
```

The `ifconfig` command is an ancestor of `ip` . It is still found on many Linux systems but is less powerful (some would call it obsolete). We’ll cover a few simple commands here, but you should be using `ip` instead. To display information about the default network interface (usually called _eth0_ ):

```
$ ifconfig eth0
eth0  Link encap:Ethernet  HWaddr 00:50:BA:48:4F:BA
      inet addr:192.168.0.10  Bcast:192.168.0.255 ...
      UP BROADCAST RUNNING MULTICAST  MTU:1500 ...
      RX packets:1955231 errors:0 dropped:0 overruns:0 ...
      TX packets:1314765 errors:0 dropped:0 overruns:0 ...
      collisions:0 txqueuelen:100
      ...
```

This includes your MAC address (00:50:BA:48:4F:BA), your IP address (192.168.0.21), your netmask (255.255.255.0), and various other information. To view all loaded network interfaces, run:

```
$ ifconfig -a
```

## **Host Location** 

|`host`|Look up hostnames, IP addresses, and DNS<br>info.|
|---|---|
|`whois`|Look up the registrants of Internet domains.|
|`ping`|Check if a remote host is reachable.|
|`tracerou`<br>`te`|View the network path to a remote host.|

When dealing with remote computers, you might want to know more about them. Who owns them? What are the IP addresses? Where on the network are they located?

#### **Name** 

host — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
host [options] name [server]
```

The `host` command looks up the hostname or IP address of a remote machine by querying DNS.

```
$ host www.ubuntu.org
www.ubuntu.com has address 91.189.90.41
$ host 91.189.90.41
41.90.189.91.in-addr.arpa domain name pointer
 jujube.canonical.com.
```

It can also find out much more:

```
$ host -a www.ubuntu.org
Trying "www.ubuntu.org"
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 16652
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ...
;; QUESTION SECTION:
;www.ubuntu.org.                     IN      ANY
;; ANSWER SECTION:
www.ubuntu.org.      60      IN      CNAME   ubuntu.org.
```

though a full discussion of this output is beyond the scope of this book. The final, optional “server” parameter specifies a particular nameserver for the query:

```
$ host www.ubuntu.org ns2.dondominio.com
Using domain server:
Name: ns2.dondominio.com
Address: 93.93.67.2#53
Aliases:
```

```
www.ubuntu.org is an alias for ubuntu.org.
ubuntu.org has address 147.83.195.55
ubuntu.org mail is handled by 10 mx2.upc.es.
ubuntu.org mail is handled by 10 mx1.upc.es.
```

To see all options, type `host` by itself.

#### **Useful options** 

> `-a`<sup>Display all available information.</sup> 

> `-t`<sup>Choose the type of nameserver query:</sup><sup>`A`,</sup><sup>`AXFR`,</sup><sup>`CNAME`,</sup><sup>`HINFO`,</sup><sup>`KEY`,</sup><sup>`MX`,</sup><sup>`NS`,</sup><sup>`PTR`,</sup><sup>`SIG`,</sup><sup>`SOA`, and so</sup> on. 

Here’s an example of the `-t` option to locate MX records:

```
$ host -t MX redhat.com
redhat.com mail is handled by 5 mx1.redhat.com.
redhat.com mail is handled by 10 mx2.redhat.com.
```

If the `host` command doesn’t do what you want, try `dig` , another powerful DNS lookup utility. You might also encounter the `nslookup` command, mostly obsolete but still found on some Linux and Unix systems.

#### **Name** 

whois — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
whois [options] domain_name
```

The `whois` command looks up the registration of an Internet domain:

```
$ whois linuxmint.com
...
Domain name:    LINUXMINT.COM
...
 Administrative Contact:
    Lefebvre, Clement
...
 Technical Contact:
    Hostmaster, Servage
...
Registrar of Record: TUCOWS, INC.
Record expires on 07-Jun-2012.
Record created on 07-Jun-2006.
...
```

plus a few screens full of legal disclaimers from the registrar.

#### **Useful options** 

`-h` Perform the lookup at the given registrar’s server. For example, `whois -h` _`registr`_ `whois.networksolutions.com yahoo.com` . _`ar`_

`-p` _`port`_ Query the given the TCP port instead of the default, 43 (the `whois` service).

#### **Name** 

ping — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
ping [options] host
```

The `ping` command tells you if a remote host is reachable. It sends small packets (ICMP packets to be precise) to a remote host and waits for responses.

```
$ ping google.com
PING google.com (74.125.226.144) from 192.168.0.10 :
56(84) bytes of data.
64 bytes from www.google.com (74.125.226.144): icmp_seq=0
  ttl=49 time=32.390 msec
64 bytes from www.google.com (74.125.226.144): icmp_seq=1
  ttl=49 time=24.208 msec
^C
--- google.com ping statistics ---
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max/mdev = 24.208/28.299/32.390/4.091 ms
```

#### **Useful options** 

`-c` Ping at most _`N`_ times. _`N`_

`-i` Wait _`N`_ seconds (default 1) between pings.

```
N
```

- `-n` Print IP addresses in the output, rather than hostnames. 

#### **Name** 

traceroute — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
traceroute [options] host [packet_length]
```

The `traceroute` command prints the network path from your local host to a remote host, and the time it takes for packets to traverse the path.

- `$ traceroute yahoo.com` 

- `1 server.example.com (192.168.0.20) 1.397 ms ...` 

- `2  10.221.16.1 (10.221.16.1) 15.397 ms ...` 

- `3  gbr2-p10.cb1ma.ip.att.net (12.123.40.190) 4.952 ms ...` 

- `16  p6.www.dcn.yahoo.com (216.109.118.69)  * ...` 

Each host in the path is sent three “probes” and the return times are reported. If five seconds pass with no response, `traceroute` prints an asterisk. Also, `traceroute` may be blocked by firewalls or unable to proceed for various reasons, in which case it prints a symbol:

|Symb||
|---|---|
|ol|Meaning|
|`!F`|Fragmentation needed.|
|`!H`|Host unreachable.|
|`!N`|Network unreachable.|
|`!P`|Protocol unreachable.|
|`!S`|Source route failed.|
|`!X`|Communication administratively<br>prohibited.|
|`!`_`N`_|ICMP unreachable code_`N`_.|

The default packet size is 40 bytes, but you can change this with the final, optional _`packet_length`_ parameter (e.g., `traceroute myhost 120` ).

#### **Useful options** 

<!-- Start of picture text --> -n Numeric mode: print IP addresses instead of<br>hostnames.<br>-w Change the timeout from five seconds to  N  seconds.<br>N<br><!-- End of picture text -->

## **Network Connections** 

|`ssh`|Securely log into a remote host, or run commands on<br>it.|
|---|---|
|`teln`<br>`et`|Log into a remote host (insecure!).|
|`scp`|Securely copy files to/from a remote host (batch).|
|`sftp`|Securely copy files to/from a remote host (interactive).|
|`ftp`|Copy files to/from a remote host (interactive,<br>insecure!).|

With Linux, it’s easy to establish network connections from one machine to another for remote logins and file transfers. Just make sure you do it securely.

#### **Name** 

ssh — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
ssh [options] host [command]
```

The `ssh` (Secure Shell) program securely logs you into a remote machine where you already have an account:

```
$ ssh remote.example.com
```

Alternatively, it can invoke a program on that remote machine without logging you in:

```
$ ssh remote.example.com who
```

`ssh` encrypts all data that travels across its connection, including your username and password (which you’ll need to access the remote machine). The SSH protocol also supports other ways to authenticate, such as public keys and host IDs. See `man sshd` for details.

#### **Useful options** 

|`-l`<br>_`us`_<br>_`er`_|Specify your remote username; otherwise,`ssh`assumes your local username. You can also use<br>the syntax_`username`_@_`host`_:|
|---|---|
||`$ ssh smith@server.example.com`|
|`-p`<br>_`po`_|Use a_`port`_number other than the default (22).|
|_`rt`_||
|`-t`|Allocate a tty on the remote system; useful when trying to run a remote command with an<br>interactive user interface, such as a text editor.|
|`-v`|Produce verbose output, useful for debugging.|

#### **Name** 

telnet — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
telnet [options] host [port]
```

The `telnet` program logs you into a remote machine where you already have an account.

```
$ telnet remote.example.com
```

Avoid `telnet` for remote logins: most implementations are insecure and send your password over the network in plain text for anyone to steal. Use `ssh` instead, which protects your password and data via encryption. There are two exceptions:

In a Kerberos environment, using enhanced (“kerberized”) telnet software on both the client and server side. See <u>http://web.mit.edu/kerberos/</u> for more information. Connecting to a remote port when you aren’t sending any sensitive information at all. For example, to check for the presence of a web server (port 80) on a remote system:

```
$ telnet remote.example.com 80
Trying 192.168.55.21...
Connected to remote.example.com (192.168.55.21).
Escape character is '^]'.
xxxType some junk and press Enter
<HTML><HEAD>      Yep, it’s a web server
<TITLE>400 Bad Request</TITLE>
</HEAD><BODY>
<H1>Bad Request</H1>
Your browser sent a request that
this server could not understand.<P>
</BODY></HTML>
Connection closed by foreign host.
```

To discourage you further from using `telnet` , we aren’t even going to describe its options.

#### **Name** 

scp — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
scp local_spec remote_spec
```

The `scp` (secure copy) command copies files and directories from one computer to another in batch. (For an interactive user interface, see `sftp` .) It encrypts all communication between the two machines. As a simple example, `scp` can copy a local file to a remote machine:

```
$ scp myfile remote.example.com:newfile
```

recursively copy a directory to a remote machine:

```
$ scp -r mydir remote.example.com:
```

copy a remote file to your local machine:

```
$ scp remote.example.com:myfile .
```

or recursively copy a remote directory to your local machine:

```
$ scp -r remote.example.com:mydir .
```

To specify an alternate username on the remote system, use the _`username`_ @ _`host`_ syntax:

```
$ scp myfile smith@remote.example.com:
```

#### **Useful options** 

> `-p`<sup>Duplicate all file attributes (permissions, timestamps) when</sup> copying. 

> `-r`<sup>Recursively copy a directory and its contents.</sup> 

> `-v`<sup>Produce verbose output, useful for debugging.</sup> 

#### **Name** 

sftp — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
sftp (hostusername@host)
```

The `sftp` program copies files interactively and securely between two computers. (As opposed to `scp` , which copies files in batch.) The user interface is much like that of `ftp` , but `ftp` is not secure.

```
$ sftp remote.example.com
Password: ********
sftp> cd MyFiles
sftp> ls
README
file1
file2
file3
sftp> get file2
Fetching /home/smith/MyFiles/file2 to file2
sftp> quit
```

If your username on the remote system is different from your local one, use the _`username`_ @ _`host`_ argument:

```
$ sftp smith@remote.example.com
```

|Command|Meaning|
|---|---|
|`help`|View a list of available commands.|
|`ls`|List the files in the current remote directory.|
|`lls`|List the files in the current local directory.|
|`pwd`|Print the remote working directory.|
|`lpwd`|Print the local working directory.|
|`cd` _`dir`_|Change your remote directory to be_`dir`_.|
|`lcd` _`dir`_|Change your local directory to be_`dir`_.|
|`get` _`file1`_<br>[_`file2`_]|Copy remote_`file1`_to local machine, optionally renamed as_`file2`_.|

|Command|Meaning|
|---|---|
|`put` _`file1`_<br>[_`file2`_]|Copy local_`file1`_to remote machine, optionally renamed as_`file2`_.|
|`mget` _`file`_*|Copy multiple remote files to the local machine using wildcards * and<br>?.|
|`mput` _`file`_*|Copy multiple local files to the remote machine using wildcards * and<br>?.|
|`quit`|Exit`sftp`.|

#### **Name** 

ftp — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
ftp [options] host
```

The `ftp` (File Transfer Protocol) program copies files between computers, but not in a secure manner: your username and password travel over the network as plain text. Use `sftp` instead if your remote server supports it. The same commands we listed for `sftp` also work for `ftp` . (However, the two programs support other, differing commands, too.)

## **Email** 

<!-- Start of picture text --> thunderbi Graphical mail client.<br>rd<br>evolution Graphical mail client.<br>mutt Text-based mail client.<br>mail Minimal text-based mail client.<br>mailq View the outgoing mail queue on your<br>system.<br><!-- End of picture text -->

Linux includes a number of mail readers, some graphical and some entirely text-based. We’ll look at several with different purposes and strengths. Other Linux mailers include kmail, alpine, and the RMAIL and vm applications built into emacs.

#### **Name** 

#### thunderbird — stdin  stdout  - file  -- opt  --help  --version **Synopsis** 

```
thunderbird
```

Thunderbird is one of the most popular graphical email programs, available not only for Linux but also Windows and Macintosh. The first time you run Thunderbird, you’ll be guided through a series of dialogs to set up your mail account. Once this is complete, the main Thunderbird window presents you with common email operations:

|Inbox|View your mail|
|---|---|
|Write|Compose a new mail message|
|Get<br>Mail|Check for new messages on your mail server|
|Reply|Reply to a message, only to the sender|
|Reply<br>All|Reply to a message, to all addresses in the To and CC<br>lines|
|Forward|Forward a message to a third party|

Thunderbird is highly configurable. You can customize the entire look and feel of the program (known as the “Theme”), install add-ons to provide new features, and more. See <u>http://www.getthunderbird.com</u> for details.

#### **Name** 

evolution — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
evolution
```

Evolution is another popular graphical email program. Run the command `evolution` from the shell to get started. As with Thunderbird, the first time you run Evolution, you’ll be guided to set up your mail account. Once this is complete, the main Evolution window offers you common email commands by point-and-click:

|Inbox|View your mail|
|---|---|
|New|Compose a new mail message|
|Send/Recei<br>ve|Check for new messages on your mail server|
|Reply|Reply to a message, only to the sender|
|Reply To<br>All|Reply to a message, to all addresses in the To and CC<br>lines|
|Forward|Forward a message to a third party|

There are many more features, so experiment, and see <u>http://projects.gnome.org/evolution</u> for more information.

#### **Name** 

mutt — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
mutt [options]
```

Mutt is a text-based mailer that runs in an ordinary terminal (or terminal window), so it can be used both locally (e.g., in an X terminal window) or remotely over an SSH connection. It is very powerful, with many commands and options. To invoke it, type:

```
$ mutt
```

When the main screen appears, any messages in your mailbox are listed briefly, one per line, and the following commands are available:

|Keystro<br>ke|Meaning|
|---|---|
|Up<br>arrow|Move to the previous message.|
|Down<br>arrow|Move to the next message.|
|PageUp|Scroll up one pageful of messages.|
|PageDo<br>wn|Scroll down one pageful of messages.|
|Home|Move to the first message.|
|End|Move to the last message.|
|`m`|Compose a new mail message. This invokes your default text editor. After editing the<br>message and exiting the editor, type`y`to send the message or`q`to postpone it.|
|`r`|Reply to current message. Works like`m`.|
|`f`|Forward the current message to a third party. Works like`m`.|
|`i`|View the contents of your mailbox.|
|`C`|Copy the current message to another mailbox.|

|Keystro||
|---|---|
|ke|Meaning|
|`d`|Delete the current message.|

While writing a message, after you exit your text editor, the following commands are available:

|Keystrok<br>e|Meaning|
|---|---|
|`a`|Attach a file (an attachment) to the<br>message.|
|`c`|Set the CC list.|
|`b`|Set the BCC list.|
|`e`|Edit the message again.|
|`r`|Edit the Reply-To field.|
|`s`|Edit the subject line.|
|`y`|Send the message.|
|`C`|Copy the message to a file.|
|`q`|Postpone the message without sending it.|

###### Additional commands are always available: 

|Keystro<br>ke|Meaning|
|---|---|
|`?`|See a list of all commands (press the`SPACEBAR`to scroll down,`q`to<br>quit).|
|`^G`|Cancel the command in progress.|
|`q`|Quit.|

The official Mutt site is <u>http://www.mutt.org.</u>

#### **Name** 

mail — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
mail [options] recipient
```

The `mail` program (equivalently, `Mail` )<sup>[</sup> <u>20</u><sup>]</sup> is a quick, simple email client. Most people want a more powerful program for regular use, but for quick messages from the command line or in scripts, `mail` is really handy. To send a quick message:

```
$ mail smith@example.com
Subject: my subject
I'm typing a message.
To end it, I type a period by itself on a line.
```

```
.
Cc: jones@example.com
$
```

To send a quick message using a single command, use a pipeline:

```
$ echo "Hello world" | mail -s "subject" smith@example.com
```

To mail a file using a single command, you can use redirection or a pipeline:

```
$ mail -s "my subject" smith@example.com < filename
$ cat filename | mail -s "my subject" smith@example.com
```

Notice how easily you can send the output of a pipeline as an email message; this is useful in scripts.

#### **Useful options** 

|`-s` _`subject`_|Set the subject line of an outgoing message.|
|---|---|
|`-v`|Verbose mode: print messages about mail delivery.|
|`-c`<br>_`addresses`_|CC the message to the given addresses, a comma-separated list.|

`-b` BCC the message to the given addresses, a comma-separated _`addresses`_ list.

[20<sup>]</sup> On older Unix systems, `Mail` and `mail` were rather different programs, but on Linux they are the same: _/usr/bin/Mail_ is a symbolic link to the `mail` command.

#### **Name** 

mailq — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
mailq
```

The `mailq` command lists any outgoing email messages awaiting delivery.

```
$ mailq
Queue ID- --Size-- ----Arrival Time--  -Sender/Recipient---
46AAB43972*    333 Tue Jan 10 21:17:14 smith@example.com
                                       jones@elsewhere.org
```

Sent mail messages are also recorded in a log file such as _/var/log/maillog_ ; the name may differ from distro to distro.

#### **Name** 

#### **Beyond Mail Readers** 

Email is more “transparent” on Linux than on other platforms that merely display your mailbox and send and receive messages. The ability to list outgoing email messages with `mailq` is just one example. Here are some other options to whet your appetite and encourage you to explore.

- You can process your mailboxes with any command-line tools, such as `grep` , because mail files are plain text. 

- You can manually retrieve messages from your mail server at the command line with the `fetchmail` command. Using a simple configuration file, this command can reach out to IMAP and POP servers and download mail in batch. See `man fetchmail` . 

- Your system can run a mail server, such as `postfix` or `sendmail` , to handle the most complex mail delivery situations. 

- You can control local mail delivery in sophisticated ways with the `procmail` command, which filters arriving email messages through any arbitrary program. See `man procmail` . 

- Spam filtering is sophisticated on Linux: check out the SpamAssassin suite of programs. You can run it personally on your incoming email, or at the server level for large numbers of users. 

In short, email is not limited to the features of your mail-reading program. Investigate and experiment!

## **Web Browsing** 

<!-- Start of picture text --> firefo Full-featured web browser.<br>x<br>lynx Text-only web browser.<br>wget Download web pages and<br>files.<br><!-- End of picture text -->

Linux offers several ways to explore the World Wide Web: traditional browsers, text-based browsers, and page-retrieval utilities.

#### **Name** 

firefox — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
firefox [options] [URL]
```

Firefox is one of the most popular web browsers for Linux and most other operating systems. Start it in the background with:

```
$ firefox &
```

Some other web browsers for Linux include Google Chrome <u>(http://www.google.com/chrome), Opera (http://www.opera.com),</u> Konqueror for KDE (http://www.konqueror.org), and Epiphany for GNOME (http://projects.gnome.org/epiphany).

#### **Name** 

lynx — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
lynx [options] [URL]
```

Lynx is a stripped-down, text-only web browser. It doesn’t display pictures, play audio or video, or even respond to your mouse. But it’s incredibly useful when you just want a quick look at a page, or when the network is slow, or for downloading the HTML of a website. It’s particularly good for checking out a suspicious URL, since Lynx doesn’t run JavaScript and won’t even accept a cookie without asking you first.

```
$ lynx http://www.yahoo.com
```

All browsing is done by keyboard. Many pages will not look quite right, especially if they use tables or frames extensively, but usually you can find your way around a site.

|Keystroke|Meaning|
|---|---|
|`?`|Get help.|
|`k`|List all keystrokes and their meanings.|
|`^G`|Cancel a command in progress.|
|`q`|Quit Lynx.|
|Enter|“Click” the current link, or finish the current form field.|
|Left arrow|Back to previous page.|
|Right<br>arrow|Forward to next page, or “click” the current link.|
|`g`|Go to a URL (you’ll be prompted to enter it).|
|`p`|Save, print, or mail the current page.|
|Space bar|Scroll down.|
|`b`|Scroll up.|

|Keystroke|Meaning|
|---|---|
|Down<br>arrow|Go to the next link or form field.|
|Up arrow|Go to the previous link or form field.|
|`^A`|Go to top of page.|
|`^E`|Go to end of page.|
|`m`|Return to the main/home page.|
|`/`|Search for text on the page.|
|`a`|Bookmark the current page.|
|`v`|View your bookmark list.|
|`r`|Delete a bookmark.|
|`=`|Display properties of the current page and link.|
|`\`|View HTML source (type again to return to normal<br>view).|

Lynx has over 100 command-line options, so the manpage is well worth exploring.

#### **Useful options** 

|`-dump`|Print the rendered page to standard output and exit. (Compare to the`-source`<br>option.)|
|---|---|
|`-source`|Print the HTML source to standard output and exit. (Compare to the`wget`<br>command.)|
|`-emacskeys`|Make Lynx obey keystrokes reminiscent of the emacs editor.|
|`-vikeys`|Make Lynx obey keystrokes reminiscent of the vim (or vi) editor.|
|`-`<br>`homepage=`_`UR`_<br>_`L`_|Set your home page URL to be_`URL`_.|
|`-color`|Turn colored text mode on.|
|`-nocolor`|Turn colored text mode off.|

#### **Name** 

wget — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
wget [options] URL
```

The `wget` command hits a URL and downloads the data to a file or standard output. It’s great for capturing individual web pages, downloading files, or duplicating entire web site hierarchies to arbitrary depth. For example, let’s capture the Yahoo home page:

```
$ wget http://www.yahoo.com
```

```
23:19:51 (220.84 KB/s) - `index.html' saved [31434]
```

which is saved to a file _index.html_ in the current directory. `wget` has the added ability to resume a download if it gets interrupted in the middle, say, due to a network failure: just run `wget -c` with the same URL and it picks up where it left off.

Perhaps the most useful feature of `wget` is its ability to download files without needing a web browser:

```
$ wget http://www.example.com/files/manual.pdf
```

This is great for large files like videos and ISO images. You can even write shell scripts to download sets of files if you know their names:

```
$ for i in 1 2 3; do wget http://example.com/$i.mpeg; done
```

Another similar command is `curl` , which writes to standard output by default — unlike `wget` , which duplicates the original page and file names by default.

```
$ curl http://www.yahoo.com > mypage.html
```

`wget` has over 70 options, so we’ll cover just a few important ones. ( `curl` has a different set of options; see its manpage.)

#### **Useful options** 

|`-i`<br>_`filename`_|Read URLs from the given file and retrieve them in turn.|
|---|---|
|`-O`<br>_`filename`_|Write all the captured HTML to the given file, one page appended after the other.|
|`-c`|Continue mode: if a previous retrieval was interrupted, leaving only a partial file as a<br>result, pick up where`wget`left off. That is, if`wget`had downloaded 100K of a 150K file,<br>the`-c`option says to retrieve only the remaining 50K and append it to the existing file.<br>`wget`can be fooled, however, if the remote file has changed since the first (partial)<br>download, so use this option only if you know the remote file hasn’t changed.|
|`-t`_`N`_|Try_`N`_times before giving up._`N`_=0 means try forever.|
|`--`<br>`progress=d`<br>`ot`|Print dots to show the download progress.|
|`--`<br>`progress=b`<br>`ar`|Print bars to show the download progress.|
|`--spider`|Don’t download, just check existence of remote pages.|
|`-nd`|Retrieve all files into the current directory, even if remotely they are in a more complex<br>directory tree. (By default,`wget`duplicates the remote directory hierarchy.)|
|`-r`|Retrieve a page hierarchy recursively, including subdirectories.|
|`-l`_`N`_|Retrieve files at most_`N`_levels deep (5 by default).|
|`-k`|Inside retrieved files, modify URLs so the files can be viewed locally in a web browser.|
|`-p`|Download all necessary files to make a page display completely, such as stylesheets<br>and images.|
|`-L`|Follow relative links (within a page) but not absolute links.|
|`-A` _`pattern`_|Accept mode: download only files whose names match a given pattern. Patterns may<br>contain the same wildcards as the shell.|
|`-R` _`pattern`_|Reject mode: download only files whose names_do not_match a given pattern.|
|`-I` _`pattern`_|Directory inclusion: download files only from directories that match a given pattern.|
|`-X` _`pattern`_|Directory exclusion: download files only from directories that_do not_match a given<br>pattern.|

## **Usenet News** 

Usenet News is one of the oldest communities online today. It consists of tens of thousands of _newsgroups_ , discussion forums in which people post (submit) messages and reply to them. One common, text-based newsreader program is `slrn` , but there are dozens more available on the Net ( `rn` , `trn` , `tin` , and so on). Usenet News can also be searched at Google Groups, <u>http://groups.google.com.</u>

In order to access Usenet, you need to connect to a news server, an Internet host that permits reading and posting of news articles. Once you can connect to a news server (say, _news.example.com_ ), a record of your subscribed newsgroups and which articles you’ve read is kept in a file in your home directory automatically. Depending on your newsreader configuration, the file is either _~/.newsrc_ or _~/.jnewsrc_ .

#### **Name** 

slrn — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
slrn [options]
```

`slrn` is a Usenet newsreader. Before using it, you must specify a news server by setting your shell’s `NNTPSERVER` variable:

```
$ export NNTPSERVER=news.example.com
```

Then create a newsgroups file (only if you haven’t used `slrn` on this computer before):

```
$ slrn --create
```

and start reading news:

```
$ slrn
```

When invoked, `slrn` displays the News Groups page with a list of your subscribed newsgroups. Some useful commands are:

|Keystro<br>ke|Meaning|
|---|---|
|`q`|Quit`slrn`.|
|Down|Select next newsgroup.|
|Up|Select previous newsgroup.|
|Enter|Read the selected newsgroup.|
|`p`|Post a new article in the selected newsgroup.|
|`a`|Add a new newsgroup (you must know the name).|
|`u`|Unsubscribe from the selected newsgroup (it will be removed after you quit). Type`s`to<br>resubscribe.|

When you press Enter to read a newsgroup, `slrn` displays a Group page, containing the available discussions (or “threads”) in that newsgroup. Some

###### useful commands on this page are: 

<!-- Start of picture text --> Keystro<br>ke Meaning<br>q Quit and go back to the News Groups page.<br>Down Select next thread.<br>Up Select previous thread.<br>Enter Begin reading the selected thread.<br>c Mark all threads as read (“catch up”): type  ESCAPE u  to<br>undo.<br><!-- End of picture text -->

###### Commands while reading an article include: 

<!-- Start of picture text --> Keystrok<br>e Meaning<br>q Quit reading and return to the Group<br>page.<br>Space Go to next page of article.<br>bar<br>b Go back to previous page of article.<br>r Reply to the author by email.<br>f Post a followup article.<br>P Post a new article.<br>o Save the article in a file.<br>n Go to next unread article.<br>p Go to previous unread article.<br><!-- End of picture text -->

At any time you can type `?` for the help page. `slrn` has a tremendous number of commands and options, and can be configured via the file _~/.slrnrc_ . We’ve covered only the basics; see _/usr/share/doc/slrn*_ and <u>www.slrn.org</u> for more information.

## **Instant Messaging** 

|`pidgi`<br>`n`|Instant messaging and IRC<br>client.|
|---|---|
|`talk`|Linux/Unix chat program.|
|`write`|Send messages to a terminal.|
|`mesg`|Prohibit`talk`and`write`.|
|`tty`|Print your terminal device name.|

Linux provides various ways to send messages to other users on the same machine or elsewhere on the Internet. These range from the ancient programs `talk` and `write` , which work over Linux terminal devices (ttys), to more modern instant messaging clients like `pidgin` .

#### **Name** 

pidgin — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
pidgin [options]
```

`pidgin` is a instant messaging client that works with many different protocols, including AOL, MSN, Yahoo, and more. It is also an IRC (Internet Relay Chat) client. It runs in an X window:

```
$ pidgin &
```

If you don’t already have an account with one of these IM services, you’ll need to create one first; for example, visit <u>www.aim.com</u> to create an AOL Instant Messenger account. Once this is done, simply click the Accounts button to indicate your account to `pidgin` , enter your screen name and password in the login window, and you should be connected.

#### **Useful options** 

|`-l`|Enable the given accounts (a comma-separated list).|
|---|---|
|_`accounts`_||
|`-n`|Don’t automatically log in when invoking`pidgin`(assuming your password is<br>stored).|
|`-m`|Let multiple copies of pidgin run at the same time.|

#### **Name** 

talk — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
talk [user[@host]] [tty]
```

The `talk` program predates modern instant messaging by a few decades: it connects two users, logged in on the same or different hosts, for one-to-one communication. It runs in a shell window, splitting it horizontally, so you can see your own typing and that of your partner.

```
$ talk friend@example.com
```

If your partner is logged in multiple times, you can specify one of his ttys for the `talk` connection.

#### **Name** 

write — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
write user [tty]
```

The `write` program is more primitive than `talk` : it sends lines of text from one logged-in user to another on the same Linux machine.

```
$ write smith
Hi, how are you?
See you later.
^D
```

`^D` ends the connection. `write` is also useful in pipelines for quick one-off messages:

```
$ echo 'Howdy!' | write smith
```

#### **Name** 

mesg — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
mesg [y|n]
```

The `mesg` program controls whether `talk` and `write` connections can reach your terminal. `mesg y` permits them, `mesg n` denies them, and `mesg` prints the current status ( `y` or `n` ). The default is `y` . `mesg` has no effect on modern instant messaging programs like `pidgin` .

```
$ mesg
is y
$ mesg n
$ mesg
is n
```

#### **Name** 

tty — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
tty
```

The `tty` program prints the name of the terminal device associated with the current shell.

```
$ tty
/dev/pts/4
```

## **Screen Output** 

|`echo`|Print simple text on standard output.|
|---|---|
|`prin`<br>`tf`|Print formatted text on standard output.|
|`yes`|Print repeated text on standard output.|
|`seq`|Print a sequence of numbers on standard<br>output.|
|`clea`<br>`r`|Clear the screen or window.|

Linux provides several commands for printing messages on standard output:

```
$ echo hello world
hello world
```

Each command has different strengths and intended purposes. These commands are invaluable for learning about Linux, debugging problems, writing shell scripts (see <u>Programming with Shell Scripts), or just talking to</u> yourself.

#### **Name** 

echo — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
echo [options] strings
```

The `echo` command simply prints its arguments:

```
$ echo We are having fun
We are having fun
```

Unfortunately, there are several different `echo` commands with slightly different behavior. There’s _/bin/echo_ , but Linux shells typically override this with a built-in command called `echo` . To find out which you’re using, run the command `type echo` .

#### **Useful options** 

> `-n`<sup>Don’t print a final newline character.</sup> 

> `-e`<sup>Recognize and interpret escape characters. For example, try</sup><sup>`echo 'hello\a'`and</sup><sup>`echo -e 'hello\a'`.</sup> The first prints literally and the second makes a beep. 

> `-E`<sup>Don’t interpret escape characters: the opposite of</sup><sup>`-e`.</sup> 

###### Available escape characters are: 

<!-- Start of picture text --> \a Alert (play a beep)<br>\b Backspace<br>\c Don’t print the final newline (same effect as  -<br>n )<br>\f Form feed<br>\n Line feed (newline)<br>\r Carriage return<br>\t Horizontal tab<br>\v Vertical tab<br><!-- End of picture text -->

|`\\`|A backslash|
|---|---|
|`\'`|Single quote|
|`\"`|Double quote|
|_`\nn`_<br>_`n`_|The character whose ASCII value is_`nnn`_in<br>octal|

#### **Name** 

printf — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
printf format_string [arguments]
```

The `printf` command is an enhanced `echo` : it prints formatted strings on standard output. It operates much like the C programming language function `printf( )` , which applies a format string to a sequence of arguments to create some specified output. For example:

```
$ printf "User %s is %d years old.\n" sandy 29
User sandy is 29 years old.
```

The first argument is the format string, which in our example contains two format specifications, `%s` and `%d` . The subsequent arguments, sandy and 29, are substituted by `printf` into the format string and then printed. Format specifications can get fancy with floating-point numbers:

```
$ printf "That\'ll be $%0.2f, sir.\n" 3
That'll be $3.00, sir.
```

There are two `printf` commands available in Linux: one built into the bash shell, and one in _/usr/bin/printf_ . The two are identical except for one format specification, `%q` , supported only by the bash built-in: it prints escape symbols (“ `\` ”) so its output can be used as shell input safely. Note the difference:

```
$ printf "This is a quote: %s\n" "\""
This is a quote: "
$ printf "This is a quote: %q\n" "\""
This is a quote: \"
```

It is your responsibility to make sure the number of format specifications ( `%` ) equals the number of arguments supplied to `printf` . If you have too many arguments, the extras are ignored, and if you have too few, `printf` assumes default values (0 for numeric formats, an empty string for string formats). Nevertheless, you should treat such mismatches as errors, even

though `printf` is forgiving. If they lurk in your shell scripts, they are bugs waiting to happen.

Format specifications are described in detail on the manpage for the C function `printf` (see `man 3 printf` ). Here are some useful ones.

<!-- Start of picture text --> %d Decimal integer<br>%ld Long decimal integer<br>%o Octal integer<br>%x Hexadecimal integer<br>%f Floating point<br>%lf Double-precision floating point<br>%c A single character<br>%s String<br>%q String with any shell metacharacters<br>escaped<br>%% A percent sign by itself<br>Just after the leading percent sign, you can insert a numeric expression for<br>the minimum width of the output. For example, “%5d” means to print a<br>decimal number in a five-character-wide field, and “%6.2f” means a<br>floating-point number in a six-character-wide field with two digits after the<br>decimal point. Some useful numeric expressions are:<br>n Minimum width  n .<br>0 Minimum width  n , padded with leading zeroes.<br>n<br>n. Minimum width  n , with  m  digits after the decimal<br>m<br>point.<br><!-- End of picture text -->

Just after the leading percent sign, you can insert a numeric expression for the minimum width of the output. For example, “%5d” means to print a decimal number in a five-character-wide field, and “%6.2f” means a floating-point number in a six-character-wide field with two digits after the decimal point. Some useful numeric expressions are:

`printf` also interprets escape characters like “\n” (print a newline character) and “\a” (ring the bell). See the `echo` command for the full list.

#### **Name** 

yes — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
yes [string]
```

The `yes` command prints the given string (or “y” by default) forever, one string per line.

```
$ yes again
again
again
again
```

Though it might seem useless at first glance, `yes` can be perfect for turning interactive commands into batch commands. Want to get rid of an annoying “Are you SURE you want to do that?” message? Pipe the output of `yes` into the input of the command to answer all those prompts:

```
$ yes | my_interactive_command
```

When _`my_interactive_command`_ terminates, so will `yes` .

#### **Name** 

seq — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
seq [options] specification
```

The `seq` command prints a sequence of integers or real numbers, suitable for piping to other programs. There are three kinds of specification arguments:

_A single number: an upper limit_

`seq` begins at 1 and counts up to the number.

```
$ seq 3
1
2
3
```

_Two numbers: lower and upper limit_

`seq` begins at the first number and counts as far as it can without passing the second number.

```
$ seq 2 5
2
3
4
5
```

_Three numbers: lower limit, increment, and upper limit_

`seq` begins at the first number, increments by the second number, and stops at (or before) the third number.

```
$ seq 1 .3 2
1
1.3
1.6
1.9
```

You can also go backward with a negative increment:

```
$ seq 5 -1 2
5
```

```
4
```

```
3
```

```
2
```

#### **Useful options** 

|`-w`|Print leading zeroes, as necessary, to give all lines the same width:|
|---|---|
||`$ seq -w 8 10`<br>`08`<br>`09`<br>`10`|
|`-f`<br>_`form`_<br>_`at`_|Format the output lines with a`printf`-like format string, which must include either`%g`(the<br>default),`%e`, or`%f`:<br>`$ seq -f '**%g**' 3`<br>`**1**`<br>`**2**`<br>`**3**`|
|`-s`<br>_`stri`_<br>_`ng`_|Use the given string as a separator between the numbers. By default, a newline is printed<br>(i.e., one number per line):|
||`$ seq -s ':' 10`<br>`1:2:3:4:5:6:7:8:9:10`|

#### **Name** 

clear — stdin  stdout  - file  -- opt  --help  --version

**Synopsis**

```
clear
```

This command simply clears your display or shell window.

## **Math and Calculations** 

|`xcal`<br>`c`|Display a graphical calculator.|
|---|---|
|`expr`|Evaluate simple math on the command<br>line.|
|`dc`|Text-based calculator.|

Need a calculator? Linux provides not only a familiar graphical calculator, but also some command-line programs to compute mathematical truths for you.

#### **Name** 

xcalc — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
xcalc [options]
```

The `xcalc` command displays a simple, graphical calculator in an X window. The default is a traditional calculator; if you prefer a reverse-polish notation (RPN) calculator, supply the `-rpn` option.

#### **Name** 

expr — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
expr expression
```

The `expr` command does simple math (and other expression evaluation) on the command line:

```
$ expr 7 + 3
10
$ expr '(' 7 + 3 ')' '*' 14   Special shell characters are quoted
140
$ expr length ABCDEFG
7
$ expr 15 '>' 16
0                           Meaning false
```

Each argument must be separated by whitespace. Notice that we had to quote or escape any characters that have special meaning to the shell. Parentheses (escaped) may be used for grouping. Operators for `expr` include:

|Operat<br>or|Numeric<br>operation|String operation|
|---|---|---|
|`+`|Addition||
|`-`|Subtraction||
|`*`|Multiplicati<br>on||
|`/`|Integer<br>division||
|`%`|Remainder<br>(modulo)||
|`<`|Less than|Earlier in dictionary.|
|`<=`|Less than or<br>equal|Earlier in dictionary, or equal.|
|`>`|Greater than|Later in dictionary.|

|Operat<br>or|Numeric<br>operation|String operation|
|---|---|---|
|`>=`|Greater than<br>or equal|Later in dictionary, or equal.|
|`=`|Equality|Equality.|
|`!=`|Inequality|Inequality.|
|`|`|Boolean<br>“or”|Boolean “or”.|
|`&`|Boolean<br>“and”|Boolean “and”.|
|`s :`<br>_`regexp`_||Does the regular expression_`regexp`_match string_`s`_?|
|`substr`<br>_`s p n`_||Print_`n`_characters of string_`s`_, beginning at position_`p`_. (_`p`_=1 is the first<br>character.)|
|`index` _`s`_<br>_`chars`_||Return the index of the first position in string_`s`_containing a character from<br>string_`chars`_. Return 0 if not found. Same behavior as the C function`index(`<br>`)`.|

For Boolean expressions, the number 0 and the empty string are considered false; any other value is true. For Boolean results, 0 is false and 1 is true. `expr` is not very efficient. For more complex needs, consider using a language like Perl instead.

#### **Name** 

dc — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
dc [options] [files]
```

The `dc` (desk calculator) command is a reverse-polish notation (RPN), stack-based calculator that reads expressions from standard input and writes results to standard output. If you know how to use a Hewlett-Packard RPN calculator, `dc` is pretty easy to use once you understand its syntax. But if you’re used to traditional calculators, `dc` may seem inscrutable. We’ll cover only some basic commands.

For stack and calculator operations:

> `q` Quit `dc` . 

> `f` Print the entire stack. 

> `c` Delete (clear) the entire stack. 

> `p` Print the topmost value on the stack. 

> `P` Pop (remove) the topmost value from the stack. 

_`n`_ Set precision of future operations to be _`n`_ decimal places (default is 0: integer `k` operations).

To pop the top two values from the stack, perform a requested operation, and push the result:

> `+` Addition. 

> `−` Subtraction. 

> `*` Multiplication. 

> `/` Division. 

> `%` Remainder. 

> `^` Exponentiation (second-to-top value is the base, top value is the exponent). 

To pop the top value from the stack, perform a requested operation, and push the result:

> `v` Square root. Examples: `$ dc` **`4 5 + p`** _`Print the sum of 4 and 5`_ `9` **`2 3 ^ p`** _`Raise 2 to the 3rd power and print the result`_ `8` **`10 * p`** _`Multiply the stack top by 10 and print the result`_ `80` **`f`** _`Print the stack`_ `80 9` **`+p`** _`Pop the top two stack values and print their sum`_ `89` 

###### Examples: 

## **Dates and Times** 

|`xclock`|Display a graphical clock.|
|---|---|
|`cal`|Print a calendar.|
|`date`|Print or set the date and time.|
|`ntpdat`<br>`e`|Set the system time using a remote<br>timeserver.|

Need a date? How about a good time? Try these programs to display and set dates and times on your system.

#### **Name** 

xclock — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
xclock [options]
```

The `xclock` command displays a simple, graphical clock in an X window. If you prefer a different style, there are other clock programs included, such as `oclock` (round clock) and the taskbar clocks displayed by GNOME and KDE.

#### **Useful options** 

|`-analog`|An analog clock with hands.|
|---|---|
|`-digital [-`<br>`brief]`|A digital clock with full date and time; add`-brief`to show only the<br>time.|
|`-update` _`N`_|Update the time display every_`N`_seconds.|

#### **Name** 

cal — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
cal [options] [month [year]]
```

The `cal` command prints a calendar — by default, the current month:

```
$ cal
   December 2011
Su Mo Tu We Th Fr Sa
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31
```

To print a different calendar, supply a month and four-digit year: `cal 8 2011` . If you omit the month ( `cal 2011` ), the entire year is printed.

#### **Useful options** 

> `-y`<sup>Print the current year’s calendar.</sup> 

> `-3`<sup>Three-month view: print the previous and next month as well.</sup> 

- `-j`<sup>Number each day by its position in the year; in our example, September 1 would be displayed as</sup> 244, September 2 as 245, and so on. 

#### **Name** 

date — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
date [options] [format]
```

The `date` command prints dates and times. The results will depend on your system’s locale settings (for your country and language). In this section we assume an English, US-based locale.

By default, `date` prints the system date and time in the local timezone:

```
$ date
Sun Sep 28 21:01:31 EDT 2003
```

You can format the output differently by supplying a format string beginning with a plus sign:

```
$ date '+%D'
09/28/03
$ date '+The time is %l:%M %p on a beautiful %A in %B'
The time is  9:01 PM on a beautiful Sunday in September
```

Here is a sampling of the `date` command’s many formats:

|Form<br>at|Meaning|Example (US English)|
|---|---|---|
|**Whol**|**e dates and times:**||
|`%c`|Full date and time, 12-hour clock|Sun 28 Sep 2003, 09:01:25<br>PM EDT|
|`%D`|Numeric date, 2-digit year|09/28/03|
|`%x`|Numeric date, 4-digit year|09/28/2003|
|`%T`|Time, 24-hour clock|21:01:25|
|`%X`|Time, 12-hour clock|09:01:25 PM|
|**Word**|**s:**||
|`%a`|Day of week (abbreviated)|Sun|

|Form<br>at|Meaning|Example (US English)|
|---|---|---|
|`%A`|Day of week (complete)|Sunday|
|`%b`|Month name (abbreviated)|Sep|
|`%B`|Month name (complete)|September|
|`%Z`|Time zone|EDT|
|`%p`|AM or PM|PM|
|**Numb**<br>|**ers:**||
|`%w`|Day of week (0–6, 0=Sunday)|0|
|`%u`|Day of week (1–7, 1=Monday)|7|
|`%d`|Day of month, leading zero|02|
|`%e`|Day of month, leading blank|2|
|`%j`|Day of year, leading zeroes|005|
|`%m`|Month number, leading zero|09|
|`%y`|Year, 2 digits|03|
|`%Y`|Year, 4 digits|2003|
|`%M`|Minute, leading zero|09|
|`%S`|Seconds, leading zero|05|
|`%l`|Hour, 12-hour clock, leading blank|9|
|`%I`|Hour, 12-hour clock, leading zero|09|
|`%k`|Hour, 24-hour clock, leading blank|9|
|`%H`|Hour, 24-hour clock, leading zero|09|
|`%N`|Nanoseconds|737418000|
|`%s`|Seconds since the beginning of Linux time: midnight<br>January 1, 1970|1068583983|
|**Other**|**:**||
|`%n`|Newline character||

|Form<br>at|Meaning|Example (US English)|
|---|---|---|
|`%t`|Tab character||
|`%%`|Percent sign|%|

Through its options, `date` can also display other dates and times.

#### **Useful options** 

|`-d`|Display the given_`date_or_time_string`_, formatted as you wish.|
|---|---|
|_`date_or_time_string`_||
|`-r` _`filename`_|Display the last-modified timestamp of the given file, formatted as you<br>wish.|
|`-s`|Set the system date and/or time; only the superuser can do this.|
|_`date_or_time_string`_||

#### **Name** 

ntpdate — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
ntpdate timeserver
```

The `ntpdate` command sets the current system time by contacting a timeserver machine on the network. You must be root to set the system time.

- `# /usr/sbin/ntpdate timeserver.someplace.edu 7 Sep 21:01:25 ntpdate[2399]: step time server 178.99.1.8 offset 0.51 sec` 

To keep your system date in sync with a timeserver over long periods, use the daemon `ntpd` instead; see <u>http://www.ntp.org. If you don’t know a local</u> timeserver, search Google for “public ntp time server”.

## **Graphics and Screensavers** 

|`eog`|Display graphics files.|
|---|---|
|`geeqie`|Display graphics files and<br>slideshows.|
|`ksnapshot`|Take a screenshot (screen capture).|
|`gimp`|Edit graphics files.|
|`dia`|Draw structured diagrams.|
|`gnuplot`|Create graphs and plots.|
|`xscreensave`<br>`r`|Run a screensaver.|

For viewing or editing graphics, Linux has handy tools with tons of options. We won’t cover these programs in much detail, just enough to pique your interest. Our goal is to make you aware of the programs so you can explore further on your own.

#### **Name** 

eog — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
eog [options] [files]
```

The `eog` (Eye of Gnome) image viewer displays graphics files in a variety of formats. If you invoke it for a single file, it displays the file. Invoked on two or more files:

```
$ eog file1.jpg file2.gif file3.pbm
```

it displays each in a separate window.

#### **Useful options** 

- `-f`<sup>Display images in full-screen</sup> mode. 

- `-s`<sup>Display images in a slideshow.</sup> 

#### **Name** 

geeqie — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
geeqie [options] [file]
```

The `geeqie` image viewer (the successor to `gqview` ) displays graphics files in a variety of formats, and can automatically switch from one image to the next, like a slideshow. By default, it displays the names of all graphics files in the current directory, and you can select names to display the images. The onscreen menus are straightforward, so explore them and try things out. Type `^q` to quit.

#### **Useful options** 

> `-f`<sup>Display images in full-screen mode. (Toggle between full-screen mode and window mode by</sup> typing `v` .) 

> `-s`<sup>Display images in a slideshow. (Turn the slideshow on and off by typing</sup><sup>`s`.)</sup> 

#### **Name** 

ksnapshot — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
ksnapshot [options]
```

The `ksnapshot` command is a versatile screen-capture utility. Simply run:

```
$ ksnapshot
```

and it takes a screenshot, displaying it in miniature. From there you can save it to a graphics file or take another screenshot. The file format will match whatever file extension you choose: _.jpg_ to produce a JPEG file, _.bmp_ for a Windows bitmap, _.pbm_ for a portable bitmap, _.eps_ for encapsulated PostScript, _.ico_ for a Windows icon, and so forth. For a list of supported file formats, click the Save Snapshot button and view the selections under Filter. For more information, click the Help button in the `ksnapshot` window, or run `ksnapshot --help-all` from the shell.

#### **Name** 

gimp — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
gimp [options] [files]
```

The GIMP (GNU Image Manipulation Program) is a full-featured imageediting package that rivals Adobe Photoshop in power and scope. It is fairly complex to use, but the results can be stunning. Visit <u>http://www.gimp.org</u> for full information. To run the program, type:

```
$ gimp
```

To edit a particular file, type:

```
$ gimp filename
```

If the GIMP is more complicated than you need, try Pinta (http://pinta- <u>project.com/) or</u> `xv` <u>(http://www.trilon.com/xv).</u> `xv` is no longer maintained, but it’s one of this author’s favorite utilities:

```
$ xv myfile.jpg
```

Click the right mouse button anywhere on the image to reveal the menu of editing tools.

#### **Name** 

dia — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
dia [options] [files]
```

The `dia` program creates structured drawings such as flowcharts, schematics, entity-relation (ER) diagrams, and more. It’s like a mini Microsoft Visio. Diagrams can be exported in popular formats like JPEG, PDF, and PNG. See <u>http://live.gnome.org/Dia</u> for full details.

#### **Name** 

gnuplot — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
gnuplot [options] [files]
```

The `gnuplot` program creates graphs, plotting points and connecting them with lines and curves, and saves them in a wide variety of printer and plotter formats, such as PostScript. To use `gnuplot` , you need to learn a small but powerful programming language. Here’s an example of plotting the curve `y = x`<sup>2</sup> from `x` = 1 to 10, which will appear in an X window on your display:

```
$ gnuplot
gnuplot> plot [1:10] x**2
gnuplot> quit
```

To do the same, saving the results as a PostScript file:

```
$ cat myfile
set terminal postscript
plot [1:10] x**2
$ gnuplot < myfile > output.ps
```

See <u>http://www.gnuplot.info</u> for full details.

#### **Name** 

xscreensaver — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
xscreensaver
```

The `xscreensaver` system is a versatile screen saver with hundreds of animations available. KDE and GNOME have their own screensavers and options, but if you prefer, you can run `xscreensaver` manually. `xscreensaver` runs in the background, and you can control it in various ways:

_After a period of inactivity_ .

You can configure `xscreensaver` to run automatically after a period of inactivity, such as five minutes.

_As a screen locker_ .

`xscreensaver` can also lock your screen on request. Your display will remain locked until you enter your login password.

_On the command line_ .

Run `xscreensaver-demo` to preview the many animations and set things up the way you like. Then run `xscreensaver-command` to control the program’s behavior:

- `$ xscreensaver-command -activate` _`Blank now`_ 

> `$ xscreensaver-command -next` _`Choose next animation`_ 

- `$ xscreensaver-command -prev` _`Choose previous animation`_ 

- `$ xscreensaver-command -cycle` _`Choose random animation`_ 

- `$ xscreensaver-command -lock` _`Lock the screen now`_ 

- `$ xscreensaver-command -exit` _`Quit`_ 

## **Audio** 

|`amarok`|Audio file player (MP3, WAV,<br>OGG).|
|---|---|
|`grip`|CD player, ripper, and MP3 encoder.|
|`cdparanoi`<br>`a`|Rip audio from CDs to WAV files.|
|`lame`|Convert from WAV to MP3.|
|`id3tag`|Edit ID3 tags.|
|`audacity`|Edit audio files.|
|`k3b`|CD burner with graphical interface.|

Audio is alive and well on Linux systems. Most of the programs we’ll cover have intuitive user interfaces, tons of features, and reasonable documentation, so we won’t discuss them in detail. Mainly, we want you to have a taste of what’s available and possible. Visit <u>http://linux-sound.org/</u> for a directory of Linux audio and MIDI programs.

#### **Name** 

amarok — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
xmms [options] [files or URLs]
```

Linux has numerous audio file players, including `amarok` , `audacious` , `rhythmbox` , and more. We’ll cover `amarok` , but your system probably has several of these programs installed.

The easiest way to get started with `amarok` is to try it, either with no arguments:

```
$ amarok
```

or providing audio files or URLs on the command line:

- `$ amarok file1.mp3 file2.wav file3.ogg ...` 

- `$ amarok http://www.example.com/song.mp3` 

#### **Useful options** 

|`--pause`|Pause the current<br>track.|
|---|---|
|`--play`|Begin playing.|
|`--stop`|Stop playing.|
|`--`<br>`previous`|Play the previous<br>track.|
|`--next`|Play the next track.|

#### **Name** 

grip — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
grip [options]
```

`grip` is a CD player and an audio ripper: it can play CDs, extract audio from CDs, save it in WAV files, and convert the files to MP3s. It has extensive built-in help and fairly intuitive controls.

`grip` hasn’t been updated in quite a while (though it’s very good), so if you prefer a program that’s still maintained, check out Sound Juicer <u>(http://burtonini.com/blog/computers/sound-juicer/) or KAudioCreator (http://www.kde.org/applications/multimedia/kaudiocreator/).</u>

#### **Name** 

cdparanoia — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
cdparanoia [options] span [outfile]
```

The `cdparanoia` command reads (rips) audio data from a CD and stores it in WAV files (or other formats: see the manpage). Common uses are:

- `$ cdparanoia` _`N`_ 

Rip track _`N`_ to a file.

- `$ cdparanoia -B` 

Rip all tracks on the CD into separate files.

- `$ cdparanoia -B 2-4` 

Rip tracks 2, 3, and 4 into separate files.

- `$ cdparanoia 2-4` 

Rip tracks 2, 3, and 4 into a single file.

If you have difficulty accessing your drive, try running `cdparanoia -Qvs` (“search for CD-ROM drives verbosely”) and look for clues.

#### **Name** 

lame — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
lame [options] file.wav
```

The `lame` command converts a WAV audio file (say, _song.wav_ ) into an MP3 file:

```
$ lame song.wav song.mp3
```

It has over 100 options to control bit rate, convert other formats, add ID3 tags, and much more.

#### **Name** 

id3tag — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
id3tag [options] files
```

The `id3tag` command adds or modifies ID3 tags in an MP3 file. For example, to tag an MP3 file with a new title and artist, run:

```
$ id3tag -A "My Album" -a "Loud Linux Squad" song.mp3
```

#### **Useful options** 

|`-A`|_`name`_|Set the artist’s name|
|---|---|---|
|`-a`|_`title`_|Set the album title|
|`-s`|_`title`_|Set the song title|
|`-y`|_`year`_|Set the year|
|`-t`||Set the track number|
|_`nu`_|_`mber`_||
|`-g`<br>_`nu`_|_`mber`_|Set the genre<br>number|

#### **Name** 

audacity — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
audacity [files]
```

`audacity` is a graphical audio file editor for making changes to WAV, MP3, and Ogg files. Once a file is loaded, you can view its waveform, cut and paste audio data, apply filters and special effects to the sound (echo, bass boost, reverse, etc.), and more. See <u>http://audacity.sourceforge.net/</u> for details.

#### **Name** 

k3b — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
k3b [options]
```

`k3b` is a CD burning program with a graphical user interface. (For a command-line interface, see <u>cdrecord.) Run the program and when the main</u> window appears, visit the File menu. Browse to New Project and select the type of disc you want to burn. A New Data Project simply burns files and directories to the disc so it can be read on other computers. New Music Project and New Video Project should be self-explanatory. Once you’ve selected the type of project, drag your desired files or folders from the top half of the window (showing your filesystem) to the bottom half (listing what will be burned). When done, click the Burn icon.

The Tools menu also has useful commands. These include copying discs, working with ISO images, and ripping audio and video discs to files.

## **Video** 

<!-- Start of picture text --> mplayer Video file<br>playback.<br>gxine Simple DVD<br>player.<br>kino Video editor.<br>HandBrak Video ripper.<br>e<br><!-- End of picture text -->

Linux has some fine programs for common video operations, such as playback, editing, and ripping. We’ll briefly survey a few popular ones.

#### **Name** 

mplayer — stdin  stdout  -file  -- opt  --help  --version **Synopsis**

```
mplayer [options] video_files...
```

The `mplayer` command plays video files in many formats: MPEG, AVI, MOV, and more:

```
$ mplayer myfile.avi
```

While the video is playing, press the space bar to pause and resume, the cursor keys to jump forward and backward in time, and Q to quit. The program has dozens of options on its manpage, and you can learn more at <u>http://www.mplayerhq.hu.</u>

Other popular video players for Linux include `vlc` <u>(http://www.videolan.org/vlc/),</u> `kaffeine` <u>(http://kaffeine.kde.org/), and</u> `xine` <u>(http://sourceforge.net/projects/xine/).</u>

#### **Name** 

gxine — stdin  stdout  -file  -- opt  --help  --version **Synopsis**

```
gxine [options] [source]
```

The `gxine` command displays a graphical video player that supports DVDs and video files. Just type `gxine` to get started with the graphical user interface, or provide a video source such as a file:

```
$ gxine myfile.mpeg
```

or a Media Resource Locator (MRL):

- `$ gxine dvd://home/jsmith/myvideo.iso` 

#### **Name** 

kino — stdin  stdout  -file  -- opt  --help  --version **Synopsis**

```
kino [file]
```

`kino` is a video editor that can split videos into parts and reassemble them in another order. It can also capture video (if you have compatible hardware) and play it back. An overview of `kino` and video editing is beyond the scope of this book, so visit <u>http://kinodv.org/</u> for full details.

#### **Name** 

HandBrake — stdin  stdout  -file  -- opt  --help  --version **Synopsis**

```
ghb [options]
HandBrakeCLI [options] -i device -o file
```

HandBrake is a video ripper (transcoder) that can copy video from DVDs and Blu-ray discs to files, as long as the discs are not copy-protected. It comes as a graphical program, `ghb` , and a command-line program, `HandBrakeCLI` (note the capital letters, unusual for a Linux command). To get started, we recommend `ghb` . Full details can be found at <u>http://handbrake.fr.</u>

## **Installing Software** 

You will probably want to add further software to your Linux system from time to time. The method of installation varies, however, because Linux has multiple standards for “packaged” software. Your distro might do installations on the command line, with one or more GUI tools, or both. The most common package types are:

- _*.deb files_ 

Debian packages, used by Debian, Ubuntu, and other distros. We’ll cover the package manager `aptitude` for installing software in this format.

- _*.rpm files_ 

RPM Package Manager files are used by Red Hat, Fedora, CentOS, and other distros. These are installed by the package managers `yum` , `rpm` , and on older systems, `up2date` .

- _*.tar.gz files, *.tar.Z files, and *.tar.bz2 files_ 

   - Compressed tar files. This kind of file isn’t an installable “package” but a collection of files created by `tar` and compressed with `gzip` ( _.gz_ ), `bzip2` ( _.bz2_ ), or `compress` (.Z). Whereas Debian and RPM packages can be installed with a single command, compressed tar files usually require multiple manual steps. 

_You must learn which package type is used by your Linux system_ . In general, you cannot (or should not) mix package types like Debian and RPM. Fortunately, modern Linux systems are usually set up with a package manager when initially installed, so all you need to do is use it.

Most new software must be installed by the superuser, so you’ll need to run the `su` command (or equivalent) before installation. For example:

```
$ su -l
Password: ********
# rpm -ivh mypackage.rpm
...etc...
```

or with `sudo` :

```
$ sudo rpm -ivh mypackage.rpm
Password: ********
```

To locate new software, run the “search” utility of your package manager, check your Linux DVDs or CD-ROMs, or visit fine sites like these:

<u>http://freecode.com/ http://freshrpms.net/ http://rpmfusion.org/ http://sourceforge.net /</u>

#### **Name** 

yum — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
yum [options] [packages]
```

`yum` is a popular package manager for RPM packages ( _.rpm_ files) found on Red Hat Enterprise Linux, Fedora, CentOS, and other distros. It is primarily a command-line tool, though you may encounter graphical front-ends for `yum` , such as PackageKit on Fedora Linux.

The following table lists common operations with `yum` . For operations on local files, which `yum` does not provide, we use the `rpm` command directly.

|Action|yum command|
|---|---|
|Search for a package that meets your needs (supports wildcards * and ?).|`yum search`<br>`command_name`|
|Check if a package is installed.|`yum list`<br>`installed`<br>_`package_name`_|
|Download a package but don’t install it. This requires installing the<br>`downloadonly`plugin first by running:<br>`yum install yum-downloadonly`|`yum --`<br>`downloadonly`<br>`install`<br>_`package_name`_|
|Download and install a package.|`yum install`<br>_`package_name`_|
|Install a package file.|`rpm -ivh`<br>_`package`_`.rpm`|
|Learn about a package.|`yum info`<br>_`package_name`_|

|Action|yum command|
|---|---|
|List the contents of a package.|`rpm -ql`_`package_name`_|
|Discover which package an installed file belongs to.|`yum provides`<br>_`/path/to/file`_|
|Update an installed package.|`yum update`<br>_`package_name`_|
|Remove an installed package.|`yum remove`<br>_`package_name`_|
|List all packages installed on the system.|`yum list`<br>`installed | less`|
|Check for updates for all packages on the system.|`yum check-update`|
|Update all packages on the system.|`yum update`|

#### **Name** 

rpm — stdin  stdout  - file  -- opt  --help  --version

#### **Synopsis** 

```
rpm [options] [files]
```

If you prefer to download and install RPM packages by hand, use `rpm` , the same package-management program that `yum` runs behind the scenes. Unlike `yum` , `rpm` works locally on your computer: it does not search software archives on the Internet for new packages.

`rpm` not only installs the software, but also makes sure your system has all prerequisites. For example, if package _superstuff_ requires package _otherstuff_ that you haven’t installed, `rpm` will not install _superstuff_ . If your system passes the test, however, `rpm` completely installs the software.

RPM filenames typically have the form _`name-version.architecture`_ `.rpm` . For example, _emacs-23.1-17.i386.rpm_ indicates the emacs package, version 23.1-17, for i386 (Intel 80386 and higher) machines. Be aware that `rpm` sometimes requires a filename argument (like _emacs-23.1-17.i386.rpm_ ) and other times just the package name (like _emacs_ ).

|Action|rpm command|
|---|---|
|Check if a package is installed|`rpm -q`_`package_name`_|
|Install a package file|`rpm -ivh`<br>_`package_file`_`.rpm`|
|Learn about a package|`rpm -qi`_`package_name`_|
|List the contents of a package|`rpm -ql`_`package_name`_|
|Discover which package an installed file belongs<br>to|`rpm -qf`_`/path/to/file`_|

|Action|rpm command|
|---|---|
|Update an installed package|`rpm -Uvh`<br>_`package_file`_`.rpm`|
|Remove an installed package|`rpm -e`_`package_name`_|
|List all packages installed on the system|`rpm -qa | less`|

#### **Name** 

aptitude — stdin  stdout  - file  -- opt  --help  --version **Synopsis**

```
aptitude [options] [packages]
```

`aptitude` is a package manager for the command line that manipulates Debian ( _.deb_ ) packages. Some older Debian package managers, including Advanced Packaging Tool (the `apt-get` command suite) and `dpkg` , are also in wide use today. (In our table of commands, we’ll use `dpkg` to work with local files, since `aptitude` does not do this.) You’ll also encounter graphical package managers like `synaptic` and Ubuntu’s `update-manager` .

|Action|yum command|
|---|---|
|Search for a package that meets your needs|`aptitude search`<br>_`package_name`_|
|Check if a package is installed (examine the output for “State: not<br>installed” or “State: installed”)|`aptitude show`<br>_`package_name`_|
|Download a package but don’t install it|`aptitude download`<br>_`package_name`_|
|Download and install a package|`aptitude install`<br>_`package_name`_|
|Install a package file|`dpkg -i`_`package_file`_`.deb`|
|Learn about a package|`aptitude show`<br>_`package_name`_|
|List the contents of a package|`dpkg -L`_`package_name`_|
|Discover which package an installed file belongs to|`dpkg -S`_`/path/to/file`_|

|Action|yum command|
|---|---|
|Update an installed package|`aptitude safe-upgrade`<br>_`package_name`_|
|Remove an installed package|`aptitude remove`<br>_`package_name`_|
|List all packages installed on the system|`aptitude search '~i'`<br>`| less`|
|Check for updates for all packages on the system|`aptitude --simulate`<br>`full-upgrade`|
|Update all packages on the system|`aptitude full-upgrade`|

#### **Name** 

#### **tar.gz and tar.bz2 Files** 

Packaged software files with names ending _.tar.gz_ and _.tar.bz2_ typically contain source code that you’ll need to compile (build) before installation. Typical build instructions are:

1. List the package contents, one file per line. Assure yourself that each file, when extracted, won’t overwrite something precious on your system, either accidentally or maliciously:<sup>[</sup> <u>21</u><sup>]</sup> 

```
$ tar tvzf package.tar.gz | less         For gzip files
```

   - `$ tar tvjf` _`package`_ `.tar.bz2 | less` _`For bzip2 files`_ 

2. If satisfied, extract the files into a new directory. Run these commands as yourself, not as root, for safety reasons: 

```
$ mkdir newdir
```

- `$ cd newdir` 

```
$ tar xvzf <path>/package.tar.gz         For gzip files
```

   - `$ tar xvjf` _`<path>`_ `/` _`package`_ `.tar.bz2` _`For bzip2 files`_ 

3. Look for an extracted file named _INSTALL_ or _README_ . Read it to learn how to build the software, for example: 

   - `$ cd newdir` 

   - `$ less INSTALL` 

4. Usually the _INSTALL_ or _README_ file will tell you to run a script called `configure` in the current directory, then run `make` , then run `make install` . Examine the options you may pass to the `configure` script: 

```
$ ./configure --help
```

Then install the software:

```
$ ./configure options
$ make
$ su
Password: *******
# make install
```

[21<sup>]</sup> A maliciously designed tar file could include an absolute file path like _/etc/passwd_ designed to overwrite your system password file.

## **Programming with Shell Scripts** 

Earlier when we covered the shell (bash), we said it had a programming language built in. In fact, you can write programs, or _shell scripts_ , to accomplish tasks that a single command cannot. Like any good programming language, the shell has variables, conditionals (if-then-else), loops, input and output, and more. Entire books have been written on shell scripting, so we’ll be covering the bare minimum to get you started. For full documentation, run `info bash` , search the Web, or pick up a more in-depth O’Reilly book.

#### **Whitespace and Linebreaks** 

`bash` shell scripts are very sensitive to whitespace and linebreaks. Because the “keywords” of this programming language are actually commands evaluated by the shell, you need to separate arguments with whitespace. Likewise, a linebreak in the middle of a command will mislead the shell into thinking the command is incomplete. Follow the conventions we present here and you should be fine.

If you must break a long command into multiple lines, end each line (except the last) with a single `\` character, which means “continued on next line”:

> `$ grep abcdefghijklmnopqrstuvwxyz file1 file2 \ file3 file4` 

#### **Variables** 

We described shell variables earlier:

```
$ MYVAR=6
$ echo $MYVAR
6
```

All values held in variables are strings, but if they are numeric, the shell will treat them as numbers when appropriate.

```
$ NUMBER="10"
$ expr $NUMBER + 5
15
```

When you refer to a variable’s value in a shell script, it’s a good idea to surround it with double quotes to prevent certain runtime errors. An undefined variable, or a variable with spaces in its value, will evaluate to something unexpected if not surrounded by quotes, causing your script to malfunction.

```
$ FILENAME="My Document"            Space in the name
$ ls $FILENAME                      Try to list it
ls: My: No such file or directory   Oops! ls saw 2 arguments
ls: Document: No such file or directory
$ ls -l "$FILENAME"                 List it properly
My Document                         ls saw only 1 argument
```

If a variable name is evaluated adjacent to another string, surround it with curly braces to prevent unexpected behavior:

```
$ HAT="fedora"
```

```
$ echo "The plural of $HAT is $HATs"
The plural of fedora is             Oops! No variable "HATs"
$ echo  "The plural of $HAT is ${HAT}s"
The plural of fedora is fedoras     What we wanted
```

#### **Input and Output** 

Script output is provided by the `echo` and `printf` commands, which we described in <u>Screen Output:</u>

```
$ echo "Hello world"
Hello world
$ printf "I am %d years old\n" `expr 20 + 20`
I am 40 years old
```

Input is provided by the `read` command, which reads one line from standard input and stores it in a variable:

```
$ read name
Sandy Smith <ENTER>
$ echo "I read the name $name"
I read the name Sandy Smith
```

#### **Booleans and Return Codes** 

Before we can describe conditionals and loops, we need to explain the concept of a Boolean (true/false) test. To the shell, the value 0 means true or success, and anything else means false or failure. (Think of zero as “no error” and other values as error codes.)

Additionally, every Linux command returns an integer value, called a _return code_ or _exit status_ , to the shell when the command exits.

You can see this value in the special variable `$?` :

```
$ cat myfile
My name is Sandy Smith and
I really like Ubuntu Linux
$ grep Smith myfile
My name is Sandy Smith and      A match was found...
$ echo $?
0                               ...so return code is “success”
$ grep aardvark myfile
$ echo $?                       No match was found...
1                               ...so return code is “failure”
```

The return codes of a command are usually documented on its manpage.

###### **test and “[”** 

The `test` command (built into the shell) will evaluate simple Boolean expressions involving numbers and strings, setting its exit status to 0 (true) or 1 (false):

```
$ test 10 -lt 5       Is 10 less than 5?
$ echo $?
1                     No, it isn’t
$ test -n "hello"     Does the string “hello” have nonzero length?
$ echo $?
0                     Yes, it does
```

Here are common `test` arguments for checking properties of integers, strings, and files:

###### **File tests** 

|`-d` _`name`_|File_`name`_is a directory|
|---|---|
|`-f` _`name`_|File_`name`_is a regular file|
|`-L` _`name`_|File_`name`_is a symbolic link|
|`-r` _`name`_|File_`name`_exists and is readable|

|`-w` _`name`_|File_`name`_exists and is writable|
|---|---|
|`-x` _`name`_|File_`name`_exists and is executable|
|`-s` _`name`_|File_`name`_exists and its size is nonzero|
|_`f1`_ `-nt` _`f2`_|File_`f1`_is newer than file_`f2`_|
|_`f1`_ `-ot` _`f2`_|File_`f1`_is older than file_`f2`_|
|**String tests**||
|_`s1`_ `=` _`s2`_|String_`s1`_equals string_`s2`_|
|_`s1`_ `!=` _`s2`_|String_`s1`_does not equal string_`s2`_|
|`-z` _`s1`_|String_`s1`_has zero length|
|`-n` _`s1`_|String_`s1`_has nonzero length|
|**Numeric tes**|**ts**<br>|
|_`a`_ `-eq` _`b`_|Integers_`a`_and_`b`_are equal|
|_`a`_ `-ne` _`b`_|Integers_`a`_and_`b`_are not equal|
|_`a`_ `-gt` _`b`_|Integer_`a`_is greater than integer_`b`_|
|_`a`_ `-ge` _`b`_|Integer_`a`_is greater than or equal to integer_`b`_|
|_`a`_ `-lt` _`b`_|Integer_`a`_is less than integer_`b`_|
|_`a`_ `-le` _`b`_|Integer_`a`_is less than or equal to integer_`b`_|
|**Combining**|**and negating tests**|
|`t1 -a t2`|And: Both tests`t1`and`t2`are true|
|`t1 -o t2`|Or: Either test`t1`or`t2`is true|
|`!` _`your_test`_|Negate the test, i.e.,`your_test`is false|
|`\(` _`your_test`_<br>`\)`|Parentheses are used for grouping, as in<br>algebra|

`test` has an unusual alias, “ `[` ” (left square bracket), as a shorthand for use with conditionals and loops. If you use this shorthand, you must supply a final argument of “ `]` ” (right square bracket) to signify the end of the test. The following tests are identical to the previous two:

```
$ [ 10 -lt 5 ]
$ echo $?
1
$ [ -n "hello" ]
$ echo $?
0
```

Remember that “ `[` ” is a command like any other, so it is followed by _individual arguments separated by whitespace_ . So if you mistakenly forget some whitespace:

```
$ [ 5 -lt 4]          No space between 4 and ]
bash: [: missing ']'
```

then `test` thinks the final argument is the string “4]” and complains that the final bracket is missing.

###### **true and false** 

bash has built-in commands `true` and `false` , which simply set their exit status to 0 and 1, respectively.

```
$ true
$ echo $?
0
$ false
$ echo $?
1
```

These will be useful when we discuss conditionals and loops.

#### **Conditionals** 

The `if` statement chooses between alternatives, each of which may have a complex test. The simplest form is the `if-then` statement:

```
if commandIf exit status of command is 0
then
body
fi
```

For example:

```
if [ `whoami` = "root" ]
then
  echo "You are the superuser"
fi
```

Next is the `if-then-else` statement:

`if` _`command`_ `then` _`body1`_ `else` _`body2`_ `fi` For example:

```
if [ `whoami` = "root" ]
then
  echo "You are the superuser"
else
  echo "You are an ordinary dude"
fi
```

Finally, we have the form `if-then-elif-else` , which may have as many tests as you like:

`if` _`command1`_ `then` _`body1`_ `elif` _`command2`_ `then` _`body2`_ `elif ... ... else` _`bodyN`_ `fi` For example:

```
if [ `whoami` = "root" ]
then
  echo "You are the superuser"
elif [ "$USER" = "root" ]
then
  echo "You might be the superuser"
elif [ "$bribe" -gt 10000 ]
then
  echo "You can pay to be the superuser"
else
  echo "You are still an ordinary dude"
fi
```

The `case` statement evaluates a single value and branches to an appropriate piece of code:

```
echo "What would you like to do?"
read answer
case "$answer" in
  eat)
    echo "OK, have a hamburger"
    ;;
  sleep)
    echo "Good night then"
    ;;
  *)
    echo "I'm not sure what you want to do"
    echo "I guess I'll see you tomorrow"
    ;;
esac
```

The general form is:

```
case string in
expr1)
body1
    ;;
expr2)
body2
    ;;
  ...
exprN)
bodyN
    ;;
  *)
bodyelse
    ;;
esac
```

where _`string`_ is any value, usually a variable value like `$myvar` , and _`expr1`_ through _`exprN`_ are patterns (run the command `info bash reserved case` for details), with the final `*` like a final “else.” Each set of commands must be terminated by `;;` (as shown):

```
case $letter in
  X)
    echo "$letter is an X"
    ;;
  [aeiou])
    echo "$letter is a vowel"
    ;;
  [0-9])
    echo "$letter is a digit, silly"
    ;;
  *)
    echo "The letter '$letter' is not supported"
    ;;
esac
```

#### **Loops** 

The `while` loop repeats a set of commands as long as a condition is true.

```
while commandWhile the exit status of command is 0
do
body
done
```

For example, if this is the script `myscript` :

```
i=0
while [ $i -lt 3 ]
do
  echo "$i"
  i=`expr $i + 1`
done
$ ./myscript
0
1
2
```

The `until` loop repeats until a condition becomes true:

```
until commandWhile the exit status of command is nonzero
do
body
done
```

For example:

```
i=0
until [ $i -ge 3 ]
do
  echo "$i"
  i=`expr $i + 1`
done
$ ./myscript
0
1
2
```

The `for` loop iterates over values from a list:

```
for variable in list
do
body
done
```

For example:

```
for name in Tom Jack Harry
do
  echo "$name is my friend"
done
$ ./myscript
Tom is my friend
Jack is my friend
Harry is my friend
```

The `for` loop is particularly handy for processing lists of files; for example, all files of a certain type in the current directory:

```
for file in *.doc *.docx
do
  echo "$file is a stinky Microsoft Word file"
done
```

Be careful to avoid infinite loops, using `while` with the condition `true` , or `until` with the condition `false` :

```
while true           Beware: infinite loop!
do
  echo "forever"
done
until false          Beware: infinite loop!
do
  echo "forever again"
done
```

Use `break` or `exit` to terminate these loops based on some condition inside their bodies.

#### **Break and Continue** 

The `break` command jumps out of the nearest enclosing loop. Consider this simple script called `myscript` :

```
for name in Tom Jack Harry
do
  echo $name
  echo "again"
done
echo "all done"
$ ./myscript
Tom
again
Jack
again
Harry
again
all done
```

Now with a `break` :

```
for name in Tom Jack Harry
do
  echo $name
  if [ "$name" = "Jack" ]
  then
    break
  fi
  echo "again"
done
echo "all done"
$ ./myscript
Tom
again
Jack            The break occurs after this line
all done
```

The `continue` command forces a loop to jump to its next iteration.

```
for name in Tom Jack Harry
do
  echo $name
  if [ "$name" = "Jack" ]
  then
    continue
  fi
  echo "again"
done
echo "all done"
$ ./myscript
Tom
again
```

```
Jack          The continue occurs after this line
Harry
again
all done
```

`break` and `continue` also accept a numeric argument ( `break` _`N`_ , `continue` _`N`_ ) to control multiple layers of loops (e.g., jump out of _`N`_ layers of loops), but this kind of scripting leads to spaghetti code and we don’t recommend it.

#### **Creating and Running Shell Scripts** 

To create a shell script, simply put bash commands into a file as you would type them. To run the script, you have three choices:

_Prepend_ _`#!/bin/bash` and make the file executable_

This is the most common way to run scripts. Add the line:

```
#!/bin/bash
```

to the very top of the script file. It must be the first line of the file, leftjustified. Then make the file executable:

```
$ chmod +x myscript
```

Optionally, move it into a directory in your search path. Then run it like any other command:

```
$ myscript
```

If the script is in your current directory, but the current directory “.” is not in your search path, you’ll need to prepend “./” so the shell finds the script:

```
$ ./myscript
```

The current directory is generally not in your search path for security reasons. (You wouldn’t want a local script named (say) “ls” to override the real `ls` command.)

_Pass to bash_

bash will interpret its argument as the name of a script and run it.

```
$ bash myscript
```

_Run in current shell with “.” or_ _`source`_

The preceding methods run your script as an independent entity that has no effect on your current shell.<sup>[</sup> <u>22</u><sup>]</sup> If you want your script to make changes to your current shell (setting variables, changing directory, and so on), it can be run in the current shell with the `source` or “.” command:

> `$ . myscript` 

> `$ source myscript` 

[22<sup>]</sup> That’s because the script runs in a separate shell (a _subshell_ or _child shell_ ) that cannot alter the original shell.

#### **Command-Line Arguments** 

Shell scripts can accept command-line arguments and options just like other Linux commands. (In fact, some common Linux commands _are_ scripts.) Within your shell script, you can refer to these arguments as `$1` , `$2` , `$3` , and so on.

```
$ cat myscript
#!/bin/bash
echo "My name is $1 and I come from $2"
$ ./myscript Johnson Wisconsin
My name is Johnson and I come from Wisconsin
$ ./myscript Bob
My name is Bob and I come from
```

Your script can test the number of arguments it received with `$#` :

```
if [ $# -lt 2 ]
then
  echo "$0 error: you must supply two arguments"
else
  echo "My name is $1 and I come from $2"
fi
```

The special value `$0` contains the name of the script, and is handy for usage and error messages:

```
$ ./myscript Bob
./myscript error: you must supply two arguments
```

To iterate over all command-line arguments, use a `for` loop with the special variable `$@` , which holds all arguments:

```
for arg in $@
do
  echo "I found the argument $arg"
done
```

#### **Exiting with a Return Code** 

The `exit` command terminates your script and passes a given return code to the shell. By tradition, scripts should return 0 for success and 1 (or other nonzero value) on failure. If your script doesn’t call `exit` , the return code is automatically 0.

```
if [ $# -lt 2 ]
then
  echo "$0 error: you must supply two arguments"
  exit 1
else
  echo "My name is $1 and I come from $2"
fi
exit 0
$ ./myscript Bob
./myscript error: you must supply two arguments
$ echo $?
1
```

#### **Beyond Shell Scripting** 

Shell scripts are fine for many purposes, but Linux comes with much more powerful scripting languages, as well as compiled programming languages. Here are a few.

|Languag<br>e|Progra<br>m|To get started...|
|---|---|---|
|C, C++|`gcc`,`g++`|`man gcc`<br>http://www.gnu.org/software/gc<br>c/|
|.NET|`mono`|`man mono`<br>http://www.mono-project.com/|
|Java|`javac`|http://java.sun.com/|
|Perl|`perl`|`man perl`<br>http://www.perl.com/|
|PHP|`php`|`man php`<br>http://www.php.net/|
|Python|`python`|`man python`<br>http://www.python.org/|
|Ruby|`ruby`|http://ruby-lang.org/|

## **Final Words** 

Although we’ve covered many commands and capabilities of Linux, we’ve just scratched the surface. Most distributions come with _thousands_ of other programs. We encourage you to continue reading, exploring, and learning the capabilities of your Linux systems. Good luck!

#### **Acknowledgments** 

I am very grateful to the many readers who purchased the first edition of this book, making the second edition possible. My heartfelt thanks also go to my long-time editor Mike Loukides and new editor Andy Oram, the O’Reilly production staff, the technical review team (Stephen Figgins, Stephen Roylance, and Ellen Siever), Chris Connors at Vistaprint, and as always, my wonderful family, Lisa and Sophia.

## **Index** 

###### **A NOTE ON THE DIGITAL INDEX** 

A link in an index entry is displayed as the section title in which that entry appears. Because some sections have multiple index markers, it is not unusual for an entry to have several links to the same section. Clicking on any link will take you directly to the place in the text in which the marker appears.

#### **Symbols** 

! (shell command history), <u>Command history</u>

& (ampersand), running background jobs,

&& (two ampersands), logical and, stopping execution of combined commands, <u>Combining commands</u>

- (dash), standard input/output, <u>Reading This Book</u> 

-- (two dashes), end of options, <u>Reading This Book</u>

--help option, <u>Getting Help</u>

. (period)

current directory, <u>The Filesystem</u>

dot files, <u>Wildcards</u>

shell script execution, <u>Creating and Running Shell Scripts</u>

.. (two periods), parent directory, <u>The Filesystem</u>

.NET, <u>Beyond Shell Scripting</u>

/ (slash), root directory, <u>The Filesystem</u>

; (semicolon), combine commands using, <u>Combining commands</u>

[ (left square bracket), alias for test command, <u>test and “[”</u>

\ (backward slash)

escaping special characters, <u>Escaping</u>

line continuation, <u>Whitespace and Linebreaks</u>

^C command (killing programs), <u>Killing a Command in Progress</u>

^Z command (suspending jobs),  ,

| (pipe operator), <u>Pipes</u> || (two pipes), logical or, stopping execution of combined commands, <u>Combining commands</u>  ̃ (tilde), denoting home directories, <u>Home Directories</u> **A** abiword command, absolute path of current directory, printing, acroread viewer, Adobe Photoshop, Advanced Packaging Tool, alias command, <u>Aliases</u> alphabetical order, sorting text in, alpine mail program, <u>Email</u> amarok command, ampersand (&), running background jobs, apt-get command, aptitude command, <u>Installing Software,</u> arguments for commands, <u>What’s a Command?</u> aspell command, at command, atq command, atrm command, attributes of files, changing, 

viewing, audacious command, audacity sound editor, audio, <u>Audio</u> editing, playback, ripping,  , awk command, <u>awk</u> vs. tr command, **B** background jobs, running, <u>Shell Job Control</u> backing up Linux files, <u>Backups and Remote Storage</u> backquotes on command line, <u>Quoting,</u> vs. xargs, <u>Useful options</u> backward slash (\) escaping special characters, <u>Escaping</u> line continuation, <u>Whitespace and Linebreaks</u> basename command, bash (Bourne-Again Shell), <u>Linux: A First View, The Shell</u> command-line editing, <u>Command-line editing</u> printf command, programming with shell scripts, <u>Programming with Shell Scripts</u> type command, <u>File Location,</u> bg command, jobs command and,

bin directory, <u>Directory path part 1: category</u> Booleans in shell scripts,  , <u>Booleans and Return Codes</u> /boot directory, <u>Operating System Directories</u> Bourne-Again Shell (see bash), <u>The Shell</u> braces expansion on command line, <u>Brace expansion</u> grep regular expressions, shell variables, <u>Variables</u> break command, <u>Break and Continue</u> browsing the Web, <u>Web Browsing</u> bunzip2 command, burning CDs and DVDs,  , bzcat command, <u>Sample commands</u> bzip2 command, tar –j command and, <u>Useful options</u> **C** C and C++ languages, <u>Beyond Shell Scripting</u> cal command, Calc program (soffice), calculator programs, <u>Math and Calculations</u> calendar printing, carriage returns, case statement, <u>Conditionals</u> cat command, revealing end-of-line characters,

tee command and, CD burning programs,  , cd command, <u>The Filesystem, The Filesystem,</u> home directories, locating, <u>Home Directories</u> CD ripping,  , cdparanoia command, cdrecord command, k3b command and, cgi-bin directory, <u>Directory path part 1: category</u> chattr command, checksums, comparing, chfn command, with useradd, <u>Useful options</u> chgrp command, <u>File Protections,  , Group Management</u> chmod command, <u>File Protections,</u> chown command, <u>File Protections,</u> chsh command, cksum command, <u>File Comparison,</u> clear command, clearing the screen, clock programs, <u>Dates and Times</u> cmp command, <u>File Comparison, Useful options</u> columns of text, extracting from files, combining commands, <u>Combining commands</u> comm command, <u>File Comparison,</u>

command-line arguments in shell scripts, <u>Command-Line Arguments</u> command-line editing with bash, <u>Command-line editing</u> commands, <u>What’s a Command?</u>

combining, <u>Combining commands</u> killing, <u>Killing a Command in Progress,</u> previous, <u>Command history</u> comparing files, <u>File Comparison</u> completing filenames with TAB key, <u>Filename completion</u> compress command, software installation and, <u>Installing Software</u> tar –Z command and, <u>Useful options</u>

compressing/uncompressing files, <u>File Compression and Packaging</u> conditionals in shell scripts, <u>Conditionals</u> configure script, <u>tar.gz and tar.bz2 Files</u> configuring the shell, <u>Tailoring Shell Behavior</u> connecting to networks, <u>Network Connections</u> continue command, <u>Break and Continue</u> controlling processes, <u>Controlling Processes</u> cp command, cpio command, <u>Backups and Remote Storage</u> cron process, crontab command, CUPS printing system, <u>Printing</u> curl command, curly-brace expressions (see braces)

cut command, **D** date command, watch command and, dates, displaying/setting, <u>Dates and Times, Useful options</u> dc command, dd command, <u>Backups and Remote Storage</u> deb file, <u>Installing Software</u> Debian packages, <u>Installing Software,</u> default editor, setting, <u>Your Default Editor</u> desktop screen capture, /dev directory, <u>Directory path part 1: category</u> df command, dia command, diff command, <u>File Comparison,</u> diff3 command, <u>File Comparison,</u> dig command, <u>Useful options</u> directories, Linux, <u>The Filesystem</u> changing, using cd command, creating, deleting empty directories, home directories, <u>Home Directories</u> operating system directories, <u>Operating System Directories</u> printing absolute path of, system directories, <u>System Directories</u>

dirname command, disk usage command (du), disks and filesystems, <u>Disks and Filesystems</u> DISPLAY environment variable, <u>Shell variables</u> dnsdomainname command, <u>Host Information</u> doc directory, Directory path part 1: category domain name service (DNS), <u>Host Location</u>

querying, domainname command, <u>Host Information</u> dot files, <u>Wildcards</u> downloading files, dpkg command, du command, dump command, chattr command and, restore command and, DVD burning, DVD playback, DVI files, dvips command, **E** echo command, <u>Your friend, the echo command,</u>

script output provided by, <u>Input and Output</u> ed line editor, <u>sed</u> diff –e command,

EDITOR environment variable, setting default editor, <u>Your Default Editor</u> egrep command, else statement, <u>Conditionals</u> emacs text editor, <u>Command-line editing</u> bash command-line editing, <u>Command-line editing</u> creating/editing files, <u>File Creation and Editing</u> email readers, <u>Email</u> lynx –emacskeys command, <u>Useful options</u> email, <u>Email</u> directory, <u>Directory path part 1: category, Shell variables</u> emacs as reader, Email file format, <u>Beyond Mail Readers</u> log file, pipelines, queue, readers, <u>Email</u> reading over SSH connection, scripting, environment variables, <u>Shell variables</u> DISPLAY, <u>Shell variables</u> EDITOR,  , <u>Your Default Editor</u> HOME, <u>Home Directories, Shell variables</u> LOGNAME, Shell variables MAIL, <u>Shell variables</u>

NNTPSERVER, OLDPWD, Shell variables PATH, <u>Shell variables</u> preserving, in new shell, <u>Useful options</u> printing, PWD, <u>Shell variables</u> SHELL, <u>Shell variables</u> TERM, <u>Shell variables</u> USER, <u>Shell variables</u> VISUAL,  , <u>Your Default Editor</u> eog (Eye of Gnome) image viewer, Epiphany web browser for GNOME, escaping special characters, <u>Escaping</u> etc directory, <u>Directory path part 1: category</u> Evolution mail program, Excel documents, editing with gnumeric, editing with soffice, exclamation point (!) for shell history, <u>Command history</u> exit command, <u>Logins, Logouts, and Shutdowns</u> exiting with return codes, <u>Exiting with a Return Code</u> terminating loops, <u>Loops</u> terminating shells, <u>Terminating a Shell</u> exit status of Linux commands, <u>Booleans and Return Codes</u> export command, <u>Shell variables</u>

expr command, ext3 filesystems, <u>Disks and Filesystems</u> chattr/lsattr commands, Eye of Gnome (eog) image viewer, **F**

false command, <u>true and false</u>

infinite loops and, <u>Loops</u> fdisk command, <u>Disks and Filesystems</u> fetchmail command, <u>Beyond Mail Readers</u> fg command,

jobs command and, file command, filename completion, <u>Filename completion</u> files

attributes of, <u>File Properties</u> copying, using cp command, counting words, creating, <u>File Creation and Editing,</u> deleting, using rm command, disk space of, editing, <u>File Creation and Editing</u> group ownership, linking, using ln command, listing, using ls command, locating, <u>File Location</u>

moving, ownership, <u>File Protections,  ,  ,</u> permissions, <u>File Protections,  ,</u> renaming, using mv command, timestamps, transferring between machines,  , viewing, <u>File Viewing</u> filesystem, <u>The Filesystem, Disks and Filesystems</u> find command, with xargs, finger command,  , Firefox web browser, <u>The Graphical Desktop,</u> floppy command, <u>Disks and Filesystems</u> fonts directory, <u>Directory path part 1: category</u> for loops, <u>Loops</u> command-line arguments and, <u>Command-Line Arguments</u> foreground, bringing jobs into, formatting disks, <u>Disks and Filesystems, Disks and Filesystems</u> free command,  , fsck command,

shutdown command and, <u>Useful options</u> ftp (File Transfer Protocol) program, insecure, use sftp, **G** g++ command, <u>Beyond Shell Scripting</u>

gcc command, <u>Beyond Shell Scripting</u> geeqie image viewer, ghb command, ghostview command, DVI files and, GIMP (GNU Image Manipulation Program), GNOME graphical environment, <u>Linux: A First View</u> Epiphany web browser, getting help with, <u>Getting Help</u> xclock command, xscreensaver program, gnome-system-monitor command,  , GNU emacs (see emacs text editor) gnumeric command, gnuplot command, Google Groups, <u>Usenet News</u> gqview (see geeqie image viewer) graphical desktop, <u>The Graphical Desktop</u> graphics, viewing/editing, <u>Graphics and Screensavers,</u> graphing data, grep command, egrep command and, ps command and, grip command,

group ownership of files, groups, <u>Group Management</u> groupadd command, groupdel command, groupmod command, groups command, id –Gn command and, <u>Useful options</u> gunzip command, gv command, DVI files and, gxine command, gzip command, software installation and, <u>Installing Software</u> tar –z command and, <u>Useful options</u> **H** HandBrake, HandBrakeCLI command, hard links, hardware platform, <u>Useful options</u> head command, help and tutorials, <u>Getting Help</u> --help option, <u>Reading This Book</u> hexadecimal dump of binary files, history command, <u>Command history</u> home directories, <u>Home Directories</u>

HOME environment variable, <u>Home Directories, Shell variables</u> host command, host information, <u>Host Information, Host Location</u> hostname command, <u>Useful options,</u> html directory, <u>Directory path part 1: category</u> **I**

ICMP packets, id command, ID3 tags,  , id3tag command, if statement, <u>Conditionals</u> ifconfig command, images, viewing/editing, <u>Graphics and Screensavers,</u> Impress program (soffice), include directory, <u>Directory path part 1: category</u> index of file locations, creating, info command, <u>Getting Help</u> init.d directory, <u>Directory path part 1: category</u> input in shell scripts, <u>Input and Output</u> input/output redirection, <u>Input/output redirection</u> installing software, <u>Installing Software</u> instant messaging on Linux, <u>Instant Messaging</u> Internet domains, looking up registration of, ip command, ISO files,  ,

**J** Java language, <u>Beyond Shell Scripting</u> javac command, <u>Beyond Shell Scripting</u> job control in Linux shells, <u>Shell Job Control</u> jobs command, jobs, scheduling,  , **K** k3b command,  , kaffeine video player, KAudioCreator, KDE graphical environment, <u>Linux: A First View</u> getting help with, <u>Getting Help</u> Konqueror web browser, running shells within, <u>Running a Shell</u> xclock command, xscreensaver program, Kerberos, kernel, <u>Linux: A First View, Linux: A First View</u> name, <u>Useful options</u> version,  , <u>Useful options</u> kill command, <u>Killing a Command in Progress,</u> kino command, kmail command, <u>Email</u> konsole command, <u>Running a Shell</u> ksnapshot command,

**L** lame command, last command, less command, cat command and, lib directory, <u>Directory path part 1: category</u> libexec directory, <u>Directory path part 1: category</u> LibreOffice, line continuation character, <u>Whitespace and Linebreaks</u> linebreaks grep, in shell scripts, <u>Whitespace and Linebreaks</u> Windows and Macintosh, links, hard vs. symbolic, Linux, components of, <u>Linux: A First View</u> linuxforums.org, <u>Getting Help</u> linuxhelp.net, <u>Getting Help</u> linuxquestions.org, Getting Help ln command, load average,  ,  , locate command, locating files, lock directory, <u>Directory path part 1: category</u> log directory, <u>Directory path part 1: category</u>

logging into remote machines,  , logname command, whoami and, LOGNAME environment variable, <u>Shell variables</u> logout command, <u>Logins, Logouts, and Shutdowns</u> look command, loops in shell scripts, <u>Loops</u> /lost+found directory, Operating System Directories lpq command, lpr command, <u>Printing</u> lprm command, LPRng printing system, <u>Printing</u> ls command, <u>Reading This Book,</u> displaying file attributes, <u>File Properties</u> file protections and, <u>File Protections</u> lsattr command, lynx web browser, **M** m4 macro-processing language, <u>m4</u> magnetic tape command (mt), mail (see email) mail command, mail directory, <u>Directory path part 1: category, Shell variables</u> MAIL environment variable, <u>Shell variables</u> mailq command,

make command, <u>tar.gz and tar.bz2 Files</u> man command, <u>Getting Help, Directory path part 1: category</u> man directory, <u>Directory path part 1: category</u> masks and protection modes, math commands, <u>Math and Calculations</u> md5sum command, <u>File Comparison,  ,</u> /media directory, Directory path part 1: category memory usage, displaying, mesg command, <u>Useful options,</u> Microsoft Excel documents, editing with gnumeric, editing with soffice, Microsoft Visio, Microsoft Word documents, editing with abiword, editing with soffice, MIDI, Audio misc directory, <u>Directory path part 1: category</u> mkdir command, mkfs command, <u>Disks and Filesystems</u> mkisofs command,  , mlocate command, /mnt directory, <u>Directory path part 1: category</u> mono command, <u>Beyond Shell Scripting</u> mount command,

movie playback, Mozilla Firefox, Thunderbird, MP3 files create from WAV, ID3 tags, playback, mplayer command, mt command, mv command, **N** nameserver (see domain name service) .NET, <u>Beyond Shell Scripting</u> network connections, establishing, <u>Network Connections</u> network interface, displaying information about,  , news, Usenet, Usenet News nice command, nisdomainname command, <u>Host Information</u> nl command, cat command and, NNTPSERVER environment variable, nslookup command, <u>Useful options</u> ntfs filesystems, <u>Disks and Filesystems</u> ntp daemon,

ntpdate command, **O** oclock command, octal dump (od) command, od (octal dump) command, OLDPWD environment variable, <u>Shell variables</u> oobase command, oocalc command, oodraw command, ooimpress command, oomath command, oowriter command, OpenOffice.org package, Opera web browser, operating system directories, <u>Operating System Directories</u> operating system name, <u>Useful options</u> options for commands, <u>What’s a Command?</u> output in shell scripts, <u>Input and Output</u> ownership of files, <u>File Protections,</u> **P** package managers, <u>Installing Software</u> PackageKit, parted command, <u>Disks and Filesystems</u> partitioning disks, <u>Disks and Filesystems, Disks and Filesystems</u> passwd command,

paste command, patch command, context diff, PATH environment variable, <u>Shell variables</u> Perl language, <u>Beyond Shell Scripting</u> permissions, file, <u>File Protections,  ,</u> photos, viewing/editing, <u>Graphics and Screensavers,</u> Photoshop, PHP language, <u>Beyond Shell Scripting</u> pidgin command, pidof command, ping command, Pinta, pipe (|) operator, <u>Pipes</u> plotting data, postfix mail server, <u>Beyond Mail Readers</u> print screen, printenv command, at command and, printf command, script output provided by, <u>Input and Output</u> -printf option (find command), <u>Useful options</u> printing, <u>Printing</u> /proc directory, <u>Directory path part 1: category, Operating System Directories</u> processes, Controlling Processes

controlling, <u>Controlling Processes</u> shell jobs vs., <u>Viewing Processes</u> viewing, <u>Viewing Processes</u> processor type, <u>Useful options</u> procmail command, <u>Beyond Mail Readers</u> ps command,  , public_html directory, <u>Directory path part 1: category</u> pwd command, <u>The Filesystem,</u> PWD environment variable, <u>Shell variables</u> Python language, <u>Beyond Shell Scripting</u> **Q** quoting in shell scripts, <u>Variables</u> on command line, <u>Quoting</u> **R** rc.d directory, <u>Directory path part 1: category</u> rcsdiff command, read command, <u>Input and Output</u> readlink command, <u>Useful options</u> redirecting input/output, <u>Input/output redirection</u> regular expressions awk command, <u>awk</u> egrep command, find –regex command, <u>Useful options</u> grep command,  ,

less command and, locate –r command, <u>Search options for locate</u> remote machines, file transfers,  , hostname lookup, logging in with ssh, logging in with telnet, sending ICMP packets to, traceroute command, renice command, reset command, <u>Killing a Command in Progress</u> restore command,  ,  , mt command and, resuming jobs with fg command, return codes of Linux commands, <u>Booleans and Return Codes, Exiting with a Return Code</u> rhythmbox command, ripping CD tracks,  , rm command, RMAIL program, <u>Email</u> rmdir command, root directory (/), <u>The Filesystem</u> /root home directory for superuser, <u>Home Directories</u> root user, <u>Users and Superusers, Becoming the Superuser</u> rpm command, <u>Installing Software,</u>

RPM Package Manager files, <u>Installing Software,  ,</u> rsync command, Ruby language, <u>Beyond Shell Scripting</u> run directory, <u>Directory path part 1: category</u> **S**

sbin directory, <u>Directory path part 1: category</u> scheduling jobs,  , scp command, screen capture, screensavers,

viewing/editing, xscreensaver program, screenshots, sdiff command, <u>File Comparison,</u> secure copy (scp) command, secure shell (ssh) program, sed command, <u>sed</u>

vs. tr command,

semicolon (;), combine commands using, <u>Combining commands</u> sendmail mail server, <u>Beyond Mail Readers</u> seq command, setting the date and time, <u>Useful options</u>

by timeserver, sfdisk command, <u>Disks and Filesystems</u> sftp command,

share directory, <u>Directory path part 1: category</u> SHELL environment variable, <u>Shell variables</u> shell prompts, <u>What’s a Command?</u> for superuser commands, <u>Shell prompts</u> shell scripts, <u>Programming with Shell Scripts</u> break and continue in, <u>Break and Continue</u> command-line arguments in, <u>Command-Line Arguments</u> conditionals in, <u>Conditionals</u> creating, <u>Creating and Running Shell Scripts</u> exiting with return codes, <u>Exiting with a Return Code</u> loops in, <u>Loops</u> programming with, <u>Programming with Shell Scripts</u> running, <u>Creating and Running Shell Scripts</u> shell windows, opening, <u>Running a Shell</u> shells, <u>Linux: A First View, The Shell</u> (see also bash) changing login shell program, history-related commands, <u>Command history</u> job control, <u>Shell Job Control</u> running, <u>Running a Shell</u> suspending, terminating, <u>Terminating a Shell</u> vs. programs, <u>The Shell Versus Programs</u> shutdown command, <u>Logins, Logouts, and Shutdowns,</u> slash (/)

directory separator, <u>The Filesystem</u> root directory, <u>The Filesystem</u> sleep command, slocate command, slrn newsreader, soffice command, soft links, software installation, <u>Installing Software</u> sort command, sound (see audio) Sound Juicer, source command, <u>Creating and Running Shell Scripts</u> spamassassin, <u>Beyond Mail Readers</u> special characters, escaping, <u>Escaping</u> spell command, spelling checkers, <u>Spell Checking</u> spool directory, <u>Directory path part 1: category</u> src directory, <u>Directory path part 1: category</u> ssh (secure shell) program, stackexchange.com, <u>Getting Help</u> standard output, printing messages on, <u>Screen Output</u> stat command, su command, <u>Users and Superusers</u> becoming superuser, <u>Becoming the Superuser</u> software installation and, <u>Installing Software</u>

whoami command and, subdirectories, Linux, <u>The Filesystem</u> sudo command, <u>Users and Superusers, Useful options, Installing Software</u> sum command, <u>File Comparison,</u> superusers, Users and Superusers becoming, <u>Becoming the Superuser</u> suspend command, symbolic links, target file of, <u>Useful options</u> symlink, synaptic package manager, sync command,  , system directories, <u>System Directories</u> system load, displaying graphically,  , **T** TAB key, completing filenames with, <u>Filename completion</u> tail command, talk command, tape drives, copying files to,  , tar command,  , mt command and, software installation and, <u>Installing Software</u> tar files, <u>Installing Software, tar.gz and tar.bz2 Files</u> bzipped, <u>bzipped tar files: sample commands</u>

compressed, <u>Compressed tar files: sample commands</u> gzipped, <u>gzipped tar files: sample commands</u> tee command, telnet command, TERM environment variable, <u>Shell variables</u> Terminal program, <u>Running a Shell</u> terminating shells, <u>Terminating a Shell</u> test command, <u>test and “[”</u> text manipulation commands, <u>File Text Manipulation</u> Thunderbird mail program, <u>The Graphical Desktop,</u> tilde ( ̃), denoting home directories, <u>Home Directories</u> time, displaying/setting, <u>Dates and Times</u> timestamps, tmp directory, <u>Directory path part 1: category</u> top command, touch command, creating empty files, <u>Creating a File Quickly</u> tr command, traceroute command, translating characters, using tr command, true command, <u>true and false</u> infinite loops and, <u>Loops</u> tty command, tutorials,

emacs,

Linux help, <u>Getting Help</u> mutt mailer, vim editor, type command, <u>File Location,</u> locating files, types of files, reporting, **U** umask command, umount command, uname command, <u>Operating System Directories,</u> uncompress command, uniq command, until loops, <u>Loops</u> infinite loops and, <u>Loops</u> unzip command, up2date command, <u>Installing Software</u> update-manager, updatedb command, uptime command, <u>Operating System Directories,  ,</u> Usenet news, Usenet News USER environment variable, <u>Shell variables</u> useradd command, userdel command, usermod command, users, <u>User Account Management</u>

creating new accounts, deleting existing users, finger command and, listing logged-in users, modifying accounts, password changes, printenv command and, printing login names, printing user IDs, superusers and, <u>Users and Superusers</u> updating information, users command, /usr/share/doc directory, <u>Getting Help</u> uxterm command, <u>Running a Shell</u> **V** /var directory, <u>Directory path part 1: category</u> variables, <u>Shell variables</u> defining, <u>Shell variables</u> in shell scripts, <u>Variables</u> vi (see vim text editor) video, <u>Video</u> editing, playback,  , ripping, viewing

files, <u>File Viewing, File Viewing</u> processes, Viewing Processes vim text editor, File Creation and Editing, bash command-line editing, <u>Command-line editing</u> less command, lynx –vikeys command, <u>Useful options</u> sed and, <u>sed</u> Visio, VISUAL environment variable, setting default editor, <u>Your Default Editor</u> vlc video player, **W** w command, watch command, wc command, <u>What’s a Command?,</u> web browsing, <u>Web Browsing</u> automation, retrieving pages via command line, text-based, wget command, <u>Useful options</u> whereis command, <u>File Location,</u> locating files, which command, locating files, while loops, <u>Loops</u>

infinite loops and, <u>Loops</u> whitespace, <u>Whitespace and Linebreaks</u> linebreaks, programming with shell scripts, <u>Whitespace and Linebreaks</u> quoting on command line, <u>Quoting</u> who command, tee command and, whoami command, logname and, whois command, wildcard characters and the shell, <u>Wildcards, Wildcards</u> (see also regular expressions) windows (shell), opening, <u>Running a Shell</u> Word documents, editing with abiword, editing with soffice, write command, Writer program (soffice), www directory, Directory path part 1: category **X**

X11 directory, <u>Directory path part 1: category, Directory path part 2: scope</u> xargs command, <u>Useful options,</u>

vs. backquotes, <u>Useful options</u> with find command, xcalc command,

xclock command, xdvi command, xine video player, xload command, xpdf viewer, xscreensaver command, xscreensaver-demo command, xterm command, <u>Running a Shell</u> xv command, alternative to GIMP, xxd command, xxdiff command, <u>File Comparison</u> **Y** yes command, ypdomainname command, <u>Host Information</u> yum command, <u>Installing Software,</u> **Z** zcat command, <u>Sample commands, Sample commands</u> zip command,

## **About the Author** 

Daniel J. Barrett has been immersed in Internet technology since 1985. Currently working as a software engineer, Dan has also been a heavy metal singer, Unix system administrator, university lecturer, web designer, and humorist. He is the author of O'Reilly's Linux Pocket Guide, and he is the coauthor of Linux Security Cookbook, and SSH, The Secure Shell: The Definitive Guide.

# **Special Upgrade Offer** 

If you purchased this ebook from a retailer other than O’Reilly, you can upgrade it for $4.99 at oreilly.com by <u>clicking here.</u>

### Linux Pocket Guide 

##### Daniel J. Barrett 

Editor

Andy Oram

Editor

Mike Loukides

###### **Revision History** 

|2012-03-07|First release|
|---|---|
|2012-05-11|Second release|
|2012-06-12|Third release|

###### Copyright © 2012 Daniel Barrett 

O’Reilly books may be purchased for educational, business, or sales promotional use. Online editions are also available for most titles (http://my.safaribooksonline.com). For more information, contact our corporate/institutional sales department: (800) 998-9938 or <u>corporate@oreilly.com.</u>

Nutshell Handbook, the Nutshell Handbook logo, and the O’Reilly logo are registered trademarks of O’Reilly Media, Inc. _Linux Pocket Guide, Second Edition_ , the cover image of a roper, and related trade dress are trademarks of O’Reilly Media, Inc.

Many of the designations used by manufacturers and sellers to distinguish their products are claimed as trademarks. Where those designations appear in this book, and O’Reilly Media, Inc., was aware of a trademark claim, the designations have been printed in caps or initial caps.

While every precaution has been taken in the preparation of this book, the publisher and author assume no responsibility for errors or omissions, or for damages resulting from the use of the information contained herein.

O’Reilly Media 1005 Gravenstein Highway North Sebastopol, CA 95472

2013-05-01T17:18:50-07:00

**Linux Pocket Guide** Table of Contents

<u>Special Upgrade Offer 1. Linux Pocket Guide What’s in This Book?</u>

<u>What’s Linux? What’s a Distro? What’s a Command? Reading This Book Shell prompts Keystrokes Your friend, the echo command Getting Help Linux: A First View The Graphical Desktop Running a Shell Input and Output Users and Superusers The Filesystem Home Directories System Directories Directory path part 1: category Directory path part 2: scope Directory path part 3: application Operating System Directories File Protections</u>

<u>The Shell The Shell Versus Programs Selected Features of the bash Shell Wildcards Brace expansion Shell variables</u>

<u>Search path Aliases Input/output redirection Pipes Combining commands Quoting Escaping Command-line editing Command history Filename completion Shell Job Control Killing a Command in Progress Terminating a Shell Tailoring Shell Behavior Basic File Operations Directory Operations File Viewing File Creation and Editing Creating a File Quickly Your Default Editor File Properties File Location File Text Manipulation File Compression and Packaging File Comparison Printing Spell Checking Disks and Filesystems Backups and Remote Storage Viewing Processes Controlling Processes Scheduling Jobs</u>

<u>Logins, Logouts, and Shutdowns Users and Their Environment User Account Management Becoming the Superuser Group Management Host Information Host Location Network Connections Email Web Browsing Usenet News Instant Messaging Screen Output Math and Calculations Dates and Times Graphics and Screensavers Audio Video Installing Software Programming with Shell Scripts Whitespace and Linebreaks Variables Input and Output Booleans and Return Codes test and “[” true and false Conditionals Loops Break and Continue Creating and Running Shell Scripts Command-Line Arguments Exiting with a Return Code</u>

###### <u>Beyond Shell Scripting Final Words</u> 

###### <u>Acknowledgments</u> 

<u>Index</u>

<u>About the Author Special Upgrade Offer Copyright</u>