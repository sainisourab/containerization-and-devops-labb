# Stage 1: Build dependencies
FROM node:18-alpine AS builder

WORKDIR /usr/src/app

# Only copy package.json initially to leverage Docker layer caching
COPY package*.json ./

# Install all dependencies
RUN npm install

# Copy application source code
COPY . .


# Stage 2: Production runtime image
FROM node:18-alpine

WORKDIR /usr/src/app

# Copy the dependencies and source from the builder stage
COPY --from=builder /usr/src/app .

# Expose backend port
EXPOSE 3000

# Set environment string for production
ENV NODE_ENV=production

# Start application
CMD ["npm", "start"]
