basics
=====

B -> set breakpoint in a file location
L -> shows current lines
F -> shows current lines + details on location ex: stack frame and current line
N -> steps over current line
S -> step into current line
C -> continue execution

## handling breakpoints
* set breakpoints by file location
  - example: b main.rs:12
  - breakpoint set --name **file**\:**line** | b **file**\:**line**
* set breakpoints by function
  - example br s -n longExpensiveFunction
  - breakpoint set --name **fn** | br s -n **fn**
* set conditional breakpoints
  - example: br s -n main.c 'strlen(abc) == 100'
  - breakpoint set --name **fn** -- condition 'C expr' | br s -n **fn** -c 'C expr'

## reading variables
* read variable
  - frame variable *var* | p *var*
* read all stack variables
  - frame variable [--no-args] | fr v [--no-args]
* read globals
  - target variable *var* | ta *var*
* read all globals
  - target variable | ta v

## attaching to programs
* attach by PID 
  - process attach --pid *pid*
* attach by name
  - process attach --name *executable name*

________________

### pipe file into stdin 
settings set target.input-path *path*

### set arguments | run with arguments
settings set target.run-args *.. args* | lldb -- *exec* *.. args*

### The number of disassembly lines to show when displaying a stopped context
set set stop-disassembly-count *count*

### Control when to display disassembly when displaying a stopped context
set set stop-disassembly-display
