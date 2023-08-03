 1. su betty = used this cmd to switch user to from current to user called betty
2. whoami = to print username of current user
3. chown betty hello = changes the owner of the file hello to the user betty
4. touch hello = touch creates file called hello
5. chmod u+x hello = this cmd gives permission to executed by the owner of the file
6. chmod ug+x,o+r hello = adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
7. chmod ugo+x hello = gives owner , group , world permission to execute
8. chmod 007 hello = gives no premission to owner and group but gives all permission to world
9. chmod 753 hello = gives all permission to the owner and gives read and execution permission to group and write and execute permission to world
10. chmod  --reference=olleh hello = refers alleh's mode to hello
11. chmod a+X * =adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users
12. mkdir -m my_dir = creates file with 751 mode
13. chgrp school hello = changes the group owner to school for the file hello
14. chown vincent:staff * = changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.
15. chown -h vincent:staff _hello = changes the owner and the group owner of _hello to vincent and staff respectively.
16. chown -R --from=guillaume betty hello
 =  changes the owner of the file hello to betty only if it is owned by the user guillaume.
17. telnet towel.blinkenlights.nl = a script that will play the StarWars IV episode in the terminal.

