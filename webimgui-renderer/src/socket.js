import io from "socket.io-client";

const socket = io("/");

socket.on("connect", () => {
  socket.emit("initialize", {
    width: window.innerWidth,
    height: window.innerHeight
  });
});

export default socket;
