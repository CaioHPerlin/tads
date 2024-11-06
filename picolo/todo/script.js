// Assets
const startSVG = './assets/start.svg';
const stopSVG = './assets/stop.svg';

// Task management
tasks = [];

const todoElement = document.querySelector('#todo .tasks');
const inProgressElement = document.querySelector('#in-progress .tasks');
const doneElement = document.querySelector('#done .tasks');

const columnToElement = {
	todo: todoElement,
	inProgress: inProgressElement,
	done: doneElement,
};

const finishTask = (index) => {
	tasks[index].column = 'done';
	localStorage.setItem('tasks', JSON.stringify(tasks));

	processTasks();
};

const processTasks = () => {
	todoElement.innerHTML = '';
	inProgressElement.innerHTML = '';
	doneElement.innerHTML = '';

	tasks.forEach((task, i) => {
		containerElement = columnToElement[task.column];

		let taskButtonsHTML = '';

		if (['todo', 'inProgress'].includes(task.column)) {
			taskButtonsHTML = `
                <div class='task-button-container'>
                ${task.column === 'todo' ? `<button onclick='finishTask(${i})'><img src='${startSVG}' /></button>` : ''}
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
		column: 'todo',
	});

	titleInput.value = '';
	descriptionInput.value = '';
	dialog.close();
});
