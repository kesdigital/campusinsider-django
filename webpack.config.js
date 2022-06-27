const path = require("path");

module.exports = {
  entry: {
    base: path.resolve(__dirname, "src/ts/base.ts"),
    home: path.resolve(__dirname, "src/ts/core/home.ts"),
  },
  devtool: 'inline-source-map',
  output: {
    path: path.resolve(__dirname, "static/js/"),
    filename: "[name].min.js",
    clean: true
  },
  module: {
    rules: [
      {
        test: /\.(c|sc)ss$/,
        use: ["style-loader", "css-loader", "sass-loader"]
      },
      {
        test: /\.ts$/,
        use: 'ts-loader',
        exclude: /node_modules/,
      },
    ]
  }
}
