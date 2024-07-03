const rootElement = document.getElementById("root"); //
const createTodo = document.createElement('button');
const todoItems = [
    {
        title: "Write code",
        isComplete: false
    },
    {
        title: "Review Code",
        isComplete: false
    },
    {
        title: "Update Code",
        isComplete: true
    }
]

setUpComponents();

function setUpComponents(){
    rootElement.style.width = "800px";

    createTodo.innerText = "Add New Todo";
    createTodoEventListener(createTodo);

    rootElement.appendChild(createTodo);
    generateToDo();
    
}

function createTodoEventListener(createButton){
    createButton.addEventListener('click', () => {
        const todo = prompt("What is the task");
        const newTodo = {
            title: todo,
            isComplete: false
        };

        todoItems.push(newTodo);
        createTodoComponent(newTodo);
    });
}

function generateToDo(){
    for (item of todoItems){
        createTodoComponent(item)
    }
}

function createTodoComponent(item){
    const todoItemContainer = document.createElement("div");    
    const todoText = document.createElement('p');
    const todoButton = document.createElement('button');

    // Handle todo Text (p tag)
    todoText.innerText = item.title;
    todoText.className = item.isComplete ? "task-complete" : "task-incomplete";

    // Button (button tag)
    todoButton.innerText = "Done";
    todoButton.addEventListener('click', () => {
        item.isComplete = true;
        todoText.className = item.isComplete ? "task-complete" : "task-incomplete";
    })

    todoItemContainer.appendChild(todoText);
    todoItemContainer.appendChild(todoButton); 
    todoItemContainer.classList.add("todoItem");

    rootElement.appendChild(todoItemContainer)
}









