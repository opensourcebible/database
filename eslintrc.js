module.exports = {
  root: true,
  ignorePatterns: [
    'node_modules',
    '*.js'
  ],
  env: {
    es2020: true,
    node: true
  },
  globals: {
    Atomics: "readonly",
    SharedArrayBuffer: "readonly"
  },
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaVersion: 12,
    sourceType: 'module'
  },
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:@typescript-eslint/recommended-requiring-type-checking',
    'airbnb-base'
  ],
  plugins: [
    '@typescript-eslint',
    'eslint-plugin-import-helpers'
  ],
  rules: {

    // allow debugger during development only
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',

    'no-void': 'off',
    'no-nested-ternary': 'off',
    'import/first': 'off',
    'import/namespace': 'error',
    'import/default': 'error',
    'import/export': 'error',
    'import/extensions': 'off',
    'import/no-unresolved': 'off',
    'import/no-extraneous-dependencies': 'off',
    'prefer-promise-reject-errors': 'off',

    'no-new': 'warn',
    'no-prototype-builtins': 'off',
    'max-classes-per-file': 'warn',
    'no-console': 'off',
    'no-param-reassign': 'off',
    'init-declarations': 'off',
    'padding-line-between-statements': 'off',
    'import/prefer-default-export': 'off',
    'no-useless-constructor': 'warn',
    'no-plusplus': 'off',
    'no-await-in-loop': 'off',
    'class-methods-use-this': 'off',
    'no-return-await': 'off',

    'max-len': ['error', {
      'code': 160,
      'tabWidth': 4,
      'ignoreUrls': true,
    }],

    "no-shadow": "off",
    "camelcase": "off",
    "prettier/prettier": "error",
    "import-helpers/order-imports": [
      "warn",
      {
        "newlinesBetween": "always",
        "groups": [
          "module",
          "/^@shared/",
          "/^@/",
          [
            "parent",
            "sibling",
            "index"
          ]
        ],
        "alphabetize": {
          "order": "asc",
          "ignoreCase": true
        }
      }
    ],

    // TypeScript
    'quotes': ['warn', 'single', { avoidEscape: true }],
    '@typescript-eslint/explicit-function-return-type': 'off',

    '@typescript-eslint/no-explicit-any': 'off',
    '@typescript-eslint/no-unused-vars': [
      'warn',
      {
        'argsIgnorePattern': '_',
      },
    ],
    '@typescript-eslint/explicit-module-boundary-types': 'off',
    '@typescript-eslint/no-empty-function': 'off',
    "@typescript-eslint/camelcase": "off",
    "@typescript-eslint/no-shadow": [
      "error"
    ],
    "@typescript-eslint/naming-convention": [
      "warn",
      {
        "selector": "interface",
        "format": [
          "PascalCase"
        ],
        "custom": {
          "regex": "^I[A-Z]",
          "match": true
        }
      }
    ],
  },
  "settings": {
    "import/resolver": {
      "typescript": {}
    }
  }
}
