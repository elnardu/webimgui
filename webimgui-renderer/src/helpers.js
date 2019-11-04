export function labelToText(label) {
  let text = label.split("#");
  if (text.length > 1) {
    text.pop();
  }
  return text.join("#");
}
