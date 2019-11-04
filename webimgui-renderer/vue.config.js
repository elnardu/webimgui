module.exports = {
  lintOnSave: false,
  devServer: {
    proxy: {
      '^/socket.io': {
        target: 'http://localhost:8080',
        // ws: true,
        changeOrigin: true
      }
    }
  }
};
