FROM node:24.12-alpine
WORKDIR /app
COPY . .
RUN yarn install --production
CMD ["node", "src/index.js"]
EXPOSE 3000


#a341ee8af87c29801e8dee2752c9990b9b161c5ec7b92051818d1fdf40393fd6