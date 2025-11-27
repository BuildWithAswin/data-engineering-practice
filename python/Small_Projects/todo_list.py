class task:
    def __init__(self, task):
        self.task = task
        

    def __str__(self):
        return (f"{self.task}")


class TaskList:
    def __init__(self):
        self.task_list = []

    def add(self,mytask):
        self.task_list.append(mytask)
    
    def view(self):
        if len(self.task_list) == 0:
            print (f"There are no tasks..!")
        else:
            print (f"You have below tasks for today..!")
            for c in self.task_list:
                print (f"- {c}")
    
    def delete(self, mytask):
        for c in self.task_list:
            if c.task.lower() == mytask.lower():
                self.task_list.remove(c)
                print (f"Task {mytask} has been deleted..!")
        
        print (f"Task not found in the list..!")
    
    

todolist = TaskList()

todolist.add("reading")
todolist.add("writing")
todolist.delete("movie")
todolist.view()

