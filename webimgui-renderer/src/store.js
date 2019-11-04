import Vue from "vue";
import Vuex from "vuex";
import socket from "./socket";

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    layout: null,
    interactiveElementsState: null,
    configuration: {}
  },
  mutations: {
    updateLayout(state, data) {
      state.layout = data.layout;
      state.interactiveElementsState = data.state;
    },
    updateConfiguration(state, configuration) {
      state.configuration = configuration;
      document.title = configuration.title;
    }
  },
  actions: {
    updateLayout(context, data) {
      context.commit("updateLayout", data);
    },
    submitAction(context, data) {
      socket.emit("action", data);
    }
  }
});

socket.on("layout", layout => store.dispatch("updateLayout", layout));
socket.on("configuration", configuration =>
  store.commit("updateConfiguration", configuration)
);

export default store;
