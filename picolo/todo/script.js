const startSVG = './assets/start.svg';
const stopSVG = './assets/stop.svg';

const todoElement = document.querySelector('#todo .tasks');
const inProgressElement = document.querySelector('#in-progress .tasks');
const doneElement = document.querySelector('#done .tasks');
const dialog = document.querySelector('dialog');
const newTaskButton = document.querySelector('#new-task-btn');
const closeDialogButton = document.querySelector('#close-dialog-btn');
const clearTaskButton = document.querySelector('#clear-tasks-btn');
const dialogForm = document.querySelector('dialog form');

let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

const stateToElement = {
	todo: todoElement,
	inProgress: inProgressElement,
	done: doneElement,
};

const init = () => {
	newTaskButton.addEventListener('click', () => dialog.showModal());
	closeDialogButton.addEventListener('click', () => dialog.close());
	clearTaskButton.addEventListener('click', clearCompletedTasks);
	dialogForm.addEventListener('submit', handleDialogSubmit);
	renderTasks();
};

const handleDialogSubmit = (e) => {
	e.preventDefault();

	const title = dialogForm.title.value.trim();

	if (!title) {
		alert('A task must have a title!');
		return;
	}

	addTask({ title, state: 'todo' });

	dialogForm.reset();
	dialog.close();
};

const addTask = (task) => {
	tasks.push(task);
	saveTasks();
	renderTasks();
};

const clearCompletedTasks = () => {
	tasks = tasks.filter((task) => task.state !== 'done');
	saveTasks();
	renderTasks();
};

const updateTaskState = (index, newState) => {
	if (tasks[index]) {
		tasks[index].state = newState;
		saveTasks();
		renderTasks();
	}
};

const renderTasks = () => {
	// Clear all columns
	Object.values(stateToElement).forEach((element) => (element.innerHTML = ''));

	tasks.forEach((task, index) => {
		const container = stateToElement[task.state];

		const taskElement = createTaskElement(task, index);
		container.appendChild(taskElement);
	});
};

const createTaskElement = (task, index) => {
	const taskElement = document.createElement('li');
	taskElement.className = 'task';

	const taskTitle = document.createElement('span');
	taskTitle.textContent = task.title;

	const buttonContainer = document.createElement('div');
	buttonContainer.className = 'task-button-container';

	if (task.state === 'todo') {
		const startButton = createButton(() => updateTaskState(index, 'inProgress'), startSVG);
		buttonContainer.appendChild(startButton);
	}

	if (['todo', 'inProgress'].includes(task.state)) {
		const finishButton = createButton(() => updateTaskState(index, 'done'), stopSVG);
		buttonContainer.appendChild(finishButton);
	}

	taskElement.appendChild(taskTitle);
	taskElement.appendChild(buttonContainer);

	return taskElement;
};

const createButton = (onClick, iconSrc) => {
	const button = document.createElement('button');
	button.addEventListener('click', onClick);

	const icon = document.createElement('img');
	icon.src = iconSrc;

	button.appendChild(icon);
	return button;
};

const saveTasks = () => localStorage.setItem('tasks', JSON.stringify(tasks));

init();
