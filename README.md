# mostfiles

List directories and number of files inside to easily find directories with most files.

Give it path (default is `.`) and just 3 boolean options
`-d`/`--dir` - each subdirectory counted as 1 file too
`-a`/`--all` - do not ignore hidden files/directories 
`-r`/`--recursive` - recursive mode. Mostfiles ALWAYS walks subdirectories recursively, but `-r` flag makes it to count files in nested directories.

Examples:
~~~shell
$ mostfiles
3 .
1 mostfiles/__pycache__
1 mostfiles
~~~
3 files in current directory, all hidden files/directories (like .gitignore, .git ) are ignored. Only LICENSE, pyproject.toml and README.md is counted. Subdirectory "mostfiles" not counted because `-d` not given.

~~~
$ mostfiles -r
5 .
2 mostfiles
1 mostfiles/__pycache__
~~~
Now `.` has 5 files. 3 in current directory, but also 2 in subdirectories.

~~~
$ mostfiles -ar | head -n 3
32 .
26 .git
13 .git/hooks
~~~
Now, count hidden files/directories (such as .git, .gitignore)
