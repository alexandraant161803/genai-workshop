# Use an official Node runtime as a parent image
FROM node:20-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

RUN npm config set -- '//gitlab.netlight.com/api/v4/projects/1217/packages/npm/:_authToken' "glpat-A6Qv2E1HiZMfzZTrkVK_"

# Copy package.json and package-lock.json (or yarn.lock) files
COPY package*.json ./

# Install any needed packages specified in package.json
RUN npm install


# Bundle app source inside the Docker image
COPY . .

EXPOSE 4173

# Build your app using Vite
RUN npm run build

# Define the command to run your app using CMD which defines your runtime
CMD [ "npm","run",  "preview" ]
