module.exports = {
  preset: '@vue/cli-plugin-unit-jest/presets/typescript-and-babel',
  "moduleFileExtensions": [
    "js",
    "ts",
    "json",
    // tell Jest to handle `*.vue` files
    "vue"
  ],
  transform: {
    '^.+\\.vue$': 'vue-jest',
    "^.+\\.tsx?$": "ts-jest"
  }
}
