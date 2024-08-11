# **Setting up Fly.io Postgres** 

#### Install flyctl and authenticate 
- Install flyctl 
- Authenticate using the ff command: `flyctl auth login`

[Source](https://medium.com/data-folks-indonesia/setup-free-postgresql-on-fly-io-and-import-database-3f8f891cbc71) 

- On the terminal, run the ff command: 
    ```bash 
    flyctl postgres create
    ```
- Follow the on-screen instructions to create a postgres database 
- Take note of the credentials and the connection string. (Note: The connection string is only used for deployed servers)


#### Accessing Postgres locally

- Input the ff. command to access postgres: 
  ```bash 
  flyctl postgres connect -a <postgres-app-name> 
  ``` 
- To view list of databases, input `\` 
- To create a database `create database <db_name>` 
- Create Credentials `create user <username> with encrypted password '<password>'` 
- Grant all privileges `grant all privileges on database <db_name> to <username>`
- Connect to the database `\c <db_name>` 
