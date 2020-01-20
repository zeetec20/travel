const path = require('path')

module.exports = {
    entry: {
        global: path.resolve(__dirname, 'static/global/js/script.js'),
        user: path.resolve(__dirname, 'static/user/js/script.js'),
        contact: path.resolve(__dirname, 'static/contact/js/script.js'),
        blog: path.resolve(__dirname, 'static/blog/js/script.js'),
    },
    output: {
        filename: '[name]/js/bundle.js',
        path: path.resolve(__dirname, 'static')
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                use: {
                    loader: 'babel-loader'
                }
            },
            {
                test: /\.css$/,
                use: [
                    {
                        loader: 'style-loader'
                    },
                    {
                        loader: 'css-loader'
                    },
                    {
                        loader: 'postcss-loader',
                        options: {
                            sourceMap: true,
                            config: {
                                path: path.resolve(__dirname, 'postcss.config.js')
                            }
                        }
                    }
                ]
            }
        ]
    }
}