const main = document.querySelector("main");
const div = document.querySelector("main > div");

main.addEventListener("click", (e) => {
  console.log("Mouse:", e.clientX, e.clientY);
  div.style.left = e.clientX - 10 + "px";
  div.style.top = e.clientY - 10 + "px";
});

document.addEventListener("keydown", (e) => {
  const currX =
    Number(div.style.left.substring(0, div.style.left.length - 2)) || 0;
  const currY =
    Number(div.style.top.substring(0, div.style.top.length - 2)) || 0;

  const moveX =
    (e.key === "ArrowRight" || e.key === "d") -
    (e.key === "ArrowLeft" || e.key === "a");
  const moveY =
    (e.key === "ArrowDown" || e.key === "s") -
    (e.key === "ArrowUp" || e.key === "w");

  const speedX = moveX * 10;
  const speedY = moveY * 10;

  div.style.left = currX + speedX + "px";
  div.style.top = currY + speedY + "px";
});
