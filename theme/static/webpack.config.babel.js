import BrowserSyncPlugin from 'browser-sync-webpack-plugin'
import MiniCssExtractPlugin from 'mini-css-extract-plugin'
import CssMinimizerPlugin from 'css-minimizer-webpack-plugin'
import { resolve } from 'path'

export default (env, argv) => {
  const isDev = argv.mode === 'development'
  const options = { sourceMap: isDev }

  const devPlugins = [
    new BrowserSyncPlugin({
      // Set your desired proxy when calling webpack
      // npm start -- --env proxy=example.com
      proxy: env && env.proxy,
      open: false
    })
  ]

  const plugins = [
    new MiniCssExtractPlugin({
      filename: '[name].css'
    })
  ].concat(isDev ? devPlugins : [])

  return {
    entry: {
      theme: './js/index.js',
    },
    output: {
      path: resolve(__dirname, 'dist'),
      filename: '[name].js'
    },
    module: {
      rules: [
        {
          test: /\.js$/,
          include: resolve(__dirname, 'js'),
          use: {
            loader: 'babel-loader'
          }
        },
        {
          test: /\.s?css$/,
          use: [
            MiniCssExtractPlugin.loader,
            { loader: 'css-loader', options },
            { loader: 'postcss-loader', options },
            { loader: 'sass-loader', options }
          ]
        }
      ]
    },
    optimization: {
      minimizer: [
        new CssMinimizerPlugin()
      ]
    },
    plugins,
    stats: {
      children: false,
      chunks: false,
      colors: true,
      hash: false,
      modules: false,
      version: false
    },
    devtool: isDev ? 'source-map' : false
  }
}
