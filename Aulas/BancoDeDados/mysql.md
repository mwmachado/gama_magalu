# Instalação
## Windows
1. https://dev.mysql.com/downloads/

## Linux
1. sudo apt update
1. sudo apt upgrade -y
1. sudo apt install mysql-server -y
1. mysql --version
1. sudo systemctl status mysql
1. sudo mysql
    1. `ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '<password>';`
    1. exit
1. mysql -u root -p
    1. `<password>`
    1. exit
1. sudo mysql_secure_installation
    1. Setup VALIDATE PASSWORD component? n
    1. Change the password for root? n
    1. Remove anonymous users? y
    1. Disallow root login remotely? y
    1. Remove test database and access to it? y
    1. Reload privilege tables now? y

# Acesso
1. instalar extensão do vscode `Database Client`
1. menu database
1. "+" -> Add Connection
    1. Name: <nome da conexão>
    1. Server Type: Mysql
    1. Host: 127.0.0.1
    1. Port: 3306
    1. Username: root
    1. Password: <password>
    1. \+ Connect
    1. x Close

# Referencia
<https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-22-04>
