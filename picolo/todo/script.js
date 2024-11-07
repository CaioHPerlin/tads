// Assets
const startSVG = './assets/start.svg';
const stopSVG = './assets/stop.svg';

// Task management
tasks = [];

const todoElement = document.querySelector('#todo .tasks');
const inProgressElement = document.querySelector('#in-progress .tasks');
const doneElement = document.querySelector('#done .tasks');

const stateToElement = {
	todo: todoElement,
	inProgress: inProgressElement,
	done: doneElement,
};

const startTask = (index) => {
	tasks[index].state = 'inProgress';
	localStorage.setItem('tasks', JSON.stringify(tasks));

	processTasks();
};

const finishTask = (index) => {
	tasks[index].state = 'done';
	localStorage.setItem('tasks', JSON.stringify(tasks));

	processTasks();
};

const processTasks = () => {
	todoElement.innerHTML = '';
	inProgressElement.innerHTML = '';
	doneElement.innerHTML = '';

	tasks.forEach((task, i) => {
		containerElement = stateToElement[task.state];

		let taskButtonsHTML = '';

		if (['todo', 'inProgress'].includes(task.state)) {
			taskButtonsHTML = `
                <div class='task-button-container'>
                ${task.state === 'todo' ? `<button onclick='startTask(${i})'><img src='${startSVG}' /></button>` : ''}
                    <button onclick='finishTask(${i})'><img src='${stopSVG}' /></button>
                </div>  
            `;
		}

		containerElement.innerHTML += `<li>${task.title}${taskButtonsHTML}</li>`;
	});
};

previousTasks = JSON.parse(localStorage.getItem('tasks'));
if (previousTasks) {
	tasks = previousTasks;
}
processTasks();

const addNewTask = (task) => {
	tasks.push(task);
	localStorage.setItem('tasks', JSON.stringify(tasks));

	processTasks();
};

const newTaskButton = document.querySelector('#new-task-btn');
const dialog = document.querySelector('dialog');

// Listen for modal opening
newTaskButton.addEventListener('click', () => {
	dialog.showModal();
});

const clearTaskButton = document.querySelector('#clear-tasks-btn');
clearTaskButton.addEventListener('click', () => {
	tasks = tasks.filter((task) => task.state !== 'done');
	localStorage.setItem('tasks', JSON.stringify(tasks));

	processTasks();
});

// Listen for modal close button
const closeDialogButton = document.querySelector('#close-dialog-btn');
closeDialogButton.addEventListener('click', () => {
	dialog.close();
});

// Listen for dialog submit
const dialogForm = document.querySelector('dialog form');
dialogForm.addEventListener('submit', (e) => {
	e.preventDefault();
	const titleInput = dialogForm.title;
	const descriptionInput = dialogForm.description;
	console.log(`Adding new task with Title=${titleInput.value} and Description=${descriptionInput.value}`);

	addNewTask({
		title: titleInput.value,
		description: descriptionInput.value,
		state: 'todo',
	});

	titleInput.value = '';
	descriptionInput.value = '';
	dialog.close();
});
