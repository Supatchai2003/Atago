def version ():
  todo =[]
  while True :
    data = input('enter add , show , exits').strip().upper()
    if data == 'ADD' :
      add_task(todo)
    elif data == 'SHOW':
      show_task(todo)
    elif data == 'EXIT':
      print('Exit the Program')
      break
    else:
      print('input')

def add_task (todo):
  task = input("enter a task")
  todo.append(task)
  print(f"Task '{task}' added.")
def show_task(todo):
  if not todo:
    print("No tasks in the task.")
  else:
    print("Tasks in the task:")
    for task in todo:
      print(task)
      
version()