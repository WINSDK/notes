# basics
b **file**\:**line** -> set breakpoint in a file location \
l -> shows current lines \
f -> shows current lines + details on location ex: stackframe and current line \
n -> steps over current line \
s -> step into current line \
c -> continue execution

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

#### pipe file into stdin 
settings set target.input-path *path*

#### set arguements | run with arguements
settings set target.run-args *.. args* | lldb -- *exec* *.. args*
