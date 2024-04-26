# Chatatouille

Using the power of AI, peel the useless junk away from online recipes.

## How to run

You need to have [NodeJS](https://nodejs.org/en) installed locally.

From the root of the frontend run the following commands

```
npm config set -- '//gitlab.netlight.com/api/v4/projects/1217/packages/npm/:_authToken' "glpat-9jzBrTuE41ns2EtmY81b"
```

```
npm i
```

to install the projects dependencies. Once those have installed, run

```
npm run dev
```

Now the project should be running on `localhost:5173`.

### What is this config command?

As this project uses the Netlight design system, which is consumed via a private NPM registry, we need to set a valid token. To keep things simple, I (Jón) created a token for this workshop specifically, which will expire in mid April. If you want to run this locally and the token doesn't work, please check out [these instructions](https://nds-dev.edgez.live/?path=/docs/doc-installation-usage--docs).
