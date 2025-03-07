@echo off

set mypath=%~dp0
@echo %mypath%
python %mypath%/../main.py %1 %2 %3
@REM  task-cli   [action] [description]
@REM  task-cli   [action] [index] [description]
@REM  task-cli   [action] [index]
@REM  task-cli   [action] 
@REM  task-cli   [action] [status]



@REM Examples
@REM  task-cli add "Buy groceries"
@REM # Output: Task added successfully (ID: 1)

@REM # Updating and deleting tasks
@REM task-cli update 1 "Buy groceries and cook dinner"
@REM task-cli delete 1

@REM # Marking a task as in progress or done
@REM task-cli mark-in-progress 1
@REM task-cli mark-done 1

@REM # Listing all tasks
@REM task-cli list

@REM # Listing tasks by status
@REM task-cli list done
@REM task-cli list todo
@REM task-cli list in-progress  