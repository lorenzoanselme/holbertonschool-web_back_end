export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    const taskTrue = true;
    const taskFalse = false;
    return [task, task2, taskTrue, taskFalse].slice(0, 2);
  }

  return [task, task2];
}
