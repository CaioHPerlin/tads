const main = document.querySelector('main');
const div = document.querySelector('main > div');
const wall = document.querySelector('span');

wall.style.left = '500px';
wall.style.top = '0px';
wall.style.height = '200px';
wall.style.width = '50px';

main.addEventListener('click', (e) => {
	console.log('Mouse:', e.clientX, e.clientY);
	div.style.left = e.clientX - 10 + 'px';
	div.style.top = e.clientY - 10 + 'px';
});

// document.addEventListener('keydown', (e) => {
// 	console.log('a');

// });

document.addEventListener('keydown', (e) => {
	const currX = Number(div.style.left.substring(0, div.style.left.length - 2));
	const currY = Number(div.style.top.substring(0, div.style.top.length - 2));

	const moveX = (e.key === 'ArrowRight') - (e.key === 'ArrowLeft');
	const moveY = (e.key === 'ArrowDown') - (e.key === 'ArrowUp');

	const horizontalSpeed = moveX * 10;
	const verticalSpeed = moveY * 10;

	const wallX = Number(
		wall.style.left.substring(0, wall.style.left.length - 2)
	);
	const wallY = Number(
		wall.style.left.substring(0, wall.style.left.length - 2)
	);

	// Horizontal Collision
	const wallHeight = Number(
		wall.style.height.substring(0, wall.style.height.length - 2)
	);

	const horizontalCollision =
		(wallX - 10 == currX + horizontalSpeed ||
			wallX + 10 == currX + horizontalSpeed) &&
		currY >= wallY &&
		currY < wallY + wallHeight;

	if (horizontalCollision) {
		horizontalSpeed = 0;
	}

	// Vertical Collision

	const verticalCollision =
		(wallY - 10 == currY + verticalSpeed ||
			wallY + wallHeight + 10 == currY + verticalSpeed) &&
		currX >= wallX - 10 &&
		currX < wallX + 10;

	if (verticalCollision) {
		verticalSpeed = 0;
	}

	div.style.left = currX + horizontalSpeed + 'px';
	div.style.top = currY + verticalSpeed + 'px';
});
